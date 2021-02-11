My solution involves the following file structure. I give an explanation
for my code design in the file task_5_data_wrangling.py.

	- task_5_data_wrangling.py: the file that cleans and merges the csv tables, outputting
		merged table to data_wrangle_merged.csv

	- data_wrangle_merged.csv: merged dataset, ready for upload.

	- format_csv/

		- csv_file_formatter.py: base class for state-level csv file formatting.

		- regions/

			- texas/

				- texas_csv_file_formatter.py: csv_file_formatter implemented for
					Texas csv files.
