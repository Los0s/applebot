# -*- coding: utf-8 -*-
import telebot
from telebot import types
import config
bot = telebot.TeleBot(config.token)



stickerone = 'CAACAgIAAxkBAAN3Xlq-wP-8yxQZkzfI6ftz5PTgo7QAAisHAAJjK-IJn8R5tQ5lfPIYBA'
stickertwo = 'CAACAgIAAxkBAAN8Xlq_qgH-niQ3tlgUT7o_g95UoOUAAlcHAAJjK-IJppyN6acxZiMYBA'
stickerthree = 'CAACAgIAAxkBAAODXlrA3ueeXsSr8a-83yXlfSqb_xcAAlAHAAJjK-IJubXxzyKBUIEYBA'
stickerfore = 'CAACAgIAAxkBAAICDF5b54GXGZHSN-vBbZppUk6RbLRxAAJFBwACYyviCXyg4f9yryE1GAQ'
stickerfive = 'CAACAgIAAxkBAAII-l5mWaCjmdCdLF2kw5z0Q3hkyZdkAAItBwACYyviCd9ykcp8jmfPGAQ'
stickersix = 'CAACAgIAAxkBAAIJZ15mXkGRkYMoXs0Ywlwk7HF_R_I8AAIyBwACYyviCQ1qcrhlzmjMGAQ'









def sti(message):
	print(message.sticker)