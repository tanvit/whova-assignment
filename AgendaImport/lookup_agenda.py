import sys
from db_table import db_table

agenda = db_table("agenda", { "date": "text NOT NULL", "time_start":"text NOT NULL", "time_end":"text NOT NULL", "session_or":"text NOT NULL", "session_title":"text NOT NULL", "location":"text", "description":"text", "speakers":"text" })

field = str(sys.argv[1])
value = str(sys.argv[2])

if not field in agenda.schema:
    raise("Not a valid field name")
else:
    out_session = agenda.selectPrettyIn(where={field : [value]})
    if len(out_session) > 0:
        out_sub = agenda.selectValues("rowid",{field : value})
        out_session += "\n"+ agenda.selectPrettyIn(where={"session_or" : out_sub})
    print(out_session)
