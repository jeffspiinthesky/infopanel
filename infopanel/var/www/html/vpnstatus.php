<?php
  $files = glob('vpnstatus/*.dat', GLOB_BRACE);
  header('Content-Type: application/xml');
?>
    <table width="768" cellpadding="0" border="1">
      <th width="15%">Age</th>
      <th width="20%">Item</th>
      <th width="10%">Code</th>
      <th width="55%">Message</th>
<?php
foreach($files as $file) {
  $currentTime = time();

  $status=file_get_contents($file, FILE_USE_INCLUDE_PATH);
  $split_text = preg_split("/\|/",$status);
  $sendTime = $split_text[0];
  $deltaTime = $currentTime-$sendTime;
  if( $deltaTime > 180 && $deltaTime < 360) {
    $timeBgcolor="#FFFF00";
  }
  elseif($deltaTime >= 360) {
    $timeBgcolor="#FF0000";
  }
  else {
    $timeBgcolor="#00FF00";
  }
  if( $deltaTime >= 3600 && $deltaTime < 86400 ) {
    $timeUnit="h";
    $deltaTime/=3600;
  }
  elseif( $deltaTime >= 60 && $deltaTime < 3600 ) {
    $timeUnit="m";
    $deltaTime/=60;
  }
  elseif( $deltaTime > 86400 ) {
    $timeUnit="d";
    $deltaTime/=86400;
  }
  else {
    $timeUnit="s";
  }
  if( $split_text[2] == '200' ) {
    $statusBgcolor="#00FF00";
  }
  else {
    $statusBgcolor="#FF0000";
  }
  print '      <tr><td bgcolor="' . $timeBgcolor . '">' . round($deltaTime,2) . $timeUnit . '</td><td bgcolor="' . $statusBgcolor . '">' . $split_text[1] . '</td><td bgcolor="' . $statusBgcolor . '">' . $split_text[2] . '</td><td bgcolor="' . $statusBgcolor . '">' . $split_text[3] . '</td></tr>' . "\xA";
}
?>
    </table>
