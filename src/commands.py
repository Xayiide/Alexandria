from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils
import msg
import database


class Commands:
    utils    = None
    database = None
    cmdArgs  = { "addtopic"      : 1,
                 "rmtopic"       : 1,
                 "addcategory"   : 2,
                 "rmcategory"    : 2,
                 "addresource"   : 3,
                 "rmresource"    : 3,
                 "showtopics"    : 0,
                 "showcategories": 1,
                 "showresources" : 2,
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
        # TODO: Add all commands
        update.message.reply_text(msg.infoHelpBot)

    def rmAddDatabase(self, update, context):
        command = update.message.text.split(" ")[0][1:]
        if (self.utils.checkCmd(update,
                                context,
                                self.cmdArgs[command],
                                True) < 0):
            print("Not a valid command")
            return -1 # TODO: Throw Exception

        # TODO: Add Exceptions
        if "topic" in command:
            topicName = context.args[0]
            if "add" in command:
                self.database.rmAddTop(topicName, "add")
            elif "rm" in command:
                self.database.rmAddTop(topicName, "rm")
        elif "category" in command:
            topicName = context.args[0]
            categName = context.args[1]
            if "add" in command:
                self.database.rmAddCat(topicName, categName, "add")
            elif "rm" in command:
                self.database.rmAddCat(topicName, categName, "rm")
        elif "resource" in command:
            topicName = context.args[0]
            categName = context.args[1]
            resURL    = context.args[2]
            if "add" in command:
                self.database.rmAddRes(topicName, categName, resURL, "add")
            elif "rm" in command:
                self.database.rmAddRes(topicName, categName, resURL, "rm")
        else:
            pass # TODO: Raise Exception

    def showTable(self, update, context):
        command = update.message.text.split(" ")[0][1:]
        if (self.utils.checkCmd(update,
                                context,
                                self.cmdArgs[command],
                                False) < 0):
            print("Not a valid command")
            return -1 # TODO: Raise Exception
        if "topics" in command:
            try:
                topics = self.database.getTopics()
                topics = self.utils.parseResources(topics)
                update.message.reply_text(topics)
            except IndexError as e:
                update.message.reply_text(msg.NoSuchTopic)
        elif "categories" in command:
            try:
                topic      = update.message.text.split(" ")[1]

                categories = self.database.getCategories(topic)
                categories = self.utils.parseResources(categories)
                update.message.reply_text(categories)
            except IndexError as e:
                update.message.reply_text(msg.NoSuchCateg)
        elif "resources" in command:
            try:
                topic = update.message.text.split(" ")[1]
                categ = update.message.text.split(" ")[2]

                res   = self.database.getResources(topic, categ)
                res   = self.utils.parseResources(res)
                update.message.reply_text(res)
            except IndexError as e:
                update.message.reply_text(msg.NoSuchTable)
        else:
            pass # TODO: Raise Exception


    def addFromFile(self, update, context):
        pass
