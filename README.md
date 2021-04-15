# Temperatur
ML Klassifizierungsmodell erkennt, ob Temperaturdaten echt oder gefälscht sind.

Die Daten sind dabei für einen Menschen schlecht unterscheidbar (https://temperatur-raten.herokuapp.com/).

Im Ordner *Beispielwerte* befinden sich zwei Bilder mit Beispielen für echte bzw. gefälschte Daten.

## Trainingsdaten
### wahre Daten
Temperaturwerte von Portland (2012-2017)

Quelle: https://www.kaggle.com/selfishgene/historical-hourly-weather-data?select=temperature.csv
### gefälschte Daten
mathematisch berechnete (Zufalls)Werte, angenähert an Kosinusfunktion

## Modell
SVC von Scikit-Learn

## Genauigkeit
Genauigkeit KI: 0,95

Genauigkeit Mensch: https://temperatur-raten.herokuapp.com/

## verwendete Pakete
- numpy
- pandas
- sklearn
- matplotlib
