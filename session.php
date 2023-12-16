<?php //exit(); ?>
<?php
session_start();
$session_nama = '';
$session_phone = '';

// buat session
if(isset($_POST['simpan_session'])){
	$_SESSION['session_nama'] = $_POST['nama'];
	$_SESSION['session_phone'] = $_POST['no_hp'];
	$session_nama = $_SESSION['session_nama'];
	$session_phone = $_SESSION['session_phone'];
}

// jika sudah ada session
if(!empty($_SESSION['session_nama'])){
	$session_nama = $_SESSION['session_nama'];
} else { $session_nama = ''; }
if(!empty($_SESSION['session_phone'])){
	$session_phone = $_SESSION['session_phone'];
} else { $session_phone = ''; }


// hapus session
if(isset($_POST['hapus_session'])){
	$session_nama = '';
	$session_phone = '';
	session_destroy();
}
?>
<html>
<head>
<title>Session</title>
<style>
.btn-success {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 6px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
}
.btn-danger {
  background-color:#900;
  border: none;
  color: white;
  padding: 6px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
}
</style>
</head>
<body>
<form action="#" method="post">
<table width="100%" border="0" cellpadding="6" cellspacing="1">
<tr>
	<td width="10%">Nama Lengkap</td>
    <td width=""><input type="text" name="nama" id="nama" placeholder="nama lengkap"></td>
</tr>
<tr>
	<td>Nomor HP</td>
    <td><input type="text" name="no_hp" id="no_hp" placeholder="nomor handphone"></td>
</tr>
<tr>
	<td colspan="2">
    	<button type="submit" class="btn-danger" name="hapus_session" id="hapus_session">Hapus Session</button>
        <button type="submit" class="btn-success" name="simpan_session" id="simpan_session">Buat Session</button>
    </td>
</tr>
</table>
</form>
<hr>
<h3>Data Session</h3>
<div>Nama Lengkap : <?= $session_nama; ?></div>
<div>Phone : <?= $session_phone; ?></div>

</body>
</html>