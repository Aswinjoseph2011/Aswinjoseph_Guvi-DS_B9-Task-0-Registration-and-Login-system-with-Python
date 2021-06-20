-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2021 at 06:42 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aswin`
--

-- --------------------------------------------------------

--
-- Table structure for table `registration_and_login`
--

CREATE TABLE `registration_and_login` (
  `id` int(11) NOT NULL,
  `User_creditional` varchar(25) NOT NULL,
  `Password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration_and_login`
--

INSERT INTO `registration_and_login` (`id`, `User_creditional`, `Password`) VALUES
(1, 'aswin@gmail.com', 'Aswin@123'),
(2, 'aswin.joseph@elenium.com', 'Aswin@123'),
(3, 'hareeni.dhayalan@elenium.', 'Hareeni@123'),
(4, 'aswin.joseph@elenium.com', 'Aswin@123'),
(5, 'rhaksha@invicara.com', 'Rhaksha@123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registration_and_login`
--
ALTER TABLE `registration_and_login`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `registration_and_login`
--
ALTER TABLE `registration_and_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
