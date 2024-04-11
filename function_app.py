import logging
import azure.functions as func
import pymssql
import logging
from datetime import datetime

app = func.FunctionApp()


@app.timer_trigger(schedule="5 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    

@app.timer_trigger(schedule="* 5 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger_Database(myTimer: func.TimerRequest) -> None:
    
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

    connesione=pymssql.connect(
                server='ce2.database.windows.net',
                user='AlgoUser',
                password='AlgoTeam123',
                database='CE')
    cursore= connesione.cursor() #Gestione chiusura connesione e ecursore MANCANTE
    
    query = "SELECT * FROM UTENTE"
    res=cursore.execute(query)

    data = cursore.fetchall()

    #Query1
    for row in data :
        logging.info (row[1])
    #query="INSERT INTO Meteo(Datatime, pressione, temperatura, velocità_vento, direzione_vento, umidità, morfologia, precipitazioni, irraggiamento) VALUES(?,?,?,?,?,?,?)"
    #res=cursore.execute(query,(datetime.now() , 0, 0, 0, 0, 0, 0, 0, 0))
    #connesione.commit()
    


@app.timer_trigger(schedule="* 5 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger_api(myTimer: func.TimerRequest) -> None:
    print('Connessione API Eseguita')
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')