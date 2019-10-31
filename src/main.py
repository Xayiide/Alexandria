# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils
import msg


def main():
    token = utils.readToken()
    
