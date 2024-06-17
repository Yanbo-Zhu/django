/*
Navicat MySQL Data Transfer

Source Server         : zhiliao
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : orm_aggregate_demo2

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001
*/

SET FOREIGN_KEY_CHECKS=0;


-- ----------------------------
-- Records of author
-- ----------------------------
INSERT INTO `front_author` VALUES (1, '曹雪芹', '35', 'cxq@qq.com');
INSERT INTO `front_author` VALUES (2, '吴承恩', '28', 'wce@qq.com');
INSERT INTO `front_author` VALUES (3, '罗贯中', '36', 'lgz@qq.com');
INSERT INTO `front_author` VALUES (4, '施耐庵', '46', 'sna@qq.com');


-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `front_book` VALUES ('1', '三国演义', '987', '98', '4.8', '3', '1');
INSERT INTO `front_book` VALUES ('2', '水浒传', '967', '97', '4.83', '4', '1');
INSERT INTO `front_book` VALUES ('3', '西游记', '1004', '95', '4.85', '2', '2');
INSERT INTO `front_book` VALUES ('4', '红楼梦', '1007', '99', '4.9', '1', '2');


-- ----------------------------
-- Records of book_order
-- ----------------------------
INSERT INTO `front_book_order` VALUES ('1', '95', '1');
INSERT INTO `front_book_order` VALUES ('2', '85', '1');
INSERT INTO `front_book_order` VALUES ('3', '88', '1');
INSERT INTO `front_book_order` VALUES ('4', '94', '2');
INSERT INTO `front_book_order` VALUES ('5', '93', '2');


-- ----------------------------
-- Records of publisher
-- ----------------------------
INSERT INTO `front_publisher` VALUES ('1', '中国邮电出版社');
INSERT INTO `front_publisher` VALUES ('2', '清华大学出版社');
