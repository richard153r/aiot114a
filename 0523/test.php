<?php
$name = $_POST["name"];
$sex = $_POST["sex"];
$edu = $_POST["edu"];  
$addr = $_POST["addr"]; 
$opinion = $_POST["opinion"];
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>表單結果</title>
</head>
<body bgcolor="#d1fce8">
    <?php 
     if($sex == "男生"){
        echo "<h2>".$name."先生 您好</h2>";

     }else{
        echo "<h2>".$name."小姐 您好</h2>";
     }
     echo "您的學歷：".$edu."<br>";
     echo "您喜歡下列哪些活動如下：<br>";
     $hobby = $_POST["hobby"]; 
     echo "<ul>";
     foreach( $_POST["hobby"] as $value){
        echo "<li>".$value."</li>";
     }
     echo "</ul>";
     echo "您的意見：<br>".$opinion."<br>";
    ?>
</body>
</html>