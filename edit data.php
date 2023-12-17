
<?php
include 'koneksi1.php';
$no                 =$_GET['no'];
$nip                =$_POST['nip'];
$nama               =$_POST['nama'];
$golongan           =$_POST['golongan'];
$timkerja              =$_POST['tim_kerja'];
$jeniskelamin      =$_POST['jenis_kelamin'];
$jabatanstatistik  =$_POST['jabatan_statistik'];
$username           =$_POST['username'];
$query = mysqli_query($mysqli,"UPDATE `db_karyawan1` SET `nip`='$nip',`nama`='$nama',`golongan`='$golongan',`tim_kerja`='$timkerja',`jenis_kelamin`='$jeniskelamin',`jabatan_statistik`='$jabatanstatistik',`username`='$username' WHERE no='$no'");

header('location:no3DataKaryawan.php');
?>
    