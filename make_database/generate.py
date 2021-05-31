import pandas as pd
import random as rand
import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.sql.selectable import Exists
import time

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
    strategy = []
    source = []
    product = []
    start = []
    finish = []
    duration = []

    # Choose random status code
    def get_status():
        return rand.choice([200, 400, 500])

    def get_strategy():
        return rand.choice(["CV_UCL", "CV_CC", "SM9", "SM10"])

    def get_sourcedata():
        return rand.choice(["UV", "Transact"])

    def get_product():
        return rand.choice(["ConsumerCredit", "CreditCard", "Mortgage"])

    # Get current time
    def get_start(finish):
         return finish + dt.timedelta(seconds=10)

    # Get finish time (current time + random choice 200-500 milisec)
    def get_finish(start):
        return start + dt.timedelta(microseconds=rand.choice([200, 300, 400, 500]))

    # Generate 1000 inserts
    for n in range(1000):
        status.append(get_status())
        strategy.append(get_strategy())
        source.append(get_sourcedata())
        product.append(get_product())
        start.append(get_start(start[n - 1] if n > 0 else dt.datetime.now()))
        finish.append(get_finish(start[n]))
        duration.append((finish[n] - start[n]).microseconds)

data = {"Status": Response.status,
        "Strategy": Response.strategy,
        "Source": Response.source,
        "Product": Response.product,
        "Start": Response.start, 
        "Finish": Response.finish,
        "Duration": Response.duration}
        
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