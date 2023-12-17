<?php
include 'koneksi1.php';

$query= mysqli_query($mysqli, "INSERT INTO `db_karyawan1`(`no`, `nip`, `nama`, `golongan`, `tim_kerja`, `jenis kelamin`, `jabatan statistik`, `username`) 
VALUES ('','','','','','','','')");
header('location:no3DataKaryawan.php');
?>