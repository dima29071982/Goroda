from opencage.geocoder import OpenCageGeocode
from tkinter import *

from scipy.ndimage import label
from tensorflow.python.ops.gen_control_flow_ops import enter
from БРОНИРОВАНИЕ_2 import window


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота: {lon}"
        else :
            return  "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"


def snow_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}: {coordinates}")



key = 'd9089f23b93d4805a4cad19cd958cdf8'


print()

window=Tk()
window.title("Координаты городов")
window.geometry("200x200")

enter = Entry()
enter.pack()

button = Button(text= "Поиск координат", comanda=get_coordinates)
button.pack()
label = Label(text= "Введите город и нажмите на кнопку")

window.mainloop()