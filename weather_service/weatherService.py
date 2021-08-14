import requests


class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
    appId = '5d6ee65792195f258ea4dab562fef198'

    # 5d6ee65792195f258ea4dab562fef198


    @classmethod
    def getForecast(cls, city, country):
        response = requests.get(cls.baseUrl, params=[
            ('appId', cls.appId),
            ('q', f'{city},{country}')
        ])
        data = response.json()

        rain = False

        for hour in data['list']:
            if hour['weather'][0]['main'] == 'Rain':
                rain = True

        return rain

if __name__ == "__main__":
    print(WeatherService.getForecast('Düsseldorf', 'de'))