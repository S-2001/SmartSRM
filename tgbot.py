import telebot
import datetime

# Replace YOUR_TOKEN_HERE with the token provided by BotFather
bot = telebot.TeleBot("6114895069:AAFI1U6Kgrd0BWdWq2nYXJfpstBYUPzdk_s")

# Define a function to handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    # Send a welcome message with a photo
    photo = open('welcome.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, "Hey! Welcome to SmartSRM! One stop solution to access all the materials ")
    bot.send_message(message.chat.id, "Type /sem6 to access all materials ")

# Define a function to handle the /help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Here are some commands you can use:\n/start - start the bot\n/help - get help\n/sem6-to access the materials ")



@bot.message_handler(commands=['sem6'])
def help(message):
    bot.send_message(message.chat.id, "List of the subjects:\n/dbms or /18CSC303J - Database Management Systems\n /cd or /18CSC304J - Compiler Design\n /ai or /18CSC305J - Artificial Intelligence\n /wsn or /18CSE451T - Wireless Sensor Networks\n /ns or /18CSE354T - Network Security \n /fooe or /18ECO107T - Fibre Optics and Opto Electronics ")
    
@bot.message_handler(commands=['wsn'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1b834vHQtR1PLaEf-lo6Vdv6Exqesjr3u?usp=share_link")

@bot.message_handler(commands=['18CSE451T'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1b834vHQtR1PLaEf-lo6Vdv6Exqesjr3u?usp=share_link")
@bot.message_handler(commands=['dbms'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1PV0laW9mYTVo28H8M_eZ3NW3fYDipVfC?usp=share_link")
@bot.message_handler(commands=['18CSC303J'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1PV0laW9mYTVo28H8M_eZ3NW3fYDipVfC?usp=share_link")
@bot.message_handler(commands=['cd'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1zR_hA3uTu5xfzdPU3tMa35NDOyQ4ysCn?usp=share_link")
@bot.message_handler(commands=['18CSC304J'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1zR_hA3uTu5xfzdPU3tMa35NDOyQ4ysCn?usp=share_link")
@bot.message_handler(commands=['ai'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1UWdFQME3PW44dRNLXHK2pLSdud0V3LvX?usp=share_link")
@bot.message_handler(commands=['18CSC305J'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1UWdFQME3PW44dRNLXHK2pLSdud0V3LvX?usp=share_link")
@bot.message_handler(commands=['ns'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1CJ6a4SeCytrRjpwOFRFeimO34aBswnHQ?usp=share_link")
@bot.message_handler(commands=['18CSE354T'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1CJ6a4SeCytrRjpwOFRFeimO34aBswnHQ?usp=share_link")
@bot.message_handler(commands=['fooe'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1BSwWNO18vpNzSK93RLDfrWVBmtQEiFSd?usp=share_link")
@bot.message_handler(commands=['18ECO107T'])
def help(message):
    bot.send_message(message.chat.id, "https://drive.google.com/drive/folders/1BSwWNO18vpNzSK93RLDfrWVBmtQEiFSd?usp=share_link")

# Define a function to handle unknown commands
@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.send_message(message.chat.id, "Sorry, I don't understand that command. Please use /help to see a list of available commands.")

# Start the bot and listen for incoming messages
bot.polling()
