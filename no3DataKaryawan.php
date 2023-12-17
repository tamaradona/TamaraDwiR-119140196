<?php
include 'koneksi1.php';
require 'navbar.php';
$query = mysqli_query($mysqli, "SELECT * from db_karyawan1");
?>


<!-- Page Content  -->
<center>
<h2 class="mb-4"><center>Magister Karyawan</h2>
    <label>Pencarian : </label>
    <input type="text" name="cari" placeholder= "masukkan nama" value="<?php if(isset($_GET['cari'])){echo $_GET['cari'];}?>">
    <button type="submit">cari</button>
</form>
<br>

<td><a href="tambah data.php"class="btn btn-sm btn-info"<left>Tambah Karyawan</a>
<table class="table table-bordered table-responsive" width="100%">
</td>
    <thead>
        <tr>
        <th>No</th><th>NIP</th><th>Nama</th><th>Golongan</th><th>Seksi</th><th>Jenis Kelamin</th><th>Jabatan Statistik</th><th>Username</th>
        
    <tbody>
      <?php
        include 'koneksi1.php';
        if(isset($_GET['cari'])){
          $pencarian = $_GET['cari'];
          $query= mysqli_query($mysqli, "SELECT * from db_karyawan1 WHERE nama like '%".$pencarian."%' ");
          }else{
          $query = mysqli_query($mysqli, "SELECT * from db_karyawan1");
        }
          $no=0;
          while($result = mysqli_fetch_array($query)){
              $no++;
              ?>
          <tr>
            <td><?php echo $result['no'];?></td>
            <td><?php echo $result['nip'];?></td>
            <td><?php echo $result['nama'];?></td>
            <td><?php echo $result['golongan'];?></td>
            <td><?php echo $result['tim_kerja'];?></td>
            <td><?php echo $result['jenis_kelamin'];?></td>
            <td><?php echo $result['jabatan_statistik'];?></td>
            <td><?php echo $result['username'];?></td>
            <td>
              <a href="hapus data.php?no=<?php echo $result['no'];?>" class="btn btn-sm btn-danger">Hapus</a>
              <a href="form edit.php?no=<?php echo $result['no'];?>" class="btn btn-sm btn-warning">Edit</a>
            </td>
          </tr>
          <?php }?>
          </thead>
        </tbody>
      </table>
    </center>
  </html>
<!-- End Page Content  -->

