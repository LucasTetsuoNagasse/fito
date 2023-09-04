<?php
if (!((key_exists("name", $_SESSION) || key_exists("email", $_SESSION)) && key_exists("password", $_SESSION))) return 1;
require "conn.php";
try {
    $query = "use " . $_ENV["MYSQL_DATABASE"] . ";";
    $conn->query($query);
    $query = "select * from users where (name = \"" . $_SESSION["name"] . "\" or email = \"" . $_SESSION["email"] . "\") and password = \"" . $_SESSION["password"] . "\";";
    $result = $conn->query($query);
    if ($result->rowCount() > 0) {
        foreach ($result as $row)
        $_SESSION["id"] = $row["id"];
        $_SESSION["name"] = $row["name"];
        $_SESSION["email"] = $row["email"];
        $_SESSION["avatar"] = $row["avatar"];
        $_SESSION["description"] = $row["description"];
        $conn = null;
        return 0;
    }
    $conn = null;
    return 2;
} catch (Exception $err) {
    $conn = null;
    return 3;
}
