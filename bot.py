import telebot
#import config
import random
 
from telebot import types
token = '1732987041:AAFtI56VaCSf16ddPcmnWYShWL3wOCgjtAo'
bot = telebot.TeleBot(token)


truth_list = ["Какая часть тела у тебя самая привлекательная и сексуальная?", "Какие мужчины и женщины нравятся? Кто из игроков больше всего похож на идеал?", 
"Как выглядело первое свидание и первый поцелуй?", "Встречался (встречалась) ли с замужними женщинами (женатыми мужчинами)?",
"Какое нижнее белье на тебе сейчас? Какое обычно предпочитаешь носить?", "В кого был (была) безответно влюблен (влюблена)?",
"Размер лифчика? Какой был максимальный и минимальный?", "За что до сих пор стыдно?", "Хотел (хотел) бы иметь раба? Кто это был бы из этой комнаты?",
"Как влюбляешь и соблазняешь? Твоя стратегия?", "Кого взял (взяла) на необитаемый остров из присутствующих?", "Встречался (встречался) ли с партнером, с которыми была большая разница в возрасте?",
"Какие отношения были самими ужасными и самыми прекрасными?", "О чем обычно врешь другим людям?", "С кем из присутствующих хочешь пойти на свидание?",
"Сколько зарабатываешь за месяц, а сколько хочешь?", "За какую звезду вышел (вышла) бы замуж без вопросов?", "Тайно влюблялся в половинку своего друга (подружки)?",
"Какая часть тела мужчины (женщины) больше всего заводит?", "Назови 3-5 женщин (мужчин) из ближайшего окружения, кого считаешь красивыми"]
def get_truth():
    global truth
    truth = random.choice(truth_list)
    return truth


dare_list = ["Поцелуй того, кто сидит напротив тебя", "Потанцуй под музыку, которую выбрали другие игроки", "Покатай на себе кого-нибудь или прокатись",
"Крикни на улице: «Кто хочет быть моей любовью?»", "Покажи, как соблазняешь других, на примере одного из игроков",
"Спародируй любого человека из присутствующих", "Встань на стул и прочитай стихотворение", "Сними один элемент одежды", 
"Укуси сам себя за ногу или другого игрока", "Изобрази свой дьявольский смех"]
def get_dare():
    global dare
    dare = random.choice(dare_list)
    return dare


 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Правда")
    item2 = types.KeyboardButton("действие")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для игры в правду или действие.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Правда':
            bot.send_message(message.chat.id, get_truth())
        elif message.text == 'действие':
            bot.send_message(message.chat.id, get_dare())
        else:
            bot.send_message(message.chat.id, 'Такой команды я не знаю')
 
 
# RUN
bot.polling(none_stop=True)