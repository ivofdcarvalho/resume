CREATE TABLE `user` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `title` varchar(255),
  `experience` int
);

CREATE TABLE `contact_info` (
  `user_id` int,
  `github` varchar(255),
  `linkedin` varchar(255),
  `website` varchar(255),
  `skype` varchar(255),
  `email` varchar(255),
  `phone` varchar(255),
  `address` varchar(255)
);

CREATE TABLE `about_me` (
  `user_id` int,
  `text` varchar(255)
);

CREATE TABLE `experience` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `title` varchar(255),
  `company` varchar(255),
  `tasks` varchar(255),
  `startdate` datetime,
  `enddate` datetime
);

CREATE TABLE `education` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `title` varchar(255),
  `school` varchar(255),
  `startdate` datetime,
  `enddate` datetime
);

CREATE TABLE `skills` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `skill` varchar(255),
  `level` varchar(255)
);

ALTER TABLE `contact_info` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `about_me` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `experience` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `education` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `skills` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
