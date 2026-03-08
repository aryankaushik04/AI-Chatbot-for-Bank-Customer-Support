from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Bank Support Bot')

# Start by training our bot with the BankSupportBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    './data/banking.yml'
)

# Now let's get responses to some banking questions
print(f"User: How to reset ATM PIN?")
print(f"Bot: {chatbot.get_response('How to reset ATM PIN?')}")

print(f"\nUser: How to open account?")
print(f"Bot: {chatbot.get_response('How to open account?')}")

print(f"\nUser: I lost my credit card.")
print(f"Bot: {chatbot.get_response('I lost my credit card.')}")
