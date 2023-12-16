<?php //exit(); ?>
<html>
<head>
<title>Local Storage</title>
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
<script src="<?= ''; ?>https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    });
    
    document.onkeydown = function(e) {
        if(event.keyCode == 123) {
            return false;
        }
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
            return false;
        }
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
            return false;
        }
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
            return false;
        }
        if(e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
            return false;
        }
    }
</script>
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
    	<button type="button" class="btn-danger" name="hapus_session" id="hapus_session" onClick="remove_storage()">Hapus Local Storage</button>
        <button type="button" class="btn-success" name="simpan_session" id="simpan_session" onClick="create_storage()">Buat Local Storage</button>
    </td>
</tr>
</table>
</form>
<hr>
<h3>Data Local Storage</h3>
<div>Nama Lengkap : <span id="session_nama"></span> </div>
<div>Phone : <span id="session_phone"></span></div>


<!-- buat local storage -->
<script>
function create_storage()
{
	// localStorage.setItem('shownotif','hidenotif_1');
	// localStorage.getItem('shownotif');
	var nama = $("#nama").val();
	var no_hp = $("#no_hp").val();
	localStorage.setItem('session_nama',nama);
	localStorage.setItem('session_phone',no_hp);
	$("#session_nama").html(nama);
	$("#session_phone").html(no_hp);
}

function remove_storage()
{
	localStorage.setItem('session_nama',"");
	localStorage.setItem('session_phone',"");
	$("#session_nama").html('');
	$("#session_phone").html('');
}

$(document).ready(function() {
	if(localStorage.getItem('session_nama')!=''){
		$("#session_nama").html(localStorage.getItem('session_nama'));
	}
	if(localStorage.getItem('session_phone')!=''){
		$("#session_phone").html(localStorage.getItem('session_phone'));
	}
});
</script>

</body>
</html>
