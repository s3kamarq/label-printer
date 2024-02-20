import csv
from datetime import date
import os.path

heute = date.today()
dateiname = str(f"./Anmeldungen/Anmeldungen_{heute}.csv")
if os.path.exists(dateiname):
    print('file exist')
else:
    with open(dateiname, "w", newline='') as csvfile:
        #filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        filewriter = csv.writer(csvfile, delimiter=",")
        filewriter.writerow(['Teilnehmer'])


def register_Teilnehmer(data_list):

    with open(dateiname, "a", newline='') as datei:
        filewriter = csv.writer(datei)
        filewriter.writerow(data_list)
	
#für testing
#register_Teilnehmer(['mail12d'])