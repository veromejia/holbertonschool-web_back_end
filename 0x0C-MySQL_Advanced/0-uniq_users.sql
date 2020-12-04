-- Defines a table for the holberton database
-- Creates a  table users
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY ( id ),
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)
