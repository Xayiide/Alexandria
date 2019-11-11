import configparser

def readConfig():
    ret_   = {}
    config = configparser.ConfigParser()
    config.read('../config.cfg')

    ret_["token"]  = config['BOT']['TOKEN']
    ret_["dbuser"] = config['DATABASE']['user']
    ret_["dbpass"] = config['DATABASE']['pass']

    return ret_
