-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 17, 2021 at 07:43 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test_qr`
--

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `medicine_id` int(11) NOT NULL,
  `medicine_name` varchar(255) NOT NULL,
  `medicine_formulation` varchar(255) NOT NULL,
  `medicine_description` varchar(255) NOT NULL,
  `medicine_dosage` int(11) NOT NULL,
  `medicine_frequency` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`medicine_id`, `medicine_name`, `medicine_formulation`, `medicine_description`, `medicine_dosage`, `medicine_frequency`) VALUES
(1, 'Telmisartan Amlodipine besilate \r\n', 'Each tablet contains: telmisartan 40mg amlodipine 5mg', 'For the treatment of hypertension, alone or with other antihypertensive agents to lower blood pressure.\r\n', 40, 1),
(2, 'Losartan Potassium', 'Is available as tablets for oral administration containing either 25 mg, 50 mg or 100 mg of losartan potassium', 'A prescription medicine used to treat the symptoms of high blood pressure (hypertension), lower the risk of stroke in certain people with heart disease and diabetic nerve pain (neuropathy). Cozaar may be used alone or with other medications.', 50, 1),
(3, 'Benazepril hydrochloride', 'Lotensin is supplied as tablets containing 10 mg, 20 mg, and 40 mg of benazepril hydrochloride for oral administration.', 'Used for the treatment of hypertension, to lower blood pressure. Lowering blood pressure reduces the risk of fatal and nonfatal cardiovascular events, primarily strokes and myocardial infarctions.', 10, 1),
(4, 'Valsartan', 'Formulated for oral administration to contain valsartan and hydrochlorothiazide, USP 80/12.5 mg, 160/12.5 mg, 160/25 mg, 320/12.5 mg, and 320/25 mg.\r\n', 'A prescription medicine called an angiotensin receptor blocker (ARB). It is used in adults to lower high blood pressure (hypertension) in adults', 80, 1),
(5, 'Enalapril', ' Enalapril maleate is a white to off-white, crystalline powder', 'A prescription medicine used to treat symptoms of high blood pressure (hypertension), left ventricular dysfunction and congestive heart failure.', 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `patient_id` int(10) NOT NULL,
  `patient_first_name` varchar(35) NOT NULL,
  `patient_last_name` varchar(35) NOT NULL,
  `patient_age` int(3) NOT NULL,
  `patient_sex` varchar(6) NOT NULL,
  `patient_email` varchar(255) NOT NULL,
  `patient_contact_number` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patient_id`, `patient_first_name`, `patient_last_name`, `patient_age`, `patient_sex`, `patient_email`, `patient_contact_number`) VALUES
(1, 'Aldrian', 'Tampoy', 20, 'Male', 'tampoy.aldrian@gmail.com', '09123456789'),
(2, 'Deni', 'Gonzales', 23, 'Female', 'deni@gmail.com', '09123456789'),
(3, 'Ryan', 'Reynolds', 50, 'Male', 'ryanreynolds@gmail.com', '09123456789'),
(4, 'Kobe', 'Bryant', 50, 'Male', 'kobebryant@gmail.com', '09123456789'),
(5, 'Angelina', 'Jolie', 50, 'Female', 'angelina@gmail.com', '09123456789'),
(6, 'Vin', 'Diesel', 50, 'Male', 'diesel@gmail.com', '09123456789'),
(7, 'Dwayne', 'Jhonson', 50, 'Male', 'therock@gmail.com', '09123456789'),
(8, 'Taylor', 'Swift', 50, 'Female', 'taylor@gmail.com', '09123456789'),
(9, 'John', 'Doe', 50, 'Male', 'john@gmail.com', '09123456789'),
(10, 'Gina', 'Wilson', 50, 'Female', 'b99@gmail.com', '09123456789'),
(11, 'Amy', 'Santiago', 50, 'Female', 'amy@gmail.com', '09123456789'),
(12, 'Terry', 'Crews', 50, 'Male', 'terry@gmail.com', '09123456789'),
(13, 'Ryan', 'Holt', 50, 'Male', 'ryan@gmail.com', '09123456789'),
(14, 'Richard', 'Flake', 50, 'Male', 'richard@gmail.com', '09123456789'),
(15, 'Martha', 'Stewart', 50, 'Female', 'martha@gmail.com', '09123456789'),
(16, 'Steve', 'Rogers', 50, 'Male', 'steve@gmail.com', '09123456789'),
(17, 'Black', 'Panther', 50, 'Male', 'black@gmail.com', '09123456789'),
(18, 'James', 'Bond', 50, 'Male', 'jamesbond@gmail.com', '09123456789'),
(19, 'Violet', 'Scar', 23, 'Female', 'violet@gmail.com', '09123456789'),
(20, 'James', 'Seagull', 54, 'Male', 'jamesseagull@yahoo.com', '09123456789');

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE `prescription` (
  `univ_uniq_identifier` varchar(36) NOT NULL,
  `patient_id` int(10) NOT NULL,
  `medicine_id` int(10) NOT NULL,
  `order_date` date NOT NULL,
  `dispense_amount` int(4) NOT NULL,
  `frequency` smallint(4) NOT NULL,
  `dosage` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prescription`
--

INSERT INTO `prescription` (`univ_uniq_identifier`, `patient_id`, `medicine_id`, `order_date`, `dispense_amount`, `frequency`, `dosage`) VALUES
('38e0c5d4-063e-451a-ac1a-79df8bd7f184', 1, 1, '2021-11-18', 24, 1, 80),
('512eb859-50b0-4053-b5cf-76491755cd10', 1, 1, '2021-11-18', 24, 2, 80),
('52497568-85a6-449d-839c-4db8da50fe52', 20, 5, '2021-11-18', 40, 4, 80),
('6dd8f3be-f7a0-4f71-acb4-738abd978812', 19, 5, '2021-11-18', 40, 4, 80),
('ba26b081-78e9-473f-b4f3-1df6c8b7ec4e', 2, 1, '2021-11-18', 12, 1, 80),
('e2af217a-19af-4972-9ea3-3f6e6ecc98be', 1, 1, '2021-11-18', 24, 1, 80);

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE `user_login` (
  `user_id` varchar(20) NOT NULL,
  `user_password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_login`
--

INSERT INTO `user_login` (`user_id`, `user_password`) VALUES
('admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`medicine_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`patient_id`);

--
-- Indexes for table `prescription`
--
ALTER TABLE `prescription`
  ADD PRIMARY KEY (`univ_uniq_identifier`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `medicine_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `patient_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
