USE flaskdb; 

-- Create table for Customer
CREATE TABLE IF NOT EXISTS `Customer` (
    `ID` INT AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(10),
    `name` VARCHAR(255) NOT NULL,
    `gender` CHAR(1) NOT NULL,
    `phone_number` VARCHAR(15) NOT NULL,
    `image` TEXT,
    `email` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create table for Address
CREATE TABLE IF NOT EXISTS `Address` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `customer_id` INT NOT NULL,
    `address` TEXT NOT NULL,
    `district` VARCHAR(255) NOT NULL,
    `city` VARCHAR(255) NOT NULL,
    `province` VARCHAR(255) NOT NULL,
    `postal_code` VARCHAR(10) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`customer_id`) REFERENCES `Customer`(`ID`) ON DELETE CASCADE
);
