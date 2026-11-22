<?php
/*
Plugin Name: Sol y Sól – baner na stronie głównej
Description: Pokazuje na górze strony głównej baner z najnowszym odcinkiem podcastu „Zagadki Costa del Sol” (dane z repozytorium: _feeds/home-promo.json) i przypina wpis z odcinkiem na początku listy.
*/
if (!defined('ABSPATH')) exit;
define('SSP_URL', 'https://raw.githubusercontent.com/Oliwiana/solysol-media/main/_feeds/home-promo.json');

function ssp_data(){
  $d = get_transient('ssp_promo');
  if ($d === false) {
    $r = wp_remote_get(SSP_URL.'?t='.time(), ['timeout'=>15]);
    $d = (!is_wp_error($r) && wp_remote_retrieve_response_code($r)===200) ? json_decode(wp_remote_retrieve_body($r), true) : null;
    if (!is_array($d)) $d = ['active'=>false];
    set_transient('ssp_promo', $d, 10*MINUTE_IN_SECONDS);
  }
  return $d;
}
add_action('init', function(){ if(isset($_GET['ssp_refresh']) && $_GET['ssp_refresh']==='sys7731'){ delete_transient('ssp_promo'); } });

/* link do wpisu z odcinkiem (po ssf_id) */
function ssp_post_link($d){
  if (!empty($d['ssf_id'])) {
    $ids = get_posts(['post_type'=>'post','post_status'=>'publish','meta_key'=>'ssf_id','meta_value'=>$d['ssf_id'],'numberposts'=>1,'fields'=>'ids']);
    if ($ids) return get_permalink($ids[0]);
  }
  return $d['link'] ?? home_url('/');
}

/* przypięcie wpisu z odcinkiem */
add_action('ssf_sync', 'ssp_stick', 20);
add_action('init', function(){ if (!get_transient('ssp_stick_chk')) { ssp_stick(); set_transient('ssp_stick_chk',1,10*MINUTE_IN_SECONDS); } });
function ssp_stick(){
  $d = ssp_data(); if (empty($d['active']) || empty($d['ssf_id'])) return;
  $ids = get_posts(['post_type'=>'post','post_status'=>'publish','meta_key'=>'ssf_id','meta_value'=>$d['ssf_id'],'numberposts'=>1,'fields'=>'ids']);
  if (!$ids) return;
  $prev = (int) get_option('ssp_sticky_id');
  if ($prev && $prev !== $ids[0]) unstick_post($prev);
  stick_post($ids[0]); update_option('ssp_sticky_id', $ids[0]);
}

function ssp_banner_html(){
  $d = ssp_data(); if (empty($d['active'])) return '';
  $e = 'esc_html'; $link = esc_url(ssp_post_link($d)); $yt = esc_url($d['youtube'] ?? '');
  $img = esc_url($d['image'] ?? '');
  ob_start(); ?>
<section class="ssp-promo" style="margin:0 auto 28px;max-width:1200px;padding:0 16px;box-sizing:border-box">
 <div style="display:flex;flex-wrap:wrap;align-items:stretch;background:#171513;color:#f2eee8;border-radius:14px;overflow:hidden;box-shadow:0 8px 28px rgba(0,0,0,.18)">
  <?php if ($img): ?><a href="<?php echo $link; ?>" style="flex:1 1 360px;min-height:220px;background:url('<?php echo $img; ?>') center/cover no-repeat;display:block" aria-label="<?php echo $e($d['title'] ?? ''); ?>"></a><?php endif; ?>
  <div style="flex:1 1 360px;padding:28px 30px;display:flex;flex-direction:column;justify-content:center;gap:10px">
   <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
    <span style="background:#E0874F;color:#171513;font:700 12px/1 sans-serif;letter-spacing:.12em;padding:7px 10px;border-radius:6px;text-transform:uppercase"><?php echo $e($d['badge'] ?? 'Nowy odcinek'); ?></span>
    <span style="font:600 13px/1.2 sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#E0874F"><?php echo $e($d['kicker'] ?? 'Zagadki Costa del Sol'); ?></span>
   </div>
   <a href="<?php echo $link; ?>" style="color:#f2eee8;text-decoration:none"><h2 style="margin:4px 0 0;font-size:30px;line-height:1.15;color:#f2eee8"><?php echo $e($d['title'] ?? ''); ?></h2></a>
   <p style="margin:0;font-size:16px;line-height:1.5;opacity:.85"><?php echo $e($d['text'] ?? ''); ?></p>
   <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:8px">
    <a href="<?php echo $link; ?>" style="background:#E0874F;color:#171513;font-weight:700;padding:11px 18px;border-radius:8px;text-decoration:none">🎧 Posłuchaj i przeczytaj</a>
    <?php if ($yt): ?><a href="<?php echo $yt; ?>" target="_blank" rel="noopener" style="border:1px solid #f2eee8;color:#f2eee8;font-weight:700;padding:10px 18px;border-radius:8px;text-decoration:none">▶ Obejrzyj na YouTube</a><?php endif; ?>
   </div>
   <?php if (!empty($d['note'])): ?><div style="font-size:13px;opacity:.6;margin-top:4px"><?php echo $e($d['note']); ?></div><?php endif; ?>
  </div>
 </div>
</section>
<?php return ob_get_clean();
}

/* baner na górze listy wpisów na stronie głównej */
add_action('loop_start', function($q){
  static $done = false;
  if ($done || is_admin() || !$q->is_main_query() || !(is_front_page() || is_home())) return;
  $done = true; echo ssp_banner_html();
});
/* gdy strona główna to strona statyczna lub motyw nie używa pętli – shortcode [solysol_promo] */
add_shortcode('solysol_promo', 'ssp_banner_html');
