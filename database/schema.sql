-- Create database
CREATE DATABASE IF NOT EXISTS incident_management;
USE incident_management;

-- Create incidents table
CREATE TABLE incidents (
    incident_id INT AUTO_INCREMENT PRIMARY KEY,
    incident_date DATE NOT NULL,
    incident_type VARCHAR(50) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    root_cause VARCHAR(50) NOT NULL,
    system_name VARCHAR(100) NOT NULL,
    resolution_time INT NOT NULL, -- in minutes
    status VARCHAR(20) NOT NULL
);

-- Optional: check table
SELECT * FROM incidents;
