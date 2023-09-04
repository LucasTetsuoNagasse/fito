<?php
if (key_exists("uploadAvatar", $_FILES)) {
    $file = $_FILES["uploadAvatar"];
}
if ($file["error"] === 0) {
    $fileName = "public/imgs/avatars/" . basename($file["name"]);
    if ($file["size"] > 524288) {
        echo "Sorry, your file is too large.";
        return 1;
    }
    $imageFileType = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
    if (
        $imageFileType !== "jpg" && $imageFileType !== "png" && $imageFileType !== "jpeg"
        && $imageFileType !== "gif"
    ) {
        echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
        return 9;
    }
    if (!getimagesize($file["tmp_name"])) {
        echo "File is not an image.";
        return 10;
    }
    if (!move_uploaded_file($file["tmp_name"], $fileName)) {
        echo "Sorry, there was an error uploading your file.";
        return 11;
    }
    return 0;
}
return $file["error"];
