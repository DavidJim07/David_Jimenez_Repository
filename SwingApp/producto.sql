CREATE DATABASE  IF NOT EXISTS `producto` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `producto`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: producto
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
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `codigoBarras` varchar(30) NOT NULL,
  `nombreProducto` varchar(30) DEFAULT NULL,
  `marcaProducto` varchar(30) DEFAULT NULL,
  `tipoProducto` varchar(30) DEFAULT NULL,
  `contenidoProducto` varchar(30) DEFAULT NULL,
  `unidadMedidaProducto` varchar(30) DEFAULT NULL,
  `cantidadProducto` int DEFAULT NULL,
  `stockMaxProducto` int DEFAULT NULL,
  `stockMinProducto` int DEFAULT NULL,
  `precioVentaProducto` float DEFAULT NULL,
  `precioCompraProducto` float DEFAULT NULL,
  `presentacionProducto` varchar(30) DEFAULT NULL,
  `descripcionProducto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`codigoBarras`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES ('1111111111112','Fanta sabor Fresa','Grupo Femsa','Refresco','2','Litros',1,32,10,28.67,23.45,'Botella de plastico','Refresco sabor Fresa'),('1111111111117','Leche Deslactosada','Lala','Alimento','500','Mililitros',10,25,15,25,19,'Caja','Leche light'),('1111111111118','Carlos V','Nestle','Chocolate','20','gramos',20,12,5,12.3,8.4,'Individual','Chocolate de barra'),('1111111111161','Gansito','Marinela','Pastelito','50','Gramos',14,16,4,15,10.52,'Sobre individual','Pastelito gansito ');
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-19  3:52:27
