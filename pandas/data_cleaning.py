import pandas as pd

'''
### Daten Laden und Übersicht ###
    pd.read_csv('datei.csv')    : Lädt eine CSV-Datei in ein DataFrame.
    df.head()                   : Zeigt die ersten n Zeilen (Standard: 5).
    df.info()                   : Zusammenfassung des DataFrames (Datentypen, Non-Null-Werte).
    df.describe()               : Statistische Zusammenfassung numerischer Spalten.
    df.columns                  : Listet alle Spaltennamen auf.
'''

df = pd.read_csv("pandas/test.csv")

print(df.head(5))

print(df.info())

print(df.describe())

print(df.columns)

'''
### Fehlende Werte ###
    df.isnull().sum()           : Zählt fehlende Werte (NaN oder None) pro Spalte.
    df.dropna()                 : Entfernt Zeilen mit mindestens einem fehlenden Wert.
    df.dropna(axis=1)           : Entfernt Spalten mit mindestens einem fehlenden Wert.
    df.fillna(wert)             : Ersetzt fehlende Werte durch einen festen Wert.

    df['Spalte'].fillna(df['Spalte'].mean(), inplace=True)     : Ersetzt fehlende Werte durch den Mittelwert der Spalte.
    df['Spalte'].fillna(df['Spalte'].mode()[0], inplace=True)  : Ersetzt fehlende Werte durch den Modus (häufigsten Wert) der Spalte.
    df['Spalte'].fillna(method='ffill')                        : Forward-Fill: Ersetzt mit dem vorherigen Wert.
'''

'''
### Duplikate ###
df.duplicated().sum()                               : Zählt alle duplizierten Zeilen (außer der ersten Instanz).
df.drop_duplicates()                                : Entfernt duplizierte Zeilen (behält die erste Instanz).
df.drop_duplicates(subset=['SpalteA', 'SpalteB'])   : Entfernt Duplikate basierend auf einer Auswahl von Spalten.
'''

'''
### Datentypen & Formatierung ###
df['Spalte'].astype('int')                          : Konvertiert den Datentyp der Spalte (z. B. zu int, str, float).
pd.to_datetime(df['Spalte'])                        : Konvertiert eine Spalte in den Datetime-Typ.
df['Spalte'].str.lower()                            : Konvertiert Text in Kleinbuchstaben.  
df['Spalte'].str.strip()                            : Entfernt Leerzeichen am Anfang und Ende des Strings.
df['Spalte'].str.replace('$', '')                   : Ersetzt ein Zeichen oder Muster durch ein anderes (hier: entfernt $).
'''

'''
### Datenstruktur & Ausreißer (Outliers) ###
df.rename(columns={'alt':'neu'})                    : Benennt Spalten um.
df[df['Spalte'] > 10]                               : Wählt Zeilen, in denen der Wert größer als 10 ist.
df['neu'] = df['alt'].apply(lambda x: x*2)          : Wendet eine Funktion (z. B. Lambda) auf die Spaltenwerte an.
df.sort_values(by='Spalte', ascending=False)        : Sortiert das DataFrame.
'''