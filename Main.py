from Network import *
from Minimax import *
import time,json,random

fun_messages = ["Helo your compuder has virus", "Mais, vous savez, moi je ne crois pas qu’il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd’hui avec vous, je dirais que c’est d’abord des rencontres, des gens qui m’ont tendu la main, peut-être à un moment où je ne pouvais pas, où j’étais seul chez moi. Et c’est assez curieux de se dire que les hasards, les rencontres forgent une destinée… Parce que quand on a le goût de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l’interlocuteur en face, je dirais, le miroir qui vous aide à avancer. Alors ce n’est pas mon cas, comme je le disais là, puisque moi au contraire, j’ai pu ; et je dis merci à la vie, je lui dis merci, je chante la vie, je danse la vie… Je ne suis qu’amour ! Et finalement, quand beaucoup de gens aujourd’hui me disent : « Mais comment fais-tu pour avoir cette humanité ? » Eh bien je leur réponds très simplement, je leur dis que c’est ce goût de l’amour, ce goût donc qui m’a poussé aujourd’hui à entreprendre une construction mécanique, mais demain, qui sait, peut-être simplement à me mettre au service de la communauté, à faire le don, le don de soi...","If you can see black body radiation, it means that it's hot", "LER: Light-Emmitting resistor", "- Vous êtes sor ? - Tout à fait sor !", "J'ai glissé chef !", "Y a pas de panneau", "H@ck3r-S1mUl4t0r","Not-a-Virus.exe unavailable (Distant socket closed). Wait for 3 seconds","Une tuiiiiile", "Quand j'te dis qu't'es tendue t'es tendue","Claudie Focan : 'On racle tout on met ça dans des grandes bassines on appelle ça des piscines'", ""]

def handleRcv(js, client):
    if js["request"] == "play":
        response = {
            "response": "move",
            "move": calculate(js["state"],weights),
            "message": fun_messages[random.randint(0,len(fun_messages)-1)]
        }
        network.send(client, json.dumps(response))
        
def train(port, w):
    global weights
    weights = w
    network = Network("10.0.0.153", 3000, port, handleRcv, f"{w[0]};{w[1]};{w[2]};{w[3]};{w[4]}", f"[\"{random.randint(0,29000)}\"]")
    if network.isSubscribed:
        print("Registered with server! Yay!")
    else: 
        print("Error when registering with server...")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    global weights
    weights = [-1,0,1,0.5]
    network = Network("10.0.0.153", 3000, 3310, handleRcv, "Je m'appeelle teus", "[\"220541\", \"221671\"]")
    if network.isSubscribed:
        print("Registered with server! Yay!")
    else: 
        print("Error when registering with server...")
    while True:
        time.sleep(1)