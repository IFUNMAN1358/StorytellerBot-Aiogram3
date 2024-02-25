from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def continue_keyboard(mod: str) -> InlineKeyboardMarkup:
    buttons = list()
    if mod == 'sleep':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"sleep")])
    elif mod == 'attack':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"attack")])
    elif mod == 'arrive':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"arrive")])
    elif mod == 'mutant':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"mutant")])
    elif mod == 'wound':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"wound")])
    elif mod == 'help':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"help")])
    elif mod == 'bandage':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"bandage")])
    elif mod == 'rest':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"rest")])
    elif mod == 'sad':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"sad")])
    elif mod == 'security1':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"security1")])
    elif mod == 'security2':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"security2")])
    elif mod == 'security3':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"security3")])
    elif mod == 'sec_dialogue':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"sec_dialogue")])
    elif mod == 'dark':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"dark")])
    elif mod == 'trap':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"trap")])
    elif mod == 'aftermath':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"aftermath")])
    elif mod == 'lied':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"lied")])
    elif mod == 'scientists':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"scientists")])
    elif mod == 'syringe':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"syringe")])
    elif mod == 'guess':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"guess")])
    elif mod == 'solution':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"solution")])
    elif mod == 'destruction':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"destruction")])
    elif mod == 'gen_life':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"gen_life")])
    elif mod == 'gen_kill':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"gen_kill")])
    elif mod == 'final':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"final")])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice2_1() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Попытаться ускориться', callback_data=f'choice2_1:speed')],
        [InlineKeyboardButton(text='Попробовать уклониться', callback_data=f'choice2_1:dodge')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice2_2() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Рассказать про документы', callback_data=f'choice2_2:fair')],
        [InlineKeyboardButton(text='Соврать', callback_data=f'choice2_2:lie')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice2_3() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Да, согласен', callback_data=f'choice2_3:yes')],
        [InlineKeyboardButton(text='Нет, не согласен', callback_data=f'choice2_3:no')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice2_4() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Убить учёных', callback_data=f'choice2_4:kill')],
        [InlineKeyboardButton(text='Оставить в живых', callback_data=f'choice2_4:life')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice2_5() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Поджечь газ', callback_data=f'choice2_5:yes')],
        [InlineKeyboardButton(text='Не поджигать', callback_data=f'choice2_5:no')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
