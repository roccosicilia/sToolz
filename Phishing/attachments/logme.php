<?php

###################################################################################################
#
# Log INFO from trackme.py
# Author: Rocco <Sheliak> Sicilia
#
###################################################################################################

// env var
$logpath = '/var/www/html/logs';

if (isset($_GET["os_ver"]) && isset($_GET["hostname"]) && isset($_GET["local_ip"]))
{
    // check vars
    $os_ver = addslashes(stripslashes($_GET["os_ver"]));
    $hostname = addslashes(stripslashes($_GET["hostname"]));
    $local_ip = addslashes(stripslashes($_GET["local_ip"]));

    $logfile = fopen("$logpath/target-info.log", "a");
    $time = date("Y-m-d H:i:s");
    $log = "[$time] $os_ver | $hostname | $local_ip \n";
    fwrite($logfile, $log);
    fclose($logfile);

    // print vars - debug
    echo "<h2>Test server for trackme.py /* add entry */</h2>\n";
    echo "Your OS is <b>$os_ver</b>, the hostname is <b>$hostname</b> and your local IP is <b>$local_ip</b>.\n";
}
else
{
    echo "<h2>Test server for trackme.py /* report */</h2>\n";
    $logfile = fopen("$logpath/target-info.log", "r");
    $out = fread($logfile,filesize("$logpath/target-info.log"));
    $out = str_replace("\n", "<br />\n", $out);
    echo "$out";
    fclose($logfile);
}

?>
