#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request, json, time
from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

last_price_data = {}
last_price_check = -1

def price():
	global last_price_data, last_price_check
	if time.time() - last_price_check >= 60:
		with urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/2011/") as url:
			data = json.loads(url.read().decode())
			last_price_data = data
			last_price_check = time.time()
	else:
		data = last_price_data
	return "XTZ/USD:	$"+str(round(data["data"]["quotes"]["USD"]["price"], 2))+"\n1hr:		"+str(data["data"]["quotes"]["USD"]["percent_change_1h"])+"%\n24hr:		"+str(data["data"]["quotes"]["USD"]["percent_change_24h"])+"%\n7d:		"+str(data["data"]["quotes"]["USD"]["percent_change_7d"])+"%"


api_key = "APIKEY"
responses = {
	"betanet"		:		"🎉🎉🎉🎉🎉 BETANET HAS LAUNCHED! https://tezosfoundation.ch/news/tezos-betanet-launch/ 🎉🎉🎉🎉🎉",
	"tothemoon"		:		"ꜩ🚀 -> 🌕 @ 🎉🎉🎉🎉🎉 ANY TIME NOW 🎉🎉🎉🎉🎉",
	"price"			:		price
}

def respond(bot, update):
	global responses
	command = update.effective_message["text"].split("/")[1].split(" ")[0].split("@")[0]
	if command in responses:
		if callable(responses[command]):
			update.message.reply_text(responses[command]())
		else:
			update.message.reply_text(responses[command])

def error(bot, update, error):
    logger.warning("Update '%s' caused error '%s'", update, error)

def main():
    updater = Updater(api_key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler(responses.keys(), respond))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()