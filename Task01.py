import logging
logging.basicConfig(filename='logTask_01',
                    level= logging.DEBUG,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q1: Create a table for attribute & dress dataset.')

import mysql.connector as connector

newdb = connector.connect(host = 'localhost', user = 'root',
    passwd = 'Mysql@894')

cursor = newdb.cursor()

cursor.execute('create database if not exists Assignment20220724')

logging.info(cursor.fetchall())

q1 = "create table if not exists Assignment20220724.Attribute(Dress_ID int(12), Style varchar(20), Price varchar(20), Rating float(5), Size varchar(5),  Season varchar(20), Neckline varchar(20), SleeveLength varchar(20), waiseline varchar(20), Material varchar(20), FabricType varchar(20), Decoration varchar(20), Patterntype varchar(20), Recommendation int(2))"

q2 = "create table if not exists Assignment20220724.DressSales(Dress_ID int (12), `29/8/2013`	int(10), `31/8/2013` int(10), `09-02-2013` int(10),	`09-04-2013` int(10), `09-06-2013` int(10),	`09-08-2013` int(10), `09-10-2013` int(10),	`09-12-2013` int(10), `14/9/2013` int(10), `16/9/2013` int(10),	`18/9/2013` int(10), `20/9/2013` int(10), `22/9/2013` int(10), `24/9/2013` int(10),	`26/9/2013` int(10), `28/9/2013` int(10), `30/9/2013` int(10), `10-02-2013`	int(10), `10-04-2013` int(10), `10-06-2013` int(10), `10-08-2010` int(10), `10-10-2013`	int(10), `10-12-2013` int(10))"

cursor.execute(q1)
cursor.execute(q2)
newdb.commit()

import pandas as pd

logging.info(pd.read_sql("select * from Assignment20220724.Attribute", newdb))
logging.info(pd.read_sql("select * from Assignment20220724.DressSales", newdb))

