import requests
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from jinja2 import Template
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError

url = 'https://notify-api.line.me/api/notify'
token = 'xxxxxxxx'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getAccessToken():
    body = { "userName": "jcluser", "password" : "Juniper!1" }
    header = {"Content-Type":"application/json", "Accept" : "application/json" }
    r=requests.post("https://xxxxxx/api/v2/login", data=json.dumps(body), headers=header,verify=False)
    return r.json()

def getAllDevice():
    call = getAccessToken()
    AccessToken = call['accessToken']
    header = {"Content-Type":"application/json" ,"Accept" : "application/json" , "Authorization" : "Token %s" % AccessToken}
    parameter = { "working": True }
    r=requests.get("https://xxxxx/api/v2/config/devices/",params=parameter, headers=header,verify=False)
    return r.json()

def getDeviceDetail(device_id):
    header = {"Content-Type":"application/json" ,"Accept" : "application/json" }
    parameter = { "working": True }
    r=requests.get("http://config-server:9000/api/v2/config/device/"+device_id,params=parameter, headers=header,verify=False) # call with internal
    print(r.url)
    return r.json()

def sendMessage(interface,host_ip,status):
    msg = 'At device ip: '+host_ip+" ,interfaces "+interface+" "+status
    r = requests.post(url, headers=headers, data = {'message':msg})


def getJunos_v2(interface, **kwargs):
    junos_details = getDeviceDetail(kwargs.get('device_id'))
    print(junos_details)
    junos_host = junos_details['host']
    junos_user = 'xxxx'
    junos_password = 'xxxx'
    device=Device(host=junos_host, user=junos_user, password=junos_password)
    device.open()
    cfg=Config(device)
    my_template = Template('delete interfaces {{ interface }} disable')
    cfg.load(my_template.render(interface=interface), format='set')
    cfg.commit()
    device.close()
    sendMessage(interface,junos_details['host'],"enable")

