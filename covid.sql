CREATE DATABASE  IF NOT EXISTS `covid` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `covid`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: covid
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` int NOT NULL AUTO_INCREMENT,
  `logoname` varchar(255) NOT NULL,
  `CompanyNames` varchar(255) NOT NULL,
  `Locations` varchar(255) NOT NULL,
  `Tags` varchar(255) NOT NULL,
  `availableJobs` int NOT NULL,
  `CompanySize` int NOT NULL,
  `details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'3.gif','Adidas','chennai','#qcsso',4,93,'Adidas AG is a multinational corporation, founded and headquartered in Herzogenaurach, Germany, that designs and manufactures shoes, clothing and accessories. It is the largest sportswear manufacturer in Europe.'),(2,'4.gif','Adobe','Hydrabad','#ztwfc',8,61,'Adobe Inc., known until October 3, 2018 as Adobe Systems Incorporated, is an American multinational computer software company headquartered in San Jose.'),(3,'5.gif','Dell','chennai','#mquua',6,55,'Dell is an American multinational computer technology company that develops, sells, repairs, and supports computers and related products and services.'),(4,'6.gif','GitHub','Hydrabad','#hcyic',4,69,'GitHub, Inc. is a United States-based global company that provides hosting for software development version control using Git. In 2018, it became a subsidiary of Microsoft for US$7.5 billion..'),(5,'2.gif','Birla Group','Mumbai','#dxjtd',9,77,'Birla Group, is an Indian multinational conglomerate, headquartered in Worli, chennai, Maharashtra, India. It operates in 34 countries with more than 120,000 employees worldwide.');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opportunities`
--

DROP TABLE IF EXISTS `opportunities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opportunities` (
  `op_id` int NOT NULL AUTO_INCREMENT,
  `id` int NOT NULL,
  `logoname` varchar(255) NOT NULL,
  `job_type` varchar(255) NOT NULL,
  `techstack` varchar(255) NOT NULL,
  `culture` varchar(255) NOT NULL,
  `D_R` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `company_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`op_id`),
  KEY `cid` (`id`),
  CONSTRAINT `cid` FOREIGN KEY (`id`) REFERENCES `company` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opportunities`
--

LOCK TABLES `opportunities` WRITE;
/*!40000 ALTER TABLE `opportunities` DISABLE KEYS */;
INSERT INTO `opportunities` VALUES (1,1,'1.gif','Backend Developer','SDE, Mobile Application, Docker','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(4,2,'2.gif','Flutter Developer','Android, Mobile Application, Docker, kotlin','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(5,3,'3.gif','Frontend Developer','Nodejs , HTML, javascript, kotlin','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(6,4,'4.gif','Full-stack developer','Nodejs , HTML, javascript, kotlin','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(7,5,'5.gif','Android developer','Android , HTML, Firebase, kotlin','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(8,1,'1.gif','Android developer','SDE, Mobile Application, Docker','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(9,1,'1.gif','Frontend developer','SDE, Mobile Application, Docker','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(10,1,'1.gif','Software developer','SDE, Mobile Application, Docker','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(11,1,'1.gif','Flutter developer','SDE, Mobile Application, Docker','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(12,1,'1.gif','Flask developer','SDE, Mobile Application, Docker','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering'),(13,1,'1.gif','Node developer','SDE, Mobile Application, Docker','International team, Global team, Very collaborative','Develop and test software to meet consumers and clients needs. Develop upgrades for existing applications. Add new features according to the need.','Software developers are the creative minds behind software programs, and they have the technical skills to build those programs or to oversee their creation by a team.','Engineering');
/*!40000 ALTER TABLE `opportunities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `logoname` varchar(255) NOT NULL,
  `ProjectNames` varchar(255) NOT NULL,
  `Locations` varchar(255) NOT NULL,
  `Tags` varchar(255) NOT NULL,
  `availableVacancies` int NOT NULL,
  `ProjectSize` int NOT NULL,
  `details` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (1,'4.gif','Project 1','Pune','#gmmrz',4,7,'Java'),(2,'5.gif','Project 2','Chennai','#chdjh',8,8,'Node.js'),(3,'4.gif','Project 3','Kolkata','#bdqog',3,7,'C++'),(4,'5.gif','Project 4','Mumbai','#ghjzb',7,8,'Flutter'),(5,'1.gif','Project 5','Pune','#uzgik',7,6,'Flutter'),(6,'1.gif','Project 6','Banglore','#kzfzl',6,7,'Kotlin'),(7,'2.gif','Project 7','Kolkata','#tzpbv',4,6,'Kotlin'),(8,'3.gif','Project 8','Kolkata','#schnv',2,9,'Kotlin'),(9,'5.gif','Project 9','Banglore','#mgnty',4,5,'Java'),(10,'1.gif','Project 10','Punjab','#jdwcm',6,5,'Dart');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token` (
  `id` int NOT NULL,
  `token` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` VALUES (1,'abcd');
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `fullname` varchar(1000) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pwd` varchar(1000) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Priyanshu Pandey','999999999','pandeyprince25@gmail.com','password');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-21 12:44:03
