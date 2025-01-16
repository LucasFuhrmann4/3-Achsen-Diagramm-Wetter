import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime

class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        # Daten für die Monate
        monate = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]

        # Beispiel-Daten (anpassen an die tatsächlichen Werte)
        hoechsttemperaturen = [-1, 0, 5, 10, 15, 20, 22, 21, 17, 10, 5, 0]
        tiefsttemperaturen = [-10, -8, -5, 0, 5, 10, 12, 11, 8, 2, -2, -7]
        frosttage = [25, 23, 20, 10, 5, 1, 0, 0, 2, 10, 20, 24]

        # Erstelle die Grafik
        fig, ax1 = plt.subplots()

        # Temperaturkurven (links)
        ax1.set_xlabel("Monate")
        ax1.set_ylabel("Temperatur (°C)", color="black")
        ax1.plot(monate, hoechsttemperaturen, color="red", marker="o", label="Höchsttemperatur")
        ax1.plot(monate, tiefsttemperaturen, color="blue", marker="o", label="Tiefsttemperatur")
        ax1.tick_params(axis="y", labelcolor="black")
        ax1.legend(loc="upper left")

        # Frosttage (rechts)
        ax2 = ax1.twinx()
        ax2.set_ylabel("Anzahl Frosttage", color="gray")
        ax2.bar(monate, frosttage, color="gray", alpha=0.5, label="Anzahl Frosttage")
        ax2.tick_params(axis="y", labelcolor="gray")

        # Titel und Layout
        plt.title("Wetterstation Brocken (1141m)\nKlimadiagramm Temperatur")
        fig.tight_layout()
        plt.show()
