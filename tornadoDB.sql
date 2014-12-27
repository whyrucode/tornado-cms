-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: tornadoDB
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authority_user_menu`
--

DROP TABLE IF EXISTS `authority_user_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authority_user_menu` (
  `id` varchar(50) NOT NULL,
  `uid` varchar(50) DEFAULT NULL,
  `menu_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authority_user_menu`
--

LOCK TABLES `authority_user_menu` WRITE;
/*!40000 ALTER TABLE `authority_user_menu` DISABLE KEYS */;
INSERT INTO `authority_user_menu` VALUES ('1','1','1'),('2','1','13');
/*!40000 ALTER TABLE `authority_user_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biz_ariticle`
--

DROP TABLE IF EXISTS `biz_ariticle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biz_ariticle` (
  `id` varchar(36) NOT NULL,
  `article_catlog1` varchar(5) NOT NULL,
  `article_catlog2` varchar(5) NOT NULL,
  `auther` varchar(50) NOT NULL,
  `title` varchar(255) NOT NULL,
  `text` varchar(255) NOT NULL,
  `info` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biz_ariticle`
--

LOCK TABLES `biz_ariticle` WRITE;
/*!40000 ALTER TABLE `biz_ariticle` DISABLE KEYS */;
INSERT INTO `biz_ariticle` VALUES ('e562fc70-8ce6-11e4-867f-00163e003074','1','2','4','3','5','6',NULL),('safdsafasfas2','0','2','wangnima@gmail.com','chrismas','happy','http://www.baidu.com',NULL),('SDFAFASFS-FDA','0','1','xiaomao@qq.com','tucao','wocaowocaowocao','/tmp/tornado/user_pic/',NULL);
/*!40000 ALTER TABLE `biz_ariticle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `business_menu`
--

DROP TABLE IF EXISTS `business_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_menu` (
  `id` varchar(36) NOT NULL,
  `p_menu_id` varchar(5) NOT NULL,
  `menu_id` varchar(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_menu`
--

LOCK TABLES `business_menu` WRITE;
/*!40000 ALTER TABLE `business_menu` DISABLE KEYS */;
INSERT INTO `business_menu` VALUES ('1','0','1','',NULL),('2','0','2','','http://www.baidu.com');
/*!40000 ALTER TABLE `business_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sys_user`
--

DROP TABLE IF EXISTS `sys_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sys_user` (
  `user_id` smallint(8) NOT NULL AUTO_INCREMENT,
  `name` char(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sys_user`
--

LOCK TABLES `sys_user` WRITE;
/*!40000 ALTER TABLE `sys_user` DISABLE KEYS */;
INSERT INTO `sys_user` VALUES (1,'zhouhao','db112358'),(2,'zhouhao','db112358'),(3,'zhouhao','db112358'),(4,'zhouhao','db112358'),(5,'zhouhao','db112358'),(6,'zhouhao','db112358'),(7,'xiaomao','123123'),(8,'xiaomao','123123'),(9,'xiaomao','123123'),(10,'xiaomao','123123'),(11,'xiaomao','123123');
/*!40000 ALTER TABLE `sys_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_user`
--

DROP TABLE IF EXISTS `test_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_user` (
  `user_id` char(36) NOT NULL DEFAULT '',
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` char(1) NOT NULL,
  `pic_dir` varchar(100) DEFAULT NULL,
  `register_time` datetime NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_user`
--

LOCK TABLES `test_user` WRITE;
/*!40000 ALTER TABLE `test_user` DISABLE KEYS */;
INSERT INTO `test_user` VALUES ('41f70125-891c-11e4-a0f8-000c2981eba8','xiaolis','123456','a',NULL,'0000-00-00 00:00:00');
/*!40000 ALTER TABLE `test_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-26 19:04:07
