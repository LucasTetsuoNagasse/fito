<?php
session_start();
require "conn.php";

if (!key_exists("dbQueryType", $_POST)) {
    return;
}
try {
    foreach ($_POST as $k => $v) {
        $_POST[$k] = htmlspecialchars($v);
    }
    switch ($_POST["dbQueryType"]) {
        case "signin":
            $query = "use " . $_ENV["MYSQL_DATABASE"] . ";";
            $conn->query($query);
            $_SESSION["name"] = $_POST["name"];
            $_SESSION["email"] = $_POST["email"];
            $_SESSION["password"] = $_POST["password"];
            $_SESSION["avatar"] = false;
            $_SESSION["description"] = "";
            $result = $conn->query("insert into users (name, email, password) values (\"" . $_SESSION["name"] . "\",\"" . $_SESSION["email"] . "\",\"" . $_SESSION["password"] . "\");");
            header("location:" . $_SERVER["SCRIPT_NAME"] . "/../../index.php");
            break;
        case "login":
            $_SESSION["name"] = $_POST["name"];
            $_SESSION["email"] = $_POST["email"];
            $_SESSION["password"] = $_POST["password"];
            header("location:" . $_SERVER["SCRIPT_NAME"] . "/../../index.php");
            break;
        case "updateProfile":
            if (!key_exists("id", $_SESSION)) {
                session_destroy();
                header("location:" . $_SERVER["SCRIPT_NAME"] . "/../../index.php");
                return 1;
            }
            if (require "uploadAvatar.php" === 0) { // if the database gets an error, the session will be wrong, maybe a session_destroy() in catch will solve
                $_SESSION["avatar"] = true;
            }
            if ($_POST["name"] !== "") {
                $_SESSION["name"] = $_POST["name"];
            }
            if ($_POST["email"] !== "") {
                $_SESSION["email"] = $_POST["email"];
            }
            if ($_POST["description"] !== "") {
                $_SESSION["description"] = $_POST["description"];
            }
            $query = "use " . $_ENV["MYSQL_DATABASE"] . ";";
            $conn->query($query);
            $result = $conn->query("update set (name = \"" . $_SESSION["name"] . "\", email = \"" . $_SESSION["email"] . "\", description = \"" . $_SESSION["description"] . "\", avatar = \"" . $_SESSION["avatar"] . "\") where id = " . $_SESSION["id"] . " and password = \"" . $_SESSION["password"] . "\";");
            break;
        case "changePassword":
            $query = "";
            break;
        case "deleteProfile":
            $query = "";
            break;
    }
    $conn = null;
} catch (Exception $err) {
    $conn = null;
    return $err;
}
