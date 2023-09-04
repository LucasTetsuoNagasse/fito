<?php
session_start();
if ((require "back/checkLogin.php") !== 0) {
    header("location:" . $_SERVER["SCRIPT_NAME"] . "/../login.php");
};
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
    <main class="basic-main">
        <form id="info" class="basic-form" action="../crud.php" method="post">
            <div class="avatar">
                <img class="img" src="<?php if ($_SESSION["avatar"]) echo "public/imgs/avatars/" . $_SESSION["id"] . ".png";
                                        else  echo "public/imgs/avatars/defaultAvatar.png"; ?>" alt="avatar.png">
                <label>
                    <input type="file" name="avatar" hidden>
                </label>
            </div>
            <button class="submit" type="submit">Save</button>
            <input class="name" type="text" name="name" value="<?php echo $_SESSION["name"]; ?>" autocomplete="name" />
            <input class="email" type="email" name="email" value="<?php echo $_SESSION["email"]; ?>" autocomplete="email" />
            <textarea class="description" type="textarea" name="description" value="<?php echo $_SESSION["description"]; ?>" rows="15"></textarea>
            <input type="hidden" name="dbQueryType" value="updateProfile" required readonly />
        </form>
        <div id="accountSettings">
            <form id="changePassword" class="basic-form" action="../crud.php" method="post">
                <h2>Change password</h2>
                <label class="field">
                    <span>Password</span>
                    <input class="password" type="password" name="password" autocomplete="current-password" required />
                </label>
                <label class="field">
                    <span>New Password</span>
                    <input class="new-password" type="password" name="newPassword" autocomplete="new-password" required />
                </label>
                <input type="hidden" name="dbQueryType" value="changePassword" required readonly />
                <button class="submit" type="submit">Change Password</button>
            </form>
            <form id="deleteProfile" class="basic-form" action="../crud.php" method="post">
                <h2>Delete account</h2>
                <label class="field">
                    <span>Name</span>
                    <input class="name" type="text" name="name" autocomplete="name" required />
                </label>
                <label class="field">
                    <span>Email</span>
                    <input class="email" type="email" name="email" autocomplete="email" required />
                </label>
                <label class="field">
                    <span>Password</span>
                    <input class="password" type="password" name="password" autocomplete="current-password" required />
                </label>
                <input type="hidden" name="dbQueryType" value="deleteAccount" required readonly />
                <button class="submit" type="submit">Delete Account</button>
            </form>
        </div>
    </main>
    <footer class="basic-footer">
        <div class="credits">
            <h3>Credits:</h3>
            <p>NineChu</p>
        </div>
    </footer>
</body>

</html>