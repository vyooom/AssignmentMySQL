import logging
logging.basicConfig(filename='logTask_08',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q8. Try to find out how many dresss is having recommendation as zero')

import mysql.connector as conn

db = conn.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894', database = 'Assignment20220724')

cursor = db.cursor()

cursor.execute('select Recommendation, Count(*) from assignment20220724.attribute where Recommendation = 0')

logging.info('We executed this command.')
logging.info('select Recommendation, Count(*) from assignment20220724.attribute where Recommendation = 0')


