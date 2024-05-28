import PySimpleGUI as sg

sg.theme("DarkAmber")

param = [[sg.Text("frequence"), sg.Input(default_text=10, size=(4,1))],
         [sg.Text("communication"), sg.Input(size=(4,1))],
         [sg.Text("moyenne d'arrivée"), sg.Input(size=(4,1))],
         [sg.Text("Ecart-type"), sg.Input(size=(4,1))],
         [sg.Text("tailles des communication"), sg.Input(size=(4,1))],
         [sg.Text("taille moyenne"), sg.Input(size=(4,1))],
         [sg.Text("ecart-Type"), sg.Input(size=(4,1))],
         [sg.Ok(key="-Generate-"), sg.Cancel(key="-CANCEL-")]]

layout = [[sg.Column(param)]]

window = sg.Window("OFDMA downlink simulation", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "-CANCEL-":
        break

window.close()