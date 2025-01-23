import telebot
import urllib
import os
import instaloader
import re

key = ""
bot = telebot.TeleBot(key)
print("A iniciar....")
bot.get_updates()

buttonMenu = telebot.types.InlineKeyboardButton(text= "Menu", callback_data="/menu")
buttonHelp = telebot.types.InlineKeyboardButton(text= "Help", callback_data="/help")
keyboard1 = telebot.types.InlineKeyboardMarkup().add(buttonMenu, buttonHelp)
buttonInstagram = telebot.types.InlineKeyboardButton(text= "Instagram", callback_data="/instagram")
buttonMemes = telebot.types.InlineKeyboardButton(text= "Memes", callback_data="/memes")
keyboardMenu = telebot.types.InlineKeyboardMarkup().add(buttonInstagram, buttonMemes)

def InstagramResponse(msg):
    chat_id = msg.chat.id
    bot.send_message(chat_id, "Envie o link do post de Instagram que quer guardar!!!!!!!!")
    bot.register_next_step_handler(msg, process_step)

def process_step(msg):
    try:
        if("www.instagram.com" not in msg.text):
            bot.send_message(msg.chat.id, "Não posso fazer nada com issooooooo")
            bot.register_next_step_handler(msg, process_step)
            return
        else:   
            username = "trashtalkbot"
            dir_name = "images"
            print("Antes do login")
            L = instaloader.Instaloader(download_comments=False, download_geotags=False, save_metadata=False, download_video_thumbnails=False)
            
            try:
                L.load_session_from_file(username)
                print("a tentar fazer login")
            except Exception as e:
                L.login(username, "Hahahaha1122")
                L.save_session_to_file(username)

            print("Fiz o login")
            regexp = '^(?:.*\/(p|tv)\/)([\d\w\-_]+)'
            post_short_code = re.search(regexp, msg.text).group(2)
            post =  instaloader.Post.from_shortcode(L.context, post_short_code)
            L.download_post(post, dir_name)            
            test = os.listdir(dir_name)
            for item in test:
                if item.endswith(".txt"):
                    os.remove(os.path.join(dir_name, item))

            for filename in os.listdir(dir_name):
                f = os.path.join(dir_name, filename)
                if os.path.isfile(f):
                    if f.endswith(".jpg"):
                        bot.send_photo(chat_id = msg.chat.id,  photo = open(f, 'rb'))
                    elif f.endswith(".mp4"):
                        bot.send_video(chat_id = msg.chat.id,  video = open(f, 'rb'), supports_streaming=True)
            
            for item in test:
                if item.endswith(".jpg") or item.endswith(".mp4"):
                    os.remove(os.path.join(dir_name, item))
            
            
            return

    except Exception as e:
        bot.reply_to(msg, 'oooops')


def MenuResponse(msg):
    bot.send_message(msg.chat.id, "Escolha uma das opções:", reply_markup=keyboardMenu)

def HelpResponse(msg):
    mensagemHelp = """
    Olá, eu sou um bot:
    - /start - Inicia o bot
    - /help - Mostra esta mensagem
    - /menu - Mostra o menu de opções   
    """

    bot.reply_to(msg, mensagemHelp)

@bot.message_handler(commands=['start'])
def startResponse(msg):
    nome = msg.from_user.first_name
    print(msg.chat.id)
    bot.send_message(msg.chat.id, f"Olá {nome}, vamos começar", reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: telebot.types.CallbackQuery):
    if call.data == "/menu":
        MenuResponse(call.message)
    elif call.data == "/help":
        HelpResponse(call.message)
    elif call.data == "/instagram":
        InstagramResponse(call.message)
    elif call.data == "/memes":
        MenuResponse(call.message)

'''
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if("www.instagram.com" in message.text):
        baseplus = "media/?size=l"
        compor = message.text
        sep = '?'
        compor = compor.split(sep, 1)[0]
        final = compor + baseplus
        f = open('out.jpg','wb')
        f.write(urllib.request.urlopen(final).read())
        f.close()
        img = open('out.jpg', 'rb')
        bot.send_photo(chat_id = message.chat.id,  photo = final)
        img.close()
        os.remove("out.jpg")
    else:
        bot.send_message(message.chat.id, "Não posso fazer nada com isso")
'''


'''
baseplus = "media/?size=l"
compor = msg.text
sep = '?'
compor = compor.split(sep, 1)[0]
final = compor + baseplus
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(final).read())
f.close()
img = open('out.jpg', 'rb')
bot.send_photo(chat_id = msg.chat.id,  photo = f)
img.close()
os.remove("out.jpg")
'''

bot.polling()