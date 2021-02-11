from format_csv.csv_file_formatter import CsvFileFormatter


class TexasCsvFileFormatter(CsvFileFormatter):
	"""Texas implementation of CSV file formatter."""


	def get_allowed_headers(self):
		headers =  ['unique_id',
					'state_code',
					'date_created',
					'date_canvassed',
					'contact_type_id',
					'contact_type_name',
					'result_short_name',
					'committee_id',
					'input_type_name',
					'county_name']

		return self.clean_headers(headers)