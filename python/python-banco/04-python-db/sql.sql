CREATE SCHEMA PYTHON_UDEMY;

USE PYTHON_UDEMY;

DROP TABLE ALUNOS;

CREATE TABLE ALUNOS(
ID INT PRIMARY KEY AUTO_INCREMENT,
NOME_COMPLETO VARCHAR(100) NOT NULL,
EMAIL VARCHAR(100) NOT NULL,
STATUS TINYINT
);

INSERT INTO ALUNOS VALUEs (null, 'Salumao Barbosa', 'salubcosta@gmail.com', 1),(null, 'Carla Lee Sa', 'carla.lee@mail.com', 0), (null,'Fernanda Amaral', 'fernanda.amaral@gmail.com', 0);

ALTER TABLE ALUNOS RENAME COLUMN NOME_COMPLETO TO NOME;

SELECT * FROM ALUNOS;