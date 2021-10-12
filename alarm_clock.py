from datetime import datetime as dt
from playsound import playsound as ps
import time

def valida(alarme):
    if len(alarme) != 8:
        return "Formato do alarme INVÁLIDO! Tente novamente...."
    else:
        if str(alarme[2:3]) != ":" or str(alarme[5:6]) != ":":
            return "Formato INVÁLIDO"
        elif int(alarme[0:2]) > 24 or int(alarme[0:2]) < 0:
            return "Formato da hora INVÁLIDO"
        elif int(alarme[3:5]) > 59:
            return "Formato dos minutos INVÁLIDO"
        elif int(alarme[6:8]) > 59:
            return "Formato dos segundos INVÁLIDO"
        else:
            return "OK"

def main():
    
    while True:
        alarme = input("Informe o alarme [HH:MM:SS]: ")
        validado = valida(alarme.lower())
        if validado != "OK":
            print(validado)
        else:
            alarme_hora = alarme[0:2]
            alarme_min = alarme[3:5]
            alarme_seg = alarme[6:8]
            print(f"Configurando o alarme para {alarme}...")
            break
                     
    while True:
        agora = dt.now()
        hora_atual = agora.strftime("%H")
        minuto_atual = agora.strftime("%M")
        segundo_atual = agora.strftime("%S")
        
        if alarme_hora == hora_atual:
            if alarme_min == minuto_atual:
                if alarme_seg == segundo_atual:
                    print("HORA DE ACORDAR VAGABUNDO!!!!!!")
                    for i in range(2):
                        time.sleep(0.3)
                        ps("song_alarm/basic_bell.mp3")
                    break
                
main()