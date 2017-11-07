"""
Revert history from ipython history file.

Command line:
sqlite3 history.sqlite -line ' select source_raw from history;' > hist_all_sql.txt
"""

import sqlite3

def fetch_all(cursor, name):
    cursor.execute("select * from %s" % name)
    return cursor.fetchall()

path = "../../tmp/ipython/profile_default/history.sqlite"
conn = sqlite3.connect(path)
cursor = conn.cursor()
cursor.execute("select name from sqlite_master where type='table'")
targets = [f[0] for f in cursor.fetchall()]
res = {t:fetch_all(cursor, t) for t in targets}
his = [h[-1] for h in res["history"]]
s = "\n".join(his)
open("ipython_hist.txt", "w").write(s)
