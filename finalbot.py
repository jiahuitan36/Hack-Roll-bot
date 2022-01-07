import telebot
from telebot import types
from rp import dictionary

TOKEN = "5084538618:AAEfaN_0LBEFD2WMXEegzxqNHeSFaQN-vLw"
bot = telebot.TeleBot(TOKEN)

H2 = {'A':20, 'B':17.5, 'C':15, 'D':12.5, 'E':10, 'S':5, 'U':0}
H1 = {'A':10, 'B':8.75, 'C':7.5, 'D':6.25, 'E':5, 'S':2.5, 'U':0}


career = {
    "doctor" : 0,
    "software engineer" : 0,
    "data scientist" : 0,
    "engineer" : 0,
    "architect" : 0,
    "entrepreneur" : 0,
    "designer" : 0, 
    "accountant" : 0, 
    "lawyer" : 0,
    "dentist" : 0,
    "teacher" : 0,
    "researcher" : 0 
}

@bot.message_handler(commands=["start"])
def start_command(message):
    keyboard = [[types.InlineKeyboardButton('Calculate RP', callback_data='calc')],
                [types.InlineKeyboardButton('Get courses based on RP', callback_data='course')],
                [types.InlineKeyboardButton('Take a career quiz', callback_data='quiz')]
    ]
    markup = types.InlineKeyboardMarkup(keyboard)

    bot.send_message(
        message.chat.id,
        "What would you like to do today?", reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(message):
    data = message.data
    if 'calc' in data:
        bot.send_message(message.from_user.id, "What are your grades? Send in 3 H2, 3 H1 format. For example, 'AABBAB'. Remember that if you take 4 H2 Subjects, please put the lowest graded H2 subject as the H1 subject.", parse_mode="Markdown")
    if 'quiz' in data:
        keyboard = [[types.InlineKeyboardButton("I'm ready", callback_data='begin')]]
        markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(
            message.from_user.id,
            "Click to start!", reply_markup=markup
        )
    if 'begin' in data:
        keyboard = [[types.InlineKeyboardButton('Empathetic', callback_data='q1a')],
                [types.InlineKeyboardButton('Creative', callback_data='q1b')],
                [types.InlineKeyboardButton('Critical thinker', callback_data='q1c')],
                [types.InlineKeyboardButton('Detail-oriented', callback_data='q1d')],
        ]
        markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(
            message.from_user.id,
            "Q1. What best describes you?", reply_markup=markup
        )
    if 'course' in data:
        bot.send_message(message.from_user.id, "Key in your RP to find courses that you can apply for!", parse_mode="Markdown")

    if 'q1' in data:
        if 'q1a' in data:
            career["doctor"] += 1
            career["dentist"] += 1
            career["lawyer"] += 1

        if 'q1b' in data:
            career["architect"] += 1
            career["designer"] += 1
            career["teacher"] += 1
            career["entrepreneur"] += 1

        if 'q1c' in data:
            career["software engineer"] += 1
            career["researcher"] += 1
            
        if 'q1d' in data:
            career["engineer"] += 1
            career["data scientist"] += 1
            career["accountant"] += 1


        keyboard = [[types.InlineKeyboardButton('Math & Sciences', callback_data='q2a')],
                [types.InlineKeyboardButton('Languages', callback_data='q2b')],
                [types.InlineKeyboardButton('Arts & Humanities', callback_data='q2c')],
        ]
        markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(
            message.from_user.id,
            "Q2. What is/was your favourite subject in school?", reply_markup=markup
        )
    
    if 'q2' in data:
        if 'q2a' in data:
            career["software engineer"] += 1
            career["engineer"] += 1
            career["data scientist"] += 1
            career["accountant"] += 1
            career["researcher"] += 1


        if 'q2b' in data:
            career["doctor"] += 1
            career["dentist"] += 1
            career["lawyer"] += 1

        if 'q2c' in data:
            career["designer"] += 1
            career["teacher"] += 1
            career["entrepreneur"] += 1
            career["architect"] += 1
            
        keyboard = [[types.InlineKeyboardButton('I love working with numbers and statistics', callback_data='q3a')],
                [types.InlineKeyboardButton('I want to help others and positively change the world', callback_data='q3b')],
                [types.InlineKeyboardButton('I love to take on leadership roles and be a supervisor', callback_data='q3c')],
                [types.InlineKeyboardButton('I would prefer to be working with my hands than sitting at a desk', callback_data='q3d')]
        ]
        markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(
            message.from_user.id,
            "Q3. Which statement do you resonate most with?", reply_markup=markup
        )


    if 'q3' in data:
        if 'q3a' in data:
            career["software engineer"] += 1
            career["engineer"] += 1
            career["data scientist"] += 1
            career["accountant"] += 1

        if 'q3b' in data:
            career["doctor"] += 1
            career["dentist"] += 1
            career["architect"] += 1
            career["teacher"] += 1
            career["researcher"] += 1

        if 'q3c' in data:
            career["entrepreneur"] += 1
            career["teacher"] += 1
            career["lawyer"] += 1

        if 'q3d' in data:
            career["doctor"] += 1
            career["dentist"] += 1
            career["engineer"] += 1
            career["researcher"] += 1
            career["designer"] += 1

        keyboard = [[types.InlineKeyboardButton('Food and Agriculture', callback_data='q4a')],
                [types.InlineKeyboardButton('Animals and the Environment', callback_data='q4b')],
                [types.InlineKeyboardButton('Psychology and Marketing', callback_data='q4c')],
                [types.InlineKeyboardButton('Technology and Media', callback_data='q4d')]
        ]
        markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(
            message.from_user.id,
            "Q4. Which of the following topics are you most interested in?", reply_markup=markup
        )

    if 'q4' in data:
        if 'q4a' in data:
            career["engineer"] += 1
            career["researcher"] += 1

        if 'q4b' in data:
            career["dentist"] += 1
            career["researcher"] += 1

        if 'q4c' in data:
            career["entrepreneur"] += 1
            career["teacher"] += 1
            career["lawyer"] += 1
            career["doctor"] += 1
            career["designer"] += 1
            career["accountant"] += 1

        if 'q4d' in data:
            career["software engineer"] += 1
            career["data scientist"] += 1

        keyboard = [[types.InlineKeyboardButton('I like figuring out the answers to mysteries and puzzles', callback_data='q5a')],
                [types.InlineKeyboardButton('I like to express myself and my ideas', callback_data='q5b')],
                [types.InlineKeyboardButton('I like to work in teams', callback_data='q5c')],
                [types.InlineKeyboardButton('I am ambitious and I enjoy setting goals for myself', callback_data='q5d')]
        ]
        markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(
            message.from_user.id,
            "Q5. Which statement do you agree with most?", reply_markup=markup
        )
    if 'q5' in data:
        if 'q5a' in data:
            career["engineer"] += 1
            career["researcher"] += 1

        if 'q5b' in data:
            career["designer"] += 1

        if 'q5c' in data:
            career["researcher"] += 1
            career["teacher"] += 1
            career["engineer"] += 1
            career["accountant"] += 1

        if 'q5d' in data:
            career["entrepreneur"] += 1

        response = "Our results show that you may be a good "
        mx = max(career.values())
        #count keeps track of how many keys have the max value
        count = 0 
        for k, v in career.items():
            if v == mx:
                if count > 0:
                    response += " or " + k
                    count += 1
                else:    
                    response += k
                    count += 1
        response += "!"
        bot.send_message(
            message.from_user.id,
            response
        )


def calc_rp(message):
    grades = message.text
    rp = 0
    for i in range(3):
        grade = grades[i].upper()
        rp += H2[grade]
    for i in range(3,6):
        grade = grades[i].upper()
        rp += H1[grade]
    return rp

def valid_grade(message):
    valid_grade = 'ABCDESU'
    msg = message.text
    if len(msg) < 6 | len(msg) < 6:
        bot.send_message(message.chat.id, "Please input all 6 grades!")
        return False 
    elif msg.isnumeric() or isfloat(msg):
        return False  
    elif len(msg) > 6 and len(msg.split()) == 6:
        bot.send_message(message.chat.id, "Please exclude the space when entering your grades!") 
        return False 
    elif len(msg) != 6:
        bot.send_message(message.chat.id, "Please input your grades in the specified format!") 
        return False 
    else:
        return True


@bot.message_handler(func=valid_grade)
def send_rp(message):
    valid_grade = 'ABCDESU'
    msg = message.text
    flag = True
    for i in range(6):
        if msg[i].upper() not in valid_grade:
            bot.send_message(message.chat.id, "Please input a valid grade for your " + str(i + 1) + "th grade!")  
            flag = False
    if flag:
        RP = calc_rp(message)
        bot.send_message(message.chat.id, "You have " + str(RP) + " Rank Points!")
        start_command(message)

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

@bot.message_handler(func=lambda msg: msg.text.isnumeric() | isfloat(msg.text))
def handle_course_message(message):
    reply = ""
    if float(message.text) >= 66.25 and float(message.text) <= 90:
        reply += "You can choose these courses:" + "\n"
        for key, value in dictionary.items():
            if float(message.text) >= key:
                for course in value:
                    reply += "Course: " + course + ", RP of the 10th percentile: " + str(key) + "RP" + "\n"
    elif float(message.text) > 90:
        reply += "Please enter a valid number for your RP"
    else:
        reply += "Unfortunately, there is no course that matches your RP"
    bot.reply_to(message, reply)

bot.polling(none_stop=True)
