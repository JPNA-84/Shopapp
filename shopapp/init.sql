CREATE DATABASE IF NOT EXISTS shopdb;
USE shopdb;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT
);

INSERT INTO products (name, description) VALUES
('Wireless Headphones', 'Over-ear noise-cancelling headphones with 30hr battery life'),
('Mechanical Keyboard', 'Compact TKL keyboard with blue switches and RGB backlight'),
('USB-C Hub', '7-in-1 hub with HDMI, USB 3.0, SD card, and PD charging'),
('Webcam 1080p', 'Full HD webcam with built-in mic and auto light correction'),
('Laptop Stand', 'Adjustable aluminium stand compatible with all laptop sizes');
