from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new instance of a ChatBot
bot = ChatBot(
    'Bank Support Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Train the bot with the banking corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('./data/banking.yml')

print('Bank Support Bot: Hello! How can I help you today? (Press Ctrl+C to exit)')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input('You: ')

        bot_response = bot.get_response(user_input)

        print(f'Bot: {bot_response}')

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
