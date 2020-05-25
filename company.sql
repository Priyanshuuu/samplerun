--
-- Database: 'covid'
--

-- --------------------------------------------------------

--
-- Table structure for table 'company'
--

CREATE TABLE IF NOT EXISTS company (
   id int(255) NOT NULL AUTO_INCREMENT,
   logoname varchar(255) NOT NULL,
   CompanyNames varchar(255) NOT NULL,
   Locations varchar(255) NOT NULL,
   Tags varchar(255) NOT NULL,
   availableJobs int(255) NOT NULL,
   CompanySize int(255) NOT NULL,
   details varchar(255) NULL,
  PRIMARY KEY (id)
);

--
-- Table structure for table 'projects'
--

CREATE TABLE IF NOT EXISTS projects (
  id int(255) NOT NULL AUTO_INCREMENT,
  logoname varchar(255) NOT NULL,
  ProjectNames varchar(255) NOT NULL,
  Locations varchar(255) NOT NULL,
  Tags varchar(255) NOT NULL,
  availableVacancies int(255) NOT NULL,
  ProjectSize int(255) NOT NULL,
  details varchar(255) NULL,
  PRIMARY KEY (id)
);

