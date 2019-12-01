# import telegram # update
import configparser
import telegram


class Utils:

    admins = []
    token  = ""
    dbhost = ""
    dbuser = ""
    dbpass = ""
    db     = ""

    def __init__(self):
        pass

    def readConfig(self):
        config = configparser.ConfigParser()
        config.read('../config.cfg')

        self.token  = config['BOT']['token']
        self.dbhost = config['DATABASE']['host']
        self.dbuser = config['DATABASE']['user']
        self.dbpass = config['DATABASE']['pass']
        self.db     = config['DATABASE']['db']

        for admin in config['BOT']['admins'].split(','):
            self.admins.append(int(admin))

    def hasNick(self, update):
        if update.message.from_user.username != None:
            return True
        return False

    def echo(self, update): # TODO: Write to log instead
        chat_id = update.message.chat_id
        name    = update.message.from_user.first_name
        msg     = update.message.text

        if self.hasNick(update):
            nick = update.message.from_user.username
            print("\n\nMessage from chat: " + str(chat_id) + " [" + name +
                    "] @" + nick + "\n\t> " + str(msg))
        else:
            print("\n\nMessage from chat: " + str(chat_id) + " [" + name +
                    "] NONICK" + "\n\t> " + str(msg))

    def isAdmin(self, user):
        return user in self.admins

    def checkCmd(self, update, context, numArgs, needsAdmin):
        if not self.isAdmin(update.message.from_user.id) and needsAdmin:
            print("Not an admin!")
            return -1 # TODO: Throw exception
        if len(context.args) != numArgs:
            print("Not appropiate format for command")
            return -2 # TODO: Throw exception
        return 0

    def parseResources(self, resources):
        count = 1
        text  = ""
        for item in resources:
            count_str = str(count)
            res_url   = item[1]
            text += (count_str + '. ' + res_url + '\n')
            count += 1
        return text
