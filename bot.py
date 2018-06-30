#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def respond_betanet(bot, update):
	update.message.reply_text("🎉🎉🎉🎉🎉 IT'S SOON GUYS 🎉🎉🎉🎉🎉")

def respond_tothemoon(bot, update):
	update.message.reply_text("ꜩ🚀 -> 🌕 @ 🎉🎉🎉🎉🎉 ANY TIME NOW 🎉🎉🎉🎉🎉")

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater("APIKEY")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("tezosbetanet", respond_betanet))
    dp.add_handler(CommandHandler("tezostothemoon", respond_tothemoon))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()