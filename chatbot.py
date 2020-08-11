
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('Mi bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")

i=0
while True:
    if i == 0:
        usuario = input('Escriba un mensaje: ')
        i = i+1
    else:
        usuario = input('Responder:')
        
#Respuesta al texto ingrresado por el usuario
    respuesta = chatbot.get_response(usuario)
    print("Bot: "+str(respuesta))
