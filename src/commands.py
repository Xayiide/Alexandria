from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils
import msg
import database


class Commands:
    utils    = None
    database = None
    cmdArgs  = { "addTopic"   : 1,
                 "rmTopic"    : 1,
                 "addCategory": 2,
                 "rmCategory" : 2,
                 "addResource": 3,
                 "rmResource" : 3,
               }

    def __init__(self, utils, database):
        self.utils    = utils
        self.database = database

    def start(self, update, context):
        """ Send welcome message.
            Let know how to start the bot. """
        print("Here we go starting")
        update.message.reply_text(msg.infoStartBot)

    def help(self, update, context):
        """ Send the list of commands used """
        utils.echo(update)
        # TODO: Add all commands
        update.message.reply_text(msg.infoHelpBot)

    def rmAddDatabase(self, update, context):
        command = update.message.text.split(" ")[0][1:]
        print("Received command: " + command)
        if (self.utils.checkCmd(update, context, self.cmdArgs[command]) < 0):
            print("Not a valid command")
            return -1 # TODO: Throw Exception

        # TODO: Add Exceptions
        if "Topic" in command:
            print("Topic")
            topicName = context.args[0]
            if "add" in command:
                print("Adding topic: " + topicName)
                self.database.addTopic(topicName)
            elif "rm" in command:
                print("Deleting topic: " + topicName)
                self.database.rmTopic(topicName)
        elif "Category" in command:
            print("Category")
            topicName = context.args[0]
            categName = context.args[1]
            if "add" in command:
                print("Adding " + categName + "to topic " + topicName)
                self.database.addCatToTopic(topicName, categName)
            elif "rm" in command:
                print("Rmving " + categName + "from topic " + topicName)
                self.database.rmCatFromTopic(topicName, categName)
        elif "Resource" in command:
            print("Resource")
            topicName = context.args[0]
            categName = context.args[1]
            resURL    = context.args[2]
            if "add" in command:
                print("Adding url: " + resURL + "to: " + topicName + categName)
                self.database.addResource(topicName, categName, resURL)
            elif "rm" in command:
                print("Rmving url: " + resURL + "from: " + topicName + categName)
                self.database.rmResource(topicName, categName, resURL)

    def addFromFile(self, update, context):
        pass
