CREATE DATABASE IF NOT EXISTS threatcheck;

USE threatcheck;

CREATE TABLE virus_hashes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hash VARCHAR(64) NOT NULL UNIQUE,
    virus_name VARCHAR(255) NOT NULL,
    threat_level VARCHAR(50),
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO virus_hashes (hash, virus_name, threat_level, details) VALUES
('dummyhash', 'Example Virus', 'High', 'This is an example virus for testing purposes.');