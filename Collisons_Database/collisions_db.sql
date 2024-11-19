CREATE DATABASE  IF NOT EXISTS `collisions_database` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `collisions_database`;
-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (x86_64)
--
-- Host: localhost    Database: collisions_database
-- ------------------------------------------------------
-- Server version	8.4.1

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
-- Table structure for table `collision`
--

DROP TABLE IF EXISTS `collision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collision` (
  `collision_id` int NOT NULL AUTO_INCREMENT,
  `crash_date` date DEFAULT NULL,
  `crash_time` time DEFAULT NULL,
  `on_street_name` varchar(45) DEFAULT NULL,
  `cross_street_name` varchar(45) DEFAULT NULL,
  `off_street_name` varchar(45) DEFAULT NULL,
  `number_of_persons_injured` int DEFAULT NULL,
  `number_of_persons_killed` int DEFAULT NULL,
  `number_of_pedestrians_injured` int DEFAULT NULL,
  `number_of_pedestrians_killed` int DEFAULT NULL,
  `number_of_cyclists_injured` int DEFAULT NULL,
  `number_of_cyclists_killed` int DEFAULT NULL,
  `number_of_motorists_injured` int DEFAULT NULL,
  `number_of_motorists_killed` int DEFAULT NULL,
  `location_id` int NOT NULL,
  PRIMARY KEY (`collision_id`),
  UNIQUE KEY `collision_id_UNIQUE` (`collision_id`),
  KEY `fk_collision_location_idx` (`location_id`),
  CONSTRAINT `fk_collision_location` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collision`
--

LOCK TABLES `collision` WRITE;
/*!40000 ALTER TABLE `collision` DISABLE KEYS */;
INSERT INTO `collision` VALUES (1,'2024-01-01','08:00:00','1st Ave','E 10th St','',2,0,0,0,0,0,2,0,1),(2,'2024-01-02','09:15:00','2nd Ave','E 20th St','',3,1,1,0,0,0,2,0,2),(3,'2024-01-03','10:30:00','3rd Ave','E 30th St','',1,0,0,0,0,1,0,0,3),(4,'2024-01-04','11:45:00','4th Ave','E 40th St','',0,0,0,0,0,0,0,0,4),(5,'2024-01-05','13:00:00','5th Ave','E 50th St','',2,1,0,0,1,0,1,1,5),(6,'2024-01-06','14:15:00','6th Ave','E 60th St','',3,1,1,1,0,0,2,0,6),(7,'2024-01-07','15:30:00','7th Ave','E 70th St','',0,0,0,0,0,0,0,0,7),(8,'2024-01-08','16:45:00','8th Ave','E 80th St','',4,2,1,1,0,0,1,1,8),(9,'2024-01-09','18:00:00','9th Ave','E 90th St','',2,0,0,0,0,0,1,0,9),(10,'2024-01-10','19:15:00','10th Ave','E 100th St','',3,1,0,0,1,0,2,1,10),(11,'2024-01-11','20:30:00','11th Ave','E 110th St','',1,0,0,0,0,1,0,0,11),(12,'2024-01-12','21:45:00','12th Ave','E 120th St','',4,2,1,1,0,0,1,1,12),(13,'2024-01-13','08:00:00','13th Ave','E 130th St','',2,0,0,0,0,0,1,0,13),(14,'2024-01-14','09:15:00','14th Ave','E 140th St','',3,1,0,0,1,0,2,1,14),(15,'2024-01-15','10:30:00','15th Ave','E 150th St','',1,0,0,0,0,1,0,0,15),(16,'2024-01-16','11:45:00','16th Ave','E 160th St','',0,0,0,0,0,0,0,0,16),(17,'2024-01-17','13:00:00','17th Ave','E 170th St','',2,1,0,0,1,0,1,1,17),(18,'2024-01-18','14:15:00','18th Ave','E 180th St','',3,1,1,1,0,0,2,0,18),(19,'2024-01-19','15:30:00','19th Ave','E 190th St','',0,0,0,0,0,0,0,0,19),(20,'2024-01-20','16:45:00','20th Ave','E 200th St','',4,2,1,1,0,0,1,1,20),(21,'2024-01-21','18:00:00','Park Ave','E 59th St','',1,0,0,0,0,0,0,0,21),(22,'2024-01-22','19:00:00','Emmons Ave','Sheepshead Bay Rd','',3,1,0,0,0,0,2,0,22),(23,'2024-01-23','20:00:00','Utopia Pkwy','Horace Harding Expy','',2,1,1,0,0,0,0,0,23),(24,'2024-01-24','21:00:00','Bruckner Blvd','Hunts Point Ave','',1,0,0,0,0,0,0,0,24),(25,'2024-01-25','22:00:00','Richmond Rd','Amboy Rd','',4,2,1,0,1,0,2,0,25),(26,'2024-01-26','23:00:00','Ave B','E 10th St','',3,1,0,0,0,0,1,1,26),(27,'2024-01-27','00:00:00','Atlantic Ave','Flatbush Ave','',2,1,0,0,0,0,2,1,27),(28,'2024-01-28','01:00:00','Jamaica Ave','Merrick Blvd','',4,2,0,0,0,0,2,0,28),(29,'2024-01-29','02:00:00','Bronx River Pkwy','E 180th St','',3,1,1,0,1,0,2,1,29),(30,'2024-01-30','03:00:00','Hylan Blvd','Midland Ave','',2,0,0,0,0,0,1,0,30);
/*!40000 ALTER TABLE `collision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collision_factor`
--

DROP TABLE IF EXISTS `collision_factor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collision_factor` (
  `collision_id` int NOT NULL,
  `contributing_factor_id` int NOT NULL,
  PRIMARY KEY (`collision_id`,`contributing_factor_id`),
  KEY `fk_collision_has_contributing_factor_contributing_factor1_idx` (`contributing_factor_id`),
  KEY `fk_collision_has_contributing_factor_collision1_idx` (`collision_id`),
  CONSTRAINT `fk_collision_has_contributing_factor_collision1` FOREIGN KEY (`collision_id`) REFERENCES `collision` (`collision_id`),
  CONSTRAINT `fk_collision_has_contributing_factor_contributing_factor1` FOREIGN KEY (`contributing_factor_id`) REFERENCES `contributing_factor` (`contributing_factor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collision_factor`
--

LOCK TABLES `collision_factor` WRITE;
/*!40000 ALTER TABLE `collision_factor` DISABLE KEYS */;
INSERT INTO `collision_factor` VALUES (1,1),(1,2),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30);
/*!40000 ALTER TABLE `collision_factor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `collisions_manhattan_2024`
--

DROP TABLE IF EXISTS `collisions_manhattan_2024`;
/*!50001 DROP VIEW IF EXISTS `collisions_manhattan_2024`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `collisions_manhattan_2024` AS SELECT 
 1 AS `collision_id`,
 1 AS `crash_date`,
 1 AS `crash_time`,
 1 AS `location_id`,
 1 AS `borough`,
 1 AS `on_street_name`,
 1 AS `cross_street_name`,
 1 AS `off_street_name`,
 1 AS `number_of_persons_injured`,
 1 AS `number_of_persons_killed`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `contributing_factor`
--

DROP TABLE IF EXISTS `contributing_factor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contributing_factor` (
  `contributing_factor_id` int NOT NULL AUTO_INCREMENT,
  `contributing_factor_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`contributing_factor_id`),
  UNIQUE KEY `contributing_factor_id_UNIQUE` (`contributing_factor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contributing_factor`
--

LOCK TABLES `contributing_factor` WRITE;
/*!40000 ALTER TABLE `contributing_factor` DISABLE KEYS */;
INSERT INTO `contributing_factor` VALUES (1,'Driver Distracted'),(2,'Failure to Yield Right-of-Way'),(3,'Backing Unsafely'),(4,'Alcohol Involved'),(5,'Unsafe Speed'),(6,'Fell Asleep'),(7,'Prescription Medication'),(8,'Driver Inexperience'),(9,'Not Following Traffic Control '),(10,'Weather Condition'),(11,'Brakes Defective'),(12,'Steering Failure'),(13,'View Obstructed/Limited'),(14,'Pavement Slippery'),(15,'Aggressive Driving/Road Rage'),(16,'Driverless/Runaway Vehicle'),(17,'Fatigued/Drowsy'),(18,'Cell Phone/Texting'),(19,'Illness'),(20,'Eating or Drinking'),(21,'Outside Car Distraction'),(22,'Glare'),(23,'Other Vehicle'),(24,'Confusion'),(25,'Tire Failure/Inadequate'),(26,'Listening/Using Headphones'),(27,'Reaction to Other Uninvolved Vehicle'),(28,'Using GPS Device'),(29,'Lighting Condition'),(30,'Mechanical Failure');
/*!40000 ALTER TABLE `contributing_factor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `borough` varchar(45) DEFAULT NULL,
  `zip_code` int DEFAULT NULL,
  `longitude` decimal(10,8) DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY `location_id_UNIQUE` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Manhattan',10001,-73.99670000,40.74860000),(2,'Brooklyn',11201,-73.99160000,40.69580000),(3,'Queens',11354,-73.82440000,40.75850000),(4,'Bronx',10451,-73.92520000,40.82700000),(5,'Staten Island',10301,-74.07560000,40.64370000),(6,'Manhattan',10018,-73.99060000,40.75530000),(7,'Brooklyn',11215,-73.99130000,40.66960000),(8,'Queens',11101,-73.93960000,40.74890000),(9,'Bronx',10458,-73.88600000,40.86570000),(10,'Staten Island',10314,-74.15020000,40.58340000),(11,'Manhattan',10025,-73.96540000,40.79990000),(12,'Brooklyn',11220,-74.01210000,40.64150000),(13,'Queens',11691,-73.75150000,40.60350000),(14,'Bronx',10463,-73.90880000,40.87680000),(15,'Staten Island',10303,-74.17260000,40.63550000),(16,'Manhattan',10011,-74.00060000,40.74090000),(17,'Brooklyn',11211,-73.95260000,40.71080000),(18,'Queens',11377,-73.89470000,40.74200000),(19,'Bronx',10467,-73.87720000,40.86860000),(20,'Staten Island',10312,-74.17230000,40.54970000),(21,'Manhattan',10022,-73.96800000,40.75810000),(22,'Brooklyn',11235,-73.95900000,40.57750000),(23,'Queens',11365,-73.78900000,40.73310000),(24,'Bronx',10474,-73.88310000,40.81100000),(25,'Staten Island',10306,-74.12100000,40.56540000),(26,'Manhattan',10009,-73.97870000,40.72780000),(27,'Brooklyn',11217,-73.98050000,40.68080000),(28,'Queens',11435,-73.79900000,40.69940000),(29,'Bronx',10470,-73.86840000,40.90330000),(30,'Staten Island',10308,-74.14960000,40.55490000);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `vehicle_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`),
  UNIQUE KEY `vehicle_id_UNIQUE` (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES (1,'Sedan'),(2,'SUV'),(3,'Pickup Truck'),(4,'Van'),(5,'Motorcycle'),(6,'Bicycle'),(7,'Bus'),(8,'Taxi'),(9,'Ambulance'),(10,'Fire Truck'),(11,'Delivery Truck'),(12,'Garbage Truck'),(13,'Police Car'),(14,'Minivan'),(15,'Sports Car'),(16,'Convertible'),(17,'Coupe'),(18,'Station Wagon'),(19,'Electric Scooter'),(20,'Moped'),(21,'Trailer'),(22,'RV'),(23,'Tractor'),(24,'Limo'),(25,'Jeep'),(26,'Mini Cooper'),(27,'Golf Cart'),(28,'Skateboard'),(29,'Segway'),(30,'ATV');
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle_collision`
--

DROP TABLE IF EXISTS `vehicle_collision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle_collision` (
  `vehicle_id` int NOT NULL,
  `collision_id` int NOT NULL,
  PRIMARY KEY (`vehicle_id`,`collision_id`),
  KEY `fk_vehicle_has_collision_collision1_idx` (`collision_id`),
  KEY `fk_vehicle_has_collision_vehicle1_idx` (`vehicle_id`),
  CONSTRAINT `fk_vehicle_has_collision_collision1` FOREIGN KEY (`collision_id`) REFERENCES `collision` (`collision_id`),
  CONSTRAINT `fk_vehicle_has_collision_vehicle1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`vehicle_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle_collision`
--

LOCK TABLES `vehicle_collision` WRITE;
/*!40000 ALTER TABLE `vehicle_collision` DISABLE KEYS */;
INSERT INTO `vehicle_collision` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25),(26,26),(27,27),(28,28),(29,29),(30,30);
/*!40000 ALTER TABLE `vehicle_collision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `collisions_manhattan_2024`
--

/*!50001 DROP VIEW IF EXISTS `collisions_manhattan_2024`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `collisions_manhattan_2024` AS select `c`.`collision_id` AS `collision_id`,`c`.`crash_date` AS `crash_date`,`c`.`crash_time` AS `crash_time`,`c`.`location_id` AS `location_id`,`l`.`borough` AS `borough`,`c`.`on_street_name` AS `on_street_name`,`c`.`cross_street_name` AS `cross_street_name`,`c`.`off_street_name` AS `off_street_name`,`c`.`number_of_persons_injured` AS `number_of_persons_injured`,`c`.`number_of_persons_killed` AS `number_of_persons_killed` from (`collision` `c` join `location` `l` on((`c`.`location_id` = `l`.`location_id`))) where ((`l`.`borough` = 'Manhattan') and (year(`c`.`crash_date`) = 2024)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-14 21:48:56
