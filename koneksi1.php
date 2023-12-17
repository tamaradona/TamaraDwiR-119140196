<?php
$host="localhost";
$dbname ="root";
$user="";
$pass="db_karyawan1";

$mysqli = mysqli_connect($host,$dbname,$user,$pass);
if(!$mysqli){
    die ("Gagal menampilkan database ".mysql_connect_error());
}
//echo "berhasil";
?>
