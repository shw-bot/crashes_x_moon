# Cincinnati Crash Data and Moon Position Analysis

## Overview
This GitHub project aims to analyze Cincinnati, Ohio crash data in relation to moon phases and astrological signs. The project pulls crash data from [data.cincinnati-oh.gov](https://data.cincinnati-oh.gov) and combines it with moon phase and astrological sign data from a CSV file. The analysis visualizes the average crash severity in different Cincinnati neighborhoods based on moon phases and astrological positions.

## Tableau Visualizations
1. [Cincinnati Crash Severity x Moon's Astrological Position](https://public.tableau.com/views/CincinnatiCrashDataxMoonPosition/CincinnatiCrashSeverityxMoonsAstrologicalPosition?:language=en-US&:display_count=n&:origin=viz_share_link): This visualization presents the average crash severity (ranging from 0 to 3, where 0 is fatality and 3 is no injuries) in each Cincinnati neighborhood based on moon phases and astrological positions.

2. [Number of Crashes x Astrological Sign Rulership (Western vs. Vedic)](https://public.tableau.com/views/NumberofCrashesxAstrologicalSignRulerWesternv_Vedic/NumberofCrashesxAstrologicalSignRulershipWesternv_Vedic?:language=en-US&:display_count=n&:origin=viz_share_link): This analysis compares the number of crashes on different days of the week based on the planetary rulers of the moon's astrological sign. The comparison is made between Western and Vedic astrological systems.

## Data Files
- `config.py`: Contains the API key needed to access the crash data from [data.cincinnati-oh.gov](https://data.cincinnati-oh.gov). Users need to sign up for free on the website to obtain this key.
- `api_to_sql_db.py`: Python script to pull crash data from the API and create an SQLite database.
- `managing_tables.py`: Python script to create and clean SQLite tables, and merge the API data with moon phase data from `moon_phases.csv`.
- `crashes_x_moonphase.py`: Python script to clean the joined table and create a CSV file for visualization in Tableau.
- `moon_phases.csv`: CSV file containing moon phase and astrological sign data for the past few months.
- `cin_traffic.db`: SQLite database containing the combined crash data and moon phase information.
- `.gitignore`: Includes the files to be ignored in the repository, such as `config.py`, `cin_traffic.db`, and the CSV file created for Tableau visualization.
- `venv`: Virtual environment file.

## Usage
To replicate the analysis and visualizations, follow these steps:

1. Obtain the API key by signing up for free on [data.cincinnati-oh.gov](https://data.cincinnati-oh.gov), and update the `config.py` file with the key.
2. Run `api_to_sql_db.py` to pull crash data from the API and create the SQLite database.
3. Execute `managing_tables.py` to create and clean the necessary tables and merge the crash data with moon phase data.
4. Run `crashes_x_moonphase.py` to clean the combined data and create a CSV file for visualization in Tableau.
5. Import the CSV file and the `moon_phases.csv` into Tableau for visualization.
6. Explore the Tableau visualizations to analyze the correlation between crash severity and moon phases, as well as the number of crashes based on astrological sign rulership.

Please note that some data files, such as the API key and SQLite database, are excluded from the repository to maintain security and privacy. Users need to generate their own API key and database locally.

## Notes
The project aims to compare Western and Vedic astrological systems and their potential influence on crash rates. The hypothesis involves analyzing the number of crashes when the moon is in signs ruled by Mars, Saturn, or Uranus. The comparison between Western and Vedic systems may provide insights into any significant differences.

## License
[MIT License](LICENSE)
