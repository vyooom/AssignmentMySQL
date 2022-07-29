import logging
logging.basicConfig(filename='logTask_10',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('Q10. Try to find out third highest most selling dress_id.')

logging.info('The query format used was    SELECT  * FROM table_name ORDER BY colm_name DESC LIMIT n - 1, 1')

logging.info('SELECT Dress_ID, (`29/8/2013`+ `31/8/2013` +`09-02-2013` + `09-04-2013` + `09-06-2013` + `09-08-2013` + `09-10-2013` + `09-12-2013`+ `14/9/2013`+ `16/9/2013`+	`18/9/2013`+ `20/9/2013`+ `22/9/2013`+ `24/9/2013`+	`26/9/2013`+ `28/9/2013`+ `30/9/2013`+ `10-02-2013`+ `10-04-2013`+ `10-06-2013`+ `10-08-2010`+`10-10-2013`+ `10-12-2013`) FROM assignment20220724.DressSales ORDER BY (`29/8/2013`+ `31/8/2013` +`09-02-2013` + `09-04-2013` + `09-06-2013` + `09-08-2013` + `09-10-2013` + `09-12-2013`+ `14/9/2013`+ `16/9/2013`+	`18/9/2013`+ `20/9/2013`+ `22/9/2013`+ `24/9/2013`+	`26/9/2013`+ `28/9/2013`+ `30/9/2013`+ `10-02-2013`+ `10-04-2013`+ `10-06-2013`+ `10-08-2010`+`10-10-2013`+ `10-12-2013`) DESC LIMIT 2, 1')

logging.info('The answer was Dress_Id = 1006032852 Sum = 75979')

