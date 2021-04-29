-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: praca_inżynierska
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `klienci`
--

DROP TABLE IF EXISTS `klienci`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `klienci` (
  `id_klient` int NOT NULL AUTO_INCREMENT,
  `imie` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nazwisko` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `e-mail` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `telefon` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `haslo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ulica` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nr domu/mieszkania` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `miejscowosc` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `kod_pocztowy` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `województwo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_klient`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `klienci`
--

LOCK TABLES `klienci` WRITE;
/*!40000 ALTER TABLE `klienci` DISABLE KEYS */;
INSERT INTO `klienci` VALUES (1,'Jakub','Szcześniak','jakub.szczesniak54@gmail.com','792313653','lol','Panoramiczna','3','Promnik','26-067','świętokrzyskie');
/*!40000 ALTER TABLE `klienci` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `magazyn`
--

DROP TABLE IF EXISTS `magazyn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `magazyn` (
  `id_zasob` int NOT NULL AUTO_INCREMENT,
  `id_produkt` int DEFAULT NULL,
  `ilosc` float NOT NULL,
  `data_produkcji` date DEFAULT NULL,
  `id_zamowienie` int DEFAULT NULL,
  `status` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_zasob`),
  KEY `magazyn_FK` (`id_zamowienie`),
  KEY `magazyn_FK_1` (`id_produkt`),
  KEY `magazyn_FK_2` (`status`),
  CONSTRAINT `magazyn_FK` FOREIGN KEY (`id_zamowienie`) REFERENCES `zamowienia` (`id_zamowienie`),
  CONSTRAINT `magazyn_FK_1` FOREIGN KEY (`id_produkt`) REFERENCES `produkty` (`id_produkt`),
  CONSTRAINT `magazyn_FK_2` FOREIGN KEY (`status`) REFERENCES `status_mag` (`id_status_mag`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `magazyn`
--

LOCK TABLES `magazyn` WRITE;
/*!40000 ALTER TABLE `magazyn` DISABLE KEYS */;
INSERT INTO `magazyn` VALUES (1,1,15,'2020-05-20',1,1),(6,1,80,'2020-07-07',1,1),(7,1,15,'2021-03-26',1,1);
/*!40000 ALTER TABLE `magazyn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pracownicy`
--

DROP TABLE IF EXISTS `pracownicy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pracownicy` (
  `id_pracownik` int NOT NULL AUTO_INCREMENT,
  `imie` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nazwisko` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `rola` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_pracownik`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pracownicy`
--

LOCK TABLES `pracownicy` WRITE;
/*!40000 ALTER TABLE `pracownicy` DISABLE KEYS */;
INSERT INTO `pracownicy` VALUES (2,'Bożena','Lisowska','0');
/*!40000 ALTER TABLE `pracownicy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produkty`
--

DROP TABLE IF EXISTS `produkty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produkty` (
  `id_produkt` int NOT NULL AUTO_INCREMENT,
  `nazwa` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `norma` float NOT NULL,
  `jm` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `technologia` int NOT NULL,
  PRIMARY KEY (`id_produkt`),
  KEY `produkty_FK` (`technologia`),
  CONSTRAINT `produkty_FK` FOREIGN KEY (`technologia`) REFERENCES `technologia` (`id_tech`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produkty`
--

LOCK TABLES `produkty` WRITE;
/*!40000 ALTER TABLE `produkty` DISABLE KEYS */;
INSERT INTO `produkty` VALUES (1,'Produkt A',12,'sz',1),(2,'Produkt B',28,'kg',1),(3,'Produkt C',30,'sz',1),(5,'Produkt D',60,'kg',1);
/*!40000 ALTER TABLE `produkty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_mag`
--

DROP TABLE IF EXISTS `status_mag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status_mag` (
  `id_status_mag` int NOT NULL AUTO_INCREMENT,
  `nazwa` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_status_mag`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_mag`
--

LOCK TABLES `status_mag` WRITE;
/*!40000 ALTER TABLE `status_mag` DISABLE KEYS */;
INSERT INTO `status_mag` VALUES (1,'wolny'),(2,'zarezerwowany'),(3,'niedostępny');
/*!40000 ALTER TABLE `status_mag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_zamow`
--

DROP TABLE IF EXISTS `status_zamow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status_zamow` (
  `id_status_zamow` int NOT NULL AUTO_INCREMENT,
  `nazwa` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_status_zamow`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_zamow`
--

LOCK TABLES `status_zamow` WRITE;
/*!40000 ALTER TABLE `status_zamow` DISABLE KEYS */;
INSERT INTO `status_zamow` VALUES (1,'zrealizowane'),(2,'w toku'),(3,'oczekujace'),(4,'opoznione'),(5,'archiwalne');
/*!40000 ALTER TABLE `status_zamow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surowce`
--

DROP TABLE IF EXISTS `surowce`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `surowce` (
  `id_surowiec` int NOT NULL AUTO_INCREMENT,
  `nazwa` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `jm` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `prog_bezp` float NOT NULL,
  PRIMARY KEY (`id_surowiec`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surowce`
--

LOCK TABLES `surowce` WRITE;
/*!40000 ALTER TABLE `surowce` DISABLE KEYS */;
/*!40000 ALTER TABLE `surowce` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `technologia`
--

DROP TABLE IF EXISTS `technologia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `technologia` (
  `id_tech` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_tech`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `technologia`
--

LOCK TABLES `technologia` WRITE;
/*!40000 ALTER TABLE `technologia` DISABLE KEYS */;
INSERT INTO `technologia` VALUES (1);
/*!40000 ALTER TABLE `technologia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zamowienia`
--

DROP TABLE IF EXISTS `zamowienia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zamowienia` (
  `id_zamowienie` int NOT NULL AUTO_INCREMENT,
  `id_produkt` int NOT NULL,
  `ilosc_zamow` float NOT NULL,
  `data_zamow` datetime NOT NULL,
  `data_realizacji` date DEFAULT NULL,
  `ilosc_pracownik` int NOT NULL DEFAULT '0',
  `wewnetrzne` int NOT NULL DEFAULT '0',
  `status` int NOT NULL,
  `id_klient` int NOT NULL,
  PRIMARY KEY (`id_zamowienie`),
  KEY `zamowienia_FK_1` (`status`),
  KEY `zamowienia_FK` (`id_klient`),
  KEY `zamowienia_FK_2` (`id_produkt`),
  CONSTRAINT `zamowienia_FK` FOREIGN KEY (`id_klient`) REFERENCES `klienci` (`id_klient`),
  CONSTRAINT `zamowienia_FK_1` FOREIGN KEY (`status`) REFERENCES `status_zamow` (`id_status_zamow`),
  CONSTRAINT `zamowienia_FK_2` FOREIGN KEY (`id_produkt`) REFERENCES `produkty` (`id_produkt`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zamowienia`
--

LOCK TABLES `zamowienia` WRITE;
/*!40000 ALTER TABLE `zamowienia` DISABLE KEYS */;
INSERT INTO `zamowienia` VALUES (1,1,20,'2020-10-12 14:15:10','2021-12-15',7,0,1,1),(2,1,15,'2020-10-15 14:15:10','2020-10-25',5,0,2,1);
/*!40000 ALTER TABLE `zamowienia` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-28 20:49:34
