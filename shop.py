# -*- coding: utf-8 -*-
import telebot
import config
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
import re
import stikerlist
from telebot import apihelper









RozetkaButtonText = 'Посмотреть в Rozetka'
FokstrotButtonText = 'Посмотреть в Фокстрот'
buyButtonText = 'Посмотреть в Buy.ua'
moyotextbutton = 'Посмотреть в MOYO'
fixerbuttontext = 'Посмотреть в Fixer'
brainbuttontext = 'Посмотреть в Brain'

modeltext = 'Выберете нужную модель'

bot = telebot.TeleBot(config.token)







def shopkeyboard(message):
	keyboardshop = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
	shopbuttonone = types.KeyboardButton('Мобильные телефоны')
	shopbuttontwo = types.KeyboardButton('Ноутбуки')
	shopbuttonthree = types.KeyboardButton('Планшеты')
	back = types.KeyboardButton('Назад') 
	keyboardshop.add(shopbuttonone, shopbuttontwo, shopbuttonthree, back)
	bot.send_message(message.chat.id, 'Выберете категорию', reply_markup = keyboardshop)









def ipad(message):
	ipadkeyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
	ipadbuttonone = types.KeyboardButton('ipad 7 10.2"') 
	back = types.KeyboardButton('На прошлую клавиатуру') 
	ipadkeyboard.add(ipadbuttonone, back)
	bot.send_message(message.chat.id, modeltext, reply_markup = ipadkeyboard)




def Iphon(message):
	bot.send_sticker(message.chat.id, stikerlist.stickerfive)
	mobilekeyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
	mibilebuttonone = types.KeyboardButton('Iphone Xs 64GB') 
	back = types.KeyboardButton('На прошлую клавиатуру') 
	mobilekeyboard.add(mibilebuttonone, back)
	bot.send_message(message.chat.id, modeltext, reply_markup = mobilekeyboard)
	
	
def laptop(message):
	bot.send_sticker(message.chat.id, stikerlist.stickersix)
	laptopkeyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
	lapbuttonone = types.KeyboardButton('MacBook Pro 13" Retina 128Gb')
	back = types.KeyboardButton('На прошлую клавиатуру')
	laptopkeyboard.add(lapbuttonone, back)
	bot.send_message(message.chat.id, modeltext, reply_markup=laptopkeyboard)


def IPhonxs(message): 
	if message.text == 'Iphone Xs 64GB':
		try:
			RozetkaAppleiPhoneXs64GB = requests.get('https://rozetka.com.ua/apple_iphone_xs_64gb_space_gray/p172930640/')
			RozetkaAppleiPhoneXs64GB = (RozetkaAppleiPhoneXs64GB.text)
			RozetkaAppleiPhoneXs64GB = BS(RozetkaAppleiPhoneXs64GB, 'html.parser')
			RozetkaAppleiPhoneXs64GB = RozetkaAppleiPhoneXs64GB.find('p',{'class': 'product-prices__big product-prices__big_color_red'})
			RozetkaAppleiPhoneXs64GB = list(RozetkaAppleiPhoneXs64GB)
			RozetkaAppleiPhoneXs64GB = RozetkaAppleiPhoneXs64GB[0]
			RozetkaAppleiPhoneXs64GBkeyboard = types.InlineKeyboardMarkup()
			RozetkaAppleiPhoneXs64GBbutton = types.InlineKeyboardButton(text = RozetkaButtonText, url='https://rozetka.com.ua/apple_iphone_xs_64gb_space_gray/p172930640/')
			RozetkaAppleiPhoneXs64GBkeyboard.add(RozetkaAppleiPhoneXs64GBbutton)
		



			FokstrotAppleiPhoneXs64GB = requests.get('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_apple_iphone-xs-64gb-silver.html?utm_medium=cpc&utm_source=hotline&utm_campaign=DIG-mobilephohe&utm_term=mobilnye_telefony_apple_iphone-xs-64gb-silver&utm_content=6423074')
			FokstrotAppleiPhoneXs64GB = (FokstrotAppleiPhoneXs64GB.text)
			FokstrotAppleiPhoneXs64GB = BS(FokstrotAppleiPhoneXs64GB, 'html.parser')	 
			FokstrotAppleiPhoneXs64GB =  FokstrotAppleiPhoneXs64GB.find('div', {'class': "card-price"})
			FokstrotAppleiPhoneXs64GB = list(FokstrotAppleiPhoneXs64GB)
			FokstrotAppleiPhoneXs64GB = FokstrotAppleiPhoneXs64GB[0]
			FokstrotPhoneXs64GBkeyboard = types.InlineKeyboardMarkup()
			FokstrotPhoneXs64GBbutton =  types.InlineKeyboardButton(text = FokstrotButtonText, url = 'https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_apple_iphone-xs-64gb-silver.html?utm_medium=cpc&utm_source=hotline&utm_campaign=DIG-mobilephohe&utm_term=mobilnye_telefony_apple_iphone-xs-64gb-silver&utm_content=6423074')
			FokstrotPhoneXs64GBkeyboard.add(FokstrotPhoneXs64GBbutton)


		


			buyAppleiPhoneXs64GB = requests.get('http://www.buy.ua/shop/1400215/1400417/1712920.html')
			buyAppleiPhoneXs64GB = (buyAppleiPhoneXs64GB.text)
			buyAppleiPhoneXs64GB = BS(buyAppleiPhoneXs64GB, 'html.parser')
			buyAppleiPhoneXs64GB = buyAppleiPhoneXs64GB.find('div', {'class':"price-info"})
			buyAppleiPhoneXs64GB = str(buyAppleiPhoneXs64GB)
			buyAppleiPhoneXs64GB = list(buyAppleiPhoneXs64GB)
			buyPhoneXs64GBkeyboard = types.InlineKeyboardMarkup()
			buyPhoneXs64GBbutton = types.InlineKeyboardButton(text = buyButtonText, url = 'http://www.buy.ua/shop/1400215/1400417/1712920.html')
			buyPhoneXs64GBkeyboard.add(buyPhoneXs64GBbutton)
			
			
			bot.send_message(message.chat.id, 'Rozetka - ' + RozetkaAppleiPhoneXs64GB + ' ₴', reply_markup = RozetkaAppleiPhoneXs64GBkeyboard)
			bot.send_message(message.chat.id, 'Фокстрот - ' + FokstrotAppleiPhoneXs64GB + ' ₴', reply_markup = FokstrotPhoneXs64GBkeyboard)
			bot.send_message(message.chat.id, 'Buy.ua - ' + str(buyAppleiPhoneXs64GB[55]) + str(buyAppleiPhoneXs64GB[56]) + ' ' + str(buyAppleiPhoneXs64GB[57]) + str(buyAppleiPhoneXs64GB[58]) + str(buyAppleiPhoneXs64GB[59]) + ' ₴', reply_markup = buyPhoneXs64GBkeyboard)
	
		except:
			bot.send_message(message.chat.id, 'Произошла ошибка')
	


def MacBook_Retina(message):
	if message.text == 'MacBook Pro 13" Retina 128Gb':
		try:	
			RozetkaRetina = requests.get('https://rozetka.com.ua/apple_macbook_pro_13_retina_128gb_muhq2_silver/p191234632/')
			RozetkaRetina = RozetkaRetina.text
			RozetkaRetina = BS(RozetkaRetina, 'html.parser')
			RozetkaRetina = RozetkaRetina.find('div', {'class':"product-prices__inner"})
			RozetkaRetina = str(RozetkaRetina)
			RozetkaRetina = list(RozetkaRetina)
			
			RozetkaRetinakeyboard = types.InlineKeyboardMarkup()
			RozetkaRetinabutton = types.InlineKeyboardButton(text = RozetkaButtonText, url = 'https://rozetka.com.ua/apple_macbook_pro_13_retina_128gb_muhq2_silver/p191234632/')
			RozetkaRetinakeyboard.add(RozetkaRetinabutton)
			
			MoyoRetina = requests.get('https://www.moyo.ua/noutbuk_apple_a1708_macbook_pro_retina_13_mpxr2ua_a_silver/361588.html')
			MoyoRetina = MoyoRetina.text
			MoyoRetina = BS(MoyoRetina, 'html.parser')
			MoyoRetina = MoyoRetina.find('span', {'class':"actual-price-amount"})
			MoyoRetina = list(MoyoRetina)
			MoyoRetina = MoyoRetina[0]
			MoyoRetinakeyboard = types.InlineKeyboardMarkup()
			MoyoRetinabutton = types.InlineKeyboardButton(text = moyotextbutton, url = 'https://www.moyo.ua/noutbuk_apple_a1708_macbook_pro_retina_13_mpxr2ua_a_silver/361588.html')
			MoyoRetinakeyboard.add(MoyoRetinabutton)
			
			
			
			
			
			
			
			
			
			
			
			bot.send_message(message.chat.id, 'Rozetka - ' + RozetkaRetina[105] + RozetkaRetina[106] + ' ' + RozetkaRetina[108] + RozetkaRetina[109] + RozetkaRetina[110] + ' ₴', reply_markup=RozetkaRetinakeyboard)
			bot.send_message(message.chat.id, 'Moyo - ' + MoyoRetina + ' ₴', reply_markup=MoyoRetinakeyboard)
		
		
		except:
			bot.send_message(bot.send_message(message.chat.id, 'Произошла ошибка'))

def appleipad(message):
	try:
		if message.text == 'ipad 7 10.2"':
			Rozetkaipad_7 = requests.get('https://rozetka.com.ua/apple-ipad-7-10-2-a2197-wi-fi-32gb-2019-16127127/g22946813/')
			Rozetkaipad_7 = Rozetkaipad_7.text
			Rozetkaipad_7 = BS(Rozetkaipad_7, 'html.parser') 
			Rozetkaipad_7 = Rozetkaipad_7.find('p', {'class':"product-prices__big"})
			Rozetkaipad_7 = list(Rozetkaipad_7)
			Rozetkaipad_7keyboard = types.InlineKeyboardMarkup()
			Rozetkaipad_7button = types.InlineKeyboardButton(text = RozetkaButtonText, url = 'https://rozetka.com.ua/apple-ipad-7-10-2-a2197-wi-fi-32gb-2019-16127127/g22946813/')
			Rozetkaipad_7keyboard.add(Rozetkaipad_7button)
			
			Fixeripad_7 = requests.get('https://fixer.com.ua/pda/apple-a2197-ipad-10.2-wi-fi-32gb-space-grey-mw742rk-a_976052.html')
			Fixeripad_7 = Fixeripad_7.text
			Fixeripad_7 = BS(Fixeripad_7, 'html.parser')
			Fixeripad_7 = Fixeripad_7.find('div', {'class':"pi_price"})
			Fixeripad_7 = str(Fixeripad_7)
			Fixeripad_7 = list(Fixeripad_7)
			Fixeripad_7keyboard = types.InlineKeyboardMarkup()
			Fixeripad_7button = types.InlineKeyboardButton(text = fixerbuttontext, url = 'https://fixer.com.ua/pda/apple-a2197-ipad-10.2-wi-fi-32gb-space-grey-mw742rk-a_976052.html')
			Fixeripad_7keyboard.add(Fixeripad_7button)
			
			
			Brainipad_7 = requests.get('https://brain.com.ua/ukr/Planshet_Apple_A2197_iPad_102_Wi-Fi_32GB_Silver_MW752RK_A-p638525.html')
			Brainipad_7 = Brainipad_7.text
			Brainipad_7 = BS(Brainipad_7, 'html.parser')
			Brainipad_7 = Brainipad_7.find('div', {'class':"br-pr-np"})
			Brainipad_7 = str(Brainipad_7)
			Brainipad_7 = list(Brainipad_7)
			Brainipad_7keyboard = types.InlineKeyboardMarkup()
			Brainipad_7button = types.InlineKeyboardButton(text = brainbuttontext, url = 'https://brain.com.ua/ukr/Planshet_Apple_A2197_iPad_102_Wi-Fi_32GB_Silver_MW752RK_A-p638525.html')
			Brainipad_7keyboard.add(Brainipad_7button)
			
			
			
			bot.send_message(message.chat.id, 'Rozetka - ' + Rozetkaipad_7[0] + ' ₴', reply_markup=Rozetkaipad_7keyboard)
			bot.send_message(message.chat.id , 'Fixer - ' + Fixeripad_7[114] + Fixeripad_7[115] + ' ' + Fixeripad_7[116] + Fixeripad_7[117] + Fixeripad_7[118] + ' ₴', reply_markup=Fixeripad_7keyboard)
			bot.send_message(message.chat.id, 'Brain - ' + Brainipad_7[139] + Brainipad_7[140] + ' ' + Brainipad_7[141] + Brainipad_7[142] + Brainipad_7[143] + ' ₴', reply_markup=Brainipad_7keyboard)

























	except:
		bot.send_message(message.chat.id, 'Произошла ошибка')













































