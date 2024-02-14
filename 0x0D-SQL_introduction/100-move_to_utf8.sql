-- 100-move_to_utf8.sql
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` MODIFY `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
