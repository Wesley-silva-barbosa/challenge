CREATE DATABASE db;
USE db;

CREATE TABLE IF NOT EXISTS insights (
id INT AUTO_INCREMENT PRIMARY KEY,
descricao VARCHAR(255) NOT NULL,
categoria VARCHAR(255) NULL
) ENGINE=INNODB;

