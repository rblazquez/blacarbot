import os
import aiml
import telebot
from telebot import types

#t.me/blacarbot
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXX' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN) #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN

kernel = aiml.Kernel()

def listener(messages): # Con esto, estamos definiendo una funcion llamada 'listener', que recibe como parametro un dato llamado 'messages'.
	for message in messages: # Por cada dato 'm' en el dato 'messages'
		cid = message.chat.id # Almacenaremos el ID de la conversacion.
		print "[" + str(cid) + "]: " + message.text # Y haremos que imprima algo parecido a esto [52033876]: /start
 
def extract_unique_code(text):
	# Extracts the unique_code from the sent /start command.
	return text.split()[1] if len(text.split()) > 1 else None
	
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	unique_code = extract_unique_code(message.text)
	cid = message.chat.id # Guardamos el ID de la conversacion para poder responder.
	if unique_code == "blacarbot":
		print  "[Hola]"
		bot.reply_to(message, "Hello!, I am blacarbot.")
		bot.reply_to(message, "Ask me anything ... let's chat!")	
	else:
		bot.reply_to(message, "[-] Password incorrecto")	
		
@bot.message_handler(func=lambda message: True)
def talk(message):
	bot_response = kernel.respond(message.text)
	bot.reply_to(message, bot_response)		
	
#Prepare the party	
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

#Starts the party	
bot.polling()
