import requests
from django.shortcuts import render

API_KEY = "7Jye09LScbvnSVoAnnWJaACbgDiUV9uL"

def weather_view(request):
    city = request.GET.get('city')
    weather_data = None
    error = None

    if city:
        city = city.strip()
        try:
            location_url = f"https://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={city}"
            location_response = requests.get(location_url)
            location_response.raise_for_status()
            locations = location_response.json()

            if not locations:
                error = "Cidade não encontrada."
            else:
                location_key = locations[0]['Key']
                city_name = locations[0]['LocalizedName']

                weather_url = f"https://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&language=pt-br&details=true"
                weather_response = requests.get(weather_url)
                weather_response.raise_for_status()
                weather = weather_response.json()[0]

                icon_num = weather.get('WeatherIcon')
                icon_url = None
                if icon_num is not None:
                    icon_url = f"https://developer.accuweather.com/sites/default/files/{icon_num:02d}-s.png"

                weather_data = {
                    "city_name": city_name,
                    "temperature": weather['Temperature']['Metric']['Value'],
                    "description": weather['WeatherText'],
                    "humidity": weather.get('RelativeHumidity'),
                    "icon_url": icon_url,
                }
        except requests.exceptions.RequestException as e:
            error = f"Erro ao consultar a API: {e}"
        except (KeyError, IndexError) as e:
            error = f"Dados da cidade inválidos: {e}"

    return render(request, "weather/tempo.html", {
        "weather_data": weather_data,
        "error": error
    })
