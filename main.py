import sys
import PySimpleGUI as sg 
from make_label1902 import make_label



sg.theme('LightGrey1')   # Add a touch of color
Druckzeit = 8 # Bitte Zeit eingeben wie lange der Drucker braucht


with open('Teilnahmebedingungen.txt', 'r') as f: # liesst die Teilnahmebedingungen aus dem Text-File
    Teilnahmebedingungen_Text = f.read()

do_label = make_label() #creates the object from module make_label that crates the labels



layout = [
          #[sg.Text(' ', size=(20, 1))],
          [sg.Push(), sg.Image('bannerkm.png', size=(None,None)), sg.Push()],
          [sg.Text(' ', size=(20, 1))],
          [sg.Text('       Bitte Ihre QR-Anmelde-Code an dem Scanner halten oder Ihre E-mail hier eingeben',justification='center')],
          [sg.Text('     '), sg.Input(key='QR-Code')],
          [sg.Text(' ', size=(20, 1))],        
          [sg.Text('       Durch Scannen der QR-Anmelde-Code oder durch das Klicken auf OK stimmen Sie die Teilnahmebedingungen zu.',justification='center')], 
          [sg.Text('     '),sg.Button('Teilnahmebedingungen')],        
          [sg.Text(' ', size=(20, 1))],
          [sg.Push(), sg.Button('OK'),sg.Button('Exit'), sg.Push()]#,
          #[sg.Text(' ', size=(20, 1))]
          ,]


window = sg.Window('Anmeldung zum Kongress 2024', layout, size=[850,500], finalize=True, resizable=True)
#window.Maximize()
window['QR-Code'].bind("<Return>", "_Enter")

while True:  # Event Loop
    event, values = window.read()
    #mailadress= input('Scan now: ')
    #do_label.check_entry(mailadress)
    #print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Teilnahmebedingungen':
        sg.popup(Teilnahmebedingungen_Text)
    elif event == "QR-Code" + "_Enter":
        print(values)
        window['QR-Code'].update("")
        do_label.check_entry(values['QR-Code'])

    elif event == "OK":
        print(values)
        do_label.check_entry(values['QR-Code'])
        window['QR-Code'].update("")

window.close()
##########################################################################################################
################################################################################################


def anmeldung_window():
    layout = [
        [sg.Text('Vorname', size=(10, 1)), sg.Input(key='-Vorname-', size=(30, 1))],
        [sg.Text('Name', size=(10, 1)), sg.Input(key='-Name-', size=(30, 1))],
        [sg.Text('Organisation', size=(10, 1)), sg.Input(key='-Organisation-', size=(30, 1))],
        [sg.Text('E-Mail', size=(10, 1)), sg.Input(key='QR-Code', size=(30, 1))],
        [sg.Button('Bestätigen')]
    ]

    window = sg.Window('Anmeldung', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Bestätigen':
            vorname = values['-Vorname-']
            name = values['-Name-']
            organisation = values['-Organisation-']
            email = values['QR-Code']
            print(values)
            do_label.check_entry(values['QR-Code'])
            #window['QR-Code'].update("")
            sg.popup('Sie haben sich erfolgreich angemeldet! Ihr Namensschild wird nun gedruckt.', auto_close=True, auto_close_duration=7)
            break
        elif event == "QR-Code" + "_Enter":
            vorname = values['-Vorname-']
            name = values['-Name-']
            organisation = values['-Organisation-']
            email = values['QR-Code']
            print(values)
            do_label.check_entry(values['QR-Code'])
            #window['QR-Code'].update("")
            sg.popup('Sie haben sich erfolgreich angemeldet! Ihr Namensschild wird nun gedruckt.', auto_close=True, auto_close_duration=7)
            break

    window.close()

sg.theme('LightGrey1')   # Füge etwas Farbe hinzu

# Layout definieren
layout = [
    [sg.Image('bannerkm.png', size=(None, None))],  # Banner einfügen
    [sg.Text(' ')],  # Leerer Text für einen Zeilenumbruch
    [sg.Text(' ')],  # Leerer Text für einen Zeilenumbruch
    [sg.Text('Willkommen!', size=(None, None), font=('Helvetica', 20), justification='center')],  # Großer Text "Willkommen!"
    [sg.Text('Zum Einchecken bitte Ihren QR-Code an den Scanner halten.', size=(None, None), font=('Helvetica', 20), justification='center')],  # Großer Text "Willkommen!"
    [sg.Text(' ')],  # Leerer Text für einen Zeilenumbruch
    [sg.Text(' ')],  # Leerer Text für einen Zeilenumbruch
    [sg.Text(' ')],  # Leerer Text für einen Zeilenumbruch
    [sg.Text('Noch nicht angemeldet?', size=(20, 1), justification='left'), sg.Button('Zur Anmeldung', size=(None, None), button_color=('white', 'black'), key='Anmeldung')],  # Button "Zur Anmeldung"
]

# Fenster erstellen
window = sg.Window('Anmeldung zum Kongress 2024', layout, size=[850, 500], finalize=True, resizable=True)
#window['QR-Code'].bind("<Return>", "_Enter")

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Anmeldung':  # Wenn der "Zur Anmeldung" Button geklickt wird
        anmeldung_window()# Hier können Sie den Code hinzufügen, um das neue Fenster für die Anmeldung zu öffnen
        
window.close()