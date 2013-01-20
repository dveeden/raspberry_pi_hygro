-- MySQL dump 10.13  Distrib 5.5.28, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: humidity
-- ------------------------------------------------------
-- Server version	5.5.28-1

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
-- Table structure for table `sensor_readings`
--

DROP TABLE IF EXISTS `sensor_readings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor_readings` (
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `temperature` decimal(3,1) NOT NULL,
  `humidity` decimal(3,1) NOT NULL,
  PRIMARY KEY (`time`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `v_humidity_per_day`
--

DROP TABLE IF EXISTS `v_humidity_per_day`;
/*!50001 DROP VIEW IF EXISTS `v_humidity_per_day`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_humidity_per_day` (
  `h_avg` tinyint NOT NULL,
  `h_min` tinyint NOT NULL,
  `h_max` tinyint NOT NULL,
  `h_stddev` tinyint NOT NULL,
  `date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_min_max_avg`
--

DROP TABLE IF EXISTS `v_min_max_avg`;
/*!50001 DROP VIEW IF EXISTS `v_min_max_avg`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_min_max_avg` (
  `h_min` tinyint NOT NULL,
  `h_max` tinyint NOT NULL,
  `h_avg` tinyint NOT NULL,
  `h_latest` tinyint NOT NULL,
  `t_min` tinyint NOT NULL,
  `t_max` tinyint NOT NULL,
  `t_avg` tinyint NOT NULL,
  `t_latest` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_per_hour`
--

DROP TABLE IF EXISTS `v_per_hour`;
/*!50001 DROP VIEW IF EXISTS `v_per_hour`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_per_hour` (
  `date` tinyint NOT NULL,
  `hour` tinyint NOT NULL,
  `t_avg` tinyint NOT NULL,
  `t_max` tinyint NOT NULL,
  `t_min` tinyint NOT NULL,
  `h_avg` tinyint NOT NULL,
  `h_max` tinyint NOT NULL,
  `h_min` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_humidity_per_day`
--

/*!50001 DROP TABLE IF EXISTS `v_humidity_per_day`*/;
/*!50001 DROP VIEW IF EXISTS `v_humidity_per_day`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY INVOKER */
/*!50001 VIEW `v_humidity_per_day` AS select avg(`sensor_readings`.`humidity`) AS `h_avg`,min(`sensor_readings`.`humidity`) AS `h_min`,max(`sensor_readings`.`humidity`) AS `h_max`,std(`sensor_readings`.`humidity`) AS `h_stddev`,cast(`sensor_readings`.`time` as date) AS `date` from `sensor_readings` group by cast(`sensor_readings`.`time` as date) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_min_max_avg`
--

/*!50001 DROP TABLE IF EXISTS `v_min_max_avg`*/;
/*!50001 DROP VIEW IF EXISTS `v_min_max_avg`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_min_max_avg` AS select min(`sensor_readings`.`humidity`) AS `h_min`,max(`sensor_readings`.`humidity`) AS `h_max`,avg(`sensor_readings`.`humidity`) AS `h_avg`,(select `sensor_readings`.`humidity` from `sensor_readings` order by `sensor_readings`.`time` desc limit 1) AS `h_latest`,min(`sensor_readings`.`temperature`) AS `t_min`,max(`sensor_readings`.`temperature`) AS `t_max`,avg(`sensor_readings`.`temperature`) AS `t_avg`,(select `sensor_readings`.`temperature` from `sensor_readings` order by `sensor_readings`.`time` desc limit 1) AS `t_latest` from `sensor_readings` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_per_hour`
--

/*!50001 DROP TABLE IF EXISTS `v_per_hour`*/;
/*!50001 DROP VIEW IF EXISTS `v_per_hour`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_per_hour` AS select cast(`sensor_readings`.`time` as date) AS `date`,hour(`sensor_readings`.`time`) AS `hour`,avg(`sensor_readings`.`temperature`) AS `t_avg`,max(`sensor_readings`.`temperature`) AS `t_max`,min(`sensor_readings`.`temperature`) AS `t_min`,avg(`sensor_readings`.`humidity`) AS `h_avg`,max(`sensor_readings`.`humidity`) AS `h_max`,min(`sensor_readings`.`humidity`) AS `h_min` from `sensor_readings` group by dayofmonth(`sensor_readings`.`time`),hour(`sensor_readings`.`time`) */;
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

-- Dump completed on 2013-01-20 11:52:44
