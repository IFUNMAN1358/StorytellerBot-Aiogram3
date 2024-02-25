from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def continue_keyboard(mod: str) -> InlineKeyboardMarkup:
    buttons = list()
    if mod == 'sleep':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"sleep")])
    elif mod == 'strange':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"strange")])
    elif mod == 'figure':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"figure")])
    elif mod == 'lake':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"lake")])
    elif mod == 'who':
        buttons.append([InlineKeyboardButton(text='Кто ты?', callback_data=f"who")])
    elif mod == 'dialogue':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f"dialogue")])
    elif mod == 'zombies':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'zombies')])
    elif mod == 'fight_cont':
        buttons.append([InlineKeyboardButton(text='Продолжить [ Шанс успеха: 90% ]', callback_data=f'fight_cont')])
    elif mod == 'old_house':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'old_house')])
    elif mod == 'radio':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'radio')])
    elif mod == 'frequency':
        buttons.append([InlineKeyboardButton(text='Выбрать частоту', callback_data=f'frequency')])
    elif mod == 'go_base':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'go_base')])
    elif mod == 'base':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'base')])
    elif mod == 'door':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'door')])
    elif mod == 'task':
        buttons.append([InlineKeyboardButton(text='Задача', callback_data=f'task')])
    elif mod == 'system':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'system')])
    elif mod == 'go_complex':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'go_complex')])
    elif mod == 'car':
        buttons.append([InlineKeyboardButton(text='Сесть в машину', callback_data=f'car')])
    elif mod == 'left':
        buttons.append([InlineKeyboardButton(text='Продолжить', callback_data=f'left')])
    elif mod == 'chapter_3':
        buttons.append([InlineKeyboardButton(text='Глава 3', callback_data=f'chapter_3')])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_5() -> InlineKeyboardMarkup:
    buttons = list()
    buttons.append([InlineKeyboardButton(text='Сражаться', callback_data=f'choice_5:fight')])
    buttons.append([InlineKeyboardButton(text='Убежать', callback_data=f'choice_5:run')])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_6(numbers_for_delete: list = None) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='87,5', callback_data=f'choice_6:first')],
        [InlineKeyboardButton(text='92,8', callback_data=f'choice_6:second')],
        [InlineKeyboardButton(text='101,7', callback_data=f'choice_6:third')],
        [InlineKeyboardButton(text='106,2', callback_data=f'choice_6:fourth')]
    ]
    if numbers_for_delete:
        new_buttons = [button for index, button in enumerate(buttons) if index + 1 not in numbers_for_delete]
        keyboard = InlineKeyboardMarkup(inline_keyboard=new_buttons)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_7(numbers_for_delete: list = None) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='10', callback_data=f'choice_7:1')],
        [InlineKeyboardButton(text='13', callback_data=f'choice_7:2')],
        [InlineKeyboardButton(text='17', callback_data=f'choice_7:3')],
        [InlineKeyboardButton(text='21', callback_data=f'choice_7:4')]
    ]
    if numbers_for_delete:
        new_buttons = [button for index, button in enumerate(buttons) if index + 1 not in numbers_for_delete]
        keyboard = InlineKeyboardMarkup(inline_keyboard=new_buttons)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_8(mod: str) -> InlineKeyboardMarkup:
    buttons = []
    if mod == 'two_buttons':
        buttons = [
            [InlineKeyboardButton(text='Продолжить', callback_data=f'choice_8:1')],
            [InlineKeyboardButton(text='Документ', callback_data=f'choice_8:2')]
        ]
    elif mod == 'only_continue':
        buttons = [
            [InlineKeyboardButton(text='Продолжить', callback_data=f'choice_8:1')]
        ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice_9(numbers_for_delete: list = None) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Переключить ключ в зажигание и повернуть его.', callback_data=f'choice_9:1')],
        [InlineKeyboardButton(text='Сдвинуться с места.', callback_data=f'choice_9:2')],
        [InlineKeyboardButton(text='Проверить аккумулятор и подключить провода.', callback_data=f'choice_9:3')],
        [InlineKeyboardButton(text='Попробовать пнуть машину сзади.', callback_data=f'choice_9:4')]
    ]
    if numbers_for_delete:
        new_buttons = [button for index, button in enumerate(buttons) if index + 1 not in numbers_for_delete]
        keyboard = InlineKeyboardMarkup(inline_keyboard=new_buttons)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def choice2_0() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='Грунтовая дорога через лес', callback_data=f'choice2_0:ground')],
        [InlineKeyboardButton(text='Асфальтированная дорога через город', callback_data=f'choice2_0:asphalt')]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
