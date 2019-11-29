# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils     as utils
import msg       as msg
import database  as database
import commands  as cmds



def main():
    print(msg.log_init)

    cfg = utils.Utils()
    cfg.readConfig()

    db_ = database.db(cfg.dbhost, cfg.dbuser, cfg.dbpass, cfg.db)
    db_.connect()

    cmd = cmds.Commands(cfg, db_)

    # Telegram-bot initialization
    updater    = Updater(token=cfg.token, workers=200, use_context=True)
    dp         = updater.dispatcher

    # Command handlers
    dp.add_handler(CommandHandler('start', cmd.start))
    dp.add_handler(CommandHandler('help', cmd.help))
    dp.add_handler(CommandHandler('addCategory', cmd.rmAddDatabase,
                                  pass_args=True))
    dp.add_handler(CommandHandler('rmCategory', cmd.rmAddDatabase,
                                  pass_args=True))

    dp.add_handler(CommandHandler('addTopic', cmd.rmAddDatabase,
                                  pass_args=True))
    dp.add_handler(CommandHandler('rmTopic', cmd.rmAddDatabase,
                                  pass_args=True))

    dp.add_handler(CommandHandler('addResource', cmd.rmAddDatabase,
                                  pass_args=True))
    dp.add_handler(CommandHandler('rmResource', cmd.rmAddDatabase,
                                  pass_args=True))

    # Message Handlers

    # Start doing things
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
