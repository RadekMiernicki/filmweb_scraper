CREATE DATABASE IF NOT EXISTS filmweb;
USE filmweb;

 CREATE TABLE IF NOT EXISTS types (
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    type_name varchar(100) NOT NULL
 );

 INSERT INTO types (type_name)
 VALUES ('movie'), ('series');

CREATE TABLE IF NOT EXISTS links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filmweb_id INT UNIQUE,
    title VARCHAR(120) NOT NULL,
    link VARCHAR(255) NOT NULL,
    year SMALLINT NOT NULL,
    type_id SMALLINT DEFAULT 0,
    create_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_on TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES types(id)
 );

 CREATE FULLTEXT INDEX titles ON links(title);

INSERT INTO links (
    filmweb_id, title, link, year, type_id
 )
VALUES (
    250272,
    'Diabeł ubiera się u Prady',
    'https://www.filmweb.pl//film/Diabe%C5%82+ubiera+si%C4%99+u+Prady-2006-250272',
    2006,
    1
),
(
    33200,
    'Kill Bill',
    'https://www.filmweb.pl//film/Kill+Bill-2003-33200',
    2003,
    1
);

250272,https://www.filmweb.pl//film/Diabe%C5%82+ubiera+si%C4%99+u+Prady-2006-250272,2006,Diabeł ubiera się u Prady
33200,https://www.filmweb.pl//film/Kill+Bill-2003-33200,2003,Kill Bill