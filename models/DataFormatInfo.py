from openpyxl.utils import column_index_from_string


class DataFormatInfo:
    def __init__(self, startLine, destColumn, codeColumn, rateColumn, endLine=-1):
        self.startLine = startLine
        self.destColumn = column_index_from_string(destColumn)
        self.codeColumn = column_index_from_string(codeColumn)
        self.rateColumn = column_index_from_string(rateColumn)
        self.endLine = endLine
