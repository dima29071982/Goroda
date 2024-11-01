from bokeh.embed import components
from nltk.sem.chat80 import country, region
from opencage.geocoder import OpenCageGeocode
from tkinter import *

from tornado.gen import Return


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            region = results[0]['components']['state']
            return f"Широта: {lat}, Долгота: {lon} Страна: {country} Регион: {region}"
        else :
            return  "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {coordinates}")


key = "8f34e7c28e0d43b19f20c8fc0d09e4e9"


window=Tk()
window.title("Координаты городов")
window.geometry("350x100")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)
button = Button(text="Поиск координат", command=show_coordinates)
button.pack()
label = Label(text= "Введите город и нажмите на кнопку")
label.pack()

window.mainloop()