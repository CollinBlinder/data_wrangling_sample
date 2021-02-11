import abc

class CsvFileFormatter():
	"""Base class for working with CSV file data being uploaded to database."""

	def merge_tables(self, table_list):
		"""Merge all tables in list of 2 or more tables."""
		if len(table_list) == 1 or type(table_list) != list:
			raise Exception('table_list must be list of tables with length > 1!')

		merged_table = table_list[0].append(table_list[1:], sort=False)
		merged_table.columns = self.clean_headers(merged_table.columns)
		return merged_table.dropna(how='all')


	def get_table_header(self, header_name):
		"""Returns header if the name exists in the list of allowed headers."""
		allowed_headers = self.get_allowed_headers()
		if header_name in allowed_headers:
			return header_name
		print('Incorrect Value: {}'.format(header_name))
		print('List of allowed values:\n{}'.format(allowed_headers))

	@abc.abstractmethod
	def get_allowed_headers(self):
		"""Returns a list of allowable header values."""


	def clean_headers(self, headers):
		"""Return headers in all lowercase if headers are correctly formatted."""
		self.verify_headers(headers)
		return [header.lower() for header in headers]


	def verify_headers(self, headers):
		"""Check allowable header list for any non-allowed characters."""
		bad_characters = [" ", "?", ",", "!", ".", "&", "$", "%"]

		if len(headers) > len(set(headers)):
			raise Exception("Header list contains duplicates!")

		for header in headers:
			for bad_char in bad_characters:
				if bad_char in header:
					raise Exception("Bad header! Header {} contains {}"
									.format(header, 
											bad_char))

