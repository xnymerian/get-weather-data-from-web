import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")
headers = {
    'content-type': "application/json",
    'authorization': "apikey 1CI6VgCxkOGLV8lGYXFZq6:0XPezv3ukjYGfwU7tQ7UGg"
    }
city=input("Sehir seciniz: ")
conn.request("GET", f"/weather/getWeather?data.lang=tr&data.city={city}", headers=headers)

res = conn.getresponse()
data = res.read()

weather_data = json.loads(data.decode("utf-8"))
print(weather_data["result"])

conn.close()
