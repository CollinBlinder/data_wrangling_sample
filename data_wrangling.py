import pandas as pd
from format_csv.regions.texas.texas_csv_file_formatter import TexasCsvFileFormatter


frame_1 = pd.read_csv("../data/data_wrangle_file1.csv")
frame_2 = pd.read_csv("../data/data_wrangle_file2.csv")

tx_file_formatter = TexasCsvFileFormatter()

frame_1.rename(columns={'unique_id': tx_file_formatter.get_table_header('unique_id'),
                    'State Code': tx_file_formatter.get_table_header('state_code'),
                    'date&created': tx_file_formatter.get_table_header('date_created'),
                    'date%canvassed': tx_file_formatter.get_table_header('date_canvassed'),
                    'contacttypeid!': tx_file_formatter.get_table_header('contact_type_id'),
                    '%contacttypename%': tx_file_formatter.get_table_header('contact_type_name'),
                    'res$ults$hortname': tx_file_formatter.get_table_header('result_short_name'),
                    'committeeID': tx_file_formatter.get_table_header('committee_id'),
                    'COUNTY': tx_file_formatter.get_table_header('county_name')},
            inplace=True)

frame_2.rename(columns={'unique_id': tx_file_formatter.get_table_header('unique_id'),
                    'state%code': tx_file_formatter.get_table_header('state_code'),
                    'DateCreated': tx_file_formatter.get_table_header('date_created'),
                    'date%CANVASSED': tx_file_formatter.get_table_header('date_canvassed'),
                    'contact%TYPE%name': tx_file_formatter.get_table_header('contact_type_name'),
                    'result?short!name': tx_file_formatter.get_table_header('result_short_name'),
                    'inputtypename': tx_file_formatter.get_table_header('input_type_name'),
                    'County': tx_file_formatter.get_table_header('county_name')},
            inplace=True)

merged_frame = tx_file_formatter.merge_tables([frame_1, frame_2])
merged_frame.contact_type_id = merged_frame.contact_type_id.map(lambda x: str(int(x)), 
                                                                na_action='ignore')

merged_frame.to_csv("./data_wrangle_merged.csv", index=False)
