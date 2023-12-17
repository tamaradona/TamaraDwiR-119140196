SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `data_karyawan1` (
  `no` int(11) NOT NULL,
  `nip` varchar(50) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `golongan` varchar(20) NOT NULL,
  `tim_kerja` varchar(20) NOT NULL,
  `jenis_kelamin` varchar(20) NOT NULL,
  `jabatan_statistik` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `data_karyawan1`
  ADD PRIMARY KEY (`no`);
COMMIT;