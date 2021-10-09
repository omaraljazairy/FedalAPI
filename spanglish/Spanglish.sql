-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Sep 23, 2021 at 07:12 PM
-- Server version: 8.0.21
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Spanglish_Dev`
--

-- --------------------------------------------------------

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
CREATE TABLE IF NOT EXISTS `Category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Language`
--

DROP TABLE IF EXISTS `Language`;
CREATE TABLE IF NOT EXISTS `Language` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` varchar(2) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `iso-639-1` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Sentence`
--

DROP TABLE IF EXISTS `Sentence`;
CREATE TABLE IF NOT EXISTS `Sentence` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sentence` varchar(255) NOT NULL,
  `language_id` int NOT NULL DEFAULT '2',
  `category_id` int NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sentence` (`sentence`),
  KEY `category` (`category_id`),
  KEY `language_idx` (`language_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Translation`
--

DROP TABLE IF EXISTS `Translation`;
CREATE TABLE IF NOT EXISTS `Translation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `word_id` int DEFAULT NULL,
  `sentence_id` int DEFAULT NULL,
  `language_id` int NOT NULL DEFAULT '1',
  `translation` varchar(255) NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `word_id` (`word_id`),
  KEY `sentence_id` (`sentence_id`),
  KEY `language_Id` (`language_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Verb`
--

DROP TABLE IF EXISTS `Verb`;
CREATE TABLE IF NOT EXISTS `Verb` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tense` enum('simple present','present perfect','simple past','past progressive','past perfect','past anterior','future','future perfect','conditional','conditional perfect') CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'simple present',
  `word_id` int NOT NULL,
  `yo` varchar(25) DEFAULT NULL,
  `tu` varchar(25) DEFAULT NULL,
  `usted` varchar(25) DEFAULT NULL,
  `nosotros` varchar(25) DEFAULT NULL,
  `vosotros` varchar(25) DEFAULT NULL,
  `ustedes` varchar(25) DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tense` (`tense`,`word_id`),
  KEY `word_id` (`word_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

--
-- Table structure for table `Word`
--

DROP TABLE IF EXISTS `Word`;
CREATE TABLE IF NOT EXISTS `Word` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `word` varchar(30) NOT NULL,
  `language_id` int NOT NULL DEFAULT '2',
  `category_id` int NOT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `word` (`word`),
  KEY `word_category_idx` (`category_id`),
  KEY `language_idx` (`language_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Sentence`
--
ALTER TABLE `Sentence`
  ADD CONSTRAINT `sentence_category_fk` FOREIGN KEY (`category_id`) REFERENCES `Category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `sentence_language_fk` FOREIGN KEY (`language_id`) REFERENCES `Language` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `Translation`
--
ALTER TABLE `Translation`
  ADD CONSTRAINT `translation_language_fk` FOREIGN KEY (`language_id`) REFERENCES `Language` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `translation_sentence_fk` FOREIGN KEY (`sentence_id`) REFERENCES `Sentence` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `translation_word_fk` FOREIGN KEY (`word_id`) REFERENCES `Word` (`Id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `Verb`
--
ALTER TABLE `Verb`
  ADD CONSTRAINT `verb_word_fk` FOREIGN KEY (`word_id`) REFERENCES `Word` (`Id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `Word`
--
ALTER TABLE `Word`
  ADD CONSTRAINT `word_category_fk` FOREIGN KEY (`category_id`) REFERENCES `Category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `word_language_fk` FOREIGN KEY (`language_id`) REFERENCES `Language` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
