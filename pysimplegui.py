import PySimpleGUI as sg

sg.theme("DarkAmber")
# Define the column headings for the table
headings = ['Time Slot', 'Frequency Subcarrier', 'User ID', 'Packet Data']
data = [
    [1, 'Subcarrier 1', 'User A', 'Packet 1'],
    [1, 'Subcarrier 2', 'User B', 'Packet 2'],
    [2, 'Subcarrier 1', 'User C', 'Packet 3'],
    [2, 'Subcarrier 2', 'User A', 'Packet 4']
]

param = [[sg.Text("frequence"), sg.Input(default_text=10, size=(4,1))],
         [sg.Text("communication"), sg.Input(size=(4,1))],
         [sg.Text("moyenne d'arrivée"), sg.Input(size=(4,1))],
         [sg.Text("Ecart-type"), sg.Input(size=(4,1))],
         [sg.Text("tailles des communication"), sg.Input(size=(4,1))],
         [sg.Text("taille moyenne"), sg.Input(size=(4,1))],
         [sg.Text("ecart-Type"), sg.Input(size=(4,1))],
         [sg.Ok(key="-OK-"), sg.Cancel(key="-CANCEL-")]]

table = [[sg.Table(values=data, headings=headings, auto_size_columns=True, display_row_numbers=True, key='-TABLE-')]]

layout = [[sg.Column(param), sg.Column(table)]]

window = sg.Window("OFDMA downlink simulation", layout, size=(1000,600))

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "-CANCEL-":
        break

window.close()