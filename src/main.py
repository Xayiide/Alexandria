# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils
import msg


def main():
    token = utils.readToken()
    print(msg.bot_init)    



if __name__ == '__main__':
    main()
