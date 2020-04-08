import flask
import random
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def req():
    return app.send_static_file('index.html')

@app.route('/', methods=['POST'])
def idc():
    ret = ""

    vSpieler = [vtemp.replace('\r', '') for vtemp in request.form['names'].split('\n')]
    vRollen = [vtemp.replace('\r', '') for vtemp in request.form['roles'].split('\n')]
    vSpecial = [vtemp.replace('\r', '') for vtemp in request.form['special'].split('\n')]

    vSpieler.sort()
    vListe = []

    if len(vRollen) == len(vSpieler):
        for _spieler in vSpieler:
            _rolle = random.choice(vRollen)
            vRollen.remove(_rolle)
            _temp = [_spieler, _rolle]
            vListe.append(_temp)
        
        for _rolle in vSpecial:
            while len(vSpecial) < len(vSpieler):
                _random = random.randrange(0, len(vSpieler) -1, 1)
                if len(vListe[_random]) == 2:
                    vListe[_random].append(_rolle)
                    break
        
        ret += "Player\tRole\tSpecial\n"
        for _index in vListe:
            for _pos in _index:
                ret += _pos + '\t'
            ret += '\n'
    
    else:
        ret += "Error! You have more "
        if len(vRollen) < len(vSpieler):
            ret += "players than roles!"
        else:
            ret += "roles than players!"

        ret += "Players: " + len(vSpieler)
        ret += "Roles: " + len(vRollen)

                


    return ret



app.run()

