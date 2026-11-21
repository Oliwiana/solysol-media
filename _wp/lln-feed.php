<?php
/*
Plugin Name: LLN Marbella – wpisy z aplikacji Redakcja
Description: Co 15 minut pobiera zaakceptowane wpisy (lln/articles/index.json z repozytorium) i publikuje je na blogu llnmarbella.com. Publikuje wyłącznie to, co zostało zaakceptowane w aplikacji.
Version: 1.0
*/
if (!defined('ABSPATH')) exit;
define('LLNF_BASE', 'https://raw.githubusercontent.com/Oliwiana/solysol-media/main/');

add_filter('cron_schedules', function($s){ $s['llnf15']=['interval'=>900,'display'=>'Co 15 min']; return $s; });
add_action('init', function(){ if(!wp_next_scheduled('llnf_sync')) wp_schedule_event(time()+60,'llnf15','llnf_sync'); });
add_action('llnf_sync','llnf_sync');
add_action('init', function(){ if(isset($_GET['llnf_sync']) && $_GET['llnf_sync']==='lln5193'){ $r=llnf_sync(); header('Content-Type: text/plain'); echo $r; exit; } });
register_deactivation_hook(__FILE__, function(){ wp_clear_scheduled_hook('llnf_sync'); });

function llnf_get($path){
  $r = wp_remote_get(LLNF_BASE.$path.'?t='.time(), ['timeout'=>30]);
  if (is_wp_error($r) || wp_remote_retrieve_response_code($r)!==200) return null;
  return wp_remote_retrieve_body($r);
}
function llnf_term($name){
  $t = term_exists($name,'category');
  if(!$t) $t = wp_insert_term($name,'category');
  return is_wp_error($t)?0:(int)(is_array($t)?$t['term_id']:$t);
}
function llnf_thumb($pid,$a,$id){
  if(empty($a['image'])) return false;
  $tmp = download_url(LLNF_BASE.ltrim($a['image'],'/').'?t='.time());
  if(is_wp_error($tmp)) return false;
  $mid = media_handle_sideload(['name'=>$id.'.jpg','tmp_name'=>$tmp],$pid,$a['title']);
  if(is_wp_error($mid)){ @unlink($tmp); return false; }
  set_post_thumbnail($pid,$mid); return true;
}
function llnf_sync(){
  $idx = json_decode(llnf_get('lln/articles/index.json') ?: '[]', true);
  if(!is_array($idx)) return 'no index';
  require_once ABSPATH.'wp-admin/includes/media.php';
  require_once ABSPATH.'wp-admin/includes/file.php';
  require_once ABSPATH.'wp-admin/includes/image.php';
  $out=[];
  foreach(array_slice($idx,-30) as $id){
    $id = preg_replace('/[^a-z0-9\-]/','',strtolower($id));
    if(!$id) continue;
    $ex = get_posts(['post_type'=>'post','post_status'=>'any','meta_key'=>'llnf_id','meta_value'=>$id,'numberposts'=>1,'fields'=>'ids']);
    $a = json_decode(llnf_get("lln/articles/$id.json") ?: 'null', true);
    if($ex){
      $pid=$ex[0]; $rev=(int)($a['rev'] ?? 1);
      if($a && $rev > (int)get_post_meta($pid,'llnf_rev',true)){
        wp_update_post(['ID'=>$pid,'post_title'=>wp_strip_all_tags($a['title']),'post_content'=>wp_kses_post($a['html']),'post_excerpt'=>wp_strip_all_tags($a['excerpt'] ?? '')]);
        update_post_meta($pid,'llnf_rev',$rev); $out[]="$id: updated";
      }
      continue;
    }
    if(!$a || empty($a['title']) || empty($a['html'])) { $out[]="$id: bad"; continue; }
    $cat = llnf_term($a['category'] ?? 'Wybór ofert');
    $pid = wp_insert_post([
      'post_title'=>wp_strip_all_tags($a['title']),
      'post_content'=>wp_kses_post($a['html']),
      'post_excerpt'=>wp_strip_all_tags($a['excerpt'] ?? ''),
      'post_status'=>'publish','post_type'=>'post',
      'post_category'=>$cat?[$cat]:[],
      'tags_input'=>$a['tags'] ?? [],
      'post_name'=>sanitize_title($a['slug'] ?? $a['title']),
    ], true);
    if(is_wp_error($pid)){ $out[]="$id: ".$pid->get_error_message(); continue; }
    update_post_meta($pid,'llnf_id',$id);
    update_post_meta($pid,'llnf_rev',(int)($a['rev'] ?? 1));
    llnf_thumb($pid,$a,$id);
    $out[]="$id: ok ".get_permalink($pid);
  }
  return implode("\n",$out) ?: 'nothing new';
}
