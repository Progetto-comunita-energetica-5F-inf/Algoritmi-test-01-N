import json
import http.client
import pymssql
def get_apidati():
    latitude = -33.856784
    longitude = 151.215297
    azimuth = 44
    tilt = 90
    start = "2024-01-25T14:45:00Z"
    duration = "P1D"
    format = "json"
    api_key = "iOyOEYM_y6XgR6inIxMrceoDSquo47ii"
    time_zone = "utc"

    conn = http.client.HTTPSConnection("api.solcast.com.au")
    conn.request("GET", f"/data/historic/radiation_and_weather?latitude={latitude}&longitude={longitude}&azimuth={azimuth}&tilt={tilt}&start={start}&duration={duration}&format={format}&api_key={api_key}&time_zone={time_zone}")

    res = conn.getresponse()
    json_data = res.read().decode("utf-8")  # Leggi il corpo della risposta e decodificalo in una stringa JSON
    dati_json = json.loads(json_data)  # Carica i dati JSON dalla stringa

    dati_stimati = dati_json["estimated_actuals"]
    return dati_stimati
def connessione():
    try:
        conn = pymssql.connect(server='ce2.database.windows.net', user='AlgoTeam', password='Algoritmi123', database='CE')
        cursore= conn.cursor()
        return cursore
        
    except Exception as e:
        print(e)
def get_dati():
    dati_stimati = get_apidati()
    ghi = []
    for dato in dati_stimati:
        ghi.append(dato["ghi"])  
    return ghi
def calcolo_produzione():
    conn = connessione()
    ghi = get_dati()
    sup = 150
    potenza = 20
    for i in ghi:
        kwh = i/1000
        cal = kwh * sup * potenza
        print(cal)


calcolo_produzione()



