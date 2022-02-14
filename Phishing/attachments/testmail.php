<?php

/* test - work in progress */

$sender = "";
$repicient = "";
$subject = "Test mail from php";
$headers = "From: $sender\r\n";
$headers .= "Reply-To: $sender\r\n";
$headers .= "X-Mailer: PHP");

# content
$username = "Test User";
$link = "";
$hidden_content = "";

$message = "";
$message .= "Hi $username, \r\n";
$message .= "Link: $link";
$message .= "Hidden content: ";

mail($repicient, $subject, $message, $headers);

?>