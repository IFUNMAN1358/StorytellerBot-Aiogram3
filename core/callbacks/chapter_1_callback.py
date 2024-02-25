from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query

from core.texts.chapter_1_text import FirstChapterText
from core.keyboards.chapter_1_keyboard import continue_keyboard, choice_1, choice_3

router = Router()


@router.callback_query(F.data == "start")
async def func_1(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.start(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=FirstChapterText.background(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('awakening'))
    await call.answer()


@router.callback_query(F.data == "awakening")
async def func_2(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.background(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=FirstChapterText.awakening(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice_1('all'))
    await call.answer()


@router.callback_query(F.data.startswith("choice_1"))
async def func_3(call: callback_query,
               state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()
    if part == 'continue' and data['actions'] == 1:
        await call.message.edit_text(text=FirstChapterText.awakening(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=FirstChapterText.variant(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('variant'))
    elif part == 'stand_up':
        await state.update_data(actions=data['actions'] + 1)
        await call.message.edit_text(text=FirstChapterText.awakening(username),
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_1('one'))
        await call.message.answer(text=FirstChapterText.stand_up(username),
                                  parse_mode=ParseMode.HTML)
    elif part == 'remember':
        await state.update_data(history=data['history'] + 1)
        await call.message.edit_text(text=FirstChapterText.awakening(username),
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=choice_1('two'))
        await call.message.answer(text=FirstChapterText.remember(username),
                                  parse_mode=ParseMode.HTML)
    else:
        await call.message.answer('Вы не выбрали действие.')
    await call.answer()


@router.callback_query(F.data.startswith("choice_2"))
async def func_4(call: callback_query,
                 state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]

    if part == 'other_way':
        await call.message.edit_text(text=FirstChapterText.variant(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=FirstChapterText.other_way(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('hallway'))
    elif part == 'gap':
        await call.message.edit_text(text=FirstChapterText.variant(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=FirstChapterText.gap(username),
                                  parse_mode=ParseMode.HTML)
        await state.clear()
    await call.answer()


@router.callback_query(F.data == "hallway")
async def func_5(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.other_way(username),
                                 parse_mode=ParseMode.HTML)

    await call.message.answer(text=FirstChapterText.hallway(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('super_hallway'))
    await call.answer()


@router.callback_query(F.data == "super_hallway")
async def func_6(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.hallway(username),
                                 parse_mode=ParseMode.HTML)

    await call.message.answer(text=FirstChapterText.super_hallway(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('find_home'))
    await call.answer()


@router.callback_query(F.data == "find_home")
async def func_7(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.super_hallway(username),
                                 parse_mode=ParseMode.HTML)

    await call.message.answer(text=FirstChapterText.find_home(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice_3('all'))
    await call.answer()


@router.callback_query(F.data.startswith("choice_3"))
async def func_8(call: callback_query,
                 state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()

    if part == 'barn':
        if data['actions'] == 2:
            await call.message.edit_text(text=FirstChapterText.find_home(username),
                                         parse_mode=ParseMode.HTML,
                                         reply_markup=choice_3('without_barn_and_pit'))
        else:
            await call.message.edit_text(text=FirstChapterText.find_home(username),
                                         parse_mode=ParseMode.HTML,
                                         reply_markup=choice_3('without_barn'))

        await state.update_data(actions=data['actions'] + 1)
        await call.message.answer(text=FirstChapterText.barn(username),
                                  parse_mode=ParseMode.HTML)
    elif part == 'pit':
        if data['actions'] == 2:
            await call.message.edit_text(text=FirstChapterText.find_home(username),
                                         parse_mode=ParseMode.HTML,
                                         reply_markup=choice_3('without_barn_and_pit'))
        else:
            await call.message.edit_text(text=FirstChapterText.find_home(username),
                                         parse_mode=ParseMode.HTML,
                                         reply_markup=choice_3('without_pit'))
        await state.update_data(actions=data['actions'] + 1)
        await call.message.answer(text=FirstChapterText.pit(username),
                                  parse_mode=ParseMode.HTML)
    elif part == 'house':
        await call.message.edit_text(text=FirstChapterText.find_home(username),
                                     parse_mode=ParseMode.HTML)

        await call.message.answer(text=FirstChapterText.house(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('knife'))
    elif part == 'forest':
        await call.message.edit_text(text=FirstChapterText.find_home(username),
                                     parse_mode=ParseMode.HTML)

        await call.message.answer(text=FirstChapterText.forest(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('chapter_2'))
    await call.answer()


@router.callback_query(F.data.startswith("choice_4"))
async def func_9(call: callback_query,
                 state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()

    if part == 'plus_knife':
        data['items']['knife'] = True
        await state.set_data(data)
        await call.message.answer(text='<b>[ Получен предмет: нож ]</b>',
                                  parse_mode=ParseMode.HTML)

        await call.message.edit_text(text=FirstChapterText.house(username),
                                     parse_mode=ParseMode.HTML)

        await call.message.answer(text=FirstChapterText.knife(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('exit_home'))
    elif part == 'minus_knife':
        await call.message.answer(text='<b>[ Пропущен предмет: нож ]</b>',
                                  parse_mode=ParseMode.HTML)
        await call.message.edit_text(text=FirstChapterText.house(username),
                                     parse_mode=ParseMode.HTML)

        await call.message.answer(text=FirstChapterText.knife(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('exit_home'))
    await call.answer()


@router.callback_query(F.data == "exit_home")
async def func_10(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.knife(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=FirstChapterText.gate(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('meeting'))
    await call.answer()


@router.callback_query(F.data == "meeting")
async def func_11(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.gate(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=FirstChapterText.meeting(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('result'))
    await call.answer()


@router.callback_query(F.data == "result")
async def func_12(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    data = await state.get_data()

    await call.message.edit_text(text=FirstChapterText.meeting(username),
                                 parse_mode=ParseMode.HTML)
    if data['items']['knife']:
        await call.message.answer(text=FirstChapterText.have_knife(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('go_forest'))
    else:
        await call.message.answer(text=FirstChapterText.gg(username),
                                  parse_mode=ParseMode.HTML)
        await state.clear()
    await call.answer()


@router.callback_query(F.data == "go_forest")
async def func_13(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=FirstChapterText.have_knife(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=FirstChapterText.forest(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('chapter_2'))
    await call.answer()
