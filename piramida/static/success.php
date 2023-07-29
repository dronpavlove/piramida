<?php
    header("Content-Type: text/html; charset=utf-8");
?>
<?php
/* Осуществляем проверку вводимых данных и их защиту от враждебных 
скриптов */
$your_name = htmlspecialchars($_POST["your_name"]);
$email = htmlspecialchars($_POST["email"]);
$tema = htmlspecialchars($_POST["tema"]);
$message = htmlspecialchars($_POST["message"]);
/* Устанавливаем e-mail адресата */
$myemail = "funfot@ya.ru";
$tema = "Поступил новый заказ консультации!";

/* Создаем новую переменную, присвоив ей значение */
$message_to_myemail = "Здравствуйте! 
Вашей контактной формой было отправлено сообщение! 
Имя отправителя: $your_name 
E-mail: $email 
Текст сообщения: $message 
Конец";
/* Отправляем сообщение, используя mail() функцию */
mail($myemail, $tema, $message_to_myemail, "From: Klinkerburg <info@klinkerburg.ru> \r\n Reply-To: $name \r\n"."MIME-Version: 1.0\r\n"."Content-type: text/html; charset=utf-8\r\n" );


?>
<!DOCTYPE html>
<html style="background: transparent url("../img/first_1.jpg") no-repeat scroll center top;">
    <head>
        <meta charset="utf-8">
        <!--[if IE 9]><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><![endif]--> 
        <title>Ваше сообщение успешно отправлено, спасибо за Ваше время! </title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="/styles/style.css" rel="stylesheet" type="text/css" />
        <link rel="shortcut icon" type="image/x-icon" href="/images/favicon.png">

       
	<style>
	
	html {
	min-height: 100%;
	}
	 body {
	 font-family: "Open Sans Reg", Arial;
	 background: url(/images/wood.jpg) repeat-y center top;
	 background-size: cover;
	 }
	 
	 .thank {
	 box-shadow: 0px 0px 48px rgba(0, 0, 0, 0.33);
color: #242424;
width: 50%;
margin: 120px auto 0px;
padding: 25px;
background: rgba(255, 255, 255, 0.92) none repeat scroll 0% 0%;
border-radius: 3px;
	 }
	 
	 .thank p {
	 text-align: center;
color: #2b2b2b;
font-size: 30px;
line-height: 1.4em;
font-family: "Open Sans Bold", Arial;
position: relative;
}

.submit2 {
clear: both;
display: block;
width: 470px;
margin: 16px auto 0px;
height: 35px;
padding-top: 4px;
text-align: center;
	}
	
	.yellow-back {
	padding: 20px 30px;
background: rgb(255, 216, 0) none repeat scroll 0% 0%;
color: black;
font-size: 18px;
text-decoration: none;
font-weight: bold;
border-radius: 5px;
	}
	
.yellow-back:active {
background: rgb(240, 203, 0) none repeat scroll 0% 0%;
}
	</style>
	
	
    </head>
    <body>

<div class="thank">
<p style="text-align: center;"><b class="bold pink-color upper">Благодарим за доверие!</b><br>
<span style="font-size: 20px;">Мы свяжемся с Вами совсем скоро, чтобы познакомиться ближе.</span>
</p>

<p style="margin-top: 30px;">
<a style="padding: 20px 30px;" class="yellow-back black radius f24px centro" href="/">Вернуться назад</a>

</p>

</div>




</body>
</html>
<?php
/* Если при заполнении формы были допущены ошибки сработает 
следующий код: */
function check_input($data, $problem = "")
{
$data = trim($data);
$data = stripslashes($data);
$data = htmlspecialchars($data);
if ($problem && strlen($data) == 0)
{
show_error($problem);
}
return $data;
}
function show_error($myError)
{
?>
<html>
<body>
<p>Пожалуйста исправьте следующую ошибку:</p>
<?php echo $myError; ?>
<a style="cursor: pointer; color: rgb(143, 184, 237);" onclick="javascript:history.back();">Назад</a>
</body>
</html>
<?php
exit();
}
?> 