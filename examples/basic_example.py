from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Bank Support Bot
chatbot = ChatBot('Bank Support Bot')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, how can I help you today?",
    "I want to check my account balance.",
    "Sure, please provide your account number.",
    "123456789",
    "Your current balance is $1,250.45."
])

# Get a response to the input text 'I want to check my account balance.'
response = chatbot.get_response('I want to check my account balance.')

print(response)
