<?php
session_start();
if (!$_SESSION["email"] || $_SESSION["email"] == "" || !$_SESSION["password"] || $_SESSION["password"] == "") {
  header("location:views/login.html");
}
?>
<html>

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="default-style" content="defaultstyle" />
  <link title="defaultStyle" rel="stylesheet" href="/public/css/defaultStyle.css" />
  <title>Home</title>
</head>

<body>
  <main class="basic-main">
    <?php
    if ($_SESSION["username"])
      echo "<p>Username: " . $_SESSION["username"] . "</p>";
    ?>
    <p>Email: <?php echo $_SESSION["email"] ?></p>
    <p>Password: <?php echo $_SESSION["password"] ?></p>
    <a href="./models/logout.php">Logout</a>
  </main>
</body>

</html>