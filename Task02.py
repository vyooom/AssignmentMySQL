import logging
logging.basicConfig(filename='logTask_02',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q2: Do a bulk load for these two datasets.')

import mysql.connector as sqlConnect

newdb = sqlConnect.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894', database = 'Assignment20220724')

cursor = newdb.cursor()

q1 = "Create table if not exists Assignment20220724.Attribute(Dress_ID int(12), Style varchar(20), Price varchar(20), Rating float(5), Size varchar(5),  Season varchar(20), Neckline varchar(20), SleeveLength varchar(20), waiseline varchar(20), Material varchar(20), FabricType varchar(20), Decoration varchar(20), Patterntype varchar(20), Recommendation int(2));"
q2 = "create table if not exists Assignment20220724.DressSales(Dress_ID int (12), `29/8/2013`	int(10), `31/8/2013` int(10), `09-02-2013` int(10),	`09-04-2013` int(10), `09-06-2013` int(10),	`09-08-2013` int(10), `09-10-2013` int(10),	`09-12-2013` int(10), `14/9/2013` int(10), `16/9/2013` int(10),	`18/9/2013` int(10), `20/9/2013` int(10), `22/9/2013` int(10), `24/9/2013` int(10),	`26/9/2013` int(10), `28/9/2013` int(10), `30/9/2013` int(10), `10-02-2013`	int(10), `10-04-2013` int(10), `10-06-2013` int(10), `10-08-2010` int(10), `10-10-2013`	int(10), `10-12-2013` int(10))"

cursor.execute(q1)
cursor.execute(q2)

'''
Now we will try to load the data directly from the files.
 But the original files are in excel format, hence we will convert them to csv format and then bulk upload the data.
 We have to take care of the Null and unwanted Values also. Here we have replaced them with zero.
 '''
logging.info('Query for the bulk upload of Attribute data.')
q3 = "LOAD DATA INFILE 'D:/iNeuron/dataBase/Attribute.csv' INTO TABLE Assignment20220724.Attribute FIELDS TERMINATED BY ',' ENCLOSED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS"

cursor.execute(q3)
logging.info('The bulk data upload of Attribute Dataset completed.')

logging.info('Query for the bulk upload of Dress Sales data.')
q4 = "LOAD DATA INFILE 'D:/iNeuron/dataBase/DressSales.csv' INTO TABLE Assignment20220724.DressSales FIELDS TERMINATED BY ',' ENCLOSED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS"

cursor.execute(q4)
logging.info('The bulk data upload of DressSales Dataset completed.')

newdb.commit()





