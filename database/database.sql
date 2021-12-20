DROP DATABASE IF EXISTS flask_unit_test;

CREATE DATABASE flask_unit_test
    DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE flask_unit_test;

CREATE TABLE data (
    id   INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    text VARCHAR(50),
    PRIMARY KEY(id)
) ENGINE=InnoDB;