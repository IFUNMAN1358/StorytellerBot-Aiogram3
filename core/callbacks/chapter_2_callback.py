from random import randint

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query

from core.keyboards.chapter_2_keyboard import continue_keyboard, choice_5, choice_6, choice_7, choice_8, choice_9, \
    choice2_0
from core.texts.chapter_1_text import FirstChapterText
from core.texts.chapter_2_text import SecondChapterText

router = Router()


@router.callback_query(F.data == "chapter_2")
async def func_14(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.forest(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.chapter_2_start(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('sleep'))
    await call.answer()


@router.callback_query(F.data == "sleep")
async def func_15(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.chapter_2_start(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.next(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('strange'))
    await call.answer()


@router.callback_query(F.data == "strange")
async def func_16(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.next(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.strange(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('figure'))
    await call.answer()


@router.callback_query(F.data == "figure")
async def func_17(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.strange(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.figure(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('lake'))
    await call.answer()


@router.callback_query(F.data == "lake")
async def func_18(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.figure(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.lake(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('who'))
    await call.answer()


@router.callback_query(F.data == "who")
async def func_19(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.lake(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.who(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('dialogue'))
    await call.answer()


@router.callback_query(F.data == 'dialogue')
async def func_20(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.who(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.dialogue(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('zombies'))
    await call.answer()


@router.callback_query(F.data == 'zombies')
async def func_21(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.dialogue(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.zombies(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice_5())
    await call.answer()


@router.callback_query(F.data.startswith("choice_5"))
async def func_22(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()
    if part == 'fight':
        await state.update_data(actions=data['actions'] + 1)
        await call.message.edit_text(text=SecondChapterText.zombies(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.fight(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('fight_cont'))
    elif part == 'run':
        await call.message.edit_text(text=SecondChapterText.zombies(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.run(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('old_house'))
    await call.answer()


@router.callback_query(F.data == 'fight_cont')
async def func_23(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    data = await state.get_data()
    random_number = randint(1, 10)
    await call.message.edit_text(text=SecondChapterText.fight(username),
                                 parse_mode=ParseMode.HTML)
    if random_number == 1:
        await call.message.answer(text=SecondChapterText.death_10(username),
                                  parse_mode=ParseMode.HTML)
        await state.clear()
    else:
        data['items']['bandage'] = True
        await state.set_data(data)
        await call.message.answer(text='<b>[ Получен предмет: бинт ]</b>',
                                  parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.bandage(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('old_house'))
    await call.answer()


@router.callback_query(F.data == 'old_house')
async def func_24(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    data = await state.get_data()
    if data['items']['bandage']:
        await call.message.edit_text(text=SecondChapterText.bandage(username),
                                     parse_mode=ParseMode.HTML)
    else:
        await call.message.edit_text(text=SecondChapterText.run(username),
                                     parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.old_house(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('radio'))
    await call.answer()


@router.callback_query(F.data == 'radio')
async def func_25(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.old_house(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.radio(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('frequency'))
    await call.answer()


@router.callback_query(F.data == 'frequency')
async def func_26(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.radio(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text='Какую частоту радио поставить?',
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice_6())
    await call.answer()


@router.callback_query(F.data.startswith('choice_6'))
async def func_27(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()
    numbers_for_delete = data['numbers_for_delete']
    if part == 'first':
        numbers_for_delete.append(1)
        await state.update_data(numbers_for_delete=numbers_for_delete)
        await call.message.edit_text(text='Какую частоту радио поставить?',
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_6(numbers_for_delete=data['numbers_for_delete']))
        await call.message.answer(text=('***Как известно, самолеты не только летают, но и болтают во время полета.'
                                        ' Почему? Потому что у них есть бортовой разговорник!***'),
                                  parse_mode=ParseMode.HTML)
    elif part == 'second':
        numbers_for_delete.append(2)
        await state.update_data(numbers_for_delete=numbers_for_delete)
        await call.message.edit_text(text='Какую частоту радио поставить?',
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_6(numbers_for_delete=data['numbers_for_delete']))
        await call.message.answer(text=('***Почему компьютер всегда выигрывает в споре?'
                                        ' Потому что у него всегда есть логические аргументы!***'),
                                  parse_mode=ParseMode.HTML)
    elif part == 'third':
        await call.message.edit_text(text='Какую частоту радио поставить?',
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.message(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('go_base'))
        await state.update_data(numbers_for_delete=list())
    elif part == 'fourth':
        numbers_for_delete.append(4)
        await state.update_data(numbers_for_delete=numbers_for_delete)
        await call.message.edit_text(text='Какую частоту радио поставить?',
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_6(numbers_for_delete=data['numbers_for_delete']))
        await call.message.answer(text=('***Почему атомы такие маленькие?'
                                        ' Потому что они веселятся в молекулярном клубе!***'),
                                  parse_mode=ParseMode.HTML)
    await call.answer()


@router.callback_query(F.data == 'go_base')
async def func_28(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.message(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.talk(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('base'))
    await call.answer()


@router.callback_query(F.data == 'base')
async def func_29(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.talk(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.clear_base(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('door'))
    await call.answer()


@router.callback_query(F.data == 'door')
async def func_30(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.clear_base(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.door(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('task'))
    await call.answer()


@router.callback_query(F.data == 'task')
async def func_31(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.door(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.task(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice_7())
    await call.answer()


@router.callback_query(F.data.startswith('choice_7'))
async def func_32(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]

    data = await state.get_data()
    numbers_for_delete = data['numbers_for_delete']
    attempts = data['attempts']

    if part == '2':
        await call.message.edit_text(text=SecondChapterText.task(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.open_door(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('system'))
        await state.update_data(numbers_for_delete=list())

    else:
        attempts -= 1
        numbers_for_delete.append(int(part))
        await state.update_data(numbers_for_delete=numbers_for_delete)
        await state.update_data(attempts=attempts)
        await call.message.edit_text(text=SecondChapterText.task(username), parse_mode=ParseMode.HTML,
                                     reply_markup=choice_7(numbers_for_delete=numbers_for_delete))
        if attempts == 1:
            await call.message.answer(text='Осталась последняя попытка.')
        else:
            pass

    if attempts == 0:
        await call.message.edit_text(text=SecondChapterText.task(username), parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.task_death(username),
                                  parse_mode=ParseMode.HTML)
        await state.clear()
    await call.answer()


@router.callback_query(F.data == 'system')
async def func_33(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.open_door(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.system(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice_8('two_buttons'))
    await call.answer()


@router.callback_query(F.data.startswith('choice_8'))
async def func_34(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()

    if part == '1':
        await call.message.edit_text(text=SecondChapterText.system(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.complex(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('go_complex'))

    elif part == '2':
        await call.message.edit_text(text=SecondChapterText.system(username),
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_8('only_continue'))
        await call.message.answer(text=SecondChapterText.document(username),
                                  parse_mode=ParseMode.HTML)
        await state.update_data(history=data['history'] + 1)
    await call.answer()


@router.callback_query(F.data == 'go_complex')
async def func_35(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.complex(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.hangar(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('car'))
    await call.answer()


@router.callback_query(F.data == 'car')
async def func_36(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.hangar(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.car(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice_9())
    await call.answer()


@router.callback_query(F.data.startswith('choice_9'))
async def func_37(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()
    numbers_for_delete = data['numbers_for_delete']

    # Wrong
    if part == '1':
        if 3 not in numbers_for_delete:
            await call.message.answer(text='Нет энергии для зажигания.',
                                      parse_mode=ParseMode.HTML)
        else:
            numbers_for_delete.append(int(part))
            await state.update_data(numbers_for_delete=numbers_for_delete)

            await call.message.edit_text(text=SecondChapterText.car(username),
                                         parse_mode=ParseMode.HTML,
                                         reply_markup=choice_9(numbers_for_delete))
            await call.message.answer(text='Вы запустили двигатель.')

    # Continue
    elif part == '2':
        if 1 not in numbers_for_delete:
            await call.message.answer(text='Двигатель не запущен.',
                                      parse_mode=ParseMode.HTML)
        else:
            await call.message.edit_text(text=SecondChapterText.car(username),
                                         parse_mode=ParseMode.HTML)
            await call.message.answer(text=SecondChapterText.drive(username),
                                      parse_mode=ParseMode.HTML,
                                      reply_markup=continue_keyboard('left'))
            await state.update_data(numbers_for_delete=list())

    # Wrong
    elif part == '3':
        numbers_for_delete.append(int(part))
        await state.update_data(numbers_for_delete=numbers_for_delete)

        await call.message.edit_text(text=SecondChapterText.car(username),
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_9(numbers_for_delete))
        await call.message.answer(text='Вы соединили провода и запустили аккумулятор.')

    # Wrong
    elif part == '4':
        numbers_for_delete.append(int(part))
        await state.update_data(numbers_for_delete=numbers_for_delete)

        await call.message.edit_text(text=SecondChapterText.car(username),
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_9(numbers_for_delete))
        await call.message.answer(text='Ладно, это вряд ли бы помогло...')
    await call.answer()


@router.callback_query(F.data == 'left')
async def func_38(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.drive(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=SecondChapterText.road(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice2_0())
    await call.answer()


@router.callback_query(F.data.startswith('choice2_0'))
async def func_39(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]

    if part == 'asphalt':
        await call.message.edit_text(text=SecondChapterText.road(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.asphalt(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('chapter_3'))

    elif part == 'ground':
        await call.message.edit_text(text=SecondChapterText.road(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=SecondChapterText.cliff(username),
                                  parse_mode=ParseMode.HTML)
        await state.clear()
    await call.answer()
