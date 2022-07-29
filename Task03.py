import logging
logging.basicConfig(filename='logTask_03',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q3. Read these data in pandas as a dataframe')

import mysql.connector as conn

import pandas as pd

db = conn.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894', database = 'Assignment20220724')

attr = pd.read_sql('select * from Assignment20220724.Attribute', db)
logging.info('Read operation of Attribute dataframe completed.')

dress = pd.read_sql('select * from Assignment20220724.DressSales', db)
logging.info('Read operation of Dress Sales dataframe completed.')

logging.info('The Attribute dataframe is:-')
logging.info(attr)
logging.info('\n')
logging.info('The Dress Sales dataframe is:-')
logging.info(dress)

