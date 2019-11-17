import utils


# Commands
def start(update, context):
    """ Send welcome message.
        Let know how to start the bot. """
    utils.echo(update)
    # TODO: Make it print what the bot's purpose is and how to start using it
    update.message.reply_text(msg.infoStartBot)



def help(update, context):
    """ Send the list of commands used """
    utils.echo(update)
    # TODO: Add all commands
    update.message.reply_text(msg.infoHelpBot)


def addFromFile(bot, update):
    pass