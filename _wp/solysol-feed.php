<?php
/*
Plugin Name: Sol y Sól – automatyczne wiadomości
Description: Co 15 minut pobiera nowe artykuły z repozytorium Oliwiana/solysol-media (articles/index.json) i publikuje je jako wpisy.
*/
if (!defined('ABSPATH')) exit;
define('SSF_BASE', 'https://raw.githubusercontent.com/Oliwiana/solysol-media/main/');

add_filter('cron_schedules', function($s){ $s['ssf15']=['interval'=>900,'display'=>'Co 15 min']; return $s; });
add_action('init', function(){ if(!wp_next_scheduled('ssf_sync')) wp_schedule_event(time()+60,'ssf15','ssf_sync'); });
add_action('ssf_sync','ssf_sync');
add_action('init', function(){ if(isset($_GET['ssf_sync']) && $_GET['ssf_sync']==='sys7731'){ $r=ssf_sync(); header('Content-Type: text/plain'); echo $r; exit; } });

function ssf_get($path){
  $r = wp_remote_get(SSF_BASE.$path.'?t='.time(), ['timeout'=>30]);
  if (is_wp_error($r) || wp_remote_retrieve_response_code($r)!==200) return null;
  return wp_remote_retrieve_body($r);
}
function ssf_term($name,$tax){
  $t = term_exists($name,$tax);
  if(!$t) $t = wp_insert_term($name,$tax);
  return is_wp_error($t)?0:(int)(is_array($t)?$t['term_id']:$t);
}
function ssf_sync(){
  $idx = json_decode(ssf_get('articles/index.json') ?: '[]', true);
  if(!is_array($idx)) return 'no index';
  require_once ABSPATH.'wp-admin/includes/media.php';
  require_once ABSPATH.'wp-admin/includes/file.php';
  require_once ABSPATH.'wp-admin/includes/image.php';
  $out=[];
  foreach(array_slice($idx,-30) as $id){
    $id = preg_replace('/[^a-z0-9\-]/','',strtolower($id));
    if(!$id) continue;
    $ex = get_posts(['post_type'=>'post','post_status'=>'any','meta_key'=>'ssf_id','meta_value'=>$id,'numberposts'=>1,'fields'=>'ids']);
    if($ex){ continue; }
    $a = json_decode(ssf_get("articles/$id.json") ?: 'null', true);
    if(!$a || empty($a['title']) || empty($a['html'])) { $out[]="$id: bad"; continue; }
    $cat = ssf_term($a['category'] ?? 'Wiadomości','category');
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
    update_post_meta($pid,'ssf_id',$id);
    if(!empty($a['image'])){
      $tmp = download_url(SSF_BASE.ltrim($a['image'],'/'));
      if(!is_wp_error($tmp)){
        $fa = ['name'=>$id.'.jpg','tmp_name'=>$tmp];
        $mid = media_handle_sideload($fa,$pid,$a['title']);
        if(!is_wp_error($mid)) set_post_thumbnail($pid,$mid); else @unlink($tmp);
      }
    }
    $out[]="$id: ok ".get_permalink($pid);
  }
  return implode("\n",$out) ?: 'nothing new';
}
