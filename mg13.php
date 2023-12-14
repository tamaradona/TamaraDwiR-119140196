<?php

class User {
    private $nama;
    private $notelp;
    private $kucing;
    private $jumlahKucing;

    public function setUserData($nama, $notelp, $kucing, $jumlahKucing) {
        $this->nama = $nama;
        $this->notelp = $notelp;
        $this->kucing = $kucing;
        $this->jumlahKucing = $jumlahKucing;
    }

    public function getUserData() {
        return [
            'nama' => $this->nama,
            'notelp' => $this->notelp,
            'kucing' => $this->kucing,
            'jumlahKucing' => $this->jumlahKucing,
        ];
    }
}

$userObj = new User();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nama = test_input($_POST["nama"]);
    $notelp = test_input($_POST["notelp"]);
    $kucing = test_input($_POST["kucing"]);
    
    $jumlahKucing = array();
    foreach ($program as $jumlahKucing) {
        if (isset($_POST['skill_' . $jumlahKucing])) {
        }
    }

    // Validasi nama (tidak boleh kosong dan hanya huruf dan spasi)
    if (empty($name)) {
        echo "<p>Nama harus diisi.</p>";
    } elseif (!preg_match("/^[a-zA-Z ]*$/", $name)) {
        echo "<p>Nama hanya boleh berisi huruf dan spasi.</p>";
    }

    // Validasi no telepon (tidak boleh kosong )
    if (empty($notelp)) {
        echo "<p>Nomor telepon harus diisi.</p>";
    }

    // Jika tidak ada kesalahan validasi, lanjutkan dengan pengolahan data
    if (empty($nama_err) && empty($notelp_err)) {
        // Mengatur data pengguna menggunakan metode setUserData
        $userObj->setUserData($nama, $notelp, $kucing, $jumlahKucing);

        echo '<h1>Hasil Input</h1>';
        echo '<ul>';
        echo '<li>Nama: ' . $nama . '</li>';
        echo '<li>No telepon: ' . $notelp . '</li>';
        echo '<li>Apakah paket lengkap (jamur dan kutu): ' . ($kucing ? $kucing : '-') . '</li>';
        echo '<li>Jumlah kucing: ' . ($jumlahKucing ? join(', ', $jumlahKucing) : '-') . '</li>';
        echo '</ul>';
    }
}

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Pemandian Kucing "Joy Pet"</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .row {
            margin: 10px 0;
        }

        .options {
            display: flex;
            gap: 10px;
        }

        .radio, .checkbox {
            display: flex;
        }
    </style>
</head>
<body>

    <h1>Form Pemandian Kucing "Joy Pet"</h1>
    <form action="" method="post">
        <!-- elemen input text -->
        <div class="row">
            <label>Nama</label>
            <input type="text" name="nama" value="<?= isset($_POST['nama']) ? htmlspecialchars($_POST['nama']) : '' ?>"/>
        </div>
        <!-- elemen input number -->
        <div class="row">
            <label>No telepon</label>
            <input type="number" name="notelp" value="<?= isset($_POST['notelp']) ? htmlspecialchars($_POST['notelp']) : '' ?>"/>
        </div>
        <!-- elemen input option -->
        <div class="row">
            <label>Apakah anda akan memandikan kucing paket lengkap(kutu dan jamur) ?</label>
            <div class="options">
                <?php
                $kucing = array('I' => 'iya', 'T' => 'tidak');
                foreach ($kucing as $kode => $detail) {
                    $checked = @$_POST['kucing'] == $kode ? ' checked="checked"' : '';
                    echo '<label class="radio">
                            <input name="kucing" type="radio" value="' . $kode . '"' . $checked . '>' . $detail . '</option>
                        </label>';
                }
                ?>
            </div>
        </div>
        <!-- elemen input checkbox -->
        <div class="row">
            <label>Ada berapa kucing yang ingin dimandikan ?(pilih salah satu)</label>
            <div class="options">
                <?php 
                $program = array('1', '2', '3', '4', '5', '6');
                foreach ($program as $jumlah) {
                    $checked = isset($_POST['skill_' . $jumlah]) ? ' checked="checked"' : '';
                    echo '<label class="checkbox">
                            <input type="checkbox" name="skill_' . $jumlah . '"' . $checked . '>' . $jumlah . 
                        '</label>';
                }
                ?>
            </div>
        </div>
        
        <div class="row">
            <input type="submit" name="submit" value="Simpan"/>
        </div>
    </form>

    <!-- Event onclick, onmouseover, dan onchange -->
    <button onclick="handleClick()">Klik saya</button>

    <p onmouseover="handleMouseOver()">Hover saya</p>

    <input type="text" id="textInput" onchange="handleChange()" placeholder="Type something">

    <script>
        // Function untuk event click
        function handleClick() {
            alert('Button diklik!');
        }

        // Function untuk event mouseover
        function handleMouseOver() {
            alert('Mouse di atas elemen!');
        }

        // Function untuk event change
        function handleChange() {
            var inputText = document.getElementById('textInput').value;
            alert('Nilai berubah: ' + inputText);
        }
    </script>
</body>
</html>
