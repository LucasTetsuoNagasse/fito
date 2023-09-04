<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Conxa</title>
    <link rel="stylesheet" href="public/css/style.css" />
</head>

<body>
    <?php
    if ((require "back/checkLogin.php") === 2) echo "<h3>Unable to login, please verify the information entered. If you don't have an account, <a href=\"signin.html\">Sign In</a></h3>"
    ?>
    <form id="login" class="basic-form main-form" action="back/crud.php" method="post">
        <h1>Login</h1>
        <label class="field">
            <span>Name</span>
            <input class="name" type="text" name="name" autocomplete="name" required autofocus />
        </label>
        <label class="field">
            <span>Email</span>
            <input class="email" type="email" name="email" autocomplete="email" required />
        </label>
        <label class="field">
            <span>Password</span>
            <input class="password" type="password" name="password" autocomplete="current-password" required />
        </label>
        <input type="hidden" name="dbQueryType" value="login" required readonly />
        <button class="submit" type="submit">Login</button>
        <menu> <a href="signin.html">Sign In</a><a href="forgotPassword.html">Forgot password ?</a></menu>
    </form>
</body>

</html>