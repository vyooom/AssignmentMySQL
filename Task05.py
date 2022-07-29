import logging
logging.basicConfig(filename='logTask_05',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q5. Store this dataset into MongoDB')

'''
We have to store the json dataframe in MongoDb.'''

import pymongo
client = pymongo.MongoClient("mongodb+srv://abhishekMishra:Mongodb894@cluster0.qhvpp.mongodb.net/?retryWrites=true&w=majority")

db = client.test

'''
We will import json to open the json file in python.
'''
import json

logging.info('Using with open json to read the json file.')

with open('D:/iNeuron/dataBase/Attribute.json') as file:
    js = json.load(file)

database = client['classAssignment']
logging.info('Created a database named classAssignment.')
table = database['AttributeJSON']
logging.info('Created a file named AttributeJSON in classAssignment database.')
table.insert_one(js)
logging.info('Inserted the Attribute data in JSON format in MongoDB.')

