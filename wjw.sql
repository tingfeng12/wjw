/*
Navicat MySQL Data Transfer

Source Server         : cr19mms
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : wjw

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2020-02-03 20:17:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dbgz
-- ----------------------------
DROP TABLE IF EXISTS `dbgz`;
CREATE TABLE `dbgz` (
  `title` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `datatime` varchar(255) DEFAULT NULL,
  `newQZ` varchar(255) DEFAULT NULL,
  `newZY` varchar(255) DEFAULT NULL,
  `allQZ` varchar(255) DEFAULT NULL,
  `men` varchar(255) DEFAULT NULL,
  `women` varchar(255) DEFAULT NULL,
  `allbv` varchar(255) DEFAULT NULL,
  `allzz` varchar(255) DEFAULT NULL,
  `allpt` varchar(255) DEFAULT NULL,
  `allCY` varchar(255) DEFAULT NULL,
  `imgsrc` varchar(255) DEFAULT NULL,
  `newCY` varchar(255) DEFAULT NULL,
  `nowJC` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
