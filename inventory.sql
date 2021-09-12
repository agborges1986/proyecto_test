-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ainel_db_inventory
-- -----------------------------------------------------
-- ERD para sistema de Inventario de Herramientas

-- -----------------------------------------------------
-- Schema ainel_db_inventory
--
-- ERD para sistema de Inventario de Herramientas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ainel_db_inventory` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `ainel_db_inventory` ;

-- -----------------------------------------------------
-- Table `ainel_db_inventory`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ainel_db_inventory`.`users` ;

CREATE TABLE IF NOT EXISTS `ainel_db_inventory`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE);


-- -----------------------------------------------------
-- Table `ainel_db_inventory`.`roles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ainel_db_inventory`.`roles` ;

CREATE TABLE IF NOT EXISTS `ainel_db_inventory`.`roles` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(45) NULL,
  `create_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_roles_user1`
    FOREIGN KEY (`user_email`)
    REFERENCES `ainel_db_inventory`.`users` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ainel_db_inventory`.`employees`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ainel_db_inventory`.`employees` ;

CREATE TABLE IF NOT EXISTS `ainel_db_inventory`.`employees` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `position` VARCHAR(45) NULL,
  `area` VARCHAR(45) NULL,
  `create_at` DATETIME NULL,
  `update_at` DATETIME NULL,
  `active` BIT(1) NULL,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ainel_db_inventory`.`tools`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ainel_db_inventory`.`tools` ;

CREATE TABLE IF NOT EXISTS `ainel_db_inventory`.`tools` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `serie` VARCHAR(30) NULL,
  `model` VARCHAR(45) NULL,
  `provider` VARCHAR(45) NULL,
  `cost` INT NULL,
  `create_at` DATETIME NULL,
  `active` BIT(1) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
COMMENT = '	';


-- -----------------------------------------------------
-- Table `ainel_db_inventory`.`moves_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ainel_db_inventory`.`moves_type` ;

CREATE TABLE IF NOT EXISTS `ainel_db_inventory`.`moves_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NULL,
  `create_at` DATETIME NULL,
  `update_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ainel_db_inventory`.`moves_type_has_tools`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ainel_db_inventory`.`moves_type_has_tools` ;

CREATE TABLE IF NOT EXISTS `ainel_db_inventory`.`moves_type_has_tools` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `move_type_id` INT NOT NULL,
  `tool_id` INT NOT NULL,
  `employee_id` INT UNSIGNED NOT NULL,
  `description` VARCHAR(255) NULL,
  `create_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_moves_type_has_tools_moves_type`
    FOREIGN KEY (`move_type_id`)
    REFERENCES `ainel_db_inventory`.`moves_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_moves_type_has_tools_tools1`
    FOREIGN KEY (`tool_id`)
    REFERENCES `ainel_db_inventory`.`tools` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_moves_type_has_tools_employees1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `ainel_db_inventory`.`employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO tools (id,name,serie,model,provider,cost,create_at,active) VALUES (1,'Herramienta1','123456790','Electrica','Easy',15000,now(),1),(2,'Herramienta2','123456790','Manual','Sodimac',25000,now(),1),(3,'Herramienta3','123456783','Manual','Corpelec',155000,now(),1);
INSERT INTO employees (id,name,last_name,position,area,create_at,update_at,active) VALUES (1,'Empleado1','Apellido1','Maestro Eléctrico','OOEE',now(),now(),1),(2,'Empleado2','Apellido2','Maestro Albañil','OOCC',now(),now(),1),(3,'Empleado3','Apellido3','Ayudante','AP',now(),now(),1);
-- INSERT INTO tools () VALUES ();