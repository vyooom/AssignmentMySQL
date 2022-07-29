import logging
logging.basicConfig(filename='logTask_06',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q6. In SQL task try to perform left join operation with attribute dataset and dress dataset on column dress_id')

import mysql.connector as con

# import pandas as pd

db = con.connect(host = 'localhost',
                 user = 'root',
                 passwd = 'Mysql@894',
                 db = 'Assignment20220724')

cursor = db.cursor()

cursor.execute('select * from Assignment20220724.Attribute LEFT JOIN Assignment20220724.DressSales using(Dress_ID)')

logging.info(' Left Join Operation complete.')
