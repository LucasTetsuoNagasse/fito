<?php
require "dotenv.php";
//  . ";dbname=" . $_ENV["MYSQL_DATABASE"]
try {
    $conn = new PDO("mysql:host=" . $_ENV["MYSQL_HOST"] . ";port=" . $_ENV["MYSQL_PORT"], $_ENV["MYSQL_USERNAME"], $_ENV["MYSQL_PASSWORD"] | "");
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    return 0;
} catch (PDOException $err) {
    return $err;
}
