CREATE DATABASE IF NOT EXISTS myDB;
USE myDB;

DROP TABLE IF EXISTS test;


CREATE TABLE IF NOT EXISTS test (
  id serial NOT NULL PRIMARY KEY,
  utime varchar(100),
  fixmode int(200),
  satellites varchar(200),
  latitude  varchar(100),
  longitude varchar(100),
  altitude varchar(100) ,
  track varchar(100),
  speed varchar(100),
  modified timestamp default CURRENT_TIMESTAMP NOT NULL,
  INDEX `modified_index` (`modified`)
);
USE myDB;
INSERT INTO test (utime, fixmode, satellites,latitude,longitude,altitude,track,speed) VALUES (1.36518E+15,3,0,0.738168312,-1.460986747,269,17.8,0);


