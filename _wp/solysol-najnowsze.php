<?php
/*
Plugin Name: Sol y Sól – pasek „Najnowsze”
Description: Przewijany pasek „Najnowsze z Sol y Sól” (5–8 ostatnich tematów z linkami) na górze strony. Dane z repozytorium: _feeds/najnowsze.json – plik aktualizuje automat publikacji Studio. Shortcode: [solysol_najnowsze].
*/
if (!defined('ABSPATH')) exit;
define('SSN_URL', 'https://raw.githubusercontent.com/Oliwiana/solysol-media/main/_feeds/najnowsze.json');

function ssn_items(){
  $d = get_transient('ssn_items');
  if ($d === false) {
    $r = wp_remote_get(SSN_URL.'?t='.time(), ['timeout'=>15]);
    $j = (!is_wp_error($r) && wp_remote_retrieve_response_code($r)===200) ? json_decode(wp_remote_retrieve_body($r), true) : null;
    if (is_array($j) && isset($j['items']) && is_array($j['items'])) $j = $j['items'];   // {items:[...]} albo [...]
    $d = [];
    if (is_array($j)) foreach ($j as $it) {
      if (!is_array($it) || empty($it['title'])) continue;
      $link = $it['link'] ?? ($it['url'] ?? '');
      if (!empty($it['ssf_id'])) {   // jeśli temat ma artykuł na stronie – link do wpisu
        $ids = get_posts(['post_type'=>'post','post_status'=>'publish','meta_key'=>'ssf_id','meta_value'=>$it['ssf_id'],'numberposts'=>1,'fields'=>'ids']);
        if ($ids) $link = get_permalink($ids[0]);
      }
      if (!$link) continue;
      $d[] = ['title'=>$it['title'], 'link'=>$link, 'date'=>$it['date'] ?? '', 'slot'=>$it['slot'] ?? ''];
      if (count($d) >= 8) break;
    }
    set_transient('ssn_items', $d, 10*MINUTE_IN_SECONDS);
  }
  return $d;
}
add_action('init', function(){ if (isset($_GET['ssn_refresh']) && $_GET['ssn_refresh']==='sys7731') delete_transient('ssn_items'); });

function ssn_bar_html(){
  $items = ssn_items(); if (count($items) < 3) return '';
  $li = '';
  foreach ($items as $it) {
    $ext = strpos($it['link'], home_url()) === 0 ? '' : ' target="_blank" rel="noopener"';
    $li .= '<a class="ssn-i" href="'.esc_url($it['link']).'"'.$ext.'><span class="ssn-dot">●</span>'.esc_html($it['title']).'</a>';
  }
  ob_start(); ?>
<div class="ssn-bar" role="region" aria-label="Najnowsze z Sol y Sól">
 <style>
 .ssn-bar{display:flex;align-items:stretch;background:#0E1B2C;color:#f6f1e7;font:600 14px/1.2 Inter,system-ui,sans-serif;overflow:hidden;position:relative;z-index:50}
 .ssn-lab{flex:none;background:#E07F45;color:#161412;padding:10px 14px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;font-size:12px;display:flex;align-items:center;white-space:nowrap}
 .ssn-win{flex:1;overflow:hidden;position:relative;-webkit-mask-image:linear-gradient(90deg,transparent,#000 24px,#000 calc(100% - 24px),transparent);mask-image:linear-gradient(90deg,transparent,#000 24px,#000 calc(100% - 24px),transparent)}
 .ssn-track{display:inline-flex;gap:36px;padding:10px 0 10px 24px;white-space:nowrap;animation:ssn-run 55s linear infinite}
 .ssn-bar:hover .ssn-track,.ssn-bar:focus-within .ssn-track{animation-play-state:paused}
 .ssn-i{color:#f6f1e7!important;text-decoration:none!important;display:inline-flex;gap:8px;align-items:center}
 .ssn-i:hover,.ssn-i:focus{color:#F2C14E!important;text-decoration:underline!important}
 .ssn-dot{color:#F2C14E;font-size:9px}
 @keyframes ssn-run{from{transform:translateX(0)}to{transform:translateX(-50%)}}
 @media (prefers-reduced-motion:reduce){.ssn-track{animation:none}.ssn-win{overflow-x:auto}}
 @media (max-width:600px){.ssn-lab{padding:9px 10px;font-size:11px}.ssn-bar{font-size:13px}}
 </style>
 <span class="ssn-lab">Najnowsze z Sol y Sól</span>
 <div class="ssn-win"><div class="ssn-track"><?php echo $li; ?><span aria-hidden="true" style="display:inline-flex;gap:36px"><?php echo str_replace('<a ', '<a tabindex="-1" ', $li); ?></span></div></div>
</div>
<?php return ob_get_clean();
}

/* pasek na samej górze każdej strony (motyw musi wywoływać wp_body_open – większość motywów to robi) */
add_action('wp_body_open', function(){ if (!is_admin()) echo ssn_bar_html(); }, 5);
/* zapasowo – shortcode do wstawienia w dowolnym miejscu: [solysol_najnowsze] */
add_shortcode('solysol_najnowsze', 'ssn_bar_html');
