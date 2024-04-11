import json
import http.client

conn = http.client.HTTPSConnection("api.solcast.com.au")
payload = ''
headers = {}
conn.request("GET", "/data/historic/radiation_and_weather?latitude=-33.856784&longitude=151.215297&azimuth=44&tilt=90&start=2024-01-25T14:45:00Z&duration=P1D&format=json&api_key=iOyOEYM_y6XgR6inIxMrceoDSquo47ii&time_zone=utc", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))