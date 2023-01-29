from tkinter import messagebox, Tk, Canvas, Frame, Entry, Button


def weather_foo():
    import requests
    city = cityInput.get()
    api_url = 'https://api.openweathermap.org/data/2.5/weather'

    param = {
        'q': city,
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'
    }

    res = requests.get(api_url, params=param)
    data = res.json()['main']['temp']
    info_str = f'Сейчас в {city} {data} градусов'
    messagebox.showinfo(title='Ответ', message=info_str)


root = Tk()

root['bg'] = 'white'
root.title('Узнай погоду')
root.wm_attributes('-alpha', 0.7)
root.geometry('300x250')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='orange')
frame.place(relx=0.25, rely=0.30, relwidth=0.5, relheight=0.3)

cityInput = Entry(frame, bg='white')
cityInput.pack()

btn = Button(frame, text='Посмотреть погоду', bg='white', command=weather_foo)
btn.pack()

root.mainloop()
