-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: location_appartement
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

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
-- Table structure for table `apartement`
--

DROP TABLE IF EXISTS `apartement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `apartement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `prix` float NOT NULL,
  `detaille` text COLLATE utf8mb4_general_ci NOT NULL,
  `adrresse` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `categorie_appartement` int NOT NULL,
  `image` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `status` int NOT NULL,
  `chambre` int NOT NULL,
  `superficie` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `image2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apartement`
--

LOCK TABLES `apartement` WRITE;
/*!40000 ALTER TABLE `apartement` DISABLE KEYS */;
INSERT INTO `apartement` VALUES (24,'Appartement 1',100,'C\'est une villa avec 5 chambres et 2 salle de bain','Mukuna',1,'543c0b6e-1873-416b-be43-870cd3c6b149.jpg',1,5,'100','efdb4ed7-0c89-44bc-aa64-18c742d235b6.jpg'),(25,'Appartement2',120,'Cette belle maisons a 4 chambre 3 salle de bains et une piscine','Mutiri',2,'40cf21c3-1891-470f-a878-fb229d977ffc.jpg',1,4,'80','cf9c30ea-8a75-4dbb-92ec-74486930e435.jpg'),(26,'Appartement3',200,'Une bele maison spacieux fait pour une famille nombreuse avec 5 chambre et 3 salle de bain','Kitulu',3,'681774b1-ed51-48a8-aec7-4f6aa53579c1.jpg',1,5,'120','dfd51fbf-0280-4acc-a7c1-951f0e399a07.jpg'),(27,'Appartement4',300,'C\'est une vila familial avec 5chambre et 3 salle de bains mais aussi une piscine','MGL',1,'51099f23-fe5e-4afb-89c1-acb20cd4cc4d.jpg',1,5,'120','740b2d52-94e4-4424-8e8c-4eb169d3dd8e.jpg'),(28,'Appartement5',100,'C\'est un appartement fais pour les jeunes marie','Furu',1,'dca45ee2-a6a9-4927-ad4f-18f0ea47a2a4.jpg',1,3,'50','f938f710-457d-4287-aa28-665dc4b9ff35.jpg'),(30,'Appartement7',120,'C\'est un appartement spacoeiux qui a 3 chambre et 2 salle de bains ','Kitulu',1,'df971122-8fbd-4757-852d-ef1e074edcf9.png',1,5,'120','4dafbb4f-4f27-4007-bc39-7115c03e77d1.jpg'),(31,'Appartement6',150,'C\'est une maison tres bien équipè avec 5 chambre et 2 salle de bain','Kitatumba',1,'cce1ce30-f269-49aa-9fc8-fe40e70f0706.png',1,5,'120','ebbc24a9-d781-45cd-935c-5d87a49ccdd2.jpg');
/*!40000 ALTER TABLE `apartement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorie_appartement`
--

DROP TABLE IF EXISTS `categorie_appartement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie_appartement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie_appartement`
--

LOCK TABLES `categorie_appartement` WRITE;
/*!40000 ALTER TABLE `categorie_appartement` DISABLE KEYS */;
INSERT INTO `categorie_appartement` VALUES (3,'VIP'),(5,'VVIP'),(6,'Normal');
/*!40000 ALTER TABLE `categorie_appartement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `postnom` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `prenom` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `etat_civil` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `catre_electeur` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (2,'MUMBERE','Kavalami','Muyisa','0841547134','Celibataire','30c2bfa1-8f84-4e65-a76c-dd6ca478c24e.png',1),(3,'Grace','Lusenge','Grace','0994154713','Marié','3e0cf6bc-ac47-4bcd-a7d4-38cae431cc6d.jpg',1),(4,'Kambale','Kavalami','Muyisa','0941547134','Marié','b07e287f-a987-46ef-98d4-b0a0aef7be64.pdf',1),(5,'Kahindo','Basisia','Gloria','0994154713','Celibataire','4a9c2305-77e5-4700-8bc4-75f8b054d7e0.jpg',1);
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commentaire`
--

DROP TABLE IF EXISTS `commentaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commentaire` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `Nom` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `message` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commentaire`
--

LOCK TABLES `commentaire` WRITE;
/*!40000 ALTER TABLE `commentaire` DISABLE KEYS */;
INSERT INTO `commentaire` VALUES (3,'2024-09-23','Mumbere','muykav@gma.com','merci'),(4,'2024-09-24','Mumbere','maggy@gmail.com','Je suis tellement satisfait'),(5,'2024-09-28','Lusenge','nzukolusenge@gmail.com','Durant mon sejour dans l\'un de vos appartements j\'etait tellement satisfait'),(6,'2024-10-03','Kavalami','muykav@gma.com','Salut'),(7,'2024-10-03','Kavalami','muykav@gma.com','Je suis ravi merci beaucoup'),(8,'2024-10-04','Jamas','muykav@gma.com','Merci votre service est exelent'),(9,'2024-10-06','Kavalami','muykav@gml.com','Je suis tellement ravis de vos service'),(10,'2024-10-08','Masimengo','muykav@gma.com','Bonjour je suis tellement satisfait de vos services'),(11,'2024-10-09','Kavalami','muykav@gma.com','Vos appartements sont genial merci beaucoup');
/*!40000 ALTER TABLE `commentaire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `image` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (1,'DRAPEAU RDC.png'),(2,'c14718d0-3bd0-402a-83ab-e89aa3c54408.png');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `debut` date NOT NULL,
  `fin` date NOT NULL,
  `client` int NOT NULL,
  `appartement` int NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (3,'2024-10-04','2024-10-17','2024-11-01',2,25,1),(4,'2024-10-08','2024-10-08','2024-12-08',4,26,1),(5,'2024-10-08','2024-10-08','2026-04-08',2,24,1),(6,'2024-10-08','2024-10-08','2024-10-11',2,28,1),(7,'2024-10-08','2024-10-08','2024-10-16',2,24,1),(8,'2024-10-08','2024-10-08','2025-02-08',3,27,1),(9,'2024-10-09','2024-10-09','2025-02-09',5,30,1);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paiement`
--

DROP TABLE IF EXISTS `paiement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paiement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `location` int NOT NULL,
  `montat` int NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paiement`
--

LOCK TABLES `paiement` WRITE;
/*!40000 ALTER TABLE `paiement` DISABLE KEYS */;
INSERT INTO `paiement` VALUES (1,'2024-10-04',2,120,1),(2,'2024-10-05',3,300,1),(3,'2024-10-08',4,1200,1),(4,'2024-10-08',8,500,1),(5,'2024-10-09',9,300,1);
/*!40000 ALTER TABLE `paiement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `appartement` int DEFAULT NULL,
  `nom` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `preuve` varchar(255) DEFAULT NULL,
  `duree` int DEFAULT NULL,
  `debut` date DEFAULT NULL,
  `lecture` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (1,'2024-10-03',25,'Muyisa Kavalami','muykav@gma.com','0841547134','47021ef8-c7a4-4c9a-a2ab-fa599b85ca9e.png',2,'2024-10-04','1'),(2,'2024-10-03',25,'Muyisa Kavalami','muykav@gma.com','0841547134','ef59ce5e-626e-4f2c-8a14-0d0ca62131cf.png',2,'2024-10-15','1'),(3,'2024-10-08',27,'Muyisa','muykav@gma.com','0841547134','2ede2784-0689-405e-8e8b-197b1615da60.jpeg',6,'2024-10-10','1'),(4,'2024-10-09',31,'Muyisa Kavalami','muykav@gma.com','0841547134','f4be91d6-2cbd-46d9-9fcf-6d146d80441c.png',6,'2024-10-12','1');
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `nom` varchar(45) DEFAULT NULL,
  `prenom` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(45) DEFAULT NULL,
  `postnom` varchar(45) DEFAULT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(45) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Muyisa','Kavalami','MKM','$2b$12$PlbGbQXofVtKgEWpEJWnUeIcxh9tWgw8PfbZABFJmBGDMK3F6QtVi','Admin','83f8f909-9c68-41a2-a43a-d5e684febe8d.jpg'),(4,'Maggy','KAGHONGYA','maggy','$2b$12$8kzYt.bt7SZj2zASjDeETeDt/LOdOV7.xvrTAk6dpXMxKDKvdcDIm','User','992428b1-cf23-4394-b731-d69c84625b5b.JPG'),(5,'Mumbere','KAGHONGYA','KH','$2b$12$fNP7sJNdKXPET4XTr3mUbebQ.E0YkChvjWrmHzufCzFr997DCwucu','Admin','c69b98a4-0758-4687-9a8c-f58b4fd697ee.JPG'),(6,'Kahindo','Jovial','jovi','$2b$12$pwF8ik5H9GrRWcdpVftOoOQIuN6sgMUem/qSj0Ad9fZmhS1Xwyx0a','User','138d4d13-4150-4113-baa7-d32d2eb0e514.JPG');
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

-- Dump completed on 2024-10-09 11:08:53
