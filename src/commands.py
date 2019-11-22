import utils
import msg

# Commands
def start(update, context):
    """ Send welcome message.
        Let know how to start the bot. """
    # TODO: Make it print what the bot's purpose is and how to start using
    update.message.reply_text(msg.infoStartBot)



def help(update, context):
    """ Send the list of commands used """
    utils.echo(update)
    # TODO: Add all commands
    update.message.reply_text(msg.infoHelpBot)


def addCategory(update, context):
    """ Add a category into the database """
    utl = utils.Utils()
    if not utl.isAdmin(update.message.from_user.id):
        return 1
    # 2. Now the user is an admin. Read the category sent
    try:
        categoryName = context.args[0]
    except (IndexError, ValueError):
        return 2
    
def rmCategory(update, context):
    """ Remove a category from the database """
    utl = utils.Utils()
    if not utl.isAdmin(update.message.from_user.id):
        return 1

    try:
        categoryName = context.args[0]
    except (IndexError, ValueError):
        return 2


def addFromFile(bot, update):
    pass
