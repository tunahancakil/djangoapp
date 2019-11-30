{{}}

<?php
ob_start();
if(!isset($_SESSION)) 
    { 
        session_start(); 
    } 

                echo "Başarılı Bir Şekilde Eklendi !";
				header('Location: ../index.php');
            
                echo "Bir Sorun Oluştu";
            /*       
$mail_adresiniz = "tunahan@talebeyayinlari.com";
$mail_sifreniz	 = "Tolgahan123+";
$gidecek_adres	 = "siparis@talebeyayinlari.com";
$domain_adresi	 = "talebeyayinlari.com";	//www olmadan yazınız
$baslik         = "Sipariş Talep Formu";

require("include/class.php");
$mail = new PHPMail();
$mail->Host       = "smtp.".$domain_adresi;
$mail->SMTPAuth   = true;
$mail->Username   = $mail_adresiniz;
$mail->Password   = $mail_sifreniz;
$mail->IsSMTP();
$mail->AddAddress($gidecek_adres);
$mail->From       = $mail_adresiniz;
$mail->FromName   = $mail_adresiniz;
$mail->Subject    = $baslik;
$mail->Body       = $_POST["bayiad"]."\n"."\n".$_POST["mat2"].$_POST["2mat"]."\n".$_POST["mat3"].$_POST["3mat"]."\n".$_POST["mat4"].$_POST["4mat"]."\n".$_POST["mat5"].$_POST["5mat"]."\n".$_POST["mat6"].$_POST["6mat"]."\n".$_POST["mat7"].$_POST["7mat"]."\n".$_POST["mat8"].$_POST["8mat"]
."\n"."\n".$_POST["turkce5"].$_POST["5turkce"]."\n".$_POST["turkce6"].$_POST["6turkce"]."\n".$_POST["turkce7"].$_POST["7turkce"]."\n".$_POST["turkce8"].$_POST["8turkce"]."\n"."\n".
$_POST["fen5"].$_POST["5fen"]."\n".$_POST["fen6"].$_POST["6fen"]."\n".$_POST["fen7"].$_POST["7fen"]."\n".$_POST["fen8"].$_POST["8fen"];
$mail->AltBody    = "";
 
if(!$mail->Send()){
   echo "<html>\n";
   echo "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
   echo "<meta http-equiv=\"Content-Language\" content=\"tr\">\n";
   echo "\n";
   echo "<meta name=\"Author\" content=\"Talebe Yayınları Destek\">\n";
   echo "<title> Talebe Yayınları - Destek </title>\n";
   echo "</head>\n";
   echo "<body>\n";
   echo "<center>\n";
   echo "<hr width=\"500\" color=\"#C0C0C0\" style=\"border-style: double; border-width: 3px\">\n";
   echo "<font face=\"Verdana\" style=\"font-size: 8pt\"><b>[</b> <font color=\"#0000FF\">\n";
   echo "Mesajınız Gönderilirken bir hata oluştu. Sunucudan gelen cevap aşağıdaki gibidir:\n";
   echo "</font> <b>]</b></font>\n";
   echo "<br><font face=\"Verdana\" style=\"font-size: 8pt\"><b>[</b> <font color=\"#0000FF\">\n";
   echo "Hata: " . $mail->ErrorInfo;
   echo "</font> <b>]</b></font>\n";
   echo "<hr width=\"500\" color=\"#C0C0C0\" style=\"border-style: double; border-width: 3px\">\n";
   echo "</center>\n";
   echo "</body>\n";
   echo "</html>\n";
   exit;
}

   echo "<html>\n";
   echo "<head>\n";
   echo "<meta http-equiv=\"Content-Language\" content=\"tr\">\n";
   echo "\n";
   echo "<meta name=\"Author\" content=\"Talebe Yayınları Bayilik Formu\">\n";
   echo "<title>Talebe Yayınları - Bayilik Formu </title>\n";
   echo "</head>\n";
   echo "<body>\n";
   echo "<center>\n";
   echo "<hr width=\"500\" color=\"#C0C0C0\" style=\"border-style: double; border-width: 3px\">\n";
   echo "<font face=\"Verdana\" style=\"font-size: 8pt\"><b>[</b> <font color=\"#0000FF\">\n";
   echo '<a href=" ../index.php ">Sipariş isteğiniz alınmıştır. Ana Sayfaya Dönmek İçin Tıklayınız</a>';
   echo "</font> <b>]</b></font>\n";
   echo "<hr width=\"500\" color=\"#C0C0C0\" style=\"border-style: double; border-width: 3px\">\n";
   echo "</center>\n";
   echo "</body>\n";
   echo "</html>\n";
*/
?>