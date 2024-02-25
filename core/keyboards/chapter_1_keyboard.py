from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def continue_keyboard(mod: str) -> InlineKeyboardMarkup:
    buttons = list()
    if mod == 'start':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"start")])
    elif mod == 'awakening':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"awakening")])
    elif mod == 'variant':
        buttons.append([InlineKeyboardButton(text='Найти другой путь', callback_data=f"choice_2:other_way")])
        buttons.append([InlineKeyboardButton(text='Залезть в трещину', callback_data=f"choice_2:gap")])
    elif mod == 'hallway':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"hallway")])
    elif mod == 'super_hallway':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"super_hallway")])
    elif mod == 'find_home':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"find_home")])
    elif mod == 'knife':
        buttons.append([InlineKeyboardButton(text='Взять', callback_data=f"choice_4:plus_knife")])
        buttons.append([InlineKeyboardButton(text='Оставить', callback_data=f"choice_4:minus_knife")])
    elif mod == 'exit_home':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"exit_home")])
    elif mod == 'meeting':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"meeting")])
    elif mod == 'result':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"result")])
    elif mod == 'go_forest':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"go_forest")])
    elif mod == 'chapter_2':
        buttons.append([InlineKeyboardButton(text='Глава 2', callback_data=f"chapter_2")])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_1(mod: str) -> InlineKeyboardMarkup:
    buttons = list()
    if mod == 'all':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"choice_1:continue")])
        buttons.append([InlineKeyboardButton(text='Встать и осмотреться', callback_data=f"choice_1:stand_up")])
        buttons.append([InlineKeyboardButton(text='Попытаться вспомнить', callback_data=f"choice_1:remember")])
    elif mod == 'two':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"choice_1:variant")])
        buttons.append([InlineKeyboardButton(text='Встать и осмотреться', callback_data=f"choice_1:stand_up")])
    elif mod == 'one':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"choice_1:continue")])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_3(mod: str) -> InlineKeyboardMarkup:
    buttons = list()
    if mod == 'all':
        buttons.append([InlineKeyboardButton(text='Исследовать заброшенный дом', callback_data=f"choice_3:house")])
        buttons.append([InlineKeyboardButton(text='Осмотреть колодец', callback_data=f"choice_3:pit")])
        buttons.append([InlineKeyboardButton(text='Скрыться в лесу', callback_data=f"choice_3:forest")])
        buttons.append([InlineKeyboardButton(text='Осмотреть сарай', callback_data=f"choice_3:barn")])
    elif mod == 'without_barn':
        buttons.append([InlineKeyboardButton(text='Исследовать заброшенный дом', callback_data=f"choice_3:house")])
        buttons.append([InlineKeyboardButton(text='Осмотреть колодец', callback_data=f"choice_3:pit")])
        buttons.append([InlineKeyboardButton(text='Скрыться в лесу', callback_data=f"choice_3:forest")])
    elif mod == 'without_pit':
        buttons.append([InlineKeyboardButton(text='Исследовать заброшенный дом', callback_data=f"choice_3:house")])
        buttons.append([InlineKeyboardButton(text='Скрыться в лесу', callback_data=f"choice_3:forest")])
        buttons.append([InlineKeyboardButton(text='Осмотреть сарай', callback_data=f"choice_3:barn")])
    elif mod == 'without_barn_and_pit':
        buttons.append([InlineKeyboardButton(text='Исследовать заброшенный дом', callback_data=f"choice_3:house")])
        buttons.append([InlineKeyboardButton(text='Скрыться в лесу', callback_data=f"choice_3:forest")])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
