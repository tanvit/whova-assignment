import sys
import xlrd
from db_table import db_table

book = xlrd.open_workbook(sys.argv[1])
sh = book.sheet_by_index(0)

agenda = db_table("agenda", { "date": "text NOT NULL", "time_start":"text NOT NULL", "time_end":"text NOT NULL", "session_or":"text NOT NULL", "session_title":"text NOT NULL", "location":"text", "description":"text", "speakers":"text" })
id = ""

for row in range(15,sh.nrows):
    if(sh.cell_value(rowx=row, colx=3).strip() == "Session"):
        id = agenda.insert({"date": sh.cell_value(rowx=row, colx=0), "time_start": sh.cell_value(rowx=row, colx=1), "time_end": sh.cell_value(rowx=row, colx=2), "session_or": sh.cell_value(rowx=row, colx=3), "session_title": sh.cell_value(rowx=row, colx=4), "location": sh.cell_value(rowx=row, colx=5), "description": sh.cell_value(rowx=row, colx=6), "speakers": sh.cell_value(rowx=row, colx=7)})
    
    else:
        if id ==  "":
            raise Exception("Some Subs have no parent Session")
        agenda.insert({"date": sh.cell_value(rowx=row, colx=0), "time_start": sh.cell_value(rowx=row, colx=1), "time_end": sh.cell_value(rowx=row, colx=2), "session_or": id, "session_title": sh.cell_value(rowx=row, colx=4), "location": sh.cell_value(rowx=row, colx=5), "description": sh.cell_value(rowx=row, colx=6), "speakers": sh.cell_value(rowx=row, colx=7)})

agenda.close()

