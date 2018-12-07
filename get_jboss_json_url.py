import requests
import json
import asyncio
import websockets
from requests.auth import HTTPDigestAuth
from lomond import WebSocket

url = 'http://localhost:9990/management'
user="admin"
passwd="passwdhere"
headers = {'content-type': 'application/json'}

def get_jboss_hostserver():
    payload = {"operation":"read-children-names","child-type":"host","json.pretty":1} #Parametros da API

    # Envia a requisicao POST
    resposta = requests.post(url, data=json.dumps(payload), auth=HTTPDigestAuth(user, passwd), headers=headers)
    # Imprime a resposta da requisicap
    #print(resposta.text)
    json_array = json.loads(resposta.text)
    return(json_array['result'][0])

def get_all_jboss_server_status(hostserver):
    payload = {"operation":"read-children-names", "address":["host",hostserver], "child-type":"server","json.pretty":1}
    resposta = requests.post(url, data=json.dumps(payload), auth=HTTPDigestAuth(user, passwd), headers=headers)
    json_array = json.loads(resposta.text)

    count=0
    lista=[]
    for servername in (json_array['result']):
        payload = {"operation":"read-attribute", "address":["host",hostserver,"server",servername], "name":"runtime-configuration-state","json.pretty":1}
        resposta = requests.post(url, data=json.dumps(payload), auth=HTTPDigestAuth(user, passwd), headers=headers)  
        json_array = json.loads(resposta.text)

        if (json_array['result']) == "ok":
            payload_suspension = {"operation":"read-attribute", "address":["host",hostserver,"server",servername], "name":"suspend-state","json.pretty":1}
            suspend_state_value = requests.post(url, data=json.dumps(payload_suspension), auth=HTTPDigestAuth(user, passwd), headers=headers)
            json_array_suspended = json.loads(suspend_state_value.text)
            suspensionvalue = json_array_suspended['result']
        else:
            suspensionvalue = "none"

        status = json_array['result']
        count=count+1
        
        #asyncio.get_event_loop().run_until_complete(hello(message))       
        #print("ID:", count, "SERVER:", servername, "STATUS:", json_array['result'], "SUSPENSION_STATE:", suspensionvalue)
        #print(json.dumps({'id': count, 'servername': servername, 'server-status': json_array['result'], 'suspension-state': suspensionvalue}, indent=2))
        #message=json.dumps({'id': count, 'servername': servername, 'server-status': json_array['result'], 'suspension-state': suspensionvalue}, indent=4)
        message=({'id': count, 'servername': servername, 'server-status': json_array['result'], 'suspension-state': suspensionvalue})
        lista.append(message)

    #print(json.dumps(lista))
    print(json.dumps(lista, sort_keys=True, indent=2))

    websocket = WebSocket('wss://localhost:8765')
    #asyncio.get_event_loop().run_until_complete(hello(lista))
    websocket.send_json(lista)
   
    
get_jboss_hostserver()
get_all_jboss_server_status(get_jboss_hostserver())
