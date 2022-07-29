import logging
logging.basicConfig(filename='logTask_07',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q7. Write a SQL query to find out how many unique dress we have.')

import mysql.connector as conn

db = conn.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894', database = 'Assignment20220724')

cursor = db.cursor()

cursor.execute('select distinct Style from Assignment20220724.Attribute')

logging.info('Selected distinct instances of the Style from Attribute dataset.')