import logging
logging.basicConfig(filename='logTask_09',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q9. Try to find out the total dress sales for each dress_id using SQL.')

logging.info('The Dress Sales table is used here.')

logging.info('The format used is "SELECT id, (value1 + value2+...) FROM table"')

logging.info('select Dress_ID, (`29/8/2013`+ `31/8/2013` +`09-02-2013` + `09-04-2013` + `09-06-2013` + `09-08-2013` + `09-10-2013` + `09-12-2013`+ `14/9/2013`+ `16/9/2013`+	`18/9/2013`+ `20/9/2013`+ `22/9/2013`+ `24/9/2013`+	`26/9/2013`+ `28/9/2013`+ `30/9/2013`+ `10-02-2013`+ `10-04-2013`+ `10-06-2013`+ `10-08-2010`+`10-10-2013`+ `10-12-2013`) from assignment20220724.dressSales')
