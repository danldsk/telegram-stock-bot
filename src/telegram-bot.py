from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup
import logging
import configparser

config = configparser.ConfigParser()
config.read('global_config.cfg')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

token = config['API Settings']['api_key']
updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher

##########
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'content-type': 'application/x-www-form-urlencoded'
    }
image_url_getter = requests.post("https://finviz.com/publish_map_submit.ashx", headers=headers)
print(image_url_getter.content, image_url_getter)
content = image_url_getter.json()
print(content)
soup = BeautifulSoup(content)
map_url = soup.find("share-map")
print(map_url)
url = requests.get(map_url) 
##########

def stock_map(update, context):
    # url = requests.get("https://finviz.com/map.ashx?t=sec", headers=headers) 
    # url = requests.post("https://finviz.com/publish_map_submit.ashx", headers=headers)
    # print(url)
    # content = url.text
    # print(content)
    # soup = BeautifulSoup(content)
    # map_url = soup.find("share-map")
    # print(map_url)
    # url = requests.get(map_url) 

    context.bot.send_message(chat_id=update.effective_chat.id, text="Ich teste hier nur.")

map_handler = CommandHandler('map', stock_map)

dispatcher.add_handler(map_handler)

# updater.start_polling()