<?php

$command = escapeshellcmd('python idkeeper.py');
$output = shell_exec($command);
echo "<p>".$output."</p";

?>
