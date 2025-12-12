# auto_backup.py
import shutil
import datetime

source = "./data"
dest = f"./backup_{datetime.date.today()}"
shutil.copytree(source, dest)
