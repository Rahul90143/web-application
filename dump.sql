/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - news
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`news` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `news`;

/*Table structure for table `auser` */

DROP TABLE IF EXISTS `auser`;

CREATE TABLE `auser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `auser` */

LOCK TABLES `auser` WRITE;

insert  into `auser`(`id`,`username`,`email`,`password`) values (1,'admin','ram@gmail.com','123');

UNLOCK TABLES;

/*Table structure for table `buser` */

DROP TABLE IF EXISTS `buser`;

CREATE TABLE `buser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `ph` varchar(15) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `buser` */

LOCK TABLES `buser` WRITE;

insert  into `buser`(`id`,`username`,`email`,`password`,`ph`,`location`) values (1,'sanjay','pamalasanjaykumar@outlook.com','123','8688957593','sai nagar'),(4,'s','moulalicce225@gmail.com','123','8688957592','sai nagar');

UNLOCK TABLES;

/*Table structure for table `newssend` */

DROP TABLE IF EXISTS `newssend`;

CREATE TABLE `newssend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `newsid` int(11) DEFAULT NULL,
  `t` varchar(255) DEFAULT NULL,
  `n` text,
  `s` varchar(255) DEFAULT NULL,
  `r` varchar(255) DEFAULT NULL,
  `u` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `newssend` */

LOCK TABLES `newssend` WRITE;

insert  into `newssend`(`id`,`newsid`,`t`,`n`,`s`,`r`,`u`) values (15,1,'amdlqd','lwwkndnq wd','s','admin','s');

UNLOCK TABLES;

/*Table structure for table `newst` */

DROP TABLE IF EXISTS `newst`;

CREATE TABLE `newst` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u` varchar(50) NOT NULL,
  `t` varchar(255) NOT NULL,
  `n` text NOT NULL,
  `s` varchar(255) DEFAULT NULL,
  `h` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `newst` */

LOCK TABLES `newst` WRITE;

insert  into `newst`(`id`,`u`,`t`,`n`,`s`,`h`) values (1,'sanjay','amdlqd','lwwkndnq wd','FAKE','848d863a64fadafb0b0d956d5c9df09c1246a179dc9c07fc369c5a16d3ad91f0'),(2,'s','Comment on Quid Pro Quo Wikileaks Email Reveals Clinton Campaign Eyeing Paul Ryans Relative for Supreme Court by lenorelee','New Wikileaks email dumps have revealed massive corruption surrounding Hillary Clinton campaign chair John Podesta  In one email dated February 29 2016 an article sent by Hillary advisor Sara Solow to Podesta and Hillarys foreign policy advisor Jake Sullivan indicates that the Clinton campaign is considering House Speaker Paul Ryans relative for the Supreme Court  Ketanji Brown is the subject of the article She is related to Paul Ryan by marriage and is a judge on the US District Court for the District of Columbia The email reads She was confirmed by without any Republican opposition in the Senate not once but twice She was confirmed to her current position in 2013 by unanimous consent  that is without any stated opposition She was also previously confirmed unanimously to a seat on the US Sentencing Commission where she became vice chair Her family is impressive She is married to a surgeon and has two young daughters Her father is a retired lawyer and her mother a retired school principal Her brother was a police officer in the unit that was the basis for the television show  The Wire  and is now a law student and she is related by marriage to Congressman and Speaker of the House Paul Ryan Earlier this month he even said he would not campaign for nor support his partys nominee Donald Trump  In fact some supporters of Trump have theorized that Ryan was somehow behind or involved in the leak of the tape in which Trump made sexually crude comments about women If you claim this is merely circumstantial then I think there is no hope for you understanding just how corrupt DC has gotten and this is the very Paul Ryan I warned you about in 2012 which everyone said was so conservative Sadly many didnt listen and voted for liberal Mitt Romney and him Perhaps Paul Ryans records and emails should be leaked and maybe we just might see that hes willing to engage Hillary in a paytoplay scheme  Courtesy of Freedom Outpost Tim Brown is an author and Editor at FreedomOutpostcom  SonsOfLibertyMediacom  GunsInTheNewscom and TheWashingtonStandardcom  He is husband to his more precious than rubies wife father of 10 mighty arrows jack of all trades Christian and lover of liberty He resides in the US occupied Great State of South Carolina Tim is also an affiliate for the Joshua Mark 5 ARAK hybrid semiautomatic rifle  Follow Tim on Twitter  Dont forget to follow the DC Clothesline on Facebook and Twitter PLEASE help spread the word by sharing our articles on your favorite social networks Share this','FAKE','fa08fc933d64c761e30d6f7c6650b12d2de678dbf2f2d521cf12fa4da2fad87f');

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
