CREATE DATABASE  IF NOT EXISTS `zapateria3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `zapateria3`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: zapateria3
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
-- Table structure for table `domicilio`
--

DROP TABLE IF EXISTS `domicilio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domicilio` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `codpost` varchar(10) NOT NULL,
  `colonia` varchar(45) NOT NULL,
  `calle` varchar(45) NOT NULL,
  `numint` varchar(10) DEFAULT NULL,
  `numext` varchar(10) NOT NULL,
  `entrecalle` varchar(255) NOT NULL,
  `idUser` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idUser_idx` (`idUser`),
  CONSTRAINT `idUser` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domicilio`
--

LOCK TABLES `domicilio` WRITE;
/*!40000 ALTER TABLE `domicilio` DISABLE KEYS */;
INSERT INTO `domicilio` VALUES (4,'México','Michoacán','Zitácuaro','61516','Damaso Cárdenas','Benedicto López Sur',NULL,'85','Matamoros y Guillermo Prieto',121217,'2023-05-18 22:59:52','2023-05-18 22:59:52'),(5,'México','Michoacán','Zitácuaro','61516','Damaso Cárdenas','Benedicto López Sur',NULL,'85','Matamoros y Guillermo Prieto',121218,'2023-05-18 23:04:41','2023-05-18 23:04:41'),(7,'México','Michoacán','Zitácuaro','61516','Damaso Cárdenas','Benedicto López Sur',NULL,'85','Matamoros y Guillermo Prieto',121220,'2023-05-18 23:12:27','2023-05-18 23:12:27'),(9,'México','Michoacán','Zitácuaro','61542','Central','Nogal',NULL,'27','Cerradas',121222,'2023-05-19 07:56:41','2023-05-19 07:56:41'),(11,'Mexico','Michoacán','Zitácuaro','61524','Saleciano','Abasolo Norte',NULL,'70','Sepa la fregada',121222,'2023-05-21 07:57:32','2023-05-21 07:57:32'),(12,'Mexico','Zacatecas','ZacatecasCuidad','93720','ZacatecasColonia','CalleZacatecas',NULL,'11','EntreCallesZacatecas',121220,'2023-05-30 02:59:45','2023-05-30 02:59:45'),(13,'México','Baja Califronia sur','Los cabos','78301','Caribe','Solecito',NULL,'90','EntreCallesBajaCalifornia',121220,'2023-05-30 12:56:20','2023-05-30 12:56:20'),(14,'México','Baja Califronia sur','Los cabos','78301','Caribe','Solecito',NULL,'90','EntreCallesBajaCalifornia',121220,'2023-05-30 12:58:41','2023-05-30 12:58:41'),(15,'México','Baja Califronia sur','Los cabos','78301','Caribe','Solecito',NULL,'90','EntreCallesBajaCalifornia',121220,'2023-05-30 12:59:18','2023-05-30 12:59:18'),(16,'México','Baja Califronia sur 2','Los cabos 2','78301 2','Caribe 2','Solecito 2',NULL,'2','EntreCallesBajaCalifornia2',121220,'2023-05-30 13:00:19','2023-05-30 13:00:19'),(17,'México','Baja Califronia sur 2','Los cabos 2','78301 2','Caribe 2','Solecito 2',NULL,'2','EntreCallesBajaCalifornia2',121220,'2023-05-30 13:00:31','2023-05-30 13:00:31'),(18,'México','Baja Califronia sur 2','Los cabos 2','78301 2','Caribe 2','Solecito 2',NULL,'2','EntreCallesBajaCalifornia2',121220,'2023-05-30 13:03:27','2023-05-30 13:03:27'),(19,'México','Baja Califronia sur 2','Los cabos 2','78301 2','Caribe 2','Solecito 2',NULL,'2','EntreCallesBajaCalifornia2',121220,'2023-05-30 13:04:09','2023-05-30 13:04:09'),(20,'México','Baja Califronia sur 2','Los cabos 2','78301 2','Caribe 2','Solecito 2',NULL,'2','EntreCallesBajaCalifornia2',121220,'2023-05-30 13:04:24','2023-05-30 13:04:24'),(21,'México','Baja Califronia sur 2','Los cabos 2','78301 2','Caribe 2','Solecito 2',NULL,'2','EntreCallesBajaCalifornia2',121220,'2023-05-30 13:07:21','2023-05-30 13:07:21'),(22,'México','Baja Califronia sur 2','Los cabos 2','78301 2','Caribe 2','Solecito 2',NULL,'2','EntreCallesBajaCalifornia2',121220,'2023-05-30 13:07:56','2023-05-30 13:07:56'),(23,'a','a','aa','rr','aaa','132',NULL,'34','ff',121220,'2023-05-30 13:40:31','2023-05-30 13:40:31'),(24,'Pais','Estado','Ciudad','13112','Colonia','Calle',NULL,'45','EntreCalles',121220,'2023-05-30 13:41:41','2023-05-30 13:41:41'),(25,'Pais','Estado','Ciudad','13112','Colonia','Calle',NULL,'45','EntreCalles',121220,'2023-05-30 13:42:43','2023-05-30 13:42:43'),(27,'Mexico','Baja Califronia sur','Los cabos','920212','Caribe','No se',NULL,'89','//',121224,'2023-06-14 04:32:29','2023-06-14 04:32:29'),(28,'Mexico','Michoacán','Zitacuaro','615812','Foviste','Avenida la barranca',NULL,'890','No hay',121225,'2023-06-14 09:34:18','2023-06-14 09:34:18'),(29,'Mexico','Michoacán','Zitacuaro','61516','Damaso Cardenas','Benedicto López Sur',NULL,'85','Matamoros y Guillermo Prieto',121225,'2023-06-14 09:57:29','2023-06-14 09:57:29'),(30,'Mexico','Michoacán','Zitacuaro','61516','Damaso Cárdenas','Benedicto López Sur',NULL,'85','Matamoros y Guillermo Prieto',121224,'2023-06-14 10:08:44','2023-06-14 10:08:44');
/*!40000 ALTER TABLE `domicilio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `subtotal` float NOT NULL,
  `fechaPedido` date NOT NULL,
  `idUser` int NOT NULL,
  `idDomicilio` int NOT NULL,
  `idTarjeta` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idUserPedido_idx` (`idUser`),
  KEY `idDomicilioPedido_idx` (`idDomicilio`),
  KEY `idTarjetaPedido_idx` (`idTarjeta`),
  CONSTRAINT `idDomicilioPedido` FOREIGN KEY (`idDomicilio`) REFERENCES `domicilio` (`id`),
  CONSTRAINT `idTarjetaPedido` FOREIGN KEY (`idTarjeta`) REFERENCES `tarjeta` (`id`),
  CONSTRAINT `idUserPedido` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
INSERT INTO `pedido` VALUES (4,3,3035,'2023-06-15',121218,5,8,'2023-06-15 09:05:38','2023-06-15 09:05:38'),(5,2,1078,'2023-06-15',121218,5,8,'2023-06-15 09:17:25','2023-06-15 09:17:25'),(6,2,1300,'2023-06-15',121218,5,8,'2023-06-15 09:19:52','2023-06-15 09:19:52'),(7,2,1200,'2023-06-15',121218,5,8,'2023-06-15 22:08:51','2023-06-15 22:08:51'),(8,1,1500,'2023-06-15',121218,5,8,'2023-06-16 00:15:09','2023-06-16 00:15:09');
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renglonpedido`
--

DROP TABLE IF EXISTS `renglonpedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renglonpedido` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `idZapato` int NOT NULL,
  `idTalla` int NOT NULL,
  `idPedido` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idZapatoRenglonPedido_idx` (`idZapato`),
  KEY `idTallaRenglonPedido_idx` (`idTalla`),
  KEY `idPedidoRenglonPedido_idx` (`idPedido`),
  CONSTRAINT `idPedidoRenglonPedido` FOREIGN KEY (`idPedido`) REFERENCES `pedido` (`id`),
  CONSTRAINT `idTallaRenglonPedido` FOREIGN KEY (`idTalla`) REFERENCES `talla` (`id`),
  CONSTRAINT `idZapatoRenglonPedido` FOREIGN KEY (`idZapato`) REFERENCES `zapato` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renglonpedido`
--

LOCK TABLES `renglonpedido` WRITE;
/*!40000 ALTER TABLE `renglonpedido` DISABLE KEYS */;
INSERT INTO `renglonpedido` VALUES (4,3,111111,1,4,'2023-06-15 09:05:38','2023-06-15 09:05:38'),(5,1,111111,3,4,'2023-06-15 09:05:38','2023-06-15 09:05:38'),(6,1,7777,5,4,'2023-06-15 09:05:38','2023-06-15 09:05:38'),(7,1,7777,2,5,'2023-06-15 09:17:25','2023-06-15 09:17:25'),(8,2,111111,1,5,'2023-06-15 09:17:25','2023-06-15 09:17:25'),(9,1,1212,6,6,'2023-06-15 09:19:52','2023-06-15 09:19:52'),(10,2,111111,1,6,'2023-06-15 09:19:52','2023-06-15 09:19:52'),(11,2,111111,1,7,'2023-06-15 22:08:51','2023-06-15 22:08:51'),(12,1,111111,4,7,'2023-06-15 22:08:51','2023-06-15 22:08:51'),(13,3,111111,1,8,'2023-06-16 00:15:09','2023-06-16 00:15:09');
/*!40000 ALTER TABLE `renglonpedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talla`
--

DROP TABLE IF EXISTS `talla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `talla` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `talla` int NOT NULL,
  `precio` float NOT NULL,
  `idzapato` int NOT NULL,
  `estado` tinyint NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idzapato_idx` (`idzapato`),
  CONSTRAINT `idzapato` FOREIGN KEY (`idzapato`) REFERENCES `zapato` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talla`
--

LOCK TABLES `talla` WRITE;
/*!40000 ALTER TABLE `talla` DISABLE KEYS */;
INSERT INTO `talla` VALUES (1,19,21,500,111111,1,'2023-05-19 02:17:52','2023-06-16 00:15:09'),(2,11,23,78,7777,1,'2023-05-20 07:00:16','2023-06-15 09:17:25'),(3,6,29,785,111111,1,'2023-05-22 11:11:46','2023-06-15 09:05:38'),(4,4,20,200,111111,1,'2023-05-24 02:15:39','2023-06-15 22:08:51'),(5,6,25,750,7777,1,'2023-05-24 06:20:06','2023-06-15 09:05:38'),(6,2,25,300,1212,0,'2023-05-24 21:15:12','2023-06-15 09:19:51'),(7,5,26,300,1212,1,'2023-05-24 21:19:28','2023-05-24 15:51:35'),(8,4,27,560,123456789,1,'2023-06-16 00:09:04','2023-06-16 00:09:04');
/*!40000 ALTER TABLE `talla` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjeta`
--

DROP TABLE IF EXISTS `tarjeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarjeta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numerotarjeta` varchar(20) NOT NULL,
  `ccv` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `fecha` varchar(10) NOT NULL,
  `estado` tinyint DEFAULT NULL,
  `idUser` int NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idUser_idx` (`idUser`),
  CONSTRAINT `idUserTarjeta` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjeta`
--

LOCK TABLES `tarjeta` WRITE;
/*!40000 ALTER TABLE `tarjeta` DISABLE KEYS */;
INSERT INTO `tarjeta` VALUES (1,'12345678912345678912',543,'TarjetaDavid','2024-07-02',1,121220,'2023-05-28 01:22:10','2023-05-28 01:25:12'),(2,'15489745555152111555',152,'SegundaTarjeta','2024-07-02',1,121220,'2023-05-28 03:27:26','2023-05-28 03:27:26'),(3,'456412345698|',123,'MiTerceraTarjeta','2023-05-27',NULL,121220,'2023-05-29 00:28:32','2023-05-29 00:28:32'),(4,'4564123459802',123,'MiCuartoIntento','2023-05-06',NULL,121220,'2023-05-29 01:20:13','2023-05-29 01:20:13'),(5,'4564123459802',456,'MiQuintoIntento','2023-05-25',NULL,121220,'2023-05-29 07:44:17','2023-05-29 07:44:17'),(6,'4564123459802',456,'MiSextoIntento','2023-05-25',NULL,121220,'2023-05-29 07:47:46','2023-05-29 07:47:46'),(7,'456412345698',789,'MiSeptimoIntento','2023-05-12',NULL,121220,'2023-05-29 07:51:50','2023-05-29 07:51:50'),(8,'131391391210',123,'PatriciaTarjet','2023-05-09',NULL,121218,'2023-05-29 08:11:45','2023-05-29 08:11:45'),(9,'84261391230919',456,'PatriciaTarjet2','2023-05-17',NULL,121218,'2023-05-29 08:12:56','2023-05-29 08:12:56'),(10,'837273234\'23',789,'PatriciaTarjet3','2023-05-11',NULL,121218,'2023-05-29 08:13:41','2023-05-29 08:13:41'),(11,'313810213131',123,'MOctavoIntento','2023-05-18',NULL,121220,'2023-05-30 13:43:19','2023-05-30 13:43:19'),(12,'66212910231213',789,'MiNovenoIntento','2023-05-18',NULL,121220,'2023-05-30 13:54:00','2023-05-30 13:54:00'),(13,'2371723123',456,'MiDecimoIntento','2023-05-11',NULL,121220,'2023-05-30 13:57:54','2023-05-30 13:57:54'),(18,'721931373601',123,'MiTarjeta','2023-06-16',NULL,121225,'2023-06-14 10:03:48','2023-06-14 10:03:48'),(20,'138132323232',345,'AlmaTarjeta','2023-06-30',NULL,121224,'2023-06-15 09:55:14','2023-06-15 09:55:14');
/*!40000 ALTER TABLE `tarjeta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `paterno` varchar(40) NOT NULL,
  `materno` varchar(40) NOT NULL,
  `fechanacimiento` date NOT NULL,
  `genero` varchar(20) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `email` varchar(40) NOT NULL,
  `role` varchar(45) DEFAULT 'U',
  `password` varchar(255) NOT NULL,
  `estado` tinyint DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121226 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (121217,'Jose Rubén','Jimenez','De Jesús','2023-05-11','M','7151594445','pepe@correo.com','U','$2y$10$L/RCfWsKmz2XsWdPQ0WZPOO5ktpVMaFBfTL/LcEUSKFm.b.g83hlC',1,'2023-05-18 22:59:52','2023-06-14 00:41:56'),(121218,'Patricia','De Jesús','López','2023-05-13','F','54445454545','patricia@correo.com','U','$2y$10$Q3HEQ8lvvtLKOMQIx/iQaeY8WO9nOPzXeVSXVzJc5KZGCuIqKpwqa',1,'2023-05-18 23:04:41','2023-06-14 00:41:56'),(121220,'David','Jiménez','De Jesús','2023-06-01','M','7151630842','micorreo@gmail.com','A','$2y$10$tjL/zww9iKEiHJFh06P6AO57SId0Iz.YLch7FlVxbSkg0IJiq9v6S',1,'2023-05-18 23:12:27','2023-06-15 00:53:25'),(121222,'Jairo','Lopez','Ayala','2001-05-04','M','8776546791','jairo@correo.com','U','$10$tjL/zww9iKEiHJFh06P6AO57SId0Iz.YLch7FlVxbSkg0IJiq9v6S',1,'2023-05-27 23:43:35','2023-06-14 00:41:56'),(121223,'Omar','Morales','Correa','2023-06-05','M','6726191290','omar@correo.com','A','$2y$10$t71.FVjAaq1ByrxMsCqZr.L6gJANly39SjNeEvqPBYgHZG2uOS6v2',0,'2023-06-14 04:30:52','2023-06-15 01:45:48'),(121224,'Alma Delia','Shate','Gallo','2023-06-15','F','6246279045','alma@correo.com','U','$2y$10$rLBAod5UHOROoyabCZG.4uSpsMSQXQX0As5NUrM5yjpirFesJg4m.',1,'2023-06-14 04:32:29','2023-06-14 04:56:39'),(121225,'Jonatan','Velazquez','Jimenez','2023-05-29','M','9371721190','jonatan@correo.com','U','$2y$10$lhvaefW1oAu.nBdB.5/yu.p1vp5z8DKAUD9PB5ZYwun2ZkrATjsW2',1,'2023-06-14 09:34:18','2023-06-14 04:56:39');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zapato`
--

DROP TABLE IF EXISTS `zapato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zapato` (
  `id` int NOT NULL,
  `color` varchar(30) NOT NULL,
  `estilo` varchar(30) NOT NULL,
  `material` varchar(300) NOT NULL,
  `modelo` varchar(30) NOT NULL,
  `url` varchar(255) NOT NULL,
  `estado` tinyint NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zapato`
--

LOCK TABLES `zapato` WRITE;
/*!40000 ALTER TABLE `zapato` DISABLE KEYS */;
INSERT INTO `zapato` VALUES (1212,'Negro','Formal','Cuero Sintetico','Zapato Formal con agujeta','zapato3.jpg',1,'2023-05-15 11:35:19','2023-05-24 21:10:51'),(7777,'Negro y Gris','Casual','Hecha de malla.','Senderimo Pro','zapato1.jpg',1,'2023-05-20 12:33:56','2023-05-27 20:52:36'),(111111,'Blanco negro','Tenis','Lona de resorte','Sport XF','zapato2.jpg',1,'2023-05-18 18:24:17','2023-05-24 00:02:21'),(123456789,'Negro','Urbano','Tela','Tenis','tenis.jpg',1,'2023-06-16 00:07:42','2023-06-16 00:20:28');
/*!40000 ALTER TABLE `zapato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'zapateria3'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-19  2:55:14
