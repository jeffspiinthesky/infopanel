<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php
  $timestamp = $_GET['timestamp'];
  $code = $_GET['code'];
  $message = $_GET['message'];
  $vpn = $_GET['vpn'];
  echo '<p>' . $timestamp . ': ' . $vpn . '|' . $code . ': ' . $message . '</p>';
  $file = '/var/www/html/vpnstatus/' . strtolower($vpn) . '.dat';
  $output = $timestamp . '|' . $vpn . '|' . $code . '|' . $message;
  file_put_contents($file,$output);
  ?> 
  </body>
</html>
