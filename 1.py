import sys
import time
import random
import datetime
import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Got command: %s' % command)
    if command == '/start':
        bot.sendMessage(chat_id, text = '''
halo, 
silakan pilih:
1. /pantau
2. /deteksi
''')
    elif command == '/pantau':
        bot.sendMessage(chat_id, text = '''sedang memantau..
foto akan segera dikirim...
/kembali''')
    elif command == '/deteksi':
        bot.sendMessage(chat_id, text = '''sedang mendeteksi, foto akan dikirim ke email ketika terdapat penyusup
/kembali''')
    elif command == '/kembali':
        bot.sendMessage(chat_id, text = '''halo,
silakan pilih:
1. /pantau
2. /deteksi
''')
bot = telepot.Bot('946120811:AAG6n3yuvLkUSV8qfXkwi1tWC2U1BWgZdiQ')
bot.message_loop(handle)
while 1:
    time.sleep(10)