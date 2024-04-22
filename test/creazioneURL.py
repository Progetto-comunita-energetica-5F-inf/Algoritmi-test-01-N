import json
import http.client
import json
import pymssql

def inserisci_dati_in_database(json_data):
    try:
        # Carica i dati JSON
        dati_json = json.loads(json_data)
        dati_stimati = dati_json["estimated_actuals"]

        # Connessione al database SQL Server
        conn = pymssql.connect(server='ce2.database.windows.net', user='AlgoUser', password='Algoritmi123', database='CE')
        cursore= connesione.cursor()

        # Inserimento dei dati nel database 
        for dato in dati_stimati:
            air_temp = dato["air_temp"]
            dni = dato["dni"]
            ghi = dato["ghi"]
            Datatime = dato["period_end"]
            cursor.execute("INSERT INTO Meteo ( Datatime,Pressione, Temperatura, Velocità_vento, Direzione_vento, Umidità, Morfologia, Precipitazioni, Irraggiamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (air_temp, dni, ghi, period_end))

        conn.commit()
        print("Dati inseriti correttamente nel database.")
        
        # Chiusura della connessione
        conn.close()
    except Exception as e:
        print("Si è verificato un errore durante l'inserimento dei dati nel database:", str(e))

# JSON fornito
json_data = '''{"estimated_actuals":[{"air_temp":25,"dni":0,"ghi":0,"period_end":"2024-01-25T15:00:00.0000000Z","period":"PT30M"},{"air_temp":25,"dni":0,"ghi":0,"period_end":"2024-01-25T15:30:00.0000000Z","period":"PT30M"},{"air_temp":25,"dni":0,"ghi":0,"period_end":"2024-01-25T16:00:00.0000000Z","period":"PT30M"},{"air_temp":25,"dni":0,"ghi":0,"period_end":"2024-01-25T16:30:00.0000000Z","period":"PT30M"},{"air_temp":25,"dni":0,"ghi":0,"period_end":"2024-01-25T17:00:00.0000000Z","period":"PT30M"},{"air_temp":26,"dni":0,"ghi":0,"period_end":"2024-01-25T17:30:00.0000000Z","period":"PT30M"},{"air_temp":26,"dni":0,"ghi":0,"period_end":"2024-01-25T18:00:00.0000000Z","period":"PT30M"},{"air_temp":26,"dni":0,"ghi":0,"period_end":"2024-01-25T18:30:00.0000000Z","period":"PT30M"},{"air_temp":26,"dni":0,"ghi":0,"period_end":"2024-01-25T19:00:00.0000000Z","period":"PT30M"},{"air_temp":27,"dni":0,"ghi":2,"period_end":"2024-01-25T19:30:00.0000000Z","period":"PT30M"},{"air_temp":27,"dni":10,"ghi":43,"period_end":"2024-01-25T20:00:00.0000000Z","period":"PT30M"},{"air_temp":28,"dni":0,"ghi":83,"period_end":"2024-01-25T20:30:00.0000000Z","period":"PT30M"},{"air_temp":29,"dni":47,"ghi":159,"period_end":"2024-01-25T21:00:00.0000000Z","period":"PT30M"},{"air_temp":29,"dni":237,"ghi":283,"period_end":"2024-01-25T21:30:00.0000000Z","period":"PT30M"},{"air_temp":30,"dni":651,"ghi":450,"period_end":"2024-01-25T22:00:00.0000000Z","period":"PT30M"},{"air_temp":31,"dni":670,"ghi":544,"period_end":"2024-01-25T22:30:00.0000000Z","period":"PT30M"},{"air_temp":31,"dni":803,"ghi":661,"period_end":"2024-01-25T23:00:00.0000000Z","period":"PT30M"},{"air_temp":32,"dni":512,"ghi":588,"period_end":"2024-01-25T23:30:00.0000000Z","period":"PT30M"},{"air_temp":32,"dni":0,"ghi":309,"period_end":"2024-01-26T00:00:00.0000000Z","period":"PT30M"},{"air_temp":33,"dni":0,"ghi":458,"period_end":"2024-01-26T00:30:00.0000000Z","period":"PT30M"},{"air_temp":33,"dni":5,"ghi":515,"period_end":"2024-01-26T01:00:00.0000000Z","period":"PT30M"},{"air_temp":33,"dni":0,"ghi":529,"period_end":"2024-01-26T01:30:00.0000000Z","period":"PT30M"},{"air_temp":33,"dni":25,"ghi":572,"period_end":"2024-01-26T02:00:00.0000000Z","period":"PT30M"},{"air_temp":33,"dni":197,"ghi":697,"period_end":"2024-01-26T02:30:00.0000000Z","period":"PT30M"},{"air_temp":33,"dni":328,"ghi":747,"period_end":"2024-01-26T03:00:00.0000000Z","period":"PT30M"},{"air_temp":32,"dni":158,"ghi":510,"period_end":"2024-01-26T03:30:00.0000000Z","period":"PT30M"},{"air_temp":31,"dni":147,"ghi":609,"period_end":"2024-01-26T04:00:00.0000000Z","period":"PT30M"},{"air_temp":29,"dni":72,"ghi":372,"period_end":"2024-01-26T04:30:00.0000000Z","period":"PT30M"},{"air_temp":27,"dni":0,"ghi":200,"period_end":"2024-01-26T05:00:00.0000000Z","period":"PT30M"},{"air_temp":25,"dni":76,"ghi":417,"period_end":"2024-01-26T05:30:00.0000000Z","period":"PT30M"},{"air_temp":24,"dni":106,"ghi":422,"period_end":"2024-01-26T06:00:00.0000000Z","period":"PT30M"},{"air_temp":24,"dni":1,"ghi":308,"period_end":"2024-01-26T06:30:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":2,"ghi":236,"period_end":"2024-01-26T07:00:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":0,"ghi":147,"period_end":"2024-01-26T07:30:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":0,"ghi":60,"period_end":"2024-01-26T08:00:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":0,"ghi":8,"period_end":"2024-01-26T08:30:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":0,"ghi":3,"period_end":"2024-01-26T09:00:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":0,"ghi":0,"period_end":"2024-01-26T09:30:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":0,"ghi":0,"period_end":"2024-01-26T10:00:00.0000000Z","period":"PT30M"},{"air_temp":23,"dni":0,"ghi":0,"period_end":"2024-01-26T10:30:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T11:00:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T11:30:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T12:00:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T12:30:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T13:00:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T13:30:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T14:00:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T14:30:00.0000000Z","period":"PT30M"},{"air_temp":22,"dni":0,"ghi":0,"period_end":"2024-01-26T15:00:00.0000000Z","period":"PT30M"}]}'''

# Chiamata alla funzione per inserire i dati nel database
inserisci_dati_in_database(json_data)


latitude = -33.856784
longitude = 151.215297
azimuth = 44
tilt = 90
start = "2024-01-25T14:45:00Z"
duration = "P1D"
format = "json"
api_key = "iOyOEYM_y6XgR6inIxMrceoDSquo47ii"
time_zone = "utc"

url = f"https://api.solcast.com.au/data/historic/radiation_and_weather?latitude={latitude}&longitude={longitude}&azimuth={azimuth}&tilt={tilt}&start={start}&duration={duration}&format={format}&api_key={api_key}&time_zone={time_zone}"
    

conn = http.client.HTTPSConnection("api.solcast.com.au")
payload = ''
headers = {}
conn.request("GET", f"/data/historic/radiation_and_weather?latitude={latitude}&longitude={longitude}&azimuth={azimuth}&tilt={tilt}&start={start}&duration={duration}&format={format}&api_key={api_key}&time_zone={time_zone}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
