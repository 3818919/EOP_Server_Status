import configparser
import os
import time
import requests
import json
import socket


###############################################################
### Get Bot Config ###
def config_file():
  config = configparser.ConfigParser()
  return config.read('config.ini') 

class settings:
  SERVER_NAME = None
  SERVER_IP = None
  SERVER_PORT = None
  STATUS_FILE = None
  WEBHOOK = None
  OFF_TITLE = None
  ON_TITLE = None
  OFF_MSG = None
  ON_MSG = None
  LOGO = None
  ONL_FILE = None
  OFF_FILE = None
  ROLE = None
  FOOTER = None
  TIMER = 30

  @classmethod
  def load_config(cls):
    config = configparser.ConfigParser()
    config.read('config.ini')

    ## EOSERV SETTINGS
    cls.SERVER_NAME = config.get('EOSERV', 'SERVER_NAME')
    cls.SERVER_IP = config.get('EOSERV', 'SERVER_IP')
    cls.SERVER_PORT = config.getint('EOSERV', 'SERVER_PORT')
    cls.LOGO = config.get('EOSERV', 'LOGO')

    ## DISCORD SETTINGS
    cls.ROLE = config.get('DISCORD', 'ROLE')
    cls.WEBHOOK = config.get('DISCORD', 'WEBHOOK')
    cls.ON_TITLE = config.get('DISCORD', 'ONLINE_TITLE')
    cls.ON_MSG = config.get('DISCORD', 'ONLINE_MESSAGE')
    cls.OFF_TITLE = config.get('DISCORD', 'OFFLINE_TITLE')
    cls.OFF_MSG = config.get('DISCORD', 'OFFLINE_MESSAGE')
    cls.FOOTER = config.get('DISCORD', 'FOOTER')

    ## FILE SETTINGS
    cls.STATUS_FILE = 'data/status.json'
    cls.ONL_FILE = 'data/server_online.json'
    cls.OFF_FILE = 'data/server_offline.json'

    ## BOT SETTINGS
    cls.TIMER = config.getint('BOT', 'TIMER')

### Load Config ###
settings.load_config()
###############################################################





###############################################################
### Get Server Status ###
def ping_server(ip, port):
  for _ in range(3):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(1)
      try:
          s.connect((ip, port))
          return True
      except:
          pass
      finally:
          s.close()
  return False


def get_state():
  ping = ping_server(settings.SERVER_IP, settings.SERVER_PORT)
  if ping == True:
    update_new_status(settings.STATUS_FILE, True)
    return True
  else:
    update_new_status(settings.STATUS_FILE, False)
    return False
###############################################################





###############################################################
### Check Server Status ###
def check_server_status(status_file, status_key):
  with open(status_file, 'r') as f:
    data = json.load(f)
    return data[status_key]

### Update Current Status ###
def update_new_status(status_file, new_status):
  with open(status_file, 'r') as f:
    data = json.load(f)
  data['new_status'] = new_status
  with open(status_file, 'w') as f:
      json.dump(data, f)

### Update Last Status
def update_last_status(status_file, new_status):
  with open(status_file, 'r') as f:
    data = json.load(f)
  data['last_status'] = new_status
  with open(status_file, 'w') as f:
    json.dump(data, f)

### Get Online Data ###
def get_online_data():
  with open(settings.ONL_FILE, 'r') as f:
    webhook_embed = json.load(f)
  return webhook_embed


### Get Offline Data ###
def get_offline_data():
  with open(settings.OFF_FILE, 'r') as f:
    webhook_embed = json.load(f)
  return webhook_embed
###############################################################





###############################################################
### Send Message ###
def send_data_to_server(webhook, webhook_data):
  requests.post(webhook, json=webhook_data)

def check_server():
  last_status = check_server_status(settings.STATUS_FILE, 'last_status')
  current_status = get_state()

  if last_status != current_status:
    update_last_status(settings.STATUS_FILE, current_status)

    if current_status:  # SERVER ONLINE
      webhook_embed = get_online_data()
      webhook_embed['username'] = webhook_embed['username'].format(settings.SERVER_NAME)
      webhook_embed['content'] = webhook_embed['content'].format(settings.ROLE)
      webhook_embed['embeds'][0]['title'] = webhook_embed['embeds'][0]['title'].format(settings.ON_TITLE)
      webhook_embed['embeds'][0]['description'] = webhook_embed['embeds'][0]['description'].format(settings.ON_MSG)
      webhook_embed['embeds'][0]['thumbnail']['url'] = webhook_embed['embeds'][0]['thumbnail']['url'].format(settings.LOGO)
      webhook_embed['embeds'][0]['footer']['text'] = webhook_embed['embeds'][0]['footer']['text'].format(settings.FOOTER)

    else:  # SERVER OFFLINE
      webhook_embed = get_offline_data()
      webhook_embed['username'] = webhook_embed['username'].format(settings.SERVER_NAME)
      webhook_embed['content'] = webhook_embed['content'].format(settings.ROLE)
      webhook_embed['embeds'][0]['title'] = webhook_embed['embeds'][0]['title'].format(settings.OFF_TITLE)
      webhook_embed['embeds'][0]['description'] = webhook_embed['embeds'][0]['description'].format(settings.OFF_MSG)
      webhook_embed['embeds'][0]['thumbnail']['url'] = webhook_embed['embeds'][0]['thumbnail']['url'].format(settings.LOGO)
      webhook_embed['embeds'][0]['footer']['text'] = webhook_embed['embeds'][0]['footer']['text'].format(settings.FOOTER)

    return webhook_embed
  return None

### Run Status Check ###
def server_alert():
  webhook_data = check_server()

  # If the server state changes
  if webhook_data is not None:
    if settings.WEBHOOK is not None:
      send_data_to_server(settings.WEBHOOK, webhook_data)
    else:
      return
###############################################################



# Main loop
while True:
  server_alert()
  # Check runs every 30 seconds
  time.sleep(settings.TIMER)
