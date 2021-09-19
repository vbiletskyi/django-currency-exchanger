import matplotlib.pyplot as plt
import psycopg2
import matplotlib
matplotlib.use('Agg', force=True)
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from django.shortcuts import render
from .models import Exchanger
from .forms import CurExForm


def connect_to_db():
    conn = psycopg2.connect('dbname=exchanger_db user=postgres password=admin')  # connect to db
    c = conn.cursor()  # db cursor
    c.execute("SELECT created_date, rate FROM exchanger_exchanger ORDER BY created_date")  # request to database
    data = c.fetchall()
    x_date = []
    y_rate = []

    for row in data:
        x_date.append(row[0])
        y_rate.append(row[1])
    c.close()
    conn.close()
    return x_date, y_rate


def show_chart(request):
    x, y = connect_to_db()
    if not x and not y:  # if data is empty
        return render(request, 'exchanger/fluctuations.html', {"data": True})
    else:
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(x, y)

        # decorations
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))  # date format
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_minor_locator(mdates.AutoDateLocator())  # date format

        ax.yaxis.set_major_locator(ticker.MultipleLocator(5))  # max delimiter
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))  # min delimiter
        plt.title('Курс валюты UAH -> USD')
        plt.xlabel('Дата')
        plt.ylabel('Сумма')

        fig.savefig('currency_exchanger/static/plot/my_plot.jpg')
        plt.close()
        return render(request, 'exchanger/fluctuations.html')


def add_rate(request):
    rates = Exchanger.objects.all()
    if request.method == "POST":
        form = CurExForm(request.POST)
        if form.is_valid():
            Exchanger.objects.create(**form.cleaned_data)
    else:
        form = CurExForm()
    return render(request, 'exchanger/newrate.html', {"form": form, 'rates': rates})


def show_main(request):
    rates = Exchanger.objects.all()
    return render(request, 'exchanger/main.html', {'rates': rates})
