CREATE TABLE `user` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `title` varchar(255),
  `contact_info` int
);

CREATE TABLE `contact_info` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `github` varchar(255),
  `linkedin` varchar(255),
  `website` varchar(255),
  `skype` varchar(255),
  `email` varchar(255),
  `phone` varchar(255),
  `address` varchar(255)
);

CREATE TABLE `about_me` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `text` LONGTEXT
);

CREATE TABLE `experience` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `title` varchar(255),
  `company` varchar(255),
  `tasks` LONGTEXT,
  `startdate` varchar(255),
  `enddate` varchar(255)
);

CREATE TABLE `education` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `title` varchar(255),
  `school` varchar(255),
  `startdate` varchar(255),
  `enddate` varchar(255)
);

CREATE TABLE `skills` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `skill` varchar(255),
  `level` varchar(255)
);

ALTER TABLE `user` ADD FOREIGN KEY (`contact_info`) REFERENCES `contact_info` (`id`);

ALTER TABLE `about_me` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `experience` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `education` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `skills` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
