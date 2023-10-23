<?php
session_start();
if ($_SESSION["username"])
  $_SESSION["username"] = $_POST["username"];
$_SESSION["email"] = $_POST["email"];
$_SESSION["password"] = $_POST["password"];
header("location:../index.php");
