from opencage.geocoder import OpenCageGeocode
from pygments.lexers.sql import language_re


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng'],
        else :
            return  "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"

key = 'd9089f23b93d4805a4cad19cd958cdf8'
city = "London"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")