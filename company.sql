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



--
-- Table structure for table 'opportunities' where D_R= Duties & Responsibilities.
--

CREATE TABLE IF NOT EXISTS opportunities (
  op_id int(255) NOT NULL AUTO_INCREMENT,
  id int(255) NOT NULL REFERENCES company(id),
  logoname varchar(255) NOT NULL,
  job_type varchar(255) NOT NULL,
  techstack varchar(255) NOT NULL,
  culture varchar(255) NOT NULL,
  D_R varchar(255) NOT NULL,
  description varchar(255) NULL,
  company_type varchar(255) NULL,
  PRIMARY KEY (op_id)
);

ALTER TABLE opportunities ADD CONSTRAINT cid FOREIGN KEY(id) REFERENCES company(id) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;


