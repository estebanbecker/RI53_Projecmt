import PySimpleGUI as sg

def settings() -> dict:
    setting_values = {}
    sg.theme("DarkAmber")

    param = [[sg.Text("Nombre de PRB"), sg.Input(default_text=10, size=(4,1))], 
            [sg.Text("Nombre de communications"), sg.Input(size=(4,1))], 
            [sg.Text("Temps Max entre 2 com (def : 1s)"), sg.Input(size=(4,1))], 
            #[sg.Text("Ecart-type"), sg.Input(size=(4,1))],
            #[sg.Text("tailles des communication"), sg.Input(size=(4,1))],
            [sg.Text("taille moyenne des comm (def : 500 bts)"), sg.Input(size=(4,1))],
            #[sg.Text("ecart-Type"), sg.Input(size=(4,1))],
            [sg.Ok(key="-Generate-"), sg.Cancel(key="-CANCEL-")]]

    layout = [[sg.Column(param)]]

    window = sg.Window("OFDMA downlink simulation", layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "-CANCEL-":
            break
        
        if event == "-Generate-":
            setting_values = values
            break
            

    window.close()
    
    return setting_values