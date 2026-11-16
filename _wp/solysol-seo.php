<?php
/*
Plugin Name: Sol y Sól – SEO
Description: Google News sitemap, strony miast, „Czytaj też”, porządki w mapie strony, tagi X, lepszy opis strony głównej.
*/
if (!defined('ABSPATH')) exit;

const SSEO_HOME_DESC = 'Wiadomości z Costa del Sol po polsku – Marbella, Málaga, Fuengirola, Estepona, Mijas, Benalmádena, Torremolinos, Nerja. Prawo, podatki, nieruchomości, sprawy kryminalne, wydarzenia i ciekawostki dla Polaków w Hiszpanii.';

function sseo_cities(){
  return [
    'Marbella'=>'Wiadomości z Marbelli po polsku – co dzieje się w Marbelli, San Pedro Alcántara i Puerto Banús: prawo, nieruchomości, wydarzenia, sprawy kryminalne i życie Polaków.',
    'Málaga'=>'Wiadomości z Malagi po polsku – decyzje miasta, ruch drogowy, lotnisko, mieszkania, wydarzenia i ciekawostki z Malagi dla Polaków na Costa del Sol.',
    'Fuengirola'=>'Wiadomości z Fuengiroli po polsku – co nowego w Fuengiroli: przepisy, mieszkania, wydarzenia, zakupy i życie Polaków.',
    'Estepona'=>'Wiadomości z Estepony po polsku – co dzieje się w Esteponie: inwestycje miasta, wydarzenia, sprawy kryminalne i życie na wybrzeżu.',
    'Mijas'=>'Wiadomości z Mijas po polsku – Mijas Pueblo, Mijas Costa, La Cala i Las Lagunas: decyzje gminy, wydarzenia i życie Polaków.',
    'Benalmádena'=>'Wiadomości z Benalmádeny po polsku – co nowego w Benalmádenie: otwarcia, wydarzenia, przepisy i ciekawostki.',
    'Torremolinos'=>'Wiadomości z Torremolinos po polsku – co dzieje się w Torremolinos: wydarzenia, przepisy, ruch drogowy i życie na wybrzeżu.',
    'Nerja'=>'Wiadomości z Nerji i Axarquii po polsku – Nerja, Torrox, Vélez-Málaga i Torre del Mar: wydarzenia, przepisy i ciekawostki.',
    'Benahavís'=>'Wiadomości z Benahavís po polsku – decyzje gminy, nieruchomości i wydarzenia.',
    'Manilva'=>'Wiadomości z Manilvy i Casares po polsku – decyzje gmin, mieszkania, wydarzenia.',
  ];
}

/* 1. Strony miast: tagi z opisami + automatyczne tagowanie wpisów */
add_action('init', function(){
  if (get_option('sseo_cities_v') == 1) return;
  foreach (sseo_cities() as $name=>$desc){
    $t = term_exists($name,'post_tag');
    if (!$t) $t = wp_insert_term($name,'post_tag',['description'=>$desc]);
    elseif (!term_description((int)(is_array($t)?$t['term_id']:$t),'post_tag')) wp_update_term((int)(is_array($t)?$t['term_id']:$t),'post_tag',['description'=>$desc]);
  }
  foreach (get_posts(['numberposts'=>-1,'post_type'=>'post','post_status'=>'publish','fields'=>'ids']) as $pid) sseo_autotag($pid);
  update_option('sseo_cities_v',1);
}, 20);
function sseo_autotag($pid){
  $p = get_post($pid); if(!$p || $p->post_type!=='post') return;
  $txt = $p->post_title.' '.wp_strip_all_tags($p->post_content);
  $alias = ['Málaga'=>['Málaga','Malaga','Maladze','Malagi'],'Marbella'=>['Marbell','San Pedro','Puerto Banús'],'Fuengirola'=>['Fuengirol'],'Estepona'=>['Estepon'],'Mijas'=>['Mijas'],'Benalmádena'=>['Benalmáden','Benalmaden'],'Torremolinos'=>['Torremolinos'],'Nerja'=>['Nerj','Torrox','Vélez','Torre del Mar','Axarqu'],'Benahavís'=>['Benahav'],'Manilva'=>['Manilv','Casares']];
  $add=[];
  foreach($alias as $tag=>$keys) foreach($keys as $k) if (mb_stripos($txt,$k)!==false){ $add[]=$tag; break; }
  if ($add) wp_set_post_tags($pid,$add,true);
}
add_action('save_post_post', function($pid){ if(!wp_is_post_revision($pid)) sseo_autotag($pid); }, 20);

/* 2. Google News sitemap: /news-sitemap.xml (wpisy z ostatnich 48 h) */
add_action('init', function(){
  $uri = strtok($_SERVER['REQUEST_URI'] ?? '','?');
  if ($uri !== '/news-sitemap.xml') return;
  $q = get_posts(['numberposts'=>100,'post_type'=>'post','post_status'=>'publish','date_query'=>[['after'=>'48 hours ago']]]);
  header('Content-Type: application/xml; charset=UTF-8');
  echo '<?xml version="1.0" encoding="UTF-8"?>'."\n".'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">'."\n";
  foreach($q as $p){
    echo '<url><loc>'.esc_url(get_permalink($p)).'</loc><news:news><news:publication><news:name>Sol y Sól</news:name><news:language>pl</news:language></news:publication><news:publication_date>'.esc_html(get_the_date('c',$p)).'</news:publication_date><news:title>'.esc_html(wp_strip_all_tags($p->post_title)).'</news:title></news:news></url>'."\n";
  }
  echo '</urlset>'; exit;
}, 1);
add_filter('robots_txt', function($out){ return $out."Sitemap: ".home_url('/news-sitemap.xml')."\n"; }, 99);

/* 3. Porządki: bez listy autorów w mapie strony, noindex dla pustych kategorii, autorów i wyszukiwarki */
add_filter('wp_sitemaps_add_provider', function($provider,$name){ return $name==='users' ? false : $provider; }, 10, 2);
add_filter('wp_sitemaps_taxonomies_query_args', function($args){ $args['hide_empty']=true; return $args; });
add_filter('wp_robots', function($r){
  if (is_author() || is_search()) { $r['noindex']=true; $r['follow']=true; }
  if (is_category() || is_tag()) { $t = get_queried_object(); if ($t && (int)$t->count === 0) { $r['noindex']=true; $r['follow']=true; } }
  return $r;
});
add_action('template_redirect', function(){ if (is_author()) { wp_redirect(home_url('/'),301); exit; } });

/* 4. Tagi X/Twitter, opisy stron miast */
add_action('wp_head', function(){
  $title = wp_get_document_title(); $desc=''; $img='';
  if (is_singular('post')) { $desc = wp_strip_all_tags(get_the_excerpt()); $img = get_the_post_thumbnail_url(null,'large'); }
  elseif (is_front_page() || is_home()) { $desc = SSEO_HOME_DESC; }
  elseif (is_tag() || is_category()) { $desc = wp_strip_all_tags(term_description()); }
  echo '<meta name="twitter:card" content="summary_large_image">'."\n";
  echo '<meta name="twitter:title" content="'.esc_attr($title).'">'."\n";
  if ($desc) echo '<meta name="twitter:description" content="'.esc_attr(wp_trim_words($desc,40)).'">'."\n";
  if ($img) echo '<meta name="twitter:image" content="'.esc_url($img).'">'."\n";
}, 2);

/* 5. Strona główna: lepszy opis i nagłówek H1 */
add_action('template_redirect', function(){
  if ((is_tag() || is_category()) && !is_paged()) {
    $d = wp_strip_all_tags(term_description());
    if ($d) ob_start(function($html) use ($d){
      $html = preg_replace('#(<meta\s+name="description"\s+content=")[^"]*(")#i', '$1'.esc_attr($d).'$2', $html, 1);
      return preg_replace('#(<meta\s+property="og:description"\s+content=")[^"]*(")#i', '$1'.esc_attr($d).'$2', $html, 1);
    });
    return;
  }
  if (!(is_front_page() || is_home()) || is_paged()) return;
  ob_start(function($html){
    $html = preg_replace('#(<meta\s+name="description"\s+content=")[^"]*(")#i', '$1'.esc_attr(SSEO_HOME_DESC).'$2', $html, 1);
    $html = preg_replace('#(<meta\s+property="og:description"\s+content=")[^"]*(")#i', '$1'.esc_attr(SSEO_HOME_DESC).'$2', $html, 1);
    $html = preg_replace('#<title>[^<]*</title>#', '<title>Sol y Sól – wiadomości z Costa del Sol po polsku | Magazyn dla Polaków</title>', $html, 1);
    $h1 = '<h1 style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap">Sol y Sól – wiadomości z Costa del Sol po polsku</h1>';
    $html = preg_replace('#(<body[^>]*>)#', '$1'.$h1, $html, 1);
    return $html;
  });
});

/* 6. „Czytaj też” pod artykułem */
add_filter('the_content', function($c){
  if (!is_singular('post') || !in_the_loop() || !is_main_query()) return $c;
  $id = get_the_ID(); $cats = wp_get_post_categories($id); $tags = wp_get_post_tags($id,['fields'=>'ids']);
  $q = get_posts(['numberposts'=>3,'post__not_in'=>[$id],'post_status'=>'publish','tax_query'=>['relation'=>'OR',['taxonomy'=>'category','terms'=>$cats],['taxonomy'=>'post_tag','terms'=>$tags ?: [0]]]]);
  if (count($q) < 3) $q = array_merge($q, get_posts(['numberposts'=>3-count($q),'post__not_in'=>array_merge([$id],wp_list_pluck($q,'ID')),'post_status'=>'publish']));
  if (!$q) return $c;
  $h = '<aside class="ss-related" style="margin:48px 0 0;padding:24px 0 0;border-top:1px solid #D9CFBF"><p style="font-size:13px;font-weight:700;letter-spacing:.18em;color:#A9531F;margin:0 0 12px">CZYTAJ TEŻ</p><ul style="list-style:none;margin:0;padding:0">';
  foreach($q as $p) $h .= '<li style="margin:0 0 10px"><a href="'.esc_url(get_permalink($p)).'" style="font-size:19px;line-height:1.3;text-decoration:none">'.esc_html(get_the_title($p)).'</a></li>';
  return $c.$h.'</ul></aside>';
}, 20);
