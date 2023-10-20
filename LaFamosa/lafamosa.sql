CREATE DATABASE  IF NOT EXISTS `lafamosa` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lafamosa`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: lafamosa
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
-- Table structure for table `acomodar`
--

DROP TABLE IF EXISTS `acomodar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acomodar` (
  `cve_aco` int unsigned NOT NULL AUTO_INCREMENT,
  `fecha_aco` date NOT NULL,
  `cant_aco` varchar(45) NOT NULL,
  `lugar_aco` varchar(45) NOT NULL,
  `num_renres` int unsigned NOT NULL,
  `cve_tie` int unsigned NOT NULL,
  PRIMARY KEY (`cve_aco`),
  KEY `fkAcomodarRenglonResurtir_idx` (`num_renres`),
  KEY `fkAcomodarTienda_idx` (`cve_tie`),
  CONSTRAINT `fkAcomodarRenglonResurtir` FOREIGN KEY (`num_renres`) REFERENCES `renglonresurtir` (`num_renres`),
  CONSTRAINT `fkAcomodarTienda` FOREIGN KEY (`cve_tie`) REFERENCES `tienda` (`cve_tie`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acomodar`
--

LOCK TABLES `acomodar` WRITE;
/*!40000 ALTER TABLE `acomodar` DISABLE KEYS */;
INSERT INTO `acomodar` VALUES (1,'2022-04-02','2','Mostrador',10,2),(2,'2022-04-03','5','Tarima',6,2),(3,'2022-04-03','3','Exibidor',9,3),(4,'2022-04-03','1','Exibidor',4,6),(5,'2022-04-02','2','Exibidor',2,7),(6,'2022-04-02','3','Exibidor',7,8),(7,'2022-04-02','4','Tarima',5,5),(8,'2022-04-03','3','Mostrador',8,9),(9,'2022-04-02','3','Mostrador',3,1),(10,'2022-04-02','2','Mostrador',1,4),(12,'2022-05-28','10','Almacen',26,4),(13,'2022-05-30','4','Almacen',27,3);
/*!40000 ALTER TABLE `acomodar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `checador`
--

DROP TABLE IF EXISTS `checador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `checador` (
  `num_che` int unsigned NOT NULL AUTO_INCREMENT,
  `hora_che` date NOT NULL,
  `tipo_che` varchar(45) NOT NULL,
  `folio_con` int unsigned NOT NULL,
  PRIMARY KEY (`num_che`),
  KEY `fkChecadorContrato_idx` (`folio_con`),
  CONSTRAINT `fkChecadorContrato` FOREIGN KEY (`folio_con`) REFERENCES `contrato` (`folio_con`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checador`
--

LOCK TABLES `checador` WRITE;
/*!40000 ALTER TABLE `checador` DISABLE KEYS */;
INSERT INTO `checador` VALUES (1,'2022-02-18','Entrada',1),(2,'2022-02-18','Entrada',2),(3,'2022-02-18','Entrada',3),(4,'2022-02-18','Entrada',4),(5,'2022-02-18','Entrada',5),(6,'2022-02-18','Entrada',6),(7,'2022-02-18','Entrada',7),(8,'2022-02-18','Entrada',8),(9,'2022-02-18','Salida',1),(10,'2022-02-18','Salida',2),(11,'2022-02-18','Salida',3),(12,'2022-02-18','Salida',4),(13,'2022-02-18','Salida',5),(14,'2022-02-18','Salida',6),(15,'2022-02-18','Salida',7),(16,'2022-02-18','Salida',8);
/*!40000 ALTER TABLE `checador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudad`
--

DROP TABLE IF EXISTS `ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudad` (
  `cve_ciu` int unsigned NOT NULL AUTO_INCREMENT,
  `nom_ciu` varchar(50) NOT NULL,
  `cve_est` int unsigned NOT NULL,
  PRIMARY KEY (`cve_ciu`),
  UNIQUE KEY `nombreCiudad_UNIQUE` (`nom_ciu`),
  KEY `fkCiudadEstado_idx` (`cve_est`),
  CONSTRAINT `fkCiudadEstado` FOREIGN KEY (`cve_est`) REFERENCES `estado` (`cve_est`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudad`
--

LOCK TABLES `ciudad` WRITE;
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` VALUES (1,'Calvillo',1),(2,'Cosio',12),(3,'Jesus Maria',1),(4,'Tecate',24),(5,'Rosarito',26),(6,'Ensenada',10),(7,'Candelaria',4),(8,'Oaxaca De Juarez',20),(9,'San Martin Tilcajete',20),(10,'Apatzingan',16),(11,'Zamora',16),(12,'Zitacuaro',16),(13,'Iguala',12),(14,'Chihuahua',6),(15,'Saltillo',8),(16,'Monterrey',19),(17,'San Luis',24),(18,'Mexicalli',2),(19,'La paz',3),(20,'Queretaro',22),(21,'Hidalgo',13),(22,'Colima',9),(23,'Guanajuato',11),(24,'Chiapas',5),(25,'Tuxpan',16),(26,'Morelia',16),(27,'Tulum',23),(28,'Cholula',21),(29,'San Lucas',3),(30,'Tijuana',2),(31,'Manzanillo',9),(32,'Culiacan',25),(33,'Jungapeo',16),(34,'Villa Victoria',15),(35,'Celaya',11),(36,'Reynosa',28),(37,'Nuevo Laredo',19),(38,'Hermosillo',26),(39,'Ciudad Juarez',6),(40,'Los Mochis',25),(41,'Cancún',31),(42,'Ciudad Del Carmen',4),(43,'Tampico',28),(44,'Lázaro Cardenas',16),(45,'Puebla de Zaragoza',21),(46,'Texmeluca',21),(47,'Huetamo',16),(48,'Ciudad Hidalgo',16);
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `cve_cli` int unsigned NOT NULL AUTO_INCREMENT,
  `fecha_clie` date NOT NULL,
  `cve_per` int unsigned NOT NULL,
  PRIMARY KEY (`cve_cli`),
  KEY `fkClientePersona_idx` (`cve_per`),
  CONSTRAINT `fkClientePersona` FOREIGN KEY (`cve_per`) REFERENCES `persona` (`cve_per`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'2021-01-05',14),(2,'2022-02-02',15),(3,'2001-09-30',16),(4,'1999-03-17',17),(5,'2006-12-15',18),(6,'2022-03-27',19),(7,'2022-03-29',20),(8,'2022-03-30',21),(9,'2022-01-17',22),(10,'2022-02-13',23),(11,'2022-03-02',24),(12,'2022-03-01',25);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codigopostal`
--

DROP TABLE IF EXISTS `codigopostal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codigopostal` (
  `cve_cod` int unsigned NOT NULL AUTO_INCREMENT,
  `cve_cui` int unsigned NOT NULL,
  PRIMARY KEY (`cve_cod`),
  KEY `fkCodigoCiudad_idx` (`cve_cui`),
  CONSTRAINT `fkCodigoCiudad` FOREIGN KEY (`cve_cui`) REFERENCES `ciudad` (`cve_ciu`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=95762 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codigopostal`
--

LOCK TABLES `codigopostal` WRITE;
/*!40000 ALTER TABLE `codigopostal` DISABLE KEYS */;
INSERT INTO `codigopostal` VALUES (95761,1),(15722,2),(54320,3),(56712,4),(77513,5),(82342,6),(69001,7),(83241,8),(76123,9),(32573,10),(31278,11),(61516,12),(90177,13),(76188,14),(21883,15),(12451,16),(24557,17),(52932,18),(53326,19),(76244,20),(91662,21),(43115,22),(23671,23),(52357,24),(82125,25),(77232,26),(37012,27),(53244,28),(73162,29),(55611,30),(78771,31),(22592,32),(23154,33),(55721,34),(11462,35),(61732,36),(72114,37),(61342,38),(94211,39),(48152,40),(69142,41),(23657,42),(15563,43),(32143,44),(44531,45),(21556,46);
/*!40000 ALTER TABLE `codigopostal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colonia`
--

DROP TABLE IF EXISTS `colonia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colonia` (
  `cve_col` int unsigned NOT NULL AUTO_INCREMENT,
  `nom_col` varchar(50) NOT NULL,
  `cve_cod` int unsigned NOT NULL,
  PRIMARY KEY (`cve_col`),
  KEY `fkColoniaCodigo_idx` (`cve_cod`),
  CONSTRAINT `fkColoniaCodigo` FOREIGN KEY (`cve_cod`) REFERENCES `codigopostal` (`cve_cod`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colonia`
--

LOCK TABLES `colonia` WRITE;
/*!40000 ALTER TABLE `colonia` DISABLE KEYS */;
INSERT INTO `colonia` VALUES (1,'El moral',95761),(2,'El aguacate',15722),(3,'Pipila',54320),(4,'Nicolas romero',56712),(5,'Benito Juarez',77513),(6,'Manzanillos',82342),(7,'Centro',69001),(8,'Mora Del Cañonazo',83241),(9,'Independecia',76123),(10,'La Mangana',32573),(11,'La Encarnacion',31278),(12,'Nuevo Amanecer',61516),(13,'Pueblo Nuevo',90177),(14,'Reforma',23671),(15,'Las palmas',43115),(16,'Educación',21883),(17,'Miguel Hidalgo',76244),(18,'Morelos',91662),(19,'Revolución',52357),(20,'El fresno',24557),(21,'Regeneración',12451),(22,'San Miguel',76188),(23,'Suprema Junta',52932),(24,'San Francisco',53326),(25,'Xinantecatl',55721),(26,'Mexica',69142),(27,'Santa María',77232),(28,'Parque Industrial',11462),(29,'La Garita',61342),(30,'Coatepec',23657),(31,'La iglesia',78771),(32,'Buena Vista',82125),(33,'Caribe',23154),(34,'Puerto Azul',55611),(35,'Lerma',61732),(36,'Condesa',94211),(37,'Seminario',53244),(38,'Sor Juana Ines',37012),(39,'Rayon',48152),(40,'Ignacio Varga',72114),(41,'Nuevo México',22592),(42,'Monarca',73162),(43,'Tres Ríos',15563),(44,'Santa Cruz',44531),(45,'Guadalupe Hidalgo',32143),(46,'Tlaxcala',21556);
/*!40000 ALTER TABLE `colonia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comisiones`
--

DROP TABLE IF EXISTS `comisiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comisiones` (
  `cve_comi` int unsigned NOT NULL AUTO_INCREMENT,
  `comision` float NOT NULL,
  `folio_con` int unsigned NOT NULL,
  `folio_tic` int unsigned NOT NULL,
  PRIMARY KEY (`cve_comi`),
  KEY `folio_tic` (`folio_tic`),
  KEY `folio_con` (`folio_con`),
  CONSTRAINT `comisiones_ibfk_1` FOREIGN KEY (`folio_tic`) REFERENCES `ticket` (`folio_tic`),
  CONSTRAINT `comisiones_ibfk_2` FOREIGN KEY (`folio_con`) REFERENCES `contrato` (`folio_con`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comisiones`
--

LOCK TABLES `comisiones` WRITE;
/*!40000 ALTER TABLE `comisiones` DISABLE KEYS */;
/*!40000 ALTER TABLE `comisiones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contrato`
--

DROP TABLE IF EXISTS `contrato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contrato` (
  `folio_con` int unsigned NOT NULL,
  `fechaInicio_con` date NOT NULL,
  `fechaFin_con` date NOT NULL,
  `puesto_con` varchar(60) NOT NULL,
  `sueldo_con` double NOT NULL,
  `periodoSueldo_con` varchar(30) NOT NULL,
  `hEntrada_con` time NOT NULL,
  `hSalida_con` time NOT NULL,
  `hInicioComida_con` time NOT NULL,
  `hFinComida_con` time NOT NULL,
  `comisiones_con` double DEFAULT NULL,
  `cve_tie` int unsigned NOT NULL,
  `cve_per` int unsigned NOT NULL,
  PRIMARY KEY (`folio_con`),
  KEY `fkContratoTienda_idx` (`cve_tie`),
  KEY `fkContratoPersona_idx` (`cve_per`),
  CONSTRAINT `fkContratoPersona` FOREIGN KEY (`cve_per`) REFERENCES `persona` (`cve_per`),
  CONSTRAINT `fkContratoTienda` FOREIGN KEY (`cve_tie`) REFERENCES `tienda` (`cve_tie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contrato`
--

LOCK TABLES `contrato` WRITE;
/*!40000 ALTER TABLE `contrato` DISABLE KEYS */;
INSERT INTO `contrato` VALUES (1,'2020-04-19','2025-04-19','Administrador de sistemas',5000,'Semanal','11:00:00','20:00:00','14:30:00','15:30:00',0,1,1),(2,'1996-05-12','2001-05-13','Cajero',1900,'Quincenal','11:00:00','20:00:00','13:00:00','14:00:00',230,2,2),(3,'2015-06-22','2020-06-22','Cajero',1900,'Quincenal','11:00:00','20:00:00','13:30:00','14:30:00',100,2,3),(4,'2013-06-15','2018-03-15','Gerente',2400,'Quincenal','11:00:00','20:00:00','14:00:00','14:00:00',0,3,4),(5,'2019-06-06','2024-06-06','Gerente',2300,'Quincenal','11:00:00','20:00:00','15:00:00','16:00:00',0,3,5),(6,'2014-03-09','2016-03-09','Secretaria',1000,'Semanal','11:00:00','20:00:00','15:30:00','16:30:00',0,4,6),(7,'2021-12-12','2026-12-12','Guardia',1100,'Quincenal','11:00:00','20:00:00','14:30:00','15:30:00',0,5,7),(8,'2007-01-08','2012-01-08','Cajero',1900,'Quincenal','11:00:00','20:00:00','14:00:00','15:00:00',155,6,8),(9,'1996-05-12','2001-05-13','Cajero',1900,'Quincenal','11:00:00','20:00:00','13:30:00','14:30:00',250,7,9),(10,'2015-06-22','2020-06-22','Cajero',3200,'Semanal','11:00:00','20:00:00','15:00:00','16:00:00',160,4,10),(11,'2013-06-15','2018-03-15','Gerente',2400,'Quincenal','11:00:00','20:00:00','14:00:00','15:00:00',0,8,11),(12,'2019-06-06','2024-06-06','Gerente',2300,'Quincenal','11:00:00','20:00:00','15:00:00','16:00:00',0,9,12),(13,'2014-03-09','2016-03-09','Cajero',3000,'Quincenal','11:00:00','20:00:00','13:30:00','14:30:00',120,9,13),(14,'2022-06-11','2024-06-11','Intendente',1100.55,'Semanal','11:00:00','20:00:00','13:20:00','14:20:00',NULL,2,26),(15,'2022-06-11','2023-08-26','Gerente',1900.12,'Quincenal','11:00:00','20:00:00','16:10:00','17:10:00',NULL,5,27),(16,'2022-06-11','2024-09-24','Chofer',1512.35,'Quincenal','11:00:00','20:00:00','12:00:00','13:00:00',NULL,4,28),(17,'2022-06-11','2024-06-11','Gerente de ventas',1537.52,'Mensual','11:00:00','20:00:00','14:20:00','15:20:00',NULL,10,29);
/*!40000 ALTER TABLE `contrato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datoenvio`
--

DROP TABLE IF EXISTS `datoenvio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `datoenvio` (
  `cve_dat` int unsigned NOT NULL AUTO_INCREMENT,
  `calle_dat` varchar(70) NOT NULL,
  `numDomicilio_dat` varchar(45) NOT NULL,
  `orientacion_dat` varchar(60) NOT NULL,
  `entreCalles_dat` varchar(150) NOT NULL,
  `cve_col` int unsigned NOT NULL,
  `folio_tic` int unsigned NOT NULL,
  PRIMARY KEY (`cve_dat`),
  KEY `fkDatoEnvioColonia_idx` (`cve_col`),
  KEY `fkDatoEnvioFolioTicket_idx` (`folio_tic`),
  CONSTRAINT `fkDatoEnvioColonia` FOREIGN KEY (`cve_col`) REFERENCES `colonia` (`cve_col`),
  CONSTRAINT `fkDatoEnvioFolioTicket` FOREIGN KEY (`folio_tic`) REFERENCES `ticket` (`folio_tic`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datoenvio`
--

LOCK TABLES `datoenvio` WRITE;
/*!40000 ALTER TABLE `datoenvio` DISABLE KEYS */;
INSERT INTO `datoenvio` VALUES (1,'19 de Noviembre','56','Oeste','Sor juana y Isidro Fabela',1,10),(2,'Las Torres','721','Este','Zaragoza y Benedicto López',13,8),(3,'La joya','89','Este','Benito Juarez y 5 de Mayo',8,1),(4,'Rio Blanco','34','Oeste','Paseo Volcan y Zafiro',5,11),(5,'Poetas','102','Norte','Morelos y Miguel Hidalgo',1,5),(6,'Cholollan','165','Norte','Moctezuma y Reforma',7,3),(7,'Del Nogal','78','Oeste','Granate y Maria Ines',4,7),(8,'Alba','23','Sur','Portales y Mora',6,2);
/*!40000 ALTER TABLE `datoenvio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `devolucion`
--

DROP TABLE IF EXISTS `devolucion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `devolucion` (
  `clave_dev` int unsigned NOT NULL AUTO_INCREMENT,
  `motivo_dev` varchar(150) NOT NULL,
  `fecha_dev` date NOT NULL,
  `folio_tic` int unsigned NOT NULL,
  PRIMARY KEY (`clave_dev`),
  KEY `fkDevolucionTicket_idx` (`folio_tic`),
  CONSTRAINT `fkDevolucionTicket` FOREIGN KEY (`folio_tic`) REFERENCES `ticket` (`folio_tic`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devolucion`
--

LOCK TABLES `devolucion` WRITE;
/*!40000 ALTER TABLE `devolucion` DISABLE KEYS */;
INSERT INTO `devolucion` VALUES (1,'El Dispositivo Venia Roto','2018-11-30',1),(2,'Faltan Piezas','2019-01-15',2),(3,'El Dispositivo Funcionaba bien al inicio pero comenzo a presentar fallas','2018-08-10',3),(4,'Dispositivo defectuoso','2019-05-29',4),(5,'El dispositivo venia rallado','2019-06-15',5),(6,'Al inicio funcionaba bien y a los 2 dias ya no encendio','2021-08-17',6),(7,'Dispositivo defectuoso','2021-06-10',7),(8,'El dispositivo venia rallado','2017-10-05',8),(9,'Al inicio funcionaba bien y a los 2 dias ya no encendio','2014-02-16',9),(10,'Dispositivo defectuoso','2021-06-20',10);
/*!40000 ALTER TABLE `devolucion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enviar`
--

DROP TABLE IF EXISTS `enviar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enviar` (
  `cve_env` int NOT NULL,
  `fecha_env` date NOT NULL,
  `ns_veh` int NOT NULL,
  `folio_con` int unsigned NOT NULL,
  PRIMARY KEY (`cve_env`),
  KEY `fkEnviarNumeroSerie_idx` (`ns_veh`),
  KEY `fkEnviarContrato_idx` (`folio_con`),
  CONSTRAINT `fkEnviarContrato` FOREIGN KEY (`folio_con`) REFERENCES `contrato` (`folio_con`),
  CONSTRAINT `fkEnviarNumeroSerie` FOREIGN KEY (`ns_veh`) REFERENCES `vehiculo` (`ns_veh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enviar`
--

LOCK TABLES `enviar` WRITE;
/*!40000 ALTER TABLE `enviar` DISABLE KEYS */;
INSERT INTO `enviar` VALUES (1,'2022-04-03',154633,5),(2,'2022-01-26',394544,1),(3,'2022-03-22',684414,9),(4,'2022-04-06',801335,12),(5,'2022-03-27',468731,6),(6,'2022-02-19',309741,3),(7,'2022-03-05',684414,4),(8,'2022-02-28',394544,5);
/*!40000 ALTER TABLE `enviar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado`
--

DROP TABLE IF EXISTS `estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado` (
  `cve_est` int unsigned NOT NULL AUTO_INCREMENT,
  `nom_est` varchar(50) NOT NULL,
  PRIMARY KEY (`cve_est`),
  UNIQUE KEY `nombreEstado_UNIQUE` (`nom_est`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado`
--

LOCK TABLES `estado` WRITE;
/*!40000 ALTER TABLE `estado` DISABLE KEYS */;
INSERT INTO `estado` VALUES (1,'Aguascalientes'),(2,'Baja California'),(3,'Baja California Sur'),(4,'Campeche'),(5,'Chiapas'),(6,'Chihuahua'),(7,'Ciudad de México'),(8,'Coahuila'),(9,'Colima'),(10,'Durango'),(11,'Guanajuato'),(12,'Guerrero'),(13,'Hidalgo'),(14,'Jalisco'),(15,'México'),(16,'Michoacán'),(17,'Morelos'),(18,'Nayarit'),(19,'Nuevo León'),(20,'Oaxaca'),(21,'Puebla'),(22,'Querétaro'),(23,'Quintana Roo'),(24,'San Luis Potosí'),(25,'Sinaloa'),(26,'Sonora'),(27,'Tabasco'),(28,'Tamaulipas'),(29,'Tlaxcala'),(30,'Veracruz'),(31,'Yucatán'),(32,'Zacatecas');
/*!40000 ALTER TABLE `estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listacarga`
--

DROP TABLE IF EXISTS `listacarga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listacarga` (
  `num_liscar` int unsigned NOT NULL AUTO_INCREMENT,
  `cve_dat` int unsigned NOT NULL,
  `cve_env` int NOT NULL,
  PRIMARY KEY (`num_liscar`),
  KEY `fkListaCargaDatoEnvio_idx` (`cve_dat`),
  KEY `fkListaCargaEnvio_idx` (`cve_env`),
  CONSTRAINT `fkListaCargaDatoEnvio` FOREIGN KEY (`cve_dat`) REFERENCES `datoenvio` (`cve_dat`),
  CONSTRAINT `fkListaCargaEnvio` FOREIGN KEY (`cve_env`) REFERENCES `enviar` (`cve_env`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listacarga`
--

LOCK TABLES `listacarga` WRITE;
/*!40000 ALTER TABLE `listacarga` DISABLE KEYS */;
INSERT INTO `listacarga` VALUES (1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5),(6,6,6),(7,7,7),(8,8,8),(9,8,8);
/*!40000 ALTER TABLE `listacarga` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minmax`
--

DROP TABLE IF EXISTS `minmax`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `minmax` (
  `num_minmax` int unsigned NOT NULL AUTO_INCREMENT,
  `min_minmax` int unsigned NOT NULL,
  `max_minmax` int unsigned NOT NULL,
  `codbar_pro` int unsigned NOT NULL,
  `cve_tie` int unsigned NOT NULL,
  PRIMARY KEY (`num_minmax`),
  KEY `fkminimoMaximoProducto_idx` (`codbar_pro`),
  KEY `fkMinimoMaximoTienda_idx` (`cve_tie`),
  CONSTRAINT `fkminimoMaximoProducto` FOREIGN KEY (`codbar_pro`) REFERENCES `producto` (`codbar_pro`),
  CONSTRAINT `fkMinimoMaximoTienda` FOREIGN KEY (`cve_tie`) REFERENCES `tienda` (`cve_tie`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minmax`
--

LOCK TABLES `minmax` WRITE;
/*!40000 ALTER TABLE `minmax` DISABLE KEYS */;
INSERT INTO `minmax` VALUES (1,1,18,5,9),(2,1,21,7,3),(3,2,15,2,2),(4,3,9,1,8),(5,2,20,10,1),(6,2,11,13,4),(7,1,17,8,6),(8,1,10,6,5),(9,5,10,18,1),(10,2,6,18,2);
/*!40000 ALTER TABLE `minmax` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `cve_per` int unsigned NOT NULL AUTO_INCREMENT,
  `nom_per` varchar(50) NOT NULL,
  `ap_per` varchar(30) NOT NULL,
  `am_per` varchar(30) NOT NULL,
  `calle_per` varchar(100) NOT NULL,
  `numDomicilio_per` varchar(10) NOT NULL,
  `orientacion_per` varchar(60) NOT NULL,
  `entreCalles_per` varchar(160) NOT NULL,
  `tel_per` varchar(20) NOT NULL,
  `mail_per` varchar(100) NOT NULL,
  `sexo_per` varchar(45) NOT NULL,
  `fNacimiento_per` date NOT NULL,
  `edoCivil_per` varchar(45) NOT NULL,
  `cve_col` int unsigned NOT NULL,
  `CURP_per` varchar(20) NOT NULL,
  PRIMARY KEY (`cve_per`),
  UNIQUE KEY `telefono_UNIQUE` (`tel_per`),
  UNIQUE KEY `correoPersona_UNIQUE` (`mail_per`),
  KEY `fkPersonaColonia_idx` (`cve_col`),
  CONSTRAINT `fkPersonaColonia` FOREIGN KEY (`cve_col`) REFERENCES `colonia` (`cve_col`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'Brisa','Martinez','Macedo','Los olivos','14','Oeste','Aldama y Zaragoza','7151667690','bmartinez@gmail.com','Femenino','2001-03-15','Soltera',10,'HJS23SFW'),(2,'Federico','Lopez','Sandoval','Aldama','25','Norte','Zaragoza Y Felipe','7157894595','Fedelobo@gmail.com','Masculino','2000-03-15','Casado',11,'K7FHBSJS21'),(3,'Martha','Nuñez','Ocasio','Nicolas Romero','4','Sur','Benito Juarez Y Aldama','7224568720','mar234@gmail.com','Femenino','1999-08-12','Soltera',12,'D42SHDGVHA'),(4,'Abigail','Moreno','Miranda','Carranza','9','Este','Mora y Revolucion','5517895642','AbiMoreno@outlook.com','Femenino','1981-05-14','Casada',13,'K8DH6DAS'),(5,'Fernanda','Lopez','Perdomo','Corregidora','52','Norte','Felipe Angeles y Juan de la Barrera','6514789325','Fermar45@outlook.com','Femenino','1905-05-09','Casada',14,'JOD9NSK12S'),(6,'Mauricio','Delgado','Flores','Miranda','103','Oeste','Pokemon Y Zarzamora','7156548951','Mauriciodel@hotmail.com','Masculino','1989-12-21','Casada',15,'SHG6672SD'),(7,'Patricio','Miranda','Fuentes','Loma Bonita','154','Norte','Soledad y Luna','5512479654','Fuentes@gmail.com','Masculino','1996-10-01','Soltero',16,'HJFD6SDKJG'),(8,'Laura','Bozo','Barragan','José Ortiz','55','Sur','Encanto y Benito Juarez','1581564780','lauraboss@hotmail.com','Femenino','1972-06-19','Casada',17,'SDFHGS6A2'),(9,'Carlota','Jhonson','Current','Linda Vista','5','Este','Magdalena y Pipila','1245365140','jhonson@outlook.com','Femenino','1981-04-14','Soltera',18,'NI23BNSSD'),(10,'Wanda','Maximoff','Frank','Santos Degollado','2','Norte','Zaragoza Y Felipe','1800512302','wandamax@icloud.com','Femenino','1982-12-22','Viuda',19,'AQN23DLS02'),(11,'James','Buchanan','Barnes','Santo Domingo','9','Oeste','Cruz y Revolucion','1531145028','buckybarnes@icloud.com','Masculino','1917-03-10','Soltero',20,'KYW12BNSY6'),(12,'Jose','Trigueros','Acuña','La fama','7','Norte','Pueblita y poetas','7151954895','josetri@gmail.com','Masculino','2003-05-06','Soltero',21,'JAQ03MRSS8'),(13,'Zayn','Javadd','Malik','Pino chino','9','Sur','Mora y Revolucion','1800314153','Zayn1d@outlook.com','Masculino','1993-01-12','Casado',22,'PU878SD3SDS'),(14,'Benito','Martinez','Ocasio','Aries','4','Sur','Italia y Zaragoza','1546895212','badbunny@outlook.com','Masculino','1986-03-13','Soltero',23,'B7USI7SAA'),(15,'Chris','Cornell','God','18 de Marzo','98','Norte','Crucero Avila y Obregon','1800265478','Audioslave@icloud.com','Masculino','1964-06-20','Casado',24,'BJA29WYXS'),(16,'Harry','Edwuard','Styles','A. Rayón','56','Norte','Independencia y Revolucion','2456987456','hs@Gmail.com','Masculino','1989-02-21','Soltero',25,'JIJ2EBJS'),(17,'Roberta','Salinas','Cruz','Abasolo','12','Oeste','Mora y Revolucion','7151668954','rics@gmail.com','Femenino','2000-06-16','Casado',26,'BABD31DSE'),(18,'Magdalena','Sanchez','Lopez','Lerdo de Tejada','105','Este','Soledad y Luna','7150002648','magda@hotmail.com','Femenino','2001-07-23','Soltera',27,'YQ723SKS'),(19,'Soledad','Balderas','Nuñez','Cristobal','3','Este','Aldama y Lerdo','7451235489','solecito@gmail.com','Femenino','2002-09-08','Soltera',28,'ANX82HSBS'),(20,'Brian','Cruz','Ramirez','Vicente guerrero','5','Oeste','Lerdo y Cuahutemoc','7221548956','tacodtripa@gmail.com','Masculino','2001-10-08','Soltero',29,'PQ12NSAC'),(21,'Julio','Marin','Ocaña','Michoacas','77','Norte','Juna Manuel y Felipe Ramos','1855455455','julion32@gmail.com','Masculino','1998-08-26','Casado',30,'TE6ABDAX'),(22,'David','Jiménez','De Jesús','Benedicto Lopez','10','Norte','Guayana y Borneo','1342841207','deivid58@outlook.com','Masculino','2000-12-12','Soltero',31,'KQ81Y3GSD'),(23,'Alan','Gallardo','Mora','Madero','96','Oeste','Zafiro y Perla','1800369784','alanj125@gmail.com','Masculino','2002-02-25','Casado',32,'HJGD67AH0S'),(24,'Erika','Robles','Almanza','Francisco villa','47','Sur','Adrian Ortega e Isidro Fabela','1596733012','erika@hotmail.com','Femenino','1985-11-20','Soltera',33,'GD7AVSD93'),(25,'Paola','Ruiz','Morales','Independencia','12','Este','Lerma y Corregidora','1068762473','paolaL943@gmail.com','Femenino','1989-06-15','Casada',34,'GD7ABED34'),(26,'David','Jiménez','De Jesús','Benedicto López','85','Sur','Matamoros y Guillermo Prieto','7151630842','david28550@gmail.com','Masculino','2002-07-02','Soltero',12,'JSA12BHUSDA'),(27,'José Rubén','Jiménez','De Jesús','Caribe','125','Oeste','La cuesta y Mar rojo','7151594445','rubenjim212@gmail.com','Masculino','1998-08-26','Casada',42,'JIJL32NA1ÑA'),(28,'Patricia','De Jesús','López','Rio grande','36','Este','Damaso cardenas y Juarez','7151121644','patridadeJes@gmail.com','Femenino','1976-11-20','Casada',35,'KRS13MASH23'),(29,'Jonathan','Velazquez','Juarez','Residencias','25','Sur','Solovino y Agripino','6245976813','jonivelazquez34@hotmail.com','Masculino','2000-10-11','Casado',42,'POP2HS3NSKA'),(30,'Gabriel','Angeles','Marin','Tula','39','Oeste','Gigantes y Mirador','79431345','gabristrix32@gamil.com','Masculino','2094-01-25','Casado',18,'YID13JS23A'),(31,'José','Maya','García','Adolfo Ruiz','125','Este','.','7159687342','joseMaya@gmail.com','Masculino','1978-07-22','Casado',45,'KOWA64HAEWB');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `precioventa`
--

DROP TABLE IF EXISTS `precioventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `precioventa` (
  `cve_pre` int unsigned NOT NULL AUTO_INCREMENT,
  `fecha_pre` date NOT NULL,
  `precio_pre` double NOT NULL,
  `codbar_pro` int unsigned NOT NULL,
  PRIMARY KEY (`cve_pre`),
  KEY `codbar_pro` (`codbar_pro`),
  CONSTRAINT `precioventa_ibfk_1` FOREIGN KEY (`codbar_pro`) REFERENCES `producto` (`codbar_pro`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `precioventa`
--

LOCK TABLES `precioventa` WRITE;
/*!40000 ALTER TABLE `precioventa` DISABLE KEYS */;
INSERT INTO `precioventa` VALUES (1,'2022-05-25',200.124,2),(2,'2022-05-25',200,1),(3,'2022-05-25',1300.56,5),(4,'2022-06-13',1300.56,7),(5,'2022-06-13',1300.56,6),(6,'2022-06-13',556036,3),(7,'2022-06-13',445,4),(8,'2022-06-13',6000.23,8),(9,'2022-06-13',7800,9),(10,'2022-06-13',200,10),(11,'2022-06-13',412,11),(12,'2022-06-13',4896,12),(13,'2022-06-13',3300.56,13),(14,'2022-06-13',690,14),(15,'2022-06-13',5863,15),(16,'2022-06-13',1548,16),(33,'2022-06-15',23,17),(36,'2022-06-15',15250,18);
/*!40000 ALTER TABLE `precioventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `codbar_pro` int unsigned NOT NULL AUTO_INCREMENT,
  `nom_pro` varchar(100) NOT NULL,
  `tipo_pro` varchar(100) NOT NULL,
  `marca_pro` varchar(50) NOT NULL,
  `color_pro` varchar(30) NOT NULL,
  `garantia_pro` varchar(45) NOT NULL,
  `uMedidaGarantia_pro` varchar(45) NOT NULL,
  `presentacion_pro` varchar(45) NOT NULL,
  `modelo_pro` varchar(70) NOT NULL,
  `alto_pro` varchar(45) NOT NULL,
  `largo_pro` varchar(45) NOT NULL,
  `ancho_pro` varchar(45) NOT NULL,
  `contenido_pro` int NOT NULL,
  `uMedida_pro` varchar(45) NOT NULL,
  `codigo_pro` varchar(20) NOT NULL,
  PRIMARY KEY (`codbar_pro`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Lavadora Multi','Lavadora','LG','Blanco','1','años','Caja de cartón','Primero','22','7','24',6,'piezas','1539876342'),(2,'C Series','Computadora','Lenovo','Blanco','4','meses','Caja de cartón','Cuarto','19','3','22',3,'piezas','5867944231'),(3,'Poco X3 NFC','Celular','Xiaomi','Negro','11','meses','Caja de cartón','Tercero','1','23','1',8,'piezas','5871340251'),(4,'IdeaPad','Computadora','Lenovo','Azul','4','meses','Caja de cartón','Tercero','2','9','7',2,'piezas','2023504004'),(5,'MacBook','Computadora','Apple','Blanco','8','meses','Caja de cartón','Segundo','16','26','17',5,'piezas','7819410155'),(6,'Xbox Series S','Consola','Microsoft','Blanco','4','años','Caja de cartón','Cuarto','6','19','26',9,'piezas','4860853414'),(7,'Play Station 5','Consola','Sony','Blanco con Negro','2','años','Caja de cartón','Tercero','17','5','21',4,'piezas','3502100487'),(8,'Pantalla All Me','Pantalla','Samsung','Negro','3','años','Caja de cartón','Primero','12','7','14',7,'piezas','8973002155'),(9,'Refrigerador Cx23','Refrigerador','LG','Azul','6','meses','Caja de cartón','Primero','17','20','24',4,'piezas','1534870031'),(10,'A20','Celular','Samsung','Rojo','9','meses','Caja de cartón','Tercero','14','25','25',3,'piezas','9348573101'),(11,'Redmi Note 10','Celular','Xiaomi','Gris','10','meses','Caja de cartón','Segundo','2','21','26',7,'piezas','5536480455'),(12,'Tost sdw','Tostadora','LG','Naranja','8','meses','Caja de cartón','Primero','10','22','2',6,'piezas','8214075381'),(13,'Asus Pro','Computadora','Asus','Rojo','4','años','Caja de cartón','Primero','13','1','12',5,'piezas','1520445789'),(14,'G5 plus','Celular','Motorola','Gris','5','años','Caja de cartón','Segundo','22','4','23',8,'piezas','2354911687'),(15,'laptop HP','laptop','Frefsa','Morado','6','meses','Caja de cartón','Cuarto','6','21','3',8,'piezas','7849415020'),(16,'Xbox series X','Consola','Microsoft','Negro','5','años','Caja de cartón','Segundo','25','25','26',3,'piezas','0351751680'),(17,'a','a','aa','aa','a','dias','a','a','a','a','a',12,'Milímetro','7455'),(18,'Flex 5','Laptop','Lenovo','Gris','365','dias','Sencilla','Flex 5 de 14\'\' pulgadas','32','28','4',1,'Centímetros','564874856');
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `cve_prov` int NOT NULL AUTO_INCREMENT,
  `nomEmpresa_prov` varchar(60) NOT NULL,
  `calle_prov` varchar(100) NOT NULL,
  `numDomicilio_prov` varchar(10) NOT NULL,
  `orientacion_prov` varchar(60) NOT NULL,
  `entreCalles_prov` varchar(150) NOT NULL,
  `tel_prov` varchar(45) NOT NULL,
  `mail_prov` varchar(60) NOT NULL,
  `cve_col` int unsigned NOT NULL,
  PRIMARY KEY (`cve_prov`),
  UNIQUE KEY `nombreProveedor_UNIQUE` (`nomEmpresa_prov`),
  UNIQUE KEY `telefonoProveedor_UNIQUE` (`tel_prov`),
  UNIQUE KEY `correoProveedor_UNIQUE` (`mail_prov`),
  KEY `fkProveedorColonia_idx` (`cve_col`),
  CONSTRAINT `fkProveedorColonia` FOREIGN KEY (`cve_col`) REFERENCES `colonia` (`cve_col`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'Samsung','Paseo reforma','1254','Oeste','Lerma y Corregidora','7225491945','samsungInc@gmail.com',35),(2,'Xiaomi','Tollocan','964','Norte','Magdalena y Pipila','7228497423','xiaomiInc@gmail.com',36),(3,'Apple','Sor Juana Inez','12','Este','Cruz y Revolucion','7891742458','appleInc@gmail.com',37),(4,'Lenovo','Adolfo López Mateos','1120','Sur','Pueblita y poetas','7226715384','lenovoInc@gmail.com',38),(5,'Microsoft','Portales','584','Este','Mora y Revolucion','9853812649','microsoftInc@gmail.com',39),(6,'Asus','Av. México','42','Este','Soledad y Luna','4246138572','asusInc@gmail.com',40),(7,'LG','Niños Heroes','89','Norte','Aldama y Lerdo','7168479541','LGInc@gmail.com',41),(8,'Fefsa','La merced','798','Norte','Zaragoza Y Felipe','3915986243','fefsaInc@gmail.com',42),(9,'Sony','C. tonallan','486','Oeste','Benito Juarez Y Aldama','8942212117','sonyInc@gmail.com',43),(10,'Motorola','Loyula','496','Sur','Pokemon Y Zarzamora','5844052178','motorolaInc@gmail.com',44),(11,'HP','Volcán','11','Norte','Mora y Revolucion','8697418762','hpInc@gmail.com',45),(12,'Alcatel','Xinantecatl','69','Oeste','Felipe Angeles y Juan de la Barrera','7532148572','alcatelInc@gmail.com',46),(13,'Lego','Adolfo Ruiz','78','Sur','Pipila y Mora','7896413527','lego12Magic@hotmail.com',15);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renglonresurtir`
--

DROP TABLE IF EXISTS `renglonresurtir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renglonresurtir` (
  `num_renres` int unsigned NOT NULL AUTO_INCREMENT,
  `cantidad_renres` int NOT NULL,
  `baja_renres` int NOT NULL,
  `fCad_renres` date NOT NULL,
  `precio_renres` double NOT NULL,
  `codbar_pro` int unsigned NOT NULL,
  `cve_res` int NOT NULL,
  PRIMARY KEY (`num_renres`),
  KEY `fkRenglonResurtirProducto_idx` (`codbar_pro`),
  KEY `fkRenglonResurtirResurtir_idx` (`cve_res`),
  CONSTRAINT `fkRenglonResurtirProducto` FOREIGN KEY (`codbar_pro`) REFERENCES `producto` (`codbar_pro`),
  CONSTRAINT `fkRenglonResurtirResurtir` FOREIGN KEY (`cve_res`) REFERENCES `resurtir` (`cve_res`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renglonresurtir`
--

LOCK TABLES `renglonresurtir` WRITE;
/*!40000 ALTER TABLE `renglonresurtir` DISABLE KEYS */;
INSERT INTO `renglonresurtir` VALUES (1,1,1,'2023-01-01',5000.06,6,1),(2,1,1,'2023-01-01',8028.06,16,1),(3,2,2,'2023-01-01',10133.78,5,2),(4,2,2,'2023-01-01',7025.36,6,3),(5,1,1,'2023-01-01',2124.3,2,4),(6,3,3,'2023-01-01',2633.35,4,4),(7,5,5,'2023-01-01',2724.83,10,5),(8,2,2,'2023-01-01',5937.5,13,6),(9,2,2,'2023-01-01',2674.11,14,7),(10,3,3,'2023-01-01',5842.37,1,8),(11,4,4,'2023-01-01',5000.06,6,1),(12,3,3,'2023-01-01',5000.06,6,1),(13,5,5,'2023-01-01',5000.06,6,1),(14,4,4,'2023-01-01',5000.06,6,1),(15,30,30,'2022-09-12',200,6,11),(19,5,5,'2022-07-02',27.25,5,17),(21,10,10,'2022-07-02',100,5,20),(22,10,10,'2022-07-02',100,5,21),(23,10,10,'2022-07-02',100,5,22),(24,10,10,'2022-07-02',100,5,23),(25,10,10,'2022-07-02',100,5,24),(26,10,10,'2022-07-02',100,5,25),(27,4,4,'2023-09-21',300,10,26);
/*!40000 ALTER TABLE `renglonresurtir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `representante`
--

DROP TABLE IF EXISTS `representante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `representante` (
  `num_rep` int NOT NULL AUTO_INCREMENT,
  `fecha_rep` date NOT NULL,
  `cve_per` int unsigned NOT NULL,
  `cve_prov` int NOT NULL,
  PRIMARY KEY (`num_rep`),
  KEY `fkRepresentanteProveedor_idx` (`cve_prov`),
  KEY `fkRepresentantePersona_idx` (`cve_per`),
  CONSTRAINT `fkRepresentantePersona` FOREIGN KEY (`cve_per`) REFERENCES `persona` (`cve_per`),
  CONSTRAINT `fkRepresentanteProveedor` FOREIGN KEY (`cve_prov`) REFERENCES `proveedor` (`cve_prov`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `representante`
--

LOCK TABLES `representante` WRITE;
/*!40000 ALTER TABLE `representante` DISABLE KEYS */;
INSERT INTO `representante` VALUES (1,'2020-03-27',20,1),(2,'2021-09-10',17,2),(3,'2022-01-08',6,3),(4,'2019-07-21',21,4),(5,'2020-03-31',12,5),(6,'2018-07-11',9,6),(7,'2021-06-30',8,8),(8,'2021-08-26',10,9),(9,'2022-06-12',21,7),(10,'2022-05-04',17,10),(11,'2021-05-12',15,11),(12,'2022-01-27',16,12),(17,'2022-06-12',31,13);
/*!40000 ALTER TABLE `representante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resurtir`
--

DROP TABLE IF EXISTS `resurtir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resurtir` (
  `cve_res` int NOT NULL AUTO_INCREMENT,
  `fecha_res` date NOT NULL,
  `total_res` double NOT NULL,
  `cve_prov` int NOT NULL,
  `cve_tie` int unsigned NOT NULL,
  PRIMARY KEY (`cve_res`),
  KEY `fkResurtirTienda_idx` (`cve_tie`),
  KEY `fkResurtirProveedor_idx` (`cve_prov`),
  CONSTRAINT `fkResurtirProveedor` FOREIGN KEY (`cve_prov`) REFERENCES `proveedor` (`cve_prov`),
  CONSTRAINT `fkResurtirTienda` FOREIGN KEY (`cve_tie`) REFERENCES `tienda` (`cve_tie`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resurtir`
--

LOCK TABLES `resurtir` WRITE;
/*!40000 ALTER TABLE `resurtir` DISABLE KEYS */;
INSERT INTO `resurtir` VALUES (1,'2021-12-15',13028,5,1),(2,'2022-02-07',20268,3,3),(3,'2022-02-17',7025,5,5),(4,'2022-01-27',10024,4,6),(5,'2022-01-28',13624,1,8),(6,'2022-02-28',11875,2,7),(7,'2022-02-12',5348,10,6),(8,'2022-01-31',17527,9,4),(9,'2022-05-28',1200.5,1,3),(10,'2022-05-28',1200.5,1,3),(11,'2022-05-28',1200.5,1,3),(14,'2022-05-28',1100.5,1,4),(15,'2022-05-28',1100.5,1,4),(17,'2022-05-28',1100.5,1,4),(20,'2022-05-28',1000,1,4),(21,'2022-05-28',1000,1,4),(22,'2022-05-28',1000,1,4),(23,'2022-05-28',1000,1,4),(24,'2022-05-28',1000,1,4),(25,'2022-05-28',1000,1,4),(26,'2022-05-30',1200,1,3),(27,'2022-06-15',1362,3,3),(28,'2022-06-15',1362,3,3),(29,'2022-06-15',1362,3,3);
/*!40000 ALTER TABLE `resurtir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `num_sta` int NOT NULL AUTO_INCREMENT,
  `fecha_sta` date NOT NULL,
  `status_sta` varchar(100) NOT NULL,
  `num_liscar` int unsigned NOT NULL,
  PRIMARY KEY (`num_sta`),
  KEY `fkStatusListaCarga_idx` (`num_liscar`),
  CONSTRAINT `fkStatusListaCarga` FOREIGN KEY (`num_liscar`) REFERENCES `listacarga` (`num_liscar`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'2022-04-03','Enviado',1),(2,'2022-04-05','Empaquetado',2),(3,'2022-04-05','Llegando hoy',3),(4,'2022-04-05','Entregado',6),(5,'2022-04-07','En camino',5),(6,'2022-05-30','En Ruta',9);
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statusvehiculo`
--

DROP TABLE IF EXISTS `statusvehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statusvehiculo` (
  `num_sta` int NOT NULL AUTO_INCREMENT,
  `fecha_sta` date NOT NULL,
  `status_sta` varchar(50) NOT NULL,
  `ns_veh` int NOT NULL,
  PRIMARY KEY (`num_sta`),
  KEY `fkEstadoVehiculoVehiculo_idx` (`ns_veh`),
  CONSTRAINT `fkEstadoVehiculoVehiculo` FOREIGN KEY (`ns_veh`) REFERENCES `vehiculo` (`ns_veh`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statusvehiculo`
--

LOCK TABLES `statusvehiculo` WRITE;
/*!40000 ALTER TABLE `statusvehiculo` DISABLE KEYS */;
INSERT INTO `statusvehiculo` VALUES (1,'2022-01-23','Funcionando bien',154633),(2,'2022-02-03','Servicio por realizar',566548),(3,'2021-12-22','Funcionando bien',394544),(4,'2022-02-26','En servicio',254058),(5,'2022-03-30','Funcionando bien',684414),(6,'2022-04-02','Descompuesto',987354),(7,'2022-03-08','Funcionando bien',801335),(8,'2022-02-18','Funcionando bien',468731),(9,'2022-03-21','Funcionando bien',309741);
/*!40000 ALTER TABLE `statusvehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `folio_tic` int unsigned NOT NULL AUTO_INCREMENT,
  `fechaVenta_tic` date NOT NULL,
  `finGarantia_tic` date NOT NULL,
  `precioVenta_tic` int NOT NULL,
  `descuento_tic` int NOT NULL,
  `cantidad_tic` varchar(45) NOT NULL,
  `formaPago_tic` varchar(45) NOT NULL,
  `folioAutenticacionPago_tic` varchar(30) DEFAULT NULL,
  `numTarjeta_tic` varchar(45) DEFAULT NULL,
  `institucionBancaria_tic` varchar(45) DEFAULT NULL,
  `codbar_pro` int unsigned NOT NULL,
  `folio_con` int unsigned NOT NULL,
  `cve_tie` int unsigned NOT NULL,
  `cve_cli` int unsigned NOT NULL,
  PRIMARY KEY (`folio_tic`),
  KEY `fkTicketProducto_idx` (`codbar_pro`),
  KEY `fkTicketContrato_idx` (`folio_con`),
  KEY `fkTicketTienda_idx` (`cve_tie`),
  KEY `fkTicketCliente_idx` (`cve_cli`),
  CONSTRAINT `fkTicketCliente` FOREIGN KEY (`cve_cli`) REFERENCES `cliente` (`cve_cli`),
  CONSTRAINT `fkTicketContrato` FOREIGN KEY (`folio_con`) REFERENCES `contrato` (`folio_con`),
  CONSTRAINT `fkTicketProducto` FOREIGN KEY (`codbar_pro`) REFERENCES `producto` (`codbar_pro`),
  CONSTRAINT `fkTicketTienda` FOREIGN KEY (`cve_tie`) REFERENCES `tienda` (`cve_tie`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,'2018-11-03','2019-11-04',9381,1876,'2','efectivo','Vacio','Vacio','Vacio',1,1,1,1),(2,'2018-12-31','2019-12-31',12413,2483,'1','efectivo','Vacio','Vacio','Vacio',2,2,2,2),(3,'2018-08-05','2019-08-05',14511,2902,'1','efectivo','Vacio','Vacio','Vacio',3,3,3,3),(4,'2019-05-21','2020-05-21',4937,987,'4','efectivo','Vacio','Vacio','Vacio',4,4,4,4),(5,'2019-05-26','2020-05-26',4567,913,'1','efectivo','Vacio','Vacio','Vacio',5,5,5,5),(6,'2021-08-07','2022-08-07',1233,247,'2','efectivo','Vacio','Vacio','Vacio',6,6,6,6),(7,'2021-06-01','2022-06-01',1093,219,'3','efectivo','Vacio','Vacio','Vacio',7,7,7,7),(8,'2017-09-30','2017-12-30',8329,1666,'2','Tarjeta','4512','12369874','BBVA',8,8,8,1),(9,'2014-02-06','2015-02-06',14730,2946,'5','Tarjeta','4512','14563201','BBVA',9,9,9,2),(10,'2021-06-19','2022-06-19',2938,588,'1','Tarjeta','3256','12361047','BBVA',10,10,1,3),(11,'2021-09-30','2022-09-30',1879,376,'3','Tarjeta','1245','14078965','HSBC',11,11,2,4),(12,'2021-01-02','2021-07-02',9323,1865,'1','Tarjeta','2368','23654102','BanCoppel',12,1,3,5),(13,'2022-02-19','2023-02-19',7636,1527,'1','Tarjeta','7890','10398752','Banamex',13,2,4,6),(14,'2022-01-03','2022-04-03',6165,1233,'1','Tarjeta','1213','2100340','Banorte',14,3,5,7),(15,'2021-12-24','2022-12-24',5379,1076,'2','Tarjeta','1254','10964152','Banco Azteca',1,4,6,1),(16,'2021-11-29','2022-11-29',11673,2335,'3','Tarjeta','7896','10547896','Santander',2,5,7,2),(17,'2021-11-29','2022-11-29',14477,2895,'2','Tarjeta','1356','36987412','Santander',3,6,8,3),(18,'2021-08-15','2022-04-15',6358,1272,'5','Tarjeta','231','25410310','BBVA',4,7,9,4),(19,'2022-12-03','2022-12-03',9300,1860,'6','Tarjeta','1463','12369874','Banorte',5,8,1,5),(20,'2022-04-02','2023-04-03',12456,2491,'8','Tarjeta','1236','1234569','Banamex',6,9,2,6);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tienda`
--

DROP TABLE IF EXISTS `tienda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tienda` (
  `cve_tie` int unsigned NOT NULL AUTO_INCREMENT,
  `fechaApertura_tie` date NOT NULL,
  `calle_tie` varchar(100) NOT NULL,
  `numDomicilio_tie` varchar(10) NOT NULL,
  `orientacion_tie` varchar(60) NOT NULL,
  `entreCalles_tie` varchar(150) NOT NULL,
  `tel_tie` varchar(20) NOT NULL,
  `mail_tie` varchar(50) NOT NULL,
  `cve_col` int unsigned NOT NULL,
  PRIMARY KEY (`cve_tie`),
  UNIQUE KEY `telefonoTienda_UNIQUE` (`tel_tie`),
  UNIQUE KEY `correoTienda_UNIQUE` (`mail_tie`),
  KEY `fkTiendaColonia_idx` (`cve_col`),
  CONSTRAINT `fkTiendaColonia` FOREIGN KEY (`cve_col`) REFERENCES `colonia` (`cve_col`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tienda`
--

LOCK TABLES `tienda` WRITE;
/*!40000 ALTER TABLE `tienda` DISABLE KEYS */;
INSERT INTO `tienda` VALUES (1,'2002-07-02','Zaragoza','37','Oeste','Matamoros y Avenida Guadalajara','9210387271','lafamosaZaragoza@gmail.com',1),(2,'1998-08-26','Abasolo','53','Norte','Niños Heroes y Revolucion','8471259264','lafamosaAbasolo@gmail.com',2),(3,'1999-11-23','Paseo San Nicolas','95','Sur','Constitución y Cárdenas','7152534017','lafamosaSanNicolas@gmail.com',3),(4,'2010-01-30','La guacamaya','86','Este','Morelos y Reforma','889172572','lafamosaLaGuacamaya@gmail.com',4),(5,'2008-10-15','Miguel Hidalgo','19','Norte','Emiliano Zapata y Artilleria','8771295355','lafamosaMiguelHidalgo@gmail.com',5),(6,'2015-08-21','Morelos','22','Oeste','Dr. Emilio y La Radio','1638206431','lafamosaMorelos@gmail.com',6),(7,'2020-10-18','Constituyentes','50','Norte','Avenida Morelia y Paseo Reforma','7630172600','lafamosaConstituyentes@gmail.com',7),(8,'1999-03-26','Benedicto López','103','Sur','Plan de Ayala y Perla','7261002457','lafamosaBenedictoLopez@gmail.com',8),(9,'2021-06-01','Periferico','56','Sur','16 de Septiembre y Aguacate','7226227269','lafamosaPeriferico@gmail.com',9),(10,'2022-06-11','Zaragoza','126','Oeste','El vado y Av. Morelia','6245973145','lafamosaBajaCal@hotmail.com',24),(12,'2022-06-14','Cañonazo','34','Oeste','Sor Jauana Ines','7672139076','lafamosaCañonazo@hotmail.com',1),(13,'2022-06-22','Sor Juana Ines ','85','Este','Cruz y Morelos','5763404561','lafamosaSorJuana@gmail.com',6),(14,'2023-06-15','Zaragoza','78','Oeste','Guillermo y Lerdo','6426412462','lafamosaMora@gmail.com',45),(15,'2022-10-28','weqqwe','12','Este','qwewew','4214214','correo',12);
/*!40000 ALTER TABLE `tienda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo`
--

DROP TABLE IF EXISTS `vehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehiculo` (
  `ns_veh` int NOT NULL AUTO_INCREMENT,
  `modelo_veh` varchar(45) NOT NULL,
  `marca_veh` varchar(45) NOT NULL,
  `color_veh` varchar(45) NOT NULL,
  `cantPuertas_veh` int NOT NULL,
  `año_veh` int DEFAULT NULL,
  `precioCompra_veh` int NOT NULL,
  `tipo_veh` varchar(45) NOT NULL,
  `cve_tie` int unsigned DEFAULT NULL,
  PRIMARY KEY (`ns_veh`),
  KEY `fkClaveTienda_idx` (`cve_tie`),
  CONSTRAINT `fkClaveTienda` FOREIGN KEY (`cve_tie`) REFERENCES `tienda` (`cve_tie`)
) ENGINE=InnoDB AUTO_INCREMENT=987355 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo`
--

LOCK TABLES `vehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo` DISABLE KEYS */;
INSERT INTO `vehiculo` VALUES (154633,'Np300','Nissan','Blanco',2,2019,350000,'Camioneta',1),(254058,'D21','Nissan','Negro',2,1995,36000,'Camioneta',3),(309741,'Tornado','Chevrolet','Blanco',2,2008,75000,'Camioneta',8),(394544,'Tacoma','Toyota','Verde',2,1998,80000,'Camioneta',5),(468731,'Silverado','Chevrolet','Blanco',2,2003,180000,'Camioneta',2),(566548,'Hilux','Toyota','Negro',4,2022,420000,'Camioneta',2),(684414,'Spark','Chevrolet','Gris Plata',4,2017,165000,'Carro',7),(801335,'Ranger','Ford','Gris',2,2000,35000,'Camioneta',6),(987354,'Frontier','Nissan','Azul',4,2005,175000,'Camioneta',9);
/*!40000 ALTER TABLE `vehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vigila`
--

DROP TABLE IF EXISTS `vigila`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vigila` (
  `cve_vig` int NOT NULL AUTO_INCREMENT,
  `fecha_vig` datetime NOT NULL,
  `usuario_vig` varchar(100) NOT NULL,
  `anterior_vig` float(8,2) NOT NULL,
  `nuevo_vig` float(8,2) NOT NULL,
  `producto_vig` int NOT NULL,
  PRIMARY KEY (`cve_vig`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vigila`
--

LOCK TABLES `vigila` WRITE;
/*!40000 ALTER TABLE `vigila` DISABLE KEYS */;
INSERT INTO `vigila` VALUES (1,'2022-05-25 12:06:01','root@localhost',24.13,200.00,1);
/*!40000 ALTER TABLE `vigila` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'lafamosa'
--

--
-- Dumping routines for database 'lafamosa'
--
/*!50003 DROP PROCEDURE IF EXISTS `sp_agregarminmax` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_agregarminmax`(minimo int, maximo int, codbar int, cve_tie int)
begin
	insert into minmax values(null,minimo,maximo,codbar,cve_tie);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_agregarProducto` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_agregarProducto`(nombre varchar(100),tipo varchar(100),marca varchar(50),color varchar(30),garantia varchar(45),presentacion varchar(45),modelo varchar(70),alto varchar(45),largo varchar(45),ancho varchar(45),contenido int,unidadMedida varchar(45),codigo varchar(20)
									,precioVenta double)
begin
	declare clave int;
    start transaction;
    set clave = (select max(codbar_pro) from producto);
    set clave = clave+1;
    insert into producto values(clave,nombre,tipo,marca,color,garantia,"dias",presentacion,modelo,alto,largo,ancho,contenido,unidaMedida,codigo);
    insert into precioventa values(null,curdate(),precioVenta,clave);
    select clave;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_agregarProveedorProcedure` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_agregarProveedorProcedure`(nomEmpresa varchar(60), calle varchar(100), numDomicilio varchar(10), orientacion varchar(60), entreCalles varchar(150), tele varchar(45), mail varchar(60), cve_col int,
											nombre varchar(50), ap varchar(50), am varchar(50), callePer varchar(50), numdomiPer varchar(10), orientacionPer varchar(60), entrecallesPer varchar(160), telefonoPer varchar(20) , correo varchar(100), sexo varchar(45), fnaci date, edocivil varchar(45), cve_colonia int, CURP_per varchar(20))
begin
	declare clave,claveper int;
	start transaction;
    set clave = (select max(cve_prov) from proveedor);
    set clave = clave+1;
    set claveper = (select max(cve_per) from persona);
    set claveper = claveper+1;
	insert into proveedor values(clave,nomEmpresa,calle,numDomicilio,orientacion,entreCalles,tele,mail,cve_col);
    insert into persona values(claveper, nombre,ap,am,callePer,numdomiPer,orientacionPer,entrecallesPer,telefonoPer,correo,sexo,fnaci,edocivil,cve_colonia,CURP_per);
	insert into representante values(null,curdate(),claveper,clave);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_agregarRepresentante` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_agregarRepresentante`(nombre varchar(50), ap varchar(50), am varchar(50), calle varchar(50), numdomi varchar(10), orientacion varchar(60), entrecalles varchar(160), telefono varchar(20) , correo varchar(100), sexo varchar(45), fnaci date, edocivil varchar(45), cve_col int, CURP_per varchar(20),cve_prov int)
begin
	declare clave int;
    set clave = (select max(cve_per) from persona);
    set clave = clave+1;
    insert into persona values(clave, nombre,ap,am,calle,numdomi,orientacion,entrecalles,telefono,correo,sexo,fnaci,edocivil,cve_col,CURP_per);
	insert into representante values(null,curdate(),clave,cve_prov);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_agregarTienda` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_agregarTienda`(fechaApertura date, calle varchar(100), numDomicilio varchar(10), orientacion varchar(60), entreCalles varchar(150), tel varchar(20), mail varchar(50), cve_col int)
begin
	start transaction;
	insert into tienda values(null,fechaApertura,calle,numDomicilio,orientacion,entreCalles,tel,mail,cve_col);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_buscarClaveProducto` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_buscarClaveProducto`(codbar varchar(20))
begin
	select * from producto where codbar_pro=codigo;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_buscarCodigoBarras` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_buscarCodigoBarras`(codigo varchar(20))
begin
	select * from producto where codigo_pro=codigo;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_buscarEmpleado` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_buscarEmpleado`(folio_contrato int)
begin
	select * from contrato where folio_con = folio_contrato;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_buscarPersonaCurp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_buscarPersonaCurp`(curp_persona varchar(20))
begin
	select * from persona where curp_per = curp_persona;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_buscarRepresentante` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_buscarRepresentante`(cve_proveedor int)
begin
	select * from representante where cve_prov=cve_proveedor;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_buscartiendasdisponibles` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_buscartiendasdisponibles`(codigoBarras int)
begin
	select * from tienda where tienda.cve_tie not in(select cve_tie from minmax where codbar_pro=codigoBarras) group by tienda.cve_tie;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_cancelarproducto` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_cancelarproducto`()
begin
	rollback;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_cancelarproveedor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_cancelarproveedor`()
begin
	rollback;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_cancelartienda` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_cancelartienda`()
begin
	rollback;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_cantidadEmpleados` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_cantidadEmpleados`(cve_tienda int)
begin
	select count(folio_con) from contrato where cve_tie = cve_tienda;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_cantidadVehiculos` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_cantidadVehiculos`(cve_tienda int)
begin
	select count(ns_veh) from vehiculo where cve_tie = cve_tienda;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_confirmarproducto` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_confirmarproducto`()
begin
	commit;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_confirmarproveedor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_confirmarproveedor`()
begin
	commit;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_confirmartienda` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_confirmartienda`()
begin
	commit;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_isEmptyEmpleados` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_isEmptyEmpleados`()
begin
	select count(*) from contrato;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_isemptyproducto` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_isemptyproducto`()
begin
	select count(*) from producto;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_isemptyproveedor` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_isemptyproveedor`()
begin
	select count(*) from proveedor;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_isEmptyTiendas` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_isEmptyTiendas`()
begin
	select count(*) from tienda;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarCiudades` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarCiudades`(cve_estado int)
begin
	select * from ciudad where cve_est = cve_estado;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarCodigosPostales` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarCodigosPostales`(cve_ciudad int)
begin
	select * from codigoPostal where cve_cui = cve_ciudad;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarColonias` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarColonias`(cve_codigo int)
begin
	select * from colonia where cve_cod = cve_codigo;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarEmpleadoPersona` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarEmpleadoPersona`(cvePer int)
begin
	select * from persona where cve_per = cvePer;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarEmpleados` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarEmpleados`()
begin
	select * from contrato;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarEstados` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarEstados`()
begin
	select * from estado;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarProducto` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarProducto`()
begin
	select * from producto;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarProveedores` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarProveedores`()
begin
	select * from proveedor;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `sp_mostrarTiendas` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_mostrarTiendas`()
begin
	select * from tienda;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-19  2:57:12
