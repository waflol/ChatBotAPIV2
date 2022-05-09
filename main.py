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

bot = ChatBot(
    'Example Bot',
    filters=[get_recent_repeated_responses],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.remove_special_character'
    ],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.95
        },
    ],
    database_uri='sqlite:///database.sqlite3'
)
#Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    'chatterbot.corpus.english.botprofile'
)

# trainer = ListTrainer(bot)
# trainer.train(
#     [
#         "What do you like?",
#         "I am interested in all kinds of things. We can talk about anything!"
#     ])

# trainer.train(
#     [
#         "What fruit do you like?",
#         "I like banana"
#     ])
# trainer.train(
#     [
#         "What are food interests?",
#         "I like banana"
#     ])

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = str(input())

        bot_response = bot.get_response(user_input)

        print(bot_response)
        

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break


