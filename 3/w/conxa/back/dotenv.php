<?php
$dotenv = file(__DIR__ . "/.env", FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
if (is_array($dotenv)) {
    foreach ($dotenv as $line) {
        $kv = explode("=", $line);
        $_ENV[$kv[0]] = $kv[1];
    }
}
