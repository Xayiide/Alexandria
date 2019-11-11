# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils
import msg
import database

# Commands
def start(update, context):
    """ Send welcome message """
    msg.echo(update)
    context.bot.send_message(chat_id=update.effective_chat.id,
                                text=msg.infoStartBot)



def help(bot, update):
    pass

def addFromFile(bot, update):
    pass


def unknown(bot, update):
    pass




def main():
    print(msg.bot_init)

    cfg = utils.readConfig()
    db_ = database.db(cfg['dbhost'], cfg['dbuser'],
                      cfg['dbpass'], cfg['db'])


    # Telegram-bot initialization
    updater    = Updater(token=cfg['token'], workers=200, use_context=True)
    dp         = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler('start', start))

    # Message Handlers


    # Start doing things
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
