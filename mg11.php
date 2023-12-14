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
            <input type="text" name="nama" value="<?=isset($_POST['nama']) ? $_POST['nama'] : ''?>"/>
        </div>
        <!-- elemen input number -->
        <div class="row">
            <label>No telepon</label>
            <input type="number" name="notelp" value="<?=isset($_POST['notelp']) ? $_POST['notelp'] : ''?>"/>
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
    <?php
    if (isset($_POST['submit'])) {
        echo '<h1>Hasil Input</h1>';
        echo '<ul>';
        echo '<li>Nama: ' . $_POST['nama'] . '</li>';
        echo '<li>No telepon: ' . $_POST['notelp'] . '</li>';
        echo '<li>Apakah paket lengkap (jamur dan kutu): ' . (isset($_POST['kucing']) ? $kucing[$_POST['kucing']] : '-') . '</li>';
        
        $list_jumlah = array();
        foreach ($program as $jumlah) {
            if ( isset($_POST['skill_' . $jumlah]) )
            {
                $list_jumlah[] = $jumlah;
            }
        }

        echo '<li>Jumlah kucing: ' . ($list_jumlah ? join(', ', $list_jumlah) : '-') . '</li>';
        echo '</ul>';
    }?>
    
    <!-- Tambahkan event onclick, onmouseover, dan onchange -->
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
