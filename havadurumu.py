import requests

def hava_durumu_al(sehir):
    api_key = 'api_gir'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': sehir, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if 'weather' in data and len(data['weather']) > 0:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f'{sehir}: {weather}, {temperature}°C'
    else:
        return 'Hava durumu hakkında bir bilgilendirme yok.'


def main():
    print("👋 Hava Durumu Konsolundan Merhabalar! (Test buildinde olduğunuzdan dolayı herhangi bir key bağlı durumda değildir, doğru çıktı alamayacaksınız.)")
    sehir = input("Şehir ismi giriniz: ")
    
    weather_info = hava_durumu_al(sehir)
    print(weather_info)

if __name__ == "__main__":
    main()
