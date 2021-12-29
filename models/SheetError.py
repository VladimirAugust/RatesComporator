from models.Sheet import Sheet

class SheetError:
    COLUMN_DEF_ERROR = "Column definition error"
    BAD_FILE_ERROR = "Bad type or corrupted file"
    CELL_VALUE_ERROR = "Cell value error"

    def __init__(self, sheet: Sheet, problem: str):
        self.sheet = sheet
        self.problem = problem

    def __str__(self):
        return f"{self.sheet.filename}: {self.problem}"