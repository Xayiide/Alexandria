# import telegram # update
import configparser
import telegram

def readConfig():
    ret_   = {}
    config = configparser.ConfigParser()
    config.read('../config.cfg')

    ret_["token"]  = config['BOT']['TOKEN']
    ret_["dbhost"] = config['DATABASE']['host']
    ret_["dbuser"] = config['DATABASE']['user']
    ret_["dbpass"] = config['DATABASE']['pass']
    ret_["db"]     = config['DATABASE']['db']

    return ret_

def hasNick(update):
    if update.message.from_user.username != None:
        return True
    return False
