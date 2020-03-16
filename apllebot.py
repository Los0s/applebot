
# -*- coding: utf-8 -*-
import telebot
import random
from telebot import types
import shop
import config
import stikerlist
import applehistory
import requests
from bs4 import BeautifulSoup as BS
import re
from telebot import apihelper
apihelper.proxy = {'http':'http://139.59.109.156:3128'}
bot = telebot.TeleBot(config.token)





@bot.message_handler(commands=['start']) #функцыя команды /start
def send_welcome(message):
	bot.send_sticker(message.chat.id, stikerlist.stickerone)
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
	buttonone = types.KeyboardButton('История📓')
	buttontwo = types.KeyboardButton('Магазин🛒')
	keyboard.add(buttonone, buttontwo)
	bot.send_message(message.chat.id, 'Добро пожаловать ' + message.from_user.first_name + ', это бот посвященный компании apple', reply_markup = keyboard)





@bot.message_handler(content_types=['text'], regexp = 'На прошлую клавиатуру')
def back(message):
	shop.shopkeyboard(message)



@bot.message_handler(content_types=['text'], regexp = 'В каком году была создана apple?')
def when(message):
	applehistory.whatyear(message)


@bot.message_handler(content_types=['text'], regexp='Кто создатель?')
def who(message):
	applehistory.whocreator(message)


@bot.message_handler(content_types=['text'], regexp = 'Что такое apple?')
def what(message):
	applehistory.whatisapple(message)

@bot.message_handler(content_types=['text'], regexp = 'Apple iPhone Xs 64GB')
def appleobj1(message):
	shop.Iphon(message)


@bot.message_handler(content_types = ['text'], regexp = 'Apple III')
def a3(message):
	applehistory.apple3(message)



@bot.message_handler(content_types = ['text'], regexp = 'Apple II')
def a2(message):
	applehistory.apple2(message)



@bot.message_handler(content_types=['text'], regexp = 'Apple I')
def a1(message):
	applehistory.apple1(message)


@bot.message_handler(content_types=['text'], regexp = 'Стивен Возник')
def voz(message):
	applehistory.voznik(message)




@bot.message_handler(content_types=['text'], regexp = 'Планшет iPad')
def his_iPad(message):
	applehistory.hispad(message)



@bot.message_handler(content_types=['text'], regexp = 'Плеер iPod')
def ipod(message):
	applehistory.ipod(message)


@bot.message_handler(content_types=['text'], regexp = 'Мобильный телефон iPhone')
def iphon(message):
	applehistory.iphon(message)













@bot.message_handler(content_types=['text'], regexp='Мобильные телефоны')
def iph(message):
	shop.Iphon(message)

@bot.message_handler(content_types=['text'], regexp='Ноутбуки')
def lap(message):
	shop.laptop(message)

@bot.message_handler(content_types=['text'], regexp='Планшеты')
def plan(message):
	shop.ipad(message)


@bot.message_handler(content_types=['text'], regexp='ipad')
def ipad(message):
	shop.appleipad(message)


@bot.message_handler(content_types=['text'], regexp='Iphone')
def iphXs64GB(message):
	shop.IPhonxs(message)


@bot.message_handler(content_types=['text'], regexp='MacBook')
def MacBook_Retina_128Gb(message):
	shop.MacBook_Retina(message)


@bot.message_handler(content_types=['text'], regexp = 'Назад')
def back(message):
	bot.send_sticker(message.chat.id, stikerlist.stickerone)
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
	buttonone = types.KeyboardButton('История📓')
	buttontwo = types.KeyboardButton('Магазин🛒')
	keyboard.add(buttonone, buttontwo)
	bot.send_message(message.chat.id, 'Вы попали на первую клавиатуру', reply_markup = keyboard)
















	



@bot.message_handler(content_types=['sticker'])
def sticker(message):
	stikerlist.sti(message)



@bot.message_handler(content_types=['text']) 
def magazinandshop(message):
	if message.text == 'Магазин🛒': # Функцыя кнопки Магазин🛒
		shop.shopkeyboard(message)
		

	if message.text == 'История📓': # Функцыя кнопки История📓
		keyboardtwo = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
		hisbuttonone = types.KeyboardButton('Кто создатель?')
		hisbuttontwo = types.KeyboardButton('В каком году была создана apple?')
		hisbuttonthree = types.KeyboardButton('Что такое apple?')
		hisbuttonfore = types.KeyboardButton('Apple I') 
		hisbuttonfive = types.KeyboardButton('Apple II')
		hisbuttonsix = types.KeyboardButton('Apple III')
		hisbuttonseven = types.KeyboardButton('Стивен Возник')
		hisbuttoneight = types.KeyboardButton('Планшет iPad')
		hisbutton_nine = types.KeyboardButton('Плеер iPod')
		hisbuttonten = types.KeyboardButton('Мобильный телефон iPhone')
		back = types.KeyboardButton('Назад') 
		keyboardtwo.add(hisbuttonthree, hisbuttonone, hisbuttontwo, hisbuttonfore, hisbuttonfive, hisbuttonsix, hisbuttonseven, hisbuttoneight, hisbutton_nine, hisbuttonten, back)
		bot.send_sticker(message.chat.id, stikerlist.stickerthree, reply_markup = keyboardtwo)
		










	
	





































































bot.polling()