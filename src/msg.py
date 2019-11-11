import utils
import telegram

###############
# Bot Messages
###############
infoStartBot = """ Start message info """






###############
# Bot Utilities
###############

#                             #
# Bot initialization message  #
#                             #
bot_init = "[+] Bot initialized"




#      #
# echo #
#      #
def echo(update):
    chat_id = update.message.chat_id
    name    = update.message.from_user.first_name
    msg     = update.message.text

    if utils.hasNick(update):
        nick = update.message.from_user.username
        print("\n\nMessage from chat: " + str(chat_id) + " [" + name + "] @" +
               nick + "\n\t> " + str(msg))
    else:
        print("\n\nMessage from chat: " + str(chat_id) + " [" + name +
              "] NONICK" + "\n\t> " + str(msg))
