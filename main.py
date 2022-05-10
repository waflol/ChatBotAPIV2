from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import logging
import warnings
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_random_response
from random import choice
from chatterbot.filters import get_recent_repeated_responses
warnings.filterwarnings("ignore")

'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

def initialize_Corpus(bot):
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train(
        'chatterbot.corpus.english'
    )

def User_teach(bot,statements):
    trainer = ListTrainer(bot)
    trainer.train(statements)
    return "Done!"


def get_response(bot,msg):
    bot_response = bot.get_response(msg)
    return bot_response

"""
DEMO
"""
# Init
bot = ChatBot(
    'Example Bot',
    filters=[get_recent_repeated_responses],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        },
        {
            'import_path':'chatterbot.logic.MathematicalEvaluation',
        
        },
        {
            'import_path':'chatterbot.logic.TimeLogicAdapter',
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.9
        },
    ],
    database_uri='sqlite:///database.sqlite3'
)

initialize_Corpus(bot)

# Teach by user
statements = ["Where is the location of UTE", "it locates on 1 Vo Van Ngan street"]
User_teach(bot,statements)


# Chat
while True:
    try:
        user_input = str(input())

        bot_response = bot.get_response(user_input)

        print(bot_response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

"""
END DEMO
"""






