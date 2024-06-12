import PySimpleGUI as sg

def settings() -> dict:
    setting_values = {}

    sg.theme("DarkAmber")

    param = [[sg.Text("Bandwidth in MHz: "), sg.Combo([1.4, 3, 5, 10, 15, 20],default_value=1.4, size=(4,1), key="bandwidth")], 
            [sg.Text("Nombre de communications"), sg.Input(size=(4,1), key="com", default_text=10)], 
            [sg.Text("Temps Max entre 2 com (def : 1s)"), sg.Input(size=(4,1), key="interval", default_text=1)], 
            #[sg.Text("Ecart-type"), sg.Input(size=(4,1))],
            #[sg.Text("tailles des communication"), sg.Input(size=(4,1))],
            [sg.Text("taille moyenne des comm (def : 500bits)"), sg.Input(size=(4,1), key="av_size", default_text=500)],
            #[sg.Text("ecart-Type"), sg.Input(size=(4,1))],
            [sg.Ok(key="-Generate-"), sg.Cancel(key="-CANCEL-")]]

    layout = [[sg.Column(param)]]

    window = sg.Window("OFDMA downlink simulation", layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "-CANCEL-":
            window.close()
            exit()
        
        if event == "-Generate-":
            setting_values = values
            
            bandwidth_rb = {1.4: 6, 3: 15, 5: 25, 10: 50, 15: 75, 20: 100}
            setting_values["RB"] = bandwidth_rb[setting_values["bandwidth"]]
            break
            

    window.close()
    
    return setting_values

if __name__ == "__main__":
    print(settings())