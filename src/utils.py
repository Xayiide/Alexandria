# import telegram # update
import configparser
import telegram


class Utils:

    def __init__(self):
        pass
    
    def readConfig(self, path):
        pass
    
    def hasNick(self, update):
        pass

    def echo(self, update):
        pass



def readConfig():
    ret_   = {}
    config = configparser.ConfigParser()
    config.read('../config.cfg')

    ret_["token"]  = config['BOT']['token']
    ret_["dbhost"] = config['DATABASE']['host']
    ret_["dbuser"] = config['DATABASE']['user']
    ret_["dbpass"] = config['DATABASE']['pass']
    ret_["db"]     = config['DATABASE']['db']

    ret["admins"] = []
    for i in config['BOT']['admins'].split(','):
        ret["admins"].append(int(i))

    return ret_

def hasNick(update):
    if update.message.from_user.username != None:
        return True
    return False

# Print the update in the bot's console.
# TODO: Write to log instead
#
def echo(update):
    chat_id = update.message.chat_id
    name    = update.message.from_user.first_name
    msg     = update.message.text

    if hasNick(update):
        nick = update.message.from_user.username
        print("\n\nMessage from chat: " + str(chat_id) + " [" + name + "] @" +
               nick + "\n\t> " + str(msg))
    else:
        print("\n\nMessage from chat: " + str(chat_id) + " [" + name +
              "] NONICK" + "\n\t> " + str(msg))
