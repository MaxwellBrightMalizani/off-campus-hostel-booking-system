-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: offcampus_db
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `accounts_customuser`
--

DROP TABLE IF EXISTS `accounts_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  `student_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser`
--

LOCK TABLES `accounts_customuser` WRITE;
/*!40000 ALTER TABLE `accounts_customuser` DISABLE KEYS */;
INSERT INTO `accounts_customuser` VALUES (1,'pbkdf2_sha256$600000$ITVJ4FhIoZdh4GI1RR3AQ4$Bd7ady2t0NeefH3t1l9Y3EdNH6YLAC+0Rwj/+EIt844=','2026-06-28 11:40:23.679690',0,'max','max',0,1,'2026-06-27 14:00:22.769202','max@gmail.com','student',NULL),(2,'pbkdf2_sha256$600000$o9yioXVIgbWcI0y41Alo3W$zhFfFiGTsyGbJVnaY4qvVWUKB4ni9Bywnl8bj9aVZoM=','2026-06-28 10:06:05.145006',1,'','',1,1,'2026-06-28 10:05:21.869134','super@gmail.com','admin',NULL),(3,'pbkdf2_sha256$600000$CtGABNZWcLQtOsv4kCgFay$tYJavIjdMOcRBToVftZUYzL5+jSTRT8qnis9SRZDWY0=','2026-06-28 19:22:48.444676',0,'Lauritta','Blake',0,1,'2026-06-28 10:08:39.560041','laurittablake@gmail.com','owner',NULL),(4,'pbkdf2_sha256$600000$iZIl4qvAejxI3NuK7pN5oS$kkT56ZiUzXsnbKVxhhtQ/vQUarG7XY1aDed6PQlT+tM=',NULL,0,'justice','mware',0,1,'2026-06-28 10:09:35.827944','justicemware@gmail.com','owner',NULL),(5,'pbkdf2_sha256$600000$XqQHzG9VsCZshBD3WaWYOf$Q35lh/f9eLVDr3klTeR7n4CApRF5e4ZNOD+7y7dm4Sg=','2026-06-28 19:25:20.173661',0,'Maxwell','Malizani',0,1,'2026-06-28 10:11:08.978807','maxwellbrightmalizani@gmail.com','owner',NULL);
/*!40000 ALTER TABLE `accounts_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_groups`
--

DROP TABLE IF EXISTS `accounts_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_groups`
--

LOCK TABLES `accounts_customuser_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_user_permissions`
--

LOCK TABLES `accounts_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add listing',7,'add_listing'),(26,'Can change listing',7,'change_listing'),(27,'Can delete listing',7,'delete_listing'),(28,'Can view listing',7,'view_listing'),(29,'Can add booking',8,'add_booking'),(30,'Can change booking',8,'change_booking'),(31,'Can delete booking',8,'delete_booking'),(32,'Can view booking',8,'view_booking');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-06-28 10:08:41.212581','3','laurittablake@gmail.com',1,'[{\"added\": {}}]',6,2),(2,'2026-06-28 10:09:38.455242','4','justicemware@gmail.com',1,'[{\"added\": {}}]',6,2),(3,'2026-06-28 10:11:10.915445','5','maxwellbrightmalizani@gmail.com',1,'[{\"added\": {}}]',6,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'accounts','customuser'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(8,'listings','booking'),(7,'listings','listing'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-06-27 13:42:26.700115'),(2,'contenttypes','0002_remove_content_type_name','2026-06-27 13:42:35.288043'),(3,'auth','0001_initial','2026-06-27 13:43:03.667195'),(4,'auth','0002_alter_permission_name_max_length','2026-06-27 13:43:06.999028'),(5,'auth','0003_alter_user_email_max_length','2026-06-27 13:43:07.159960'),(6,'auth','0004_alter_user_username_opts','2026-06-27 13:43:07.286874'),(7,'auth','0005_alter_user_last_login_null','2026-06-27 13:43:07.438079'),(8,'auth','0006_require_contenttypes_0002','2026-06-27 13:43:10.614696'),(9,'auth','0007_alter_validators_add_error_messages','2026-06-27 13:43:11.115291'),(10,'auth','0008_alter_user_username_max_length','2026-06-27 13:43:11.351206'),(11,'auth','0009_alter_user_last_name_max_length','2026-06-27 13:43:11.644115'),(12,'auth','0010_alter_group_name_max_length','2026-06-27 13:43:12.929237'),(13,'auth','0011_update_proxy_permissions','2026-06-27 13:43:13.560654'),(14,'auth','0012_alter_user_first_name_max_length','2026-06-27 13:43:13.933571'),(15,'accounts','0001_initial','2026-06-27 13:43:45.117434'),(16,'admin','0001_initial','2026-06-27 13:43:53.714398'),(17,'admin','0002_logentry_remove_auto_add','2026-06-27 13:43:54.008782'),(18,'admin','0003_logentry_add_action_flag_choices','2026-06-27 13:43:55.845106'),(19,'listings','0001_initial','2026-06-27 13:44:02.086202'),(20,'admin','0001_initial','2026-06-27 13:44:04.730037'),(21,'admin','0002_logentry_remove_auto_add','2026-06-27 13:44:05.176134'),(22,'admin','0003_logentry_add_action_flag_choices','2026-06-27 13:44:05.595822'),(23,'listings','0001_initial','2026-06-27 13:44:05.950956'),(24,'accounts','0001_initial','2026-06-27 13:44:12.190548'),(25,'listings','0002_booking','2026-06-27 13:44:15.669397'),(26,'listings','0003_listing_owner','2026-06-27 13:44:19.963676'),(27,'sessions','0001_initial','2026-06-27 13:44:25.213481');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('e66em8r0x8pragzk1ziok3o1ecpi1ncz','.eJxVjEEKwyAQAP_iuciiRk2PvfcN4rprTVsUYnIK_XsRcmivM8McIsR9K2HvvIaFxFVM4vLLMKYX1yHoGeujydTqti4oRyJP2-W9Eb9vZ_s3KLGXsQXErCAB2DQjMCl26KPLdk7AUZtJkXEqKaMxo0HwZD1lm9lpJuPF5wv48TiP:1wdv85:E3hRjDZbZkUpidhKEH3v0B8KWUx0Jd46FtiiAEWegPM','2026-07-12 19:25:21.270390'),('yyni1pmux5vub4ywwmpyp2y55q6pr7gq','.eJxVjMEOwiAQRP-FsyEsuAIevfcbCLCLVA1NSnsy_rtt0oMeZ96beYsQ16WGtfMcRhJXAeL026WYn9x2QI_Y7pPMU1vmMcldkQftcpiIX7fD_TuosddtbTRh8gikUjIJMisyPqM-GwCb1QW2FMkwayTrIaK12qjiQBd0hZ34fAHVsjdj:1wdVpT:rIZUPsO7IzZmS4g3RD1MHn7pxLvxevmXQbpaG9U-jFA','2026-07-11 16:24:27.375469');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listings_booking`
--

DROP TABLE IF EXISTS `listings_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listings_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `listing_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `listings_booking_listing_id_49e4e776_fk_listings_listing_id` (`listing_id`),
  KEY `listings_booking_user_id_9c468db0_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `listings_booking_listing_id_49e4e776_fk_listings_listing_id` FOREIGN KEY (`listing_id`) REFERENCES `listings_listing` (`id`),
  CONSTRAINT `listings_booking_user_id_9c468db0_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listings_booking`
--

LOCK TABLES `listings_booking` WRITE;
/*!40000 ALTER TABLE `listings_booking` DISABLE KEYS */;
INSERT INTO `listings_booking` VALUES (2,'cancelled','2026-06-28 10:55:12.109914','2026-06-28 10:55:21.093018',10,1),(3,'pending','2026-06-28 11:40:29.701649','2026-06-28 11:40:29.701701',9,1);
/*!40000 ALTER TABLE `listings_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listings_listing`
--

DROP TABLE IF EXISTS `listings_listing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listings_listing` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `address` varchar(250) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `owner_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `listings_listing_owner_id_1628c897_fk_accounts_customuser_id` (`owner_id`),
  CONSTRAINT `listings_listing_owner_id_1628c897_fk_accounts_customuser_id` FOREIGN KEY (`owner_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listings_listing`
--

LOCK TABLES `listings_listing` WRITE;
/*!40000 ALTER TABLE `listings_listing` DISABLE KEYS */;
INSERT INTO `listings_listing` VALUES (3,'Blake Hostels','Enjoy a peaceful and comfortable stay in this well-maintained hostel. The hostel features a plasma TV with DStv for your entertainment and reliable water and electricity backup to ensure a hassle-free living experience. Conveniently designed for students, it provides a secure and welcoming environment close to essential amenities.',50000.00,'chigwiri Market, likuni','2026-06-28 10:20:49.829250',3),(4,'Amazing Hostels','Stay in a comfortable and modern hostel equipped with a plasma TV and DStv for your entertainment. The hostel also provides dependable water and electricity backup, ensuring a convenient and uninterrupted living experience.',45000.00,'Mpunga villlage, Chigwiri','2026-06-28 10:21:52.765578',3),(5,'Grace Girls Hostels','Enjoy a comfortable stay in this well-equipped hostel featuring a plasma TV with DStv for entertainment. The girls hostel  which is also has reliable water and electricity backup systems to ensure uninterrupted services and a convenient living experience.',65000.00,'Chigwiri Market','2026-06-28 10:26:33.015143',3),(6,'Destination Hostels','Enjoy a comfortable and peaceful stay in our fully fenced hostel. The hostel offers free Wi-Fi, reliable water and electricity backup, and a quiet environment that is perfect for studying and relaxation.',60000.00,'Likuni','2026-06-28 10:27:57.507109',3),(7,'KirkRange Hostels','Experience comfortable and secure living in a quiet and peaceful environment. This hostel offers reliable water and electricity backup systems to ensure uninterrupted services at all times. Residents also enjoy free high-speed Wi-Fi, making it ideal for studying and staying connected. The property is fully fenced, providing enhanced security and privacy for all occupants. It is the perfect place for students seeking a safe, convenient, and conducive living environment.',70000.00,'Ngwizi','2026-06-28 10:35:14.166887',5),(8,'Dzidyana Boys & Girls Hostels','a hostel with favorable conditions for students , with water and electricity backups. free WiFi is also provided',45000.00,'Ngwizi Market','2026-06-28 10:38:37.040683',5),(9,'Kest Hostels','A peaceful stay in our fully fenced hostel. The hostel offers free Wi-Fi, reliable water and electricity backup, and a quiet environment that is perfect for studying and relaxation. and with football and basketball grounds',90000.00,'Chitipi','2026-06-28 10:42:24.983801',5),(10,'Ayankha Hostels','A modern hostel  with a plasma TV and DStv for entertainment. The hostel also provides dependable water and electricity backup',55000.00,'Likuni','2026-06-28 10:44:50.292743',5);
/*!40000 ALTER TABLE `listings_listing` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-28 22:38:08
