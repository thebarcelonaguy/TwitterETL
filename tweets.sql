CREATE TABLE `twitterdb`.`tweets` (
  `id` VARCHAR(25) NOT NULL,
  `username` VARCHAR(255) NULL,
  `created_at` VARCHAR(45) NULL,
  `tweet` TEXT NULL,
  `retweet_count` INT(11) NULL,
  `location` VARCHAR(100) NULL,
  `place` VARCHAR(100) NULL,
  PRIMARY KEY (`id`));

