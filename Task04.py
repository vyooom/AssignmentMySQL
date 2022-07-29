import logging
logging.basicConfig(filename='logTask_04',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q4. Convert attribute dataset in Json format')

import mysql.connector as con

import pandas as pd

db = con.connect(host = 'localhost',
                 user = 'root',
                 passwd = 'Mysql@894',
                 db = 'Assignment20220724')

df = pd.read_sql('select * from Assignment20220724.Attribute', db)
logging.info('Read attribute dataframe in pandas complete.')

a = df.to_json()

logging.info('Converting the Attribute dataframe to JSON format. The output is:- ')

logging.info(a)

logging.info('Saving the JSON file for future use at D:/iNeuron/dataBase/Attribute.json')
df.to_json('D:/iNeuron/dataBase/Attribute.json')