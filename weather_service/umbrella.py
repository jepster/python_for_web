from weatherService import WeatherService


def makeUmbrellaDecision() -> bool:
    if WeatherService.getForecast('Düsseldorf', 'de'):
        print('You must take an umbrella.')
        return True
    print('You must not take an umbrella.')
    return False


if __name__ == "__main__":
    makeUmbrellaDecision()
