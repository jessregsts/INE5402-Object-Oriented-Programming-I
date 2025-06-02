-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `mikanvideo`
--

DROP TABLE IF EXISTS `mikanvideo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mikanvideo` (
  `member` varchar(40) NOT NULL,
  `cad` varchar(45) NOT NULL,
  `idcpf` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `phonenumber` varchar(45) DEFAULT NULL,
  `dvdid` varchar(45) DEFAULT NULL,
  `director` varchar(45) DEFAULT NULL,
  `date1` varchar(45) DEFAULT NULL,
  `date2` varchar(45) DEFAULT NULL,
  `date3` varchar(45) DEFAULT NULL,
  `latedays` varchar(45) DEFAULT NULL,
  `finalprice` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cad`,`idcpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mikanvideo`
--

LOCK TABLES `mikanvideo` WRITE;
/*!40000 ALTER TABLE `mikanvideo` DISABLE KEYS */;
INSERT INTO `mikanvideo` VALUES ('Jedi Master','1234567','1234567','1234567a','1234567','1234567','7654321a','Jéssicaaa','Santos','Rua XXXX','YYY-YYYYY','BTS00001','Brian De Palma','2022-07-17 20:00:45.556408');
/*!40000 ALTER TABLE `mikanvideo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'mydata'
--

--
-- Dumping routines for database 'mydata'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-18  9:33:06
