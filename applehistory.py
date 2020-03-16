# -*- coding: utf-8 -*-
import telebot
from telebot import types
import config
import stikerlist
from telebot import apihelper

bot = telebot.TeleBot(config.token)

def whocreator(message):
	keyboardthree = types.InlineKeyboardMarkup()
	wikibutton = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/%D0%94%D0%B6%D0%BE%D0%B1%D1%81,_%D0%A1%D1%82%D0%B8%D0%B2')
	keyboardthree.add(wikibutton)
	bot.send_message(message.chat.id, 'Компания основана Стивом Джобсом', reply_markup = keyboardthree)


def whatyear(message):
	keyboardfore = types.InlineKeyboardMarkup()
	wikibuttontwo = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/Apple')
	keyboardfore.add(wikibuttontwo)
	bot.send_message(message.chat.id, 'Продав несколько десятков компьютеров, молодые предприниматели получили финансирование и официально зарегистрировали фирму Apple Computer, Inc. 1 апреля 1976 года', reply_markup = keyboardfore)



def whatisapple(message):
	keyboardfive = types.InlineKeyboardMarkup()
	wikibuttonthree = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/Apple')
	keyboardfive.add(wikibuttonthree)
	bot.send_message(message.chat.id, 'Apple — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, телефонов, программного обеспечения', reply_markup = keyboardfive)
	bot.send_sticker(message.chat.id, stikerlist.stickerfore)

def apple1(message):
	keyboardsix = types.InlineKeyboardMarkup()
	wikibuttonfore = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/Apple_I')
	keyboardsix.add(wikibuttonfore)
	bot.send_message(message.chat.id, 'Apple I — ранний персональный компьютер, первый компьютер Apple Computer, возможно, первый персональный компьютер, продававшийся в полностью собранном виде. Компьютер был разработан Стивом Возняком для личного использования. У друга Возняка Стива Джобса появилась идея продавать его. Apple I стал первым продуктом компании Apple Computer (теперь Apple Inc.), продемонстрированным в апреле 1976 года в «Клубе самодельных компьютеров» в Пало-Альто, Калифорния.', reply_markup = keyboardsix)


def apple2(message):
	keyboardseven = types.InlineKeyboardMarkup()
	wikibuttonfive = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/Apple_II')
	keyboardseven.add(wikibuttonfive)
	bot.send_message(message.chat.id, 'Apple II — первый персональный компьютер, серийно выпускавшийся компанией Apple Computer. Apple II стал прямым наследником любительского компьютера Apple I, никогда не производившегося в больших количествах, но уже содержавшего многие идеи, которые обеспечили успех Apple II', reply_markup = keyboardseven)



def apple3(message):
	keyboardeight = types.InlineKeyboardMarkup()
	wikibuttonsix = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/Apple_III')
	keyboardeight.add(wikibuttonsix)
	bot.send_message(message.chat.id, 'При разработке Apple III впервые во главу угла ставились маркетинговые задачи. Работа над этой моделью началась в конце 1978 года под непосредственным руководством доктора Уэнделла Сандера, так как Возняк курировал направление Apple II, разрабатывая различные его модификации, и не считал нужным проектировать что-то иное, поскольку идеальный компьютер, по его мнению, уже был создан[1]. Проект Apple III фактически был отдан на откуп маркетинговому отделу и лично Стиву Джобсу. Apple III являлся кардинальной переработкой компьютера Возняка, ориентированной на бизнес, а Apple II предполагалось перепозиционировать как младшую модель, любительский компьютер для дома.', reply_markup = keyboardeight)



def voznik(message):
	keyboardnine = types.InlineKeyboardMarkup()
	wikibuttonseven = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B7%D0%BD%D1%8F%D0%BA,_%D0%A1%D1%82%D0%B8%D0%B2')
	keyboardnine.add(wikibuttonseven)
	bot.send_message(message.chat.id, 'Сти́вен Гэ́ри Во́зник, известный как Воз — американский изобретатель, инженер-электронщик и программист, соучредитель компании Apple Computer вместе со Стивом Джобсом и Рональдом Уэйном в 1976 году. В середине 1970-х в одиночку спроектировал компьютеры Apple I и Apple II, которые начали «микрокомпьютерную революцию» и определили развитие отрасли', reply_markup = keyboardnine)
	
def hispad(message):
	keyboardten = types.InlineKeyboardMarkup()
	wikibuttoneight = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/IPad')
	keyboardten.add(wikibuttoneight)
	bot.send_message(message.chat.id, 'Apple iPad является классическим примером интернет-планшетов и принципиально отличается от персональных настольных компьютеров. Многие аналитики относят интернет-планшеты к устройствам посткомпьютерной эпохи, которые проще и понятнее привычных персональных компьютеров и со временем могут вытеснить ПК с ИТ-рынка.', reply_markup=keyboardten)


def ipod(message):
	keyboardeleven = types.InlineKeyboardMarkup()
	wikibutton_nine = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/IPod')
	keyboardeleven.add(wikibutton_nine)
	bot.send_message(message.chat.id, 'iPod — торговая марка серии портативных медиапроигрывателей компании Apple, в качестве носителя данных использующих флеш-память или, в ряде моделей, жёсткий диск.')


def iphon(message):
	keyboard12 = types.InlineKeyboardMarkup()
	wikibutton10 = types.InlineKeyboardButton(text = 'Подробние', url = 'https://ru.wikipedia.org/wiki/IPhone')
	keyboard12.add(wikibutton10)
	bot.send_message(message.chat.id, 'iPhone — серия смартфонов, разработанных корпорацией Apple. Работают под управлением операционной системы iOS, представляющей собой упрощённую и оптимизированную для функционирования на мобильном устройстве версию macOS.')
