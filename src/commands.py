from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import utils
import msg
import database


class Commands:
    utils    = None
    database = None

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


    def addCategory(self, update, context):
        """ Add a category into the database
            /addCategory [catName] [topicName] """
        if not self.utils.isAdmin(update.message.from_user.id):
            return 1
        if len(context.args) != 2:
            # TODO: mandar mensaje de error y salir
            print("[!!] Formato incorrecto - addCategory")
            return 1
        try:
            categoryName = context.args[0]
            topicName    = context.args[1]
            self.database.addCatToTopic(categoryName, topicName)
        except (IndexError, ValueError):
            return 2

    def rmCategory(self, update, context):
        """ Remove a category from the database
            /rmCategory [catName] [topicName] """
        if not self.utils.isAdmin(update.message.from_user.id):
            return 1
        if len(context.args) != 2:
            # TODO: mandar mensaje de error y salir
            print("[!!] Formato incorrecto - rmCategory")
            return 1
        try:
            categoryName = context.args[0]
            topicName    = context.args[1]
            self.database.rmCatFromTopic(categoryName, topicName)
        except (IndexError, ValueError):
            return 2


    def addTopic(self, update, context):
        """ Add a topic to the database
            /addTopic [topicName] """
        if not self.utils.isAdmin(update.message.from_user.id):
            return 1
        if (len(context.args) != 1):
            print("[!!] Formato incorrecto - addTopic")
            return 1
        try:
            topicName = context.args[0]
            self.database.addTopic(topicName)
        except Exception as e:
            return 2

    def rmTopic(self, update, context):
        """ rm a topic from the DATABASE
            /rmTopic [topicName] """
        if not self.utils.isAdmin(update.message.from_user.id):
            return 1
        if (len(context.args) != 1):
            print("[!!] Formato incorrecto - rmTopic")
            return 1
        try:
            topicName = context.args[0]
            self.database.rmTopic(topicName)
        except Exception as e:
            return 2


    def addFromFile(self, update, context):
        pass
