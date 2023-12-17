<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<!doctype html>
<html lang="en">
<head>
  	<title>Magister Karyawan</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900" rel="stylesheet">
		
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
		<link rel="stylesheet" href="css/style.css">
    </head>
  <body>
		
		<div class="wrapper d-flex align-items-stretch">
			<nav id="sidebar">
				<div class="custom-menu">
					<button type="button" id="sidebarCollapse" class="btn btn-primary">
	          <i class="fa fa-bars"></i>
	          <span class="sr-only">Toggle Menu</span>
	        </button>
        </div>
	  		<h1><a href="index.html" class="logo">Project Name</a></h1>
        <ul class="list-unstyled components mb-5">
          <li class="active">
            <a href="homepage.php"><span class="fa fa-home mr-3"></span> Homepage</a>
          </li>
          <li>
              <a href="#"><span class="fa fa-user mr-3" href="#!"></span> Dashboard</a>
          </li>
          <li>
            <a href="#"><span class="fa fa-edit mr-3" href="#!"></span> Penilaian Kinerja</a>
          </li>
          <li>
            <a href="#"><span class="fa fa-money mr-3" href="#!"></span> Honor Kegiatan</a>
          </li>
          <li>
            <a href="#"><span class="fa fa-sticky-note mr-3" ></span> Master Pegawai</a>
          </li>
          <li>
            <a href="#"><span class="fa fa-sticky-note mr-3" ></span> Master Mitra</a>
          </li>
          <li>
            <a href="#"><span class="fa fa-sticky-note mr-3" ></span> Master Kegiatan</a>
          </li>
          <li>
            <a href="logout.php"><span class="fa fa-sign-out mr-3"></span> Sign Out</a>
          </li>
        </ul>

    	</nav>
  <!-- Page Content  -->
  <div id="content" class="p-4 p-md-5 pt-5">
      <h2 class="mb-4"><center>Edit Magister Karyawan</h2>
		  
<form action="edit data.php?no=<?php echo $_GET['no'];?>" method="post">
  <div class="form-row">
    <div class="form-group col-md-6">
      <label for="inputEmail4">NIP</label>
      <input type="text" class="form-control" id="inputNIP" placeholder="nip" name="nip" required>
    </div>
  <div class="form-group">
    <label for="inputAddress">nama</label>
    <input type="text" class="form-control" id="inputNama" placeholder="" name="nama" required>
  </div>
  </div>
  <div class="form-group">
    <label for="inputAddress">Golongan</label>
    <input type="text" class="form-control" id="inputGolongan" placeholder="golongan" name="golongan" required>
  </div>
  <div class="form-group">
    <label for="inputAddress2">Tim Kerja</label>
    <select id="inputAddress2" class="form-control" id="inputSeksi" name="tim_kerja" required>
    <option selected>Pilih..</option>
    <option>umum</option>
    <option>exksk</option>
    <option>IPDS</option>
    <option>produksi</option>
    <option>sosial</option>
    <option>distribusi</option>
    <option>nerwils</option>
</select>
  </div>
  <div class="form-row">
    <div class="form-group col-md-6">
      <label for="inputCity">Jenis Kelamin</label>
      <select id= "inputCity" class="form-control" id="inputJenisKelamin" name="jenis_kelamin" required>
        <option selected>Pilih..</option>
        <option>laki-Laki</option>
        <option>perempuan</option>
    </select>
    </div>
  </div>
  <div class="form-group">
    <label for="inputAddress">Jabatan Statistik</label>
    <select id="inputAddress" class="form-control" id="inputJabatanStatistik" name="jabatan_statistik" required>
    <option selected>Pilih..</option>
    <option>Kepala BPS Kabupaten/Kota</option>
    <option>Statisi Pelaksana BPS Kabupaten/Kota</option>
    <option>Statisi Pertama BPS Kabupaten/Kota</option>
    <option>Staf BPS Kabupaten/Kota</option>
    <option>Statisi Muda BPS Kabupaten/Kota</option>
    <option>Fungsional Umum BPS Kabupaten/Kota</option>
</select>
  </div>
  <div class="form-row">
  <div class="form-group col-md-6">
      <label for="inputCity2">Username</label>
      <input type="text" class="form-control" id="inputUsername" placeholder="username" name="username" required>
  </div>
</div>

  <button type="submit" class="btn btn-primary">Simpan</button>
</form>

