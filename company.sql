--
-- Database: `covid`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `logoname` varchar(255) NOT NULL,
  `CompanyNames` varchar(255) NOT NULL,
  `Locations` varchar(255) NOT NULL,
  `Tags` varchar(255) NOT NULL,
  `availableJobs` int(255) NOT NULL,
  `CompanySize` int(255) NOT NULL,
  `details` varchar(255) NULL
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);
COMMIT;

