import pandas as pd
import random as rand
import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.sql.selectable import Exists

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# TODO
# Add Strateges in df (CV_UCL, CV_CC, SM9, SM10)

class Response:
    
    status = []
    start = []
    finish = []
    duaration = []

    # Choose random status code
    def get_status():
        return rand.choice([200, 400, 500])

    # Get current time
    def get_start():
        return dt.datetime.now()

    # Get finish time (current time + random choice 200-500 milisec)
    def get_finish():
        return dt.datetime.now() + dt.timedelta(microseconds=rand.choice([200, 300, 400, 500]))

    # Generate 10000 inserts
    for n in range(10000):
        status.append(get_status())
        start.append(get_start())
        finish.append(get_finish())
        duaration.append(finish[n] - start[n])

data = {"Status": Response.status, 
        "Start": Response.start, 
        "Finish": Response.finish,
        "Duration": Response.duaration}
        
df = pd.DataFrame(data = data)
df.to_csv("responses.csv", index = False)
print(df)

# Fill DB
try:
    engine = create_engine('postgresql://admin:admin@localhost:5432/postgres')
    print(f"{bcolors.OKGREEN}Succesfully connected with DB.{bcolors.ENDC}")
    df.to_sql('responses', engine, if_exists='replace')
    print(f"{bcolors.OKGREEN}Succesfully load data in DB.{bcolors.ENDC}")
except Exception:
    print(f"{bcolors.FAIL}Cannot connect with DB!{bcolors.ENDC}")