"""
Assignment
Complete the get_csv_status function. It should use a match case statement to select the correct response depending on the status of the export operation. Create functions to handle each operation as follows:

1. PENDING: return a tuple with the string "Pending..." and the data converted from a list of lists of anything, to a list of lists of strings.
    1. Try to use nested map functions to convert the data items into strings.
    2. Remember to convert from a map object back into a list.
2. PROCESSING: return a tuple with the string "Processing..." and the data converted from a list of lists of strings into one string in CSV format.
    1. For each list of strings, combine the strings with join with commas in between to form a row.
    2. For each row string, combine the strings with join with newlines "\n" in between to form a table.
3. SUCCESS: return a tuple with the string "Success!" and simply return the data as is.
4. FAILURE: return a tuple with the string "Unknown error, retrying..." and the data after it has been prepared and processed into a CSV string, by combining the steps for Pending and Processing.
5. Any Other Status: raise an Exception with the string "unknown export status".
"""

from enum import Enum

CSVExportStatus = Enum(
    "CSVExportStatus", ["PENDING", "PROCESSING", "SUCCESS", "FAILURE"]
)


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return ("Pending...", convert_to_string(data))
        case CSVExportStatus.PROCESSING:
            return ("Processing...", convert_to_string_and_CSV(data))
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            return ("Unknown error, retrying...", convert_to_string_and_CSV(convert_to_string(data)))
        case _:
            raise Exception("unknown export status")

def convert_to_string(lists_to_convert):
    return [list(map(str, row)) for row in lists_to_convert]
    
def convert_to_string_and_CSV(lists_to_convert):
    rows = [",".join(map(str, row)) for row in lists_to_convert]
    return "\n".join(rows)
