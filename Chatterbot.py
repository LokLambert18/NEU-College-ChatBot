from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a chatbot named NEU Chatbot
chatbot = ChatBot('NEU Chatbot')

trainer = ListTrainer(chatbot)

trainer.train(['Hi','Hello','How are you?','I am fine and You?','Greate','What are you Doing?','nothing just roaming around.'])

while True:
	input_data = input("You- ")
	response = chatbot.get_response(input_data)
	print("NEUChatbot- ",response)

