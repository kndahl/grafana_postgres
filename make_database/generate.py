import pandas as pd
import random as rand
import datetime as dt
from sqlalchemy import create_engine

class Response:
    
    status = []
    start = []
    finish = []
    duaration = []

    def get_status():
        return rand.choice([200, 400, 500])

    def get_start():
        return dt.datetime.now()

    def get_finish():
        return dt.datetime.now() + dt.timedelta(microseconds=rand.choice([200, 300, 400, 500]))

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
engine = create_engine('postgresql://admin:admin@localhost:5432/postgres')
df.to_sql('responses', engine, if_exists='replace')