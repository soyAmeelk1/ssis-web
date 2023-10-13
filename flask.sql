-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ssis_web
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ssis_web
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ssis_web` DEFAULT CHARACTER SET utf8 ;
USE `ssis_web` ;

-- -----------------------------------------------------
-- Table `ssis_web`.`colleges`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssis_web`.`colleges` (
  `idcolleges` INT NOT NULL,
  `collegename` VARCHAR(45) NULL,
  `collegescode` VARCHAR(45) NULL,
  PRIMARY KEY (`idcolleges`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ssis_web`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssis_web`.`courses` (
  `idcourses` INT NOT NULL,
  `coursename` VARCHAR(45) NULL,
  `coursecode` VARCHAR(45) NULL,
  `colleges_idcolleges` INT NOT NULL,
  PRIMARY KEY (`idcourses`),
  INDEX `fk_courses_colleges_idx` (`colleges_idcolleges` ASC) VISIBLE,
  CONSTRAINT `fk_courses_colleges`
    FOREIGN KEY (`colleges_idcolleges`)
    REFERENCES `ssis_web`.`colleges` (`idcolleges`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ssis_web`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ssis_web`.`students` (
  `idstudents` VARCHAR(255) NOT NULL,
  `firstname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  `courses_idcourses` INT NOT NULL,
  `year` VARCHAR(45) NULL,
  `gender` VARCHAR(45) NULL,
  PRIMARY KEY (`idstudents`),
  INDEX `fk_students_courses1_idx` (`courses_idcourses` ASC) VISIBLE,
  CONSTRAINT `fk_students_courses1`
    FOREIGN KEY (`courses_idcourses`)
    REFERENCES `ssis_web`.`courses` (`idcourses`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
