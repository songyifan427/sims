/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost:3306
 Source Schema         : sims

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 24/05/2019 21:03:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class_info
-- ----------------------------
DROP TABLE IF EXISTS `class_info`;
CREATE TABLE `class_info`  (
  `cls_id` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '班级号',
  `major_id` int(9) NOT NULL COMMENT '专业id',
  `state` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`cls_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of class_info
-- ----------------------------
INSERT INTO `class_info` VALUES ('计算1501', 1, 1, '2019-05-13 18:05:35');

-- ----------------------------
-- Table structure for estimate
-- ----------------------------
DROP TABLE IF EXISTS `estimate`;
CREATE TABLE `estimate`  (
  `id` int(9) NOT NULL AUTO_INCREMENT COMMENT '唯一id',
  `tea_id` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '对象工号',
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '内容',
  `state` tinyint(1) NOT NULL DEFAULT 0 COMMENT '状态',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of estimate
-- ----------------------------
INSERT INTO `estimate` VALUES (1, '0001', '非常好:100%;好:0%;中等:0%;差:0%;非常差:0%', 1, '2019-05-15 18:07:51');

-- ----------------------------
-- Table structure for majortable
-- ----------------------------
DROP TABLE IF EXISTS `majortable`;
CREATE TABLE `majortable`  (
  `major_id` int(9) NOT NULL AUTO_INCREMENT COMMENT '唯一id',
  `major_name` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '专业名',
  `state` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`major_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of majortable
-- ----------------------------
INSERT INTO `majortable` VALUES (1, '信息与计算科学', 1, '2019-05-13 19:02:55');
INSERT INTO `majortable` VALUES (2, '应用化学', 1, '2019-05-24 21:02:57');
INSERT INTO `majortable` VALUES (3, '物理学', 1, '2019-05-24 09:08:31');
INSERT INTO `majortable` VALUES (4, '英语', 1, '2019-05-24 09:08:32');
INSERT INTO `majortable` VALUES (5, '汉语言文学', 1, '2019-05-24 09:36:19');
INSERT INTO `majortable` VALUES (6, '软件工程', 0, '2019-05-24 09:09:07');

-- ----------------------------
-- Table structure for notice
-- ----------------------------
DROP TABLE IF EXISTS `notice`;
CREATE TABLE `notice`  (
  `id` int(9) NOT NULL AUTO_INCREMENT COMMENT '唯一id',
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '内容',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `create_userid` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '创建人',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of notice
-- ----------------------------
INSERT INTO `notice` VALUES (1, '今天是五月十三日', '2019-05-13 17:31:59', 'admin');
INSERT INTO `notice` VALUES (2, '今天是五月十四日', '2019-05-14 10:14:58', 'admin');
INSERT INTO `notice` VALUES (3, '今天是五月二十二日', '2019-05-22 14:54:13', 'admin');
INSERT INTO `notice` VALUES (4, '今天是五月二十四日', '2019-05-24 19:04:33', 'admin');

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score`  (
  `id` int(9) NOT NULL AUTO_INCREMENT COMMENT '唯一id',
  `stu_id` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '对象学号',
  `project` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '课程名',
  `score` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '成绩',
  `state` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for student_info
-- ----------------------------
DROP TABLE IF EXISTS `student_info`;
CREATE TABLE `student_info`  (
  `stu_id` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学号',
  `name` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '姓名',
  `sex` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
  `cls_id` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '班级',
  `major_id` int(9) NOT NULL COMMENT '专业id',
  `state` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `is_est` tinyint(1) NULL DEFAULT 0 COMMENT '是否已教学评估',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`stu_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of student_info
-- ----------------------------
INSERT INTO `student_info` VALUES ('15010101', '张三', '男', '计算1501', 1, 1, 0, '2019-05-13 17:59:41');

-- ----------------------------
-- Table structure for teacher_info
-- ----------------------------
DROP TABLE IF EXISTS `teacher_info`;
CREATE TABLE `teacher_info`  (
  `tea_id` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '工号',
  `name` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '姓名',
  `sex` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别',
  `subject` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '课程',
  `cls_ids` varchar(510) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '任课班级',
  `state` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`tea_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of teacher_info
-- ----------------------------
INSERT INTO `teacher_info` VALUES ('0001', '杨过', '男', '运筹学', '计算1501,', 1, '2019-05-14 10:48:03');

-- ----------------------------
-- Table structure for timetable
-- ----------------------------
DROP TABLE IF EXISTS `timetable`;
CREATE TABLE `timetable`  (
  `id` int(9) NOT NULL AUTO_INCREMENT COMMENT '唯一id',
  `obj_id` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '对象工号/班级',
  `content` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '内容',
  `state` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info`  (
  `userid` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '账号(学号/工号)',
  `password` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `name` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `role` char(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '角色',
  `state` tinyint(1) NOT NULL DEFAULT 1 COMMENT '状态',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '创建时间'
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES ('admin', 'e10adc3949ba59abbe56e057f20f883e', '管理员', 'admin', 1, '2019-05-23 16:18:19');
INSERT INTO `user_info` VALUES ('0001', 'e10adc3949ba59abbe56e057f20f883e', '杨过', 'teacher', 1, '2019-05-23 16:18:29');
INSERT INTO `user_info` VALUES ('15010101', 'e10adc3949ba59abbe56e057f20f883e', '张三', 'student', 1, '2019-05-23 18:37:10');

SET FOREIGN_KEY_CHECKS = 1;
