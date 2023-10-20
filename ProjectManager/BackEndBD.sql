CREATE DATABASE  IF NOT EXISTS `backend` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `backend`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: backend
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
-- Table structure for table `actividad`
--

DROP TABLE IF EXISTS `actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actividad` (
  `id_act` int NOT NULL AUTO_INCREMENT,
  `descripcion` longtext NOT NULL,
  `finicio` date NOT NULL,
  `ffin` date NOT NULL,
  `testimado` varchar(45) NOT NULL,
  `prioridad` varchar(45) NOT NULL,
  `estado` tinyint NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_act`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividad`
--

LOCK TABLES `actividad` WRITE;
/*!40000 ALTER TABLE `actividad` DISABLE KEYS */;
INSERT INTO `actividad` VALUES (1,'Descripcion de prueba','2022-11-21','2022-12-01','10 dias','media',1,'2022-11-22 00:04:56','2022-11-22 01:18:15'),(2,'Descripcion de prueba2','2022-11-22','2022-12-02','10 dias','media',1,'2022-11-22 00:04:56','2022-11-22 01:18:15');
/*!40000 ALTER TABLE `actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos`
--

DROP TABLE IF EXISTS `datos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `datos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dificultad` int NOT NULL,
  `palabra` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=361 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos`
--

LOCK TABLES `datos` WRITE;
/*!40000 ALTER TABLE `datos` DISABLE KEYS */;
INSERT INTO `datos` VALUES (311,1,'camara'),(312,3,'base de datos'),(313,3,'desoxirribonuclico'),(314,1,'computadora'),(315,1,'chispa'),(316,3,'microcontrolador'),(317,2,'centro de computo'),(318,1,'cafeteria'),(319,1,'carro'),(320,2,'silverado'),(321,1,'camara'),(322,3,'base de datos'),(323,3,'desoxirribonuclico'),(324,1,'computadora'),(325,1,'chispa'),(326,3,'microcontrolador'),(327,2,'centro de computo'),(328,1,'cafeteria'),(329,1,'carro'),(330,2,'silverado'),(331,1,'camara'),(332,3,'base de datos'),(333,3,'desoxirribonuclico'),(334,1,'computadora'),(335,1,'chispa'),(336,3,'microcontrolador'),(337,2,'centro de computo'),(338,1,'cafeteria'),(339,1,'carro'),(340,2,'silverado'),(341,1,'camara'),(342,3,'base de datos'),(343,3,'desoxirribonuclico'),(344,1,'computadora'),(345,1,'chispa'),(346,3,'microcontrolador'),(347,2,'centro de computo'),(348,1,'cafeteria'),(349,1,'carro'),(350,2,'silverado'),(351,1,'camara'),(352,3,'base de datos'),(353,3,'desoxirribonuclico'),(354,1,'computadora'),(355,1,'chispa'),(356,3,'microcontrolador'),(357,2,'centro de computo'),(358,1,'cafeteria'),(359,1,'carro'),(360,2,'silverado');
/*!40000 ALTER TABLE `datos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro` (
  `isbn` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) NOT NULL,
  `autor` varchar(75) NOT NULL,
  `edicion` varchar(75) NOT NULL,
  `editorial` varchar(75) NOT NULL,
  `clasificacion` varchar(75) NOT NULL,
  PRIMARY KEY (`isbn`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
INSERT INTO `libro` VALUES (1,'A mitad del camino','AMLO','Primera','Planeta','Politica'),(2,'Matematicas para la computación','Raúl','Primera','Alfa y Omega','Computación'),(10,'aaaa','autor','edicion','editorial','clasificacion'),(11,'aaaa','autor','edicion','editorial','clasificacion'),(12,'Álgebra de Baldor','Baldor','Cuarta','Patria','Academico'),(13,'aaaa','autor','edicion','editorial','clasificacion'),(14,'aaaa','autor','edicion','editorial','clasificacion'),(15,'aaaa','autor','edicion','editorial','clasificacion'),(16,'aaaa','autor','edicion','editorial','clasificacion'),(17,'aaaa','autor','edicion','editorial','clasificacion'),(18,'aaaa','autor','edicion','editorial','clasificacion'),(19,'aaaa','autor','edicion','editorial','clasificacion'),(20,'aaaa','autor','edicion','editorial','clasificacion'),(21,'aaaa','autor','edicion','editorial','clasificacion'),(22,'aaaa','autor','edicion','editorial','clasificacion'),(23,'Seguridad Informatica','David','Segunda','Diamante','Computación'),(24,'Fundamentos','Felicitas','Primera','Tecnologico','Computación'),(25,'aaaa','autor','edicion','editorial','clasificacion');
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permiso`
--

DROP TABLE IF EXISTS `permiso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permiso` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `estado` tinyint NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permiso`
--

LOCK TABLES `permiso` WRITE;
/*!40000 ALTER TABLE `permiso` DISABLE KEYS */;
INSERT INTO `permiso` VALUES (1,'nuevo_usuario',1,'2022-11-14 21:40:59','2022-11-14 21:40:59'),(2,'consulta_usuario',1,'2022-11-14 21:40:59','2022-11-14 21:40:59'),(3,'modificar_usuario',1,'2022-11-14 21:40:59','2022-11-14 21:40:59'),(4,'eliminar_usuario',1,'2022-11-14 21:40:59','2022-11-14 21:40:59'),(5,'nuevop',0,'2022-11-16 23:32:44','2022-11-16 23:33:12'),(6,'Listarrrr',0,'2022-11-17 03:32:18','2022-11-17 03:32:35');
/*!40000 ALTER TABLE `permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `id_per` int NOT NULL,
  `nombre_per` varchar(20) NOT NULL,
  `ap_persona` varchar(20) NOT NULL,
  PRIMARY KEY (`id_per`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'vanessa','martinez'),(2,'david','jimenez'),(3,'pedro','luna'),(4,'brian','perez'),(5,'emmanuel','soria'),(6,'josue','marin'),(7,'citlaly','lopez'),(8,'juan','rodriguez'),(9,'sammuel','jimenez'),(10,'jose','tellez'),(12,'carlos','diaz');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto`
--

DROP TABLE IF EXISTS `proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyecto` (
  `id_pro` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `tiempoestimado` varchar(45) NOT NULL,
  `descripcion` longtext NOT NULL,
  `requerimientos` longtext NOT NULL,
  `estado` tinyint NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_pro`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto`
--

LOCK TABLES `proyecto` WRITE;
/*!40000 ALTER TABLE `proyecto` DISABLE KEYS */;
INSERT INTO `proyecto` VALUES (1,'tareaBackEnd','5 dias','xd','xd',1,'2022-11-22 00:06:26','2022-11-22 00:06:26'),(2,'tareaBackEnd2','5 dias','xd','xd',1,'2022-11-22 00:06:26','2022-11-22 00:06:26');
/*!40000 ALTER TABLE `proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relacion`
--

DROP TABLE IF EXISTS `relacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `relacion` (
  `id_rel` int NOT NULL,
  `id_pro` int NOT NULL,
  `id_act` int NOT NULL,
  `id_usu` int NOT NULL,
  PRIMARY KEY (`id_rel`),
  KEY `id_act` (`id_act`),
  KEY `id_pro` (`id_pro`),
  KEY `id_usu` (`id_usu`),
  CONSTRAINT `id_act` FOREIGN KEY (`id_act`) REFERENCES `actividad` (`id_act`),
  CONSTRAINT `id_pro` FOREIGN KEY (`id_pro`) REFERENCES `proyecto` (`id_pro`),
  CONSTRAINT `id_usu` FOREIGN KEY (`id_usu`) REFERENCES `usuario3` (`id_usu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relacion`
--

LOCK TABLES `relacion` WRITE;
/*!40000 ALTER TABLE `relacion` DISABLE KEYS */;
INSERT INTO `relacion` VALUES (1,1,1,1),(2,1,2,2);
/*!40000 ALTER TABLE `relacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `estado` tinyint NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'Administrador',1,'2022-11-14 21:31:43','2022-11-14 21:31:43'),(2,'Usuario',1,'2022-11-14 21:31:43','2022-11-14 21:31:43'),(3,'Jefeeee',0,'2022-11-16 10:27:57','2022-11-16 10:35:48'),(4,'nuevopermisoxd',0,'2022-11-16 23:30:09','2022-11-16 23:34:02'),(5,'Jefeeeee',0,'2022-11-17 03:31:06','2022-11-17 03:31:28');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol_permiso`
--

DROP TABLE IF EXISTS `rol_permiso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol_permiso` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rol_id` int NOT NULL,
  `permiso_id` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `rol_id` (`rol_id`),
  KEY `permiso_id` (`permiso_id`),
  CONSTRAINT `rol_permiso_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`),
  CONSTRAINT `rol_permiso_ibfk_2` FOREIGN KEY (`permiso_id`) REFERENCES `permiso` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol_permiso`
--

LOCK TABLES `rol_permiso` WRITE;
/*!40000 ALTER TABLE `rol_permiso` DISABLE KEYS */;
INSERT INTO `rol_permiso` VALUES (1,1,1,'2022-11-14 21:47:40','2022-11-14 21:47:40'),(2,1,2,'2022-11-14 21:47:40','2022-11-14 21:47:40'),(3,1,3,'2022-11-14 21:47:40','2022-11-14 21:47:40'),(4,1,4,'2022-11-14 21:47:40','2022-11-14 21:47:40'),(5,2,2,'2022-11-14 21:47:40','2022-11-14 21:47:40'),(6,1,1,'2022-11-17 04:56:24','2022-11-17 04:56:24');
/*!40000 ALTER TABLE `rol_permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `paterno` varchar(100) NOT NULL,
  `materno` varchar(100) NOT NULL,
  `edad` varchar(5) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `genero` varchar(5) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'David','Jimenez','De Jesus','20','2022-10-19','on','david_jim','$2y$10$yHuVDzoa5nXMCTMRrGcYA.Q5ymEPlDgTRjaswbnFyItHaDjJGHGR6'),(2,'David','Jimenez','De Jesus','20','2022-10-19','on','david_jim','$2y$10$gQ7x8uRRIzdmQoQhL86zfe5f730hJWA4Qz5bSsa4QfsEl/fWG8gIO'),(3,'Jose Rubén','Jimenez','De Jesus','24','2022-10-04','M','pepe_jim','$2y$10$E9S.GhQMjydfuMCHHskzDO4rINpfLi1hfZm9q8mBQL.8c7drDaTuG'),(4,'David','Jimenez','De Jesus','20','2022-10-13','M','david_jim1','$2y$10$iT5C4tBELnSM89rwvEAOSewQ4myMd8rAjgQrzqLbtHHlIc7CqqOjq');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario2`
--

DROP TABLE IF EXISTS `usuario2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario2` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `paterno` varchar(100) NOT NULL,
  `materno` varchar(100) NOT NULL,
  `edad` varchar(5) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `genero` varchar(5) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `estado` tinyint NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario2`
--

LOCK TABLES `usuario2` WRITE;
/*!40000 ALTER TABLE `usuario2` DISABLE KEYS */;
INSERT INTO `usuario2` VALUES (1,'David','Jimenez','De Jesus','20','2002-07-02','M','davidjim','123',1,'2022-11-04 20:50:01','2022-11-11 18:47:39'),(2,'Jose Rubén','Jimenez','De Jesus','24','2022-11-30','M','ruben123','123',1,'2022-11-08 04:34:51','2022-11-08 04:34:51');
/*!40000 ALTER TABLE `usuario2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario3`
--

DROP TABLE IF EXISTS `usuario3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario3` (
  `id_usu` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `paterno` varchar(100) NOT NULL,
  `materno` varchar(100) NOT NULL,
  `nacimiento` date NOT NULL,
  `genero` varchar(2) NOT NULL,
  `telefono` int NOT NULL,
  `correo` varchar(45) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `estado` tinyint NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usu`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario3`
--

LOCK TABLES `usuario3` WRITE;
/*!40000 ALTER TABLE `usuario3` DISABLE KEYS */;
INSERT INTO `usuario3` VALUES (1,'David','Jiménez','De Jesús','2002-07-02','M',2147483647,'correo@david.com','david_jim','123',1,'2022-11-22 00:07:38','2022-11-22 01:13:36'),(2,'Carlos','Diaz','De Jesús','2002-07-02','M',2147483647,'correo@david.com','david_jim','123',1,'2022-11-22 00:07:38','2022-11-22 01:13:36');
/*!40000 ALTER TABLE `usuario3` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-19  2:58:35
