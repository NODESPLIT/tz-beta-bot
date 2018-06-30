#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

api_key = "APIKEY"
responses = {
	"tezosbetanet"		:	"🎉🎉🎉🎉🎉 BETANET WILL BE TODAY! 🎉🎉🎉🎉🎉",
	"tezostothemoon"	:	"ꜩ🚀 -> 🌕 @ 🎉🎉🎉🎉🎉 ANY TIME NOW 🎉🎉🎉🎉🎉"
}

def respond(bot, update):
	command = update.effective_message['text'].split('/')[1].split(' ')[0].split('@')[0]
	if command in responses:
		update.message.reply_text(responses[command])

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater(api_key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler(responses.keys(), respond))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()