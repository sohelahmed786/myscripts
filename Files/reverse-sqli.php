<?php
//some comment
$out = explode("\n", urldecode(
    `strings 400.pcap  | egrep "GET|Content-Length" | grep -A1 LIMIT`
));

$score = array();
$lastk = '';

for($i = 0; $i < count($out); $i += 2) {
    $out[$i] = trim(preg_replace('!\s+!', ' ',
        preg_replace('/[^0-9 ]/', "", $out[$i])
    ));

    $p = explode(" ", $out[$i]);

    if (count($p) < 6)
        continue;

    if (substr($out[$i+1],0,16) != "Content-Length: ")
        continue;

    $p[] = trim(substr($out[$i+1], 16));
    $p   = array_slice($p, -6, 6);

    $k = $p[0].$p[1].$p[2];

    if ($k!=$lastk) {
        $score[] = 0;
    }

    if ($p[5] == "4")
        $p[3]++;

    $score[count($score)-1]=$p[3];
    $lastk = $k;
}

foreach ($score as $key => $val) {
    if($val==1)
        $val=0x0a;

    echo chr($val);
}
?>
