<?php
$xml=("http://feeds.bbci.co.uk/news/rss.xml?edition=uk");

$xmlDoc = new DOMDocument();
$xmlDoc->load($xml);

//get elements from "<channel>"
$channel=$xmlDoc->getElementsByTagName('channel')->item(0);
$channel_title = $channel->getElementsByTagName('title')
->item(0)->childNodes->item(0)->nodeValue;
$channel_link = $channel->getElementsByTagName('link')
->item(0)->childNodes->item(0)->nodeValue;
$channel_desc = $channel->getElementsByTagName('description')
->item(0)->childNodes->item(0)->nodeValue;
$channel_image = $channel->getElementsByTagName('image')
->item(0)->getElementsByTagName('url')->item(0)->nodeValue;

//get and output "<item>" elements
$x=$xmlDoc->getElementsByTagName('item');
for ($i=0; $i<=4; $i++) {
  $item_title=$x->item($i)->getElementsByTagName('title')
  ->item(0)->childNodes->item(0)->nodeValue;
  $item_link=$x->item($i)->getElementsByTagName('link')
  ->item(0)->childNodes->item(0)->nodeValue;
  $item_desc=$x->item($i)->getElementsByTagName('description')
  ->item(0)->childNodes->item(0)->nodeValue;
  $item_thumbnail=$x->item($i)->getElementsByTagNameNS('http://search.yahoo.com/mrss/','thumbnail')
  ->item(0)->getAttribute('url');
  //$item_thumbnail="http://localhost/dummy.jpg";
  echo ("<div class='newsItem'><div class='channel'><img class='channelImage' src='" . $channel_image . "' style='display: block'/></div><div class='headline'>" . $item_title . "</div><div class='thumbnail'><img class='channelImage' src='" . $item_thumbnail . "'/></div></div>");
}
?>
