{{}}

<?php/*
ob_start();
if(!isset($_SESSION)) 
    { 
        session_start(); 
    } 

                echo "Başarılı Bir Şekilde Eklendi !";
				header('Location: ../index.php');
            
                echo "Bir Sorun Oluştu";
       */       
$mail_adresiniz = "info@ttyazilim.net";
$mail_sifreniz	 = "Tolgahan123+";
$gidecek_adres	 = "cakil@ttyazilim.net";
$domain_adresi	 = "ttyazilim.net";	//www olmadan yazınız
$baslik         = "Bilgilendirme";

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
$mail->Body       = "Merhaba Tunahan!";
 
if(!$mail->Send()){
   echo "<html>\n";
   echo "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=windows-1254\">\n";
   echo "<meta http-equiv=\"Content-Language\" content=\"tr\">\n";
   echo "\n";
   echo "<meta name=\"Author\" content=\"TT Yazılım\">\n";
   echo "<title> TT Yazılım - Destek </title>\n";
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
   echo "<meta name=\"Author\" content=\"TT Yazılım\">\n";
   echo "<title>TT Yazılım</title>\n";
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