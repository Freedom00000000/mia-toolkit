import urllib.request, json

def run(args):
    city = '+'.join(args) if args else 'London'
    url = f"https://wttr.in/{city}?format=j1"
    print(f"\n\033[1;36m[ WEATHER: {city.replace('+', ' ')} ]\033[0m")
    try:
        with urllib.request.urlopen(url, timeout=8) as r:
            data = json.loads(r.read())
        cur = data['current_condition'][0]
        area = data['nearest_area'][0]
        aname = area['areaName'][0]['value']
        country = area['country'][0]['value']
        desc = cur['weatherDesc'][0]['value']
        temp_c = cur['temp_C']
        feels = cur['FeelsLikeC']
        humidity = cur['humidity']
        wind = cur['windspeedKmph']
        print(f"  Location  : {aname}, {country}")
        print(f"  Condition : {desc}")
        print(f"  Temp      : {temp_c}\u00b0C (feels like {feels}\u00b0C)")
        print(f"  Humidity  : {humidity}%")
        print(f"  Wind      : {wind} km/h")
    except Exception as e:
        print(f"  [!] Could not fetch weather: {e}")
    print()
