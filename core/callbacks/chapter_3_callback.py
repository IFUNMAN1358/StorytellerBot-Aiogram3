from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query

from core.keyboards.chapter_3_keyboard import continue_keyboard, choice2_1, choice2_2, choice2_3, choice2_4, choice2_5
from core.texts.chapter_2_text import SecondChapterText
from core.texts.chapter_3_text import ThirdChapterText

router = Router()


@router.callback_query(F.data == "chapter_3")
async def func_40(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=SecondChapterText.asphalt(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.chapter_3_start(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('attack'))
    await call.answer()


@router.callback_query(F.data == "attack")
async def func_41(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.chapter_3_start(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.attack(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice2_1())
    await call.answer()


@router.callback_query(F.data.startswith('choice2_1'))
async def func_42(call: callback_query):
    username = call.from_user.username
    part = call.data.split(':')[1]

    if part == 'speed':
        await call.message.edit_text(text=ThirdChapterText.attack(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.speed(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('arrive'))

    elif part == 'dodge':
        await call.message.edit_text(text=ThirdChapterText.attack(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.dodge(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('mutant'))
    await call.answer()


@router.callback_query(F.data == "arrive")
async def func_43(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.speed(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.complex(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('security3'))
    await call.answer()


@router.callback_query(F.data == "mutant")
async def func_44(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.dodge(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.fear(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('wound'))
    await call.answer()


@router.callback_query(F.data == "wound")
async def func_45(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.fear(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.wound(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('help'))
    await call.answer()


@router.callback_query(F.data == "help")
async def func_46(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.wound(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.help(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('bandage'))
    await call.answer()


@router.callback_query(F.data == "bandage")
async def func_47(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    data = await state.get_data()
    if data['items']['bandage']:
        await call.message.edit_text(text=ThirdChapterText.help(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.have_bandage(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('rest'))
    else:
        await call.message.edit_text(text=ThirdChapterText.help(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.not_have_bandage(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('sad'))
    await call.answer()


@router.callback_query(F.data == "rest")
async def func_48(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.have_bandage(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.complex(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('security1'))
    await call.answer()


@router.callback_query(F.data == "sad")
async def func_49(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.not_have_bandage(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.complex_without_alice(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('security2'))
    await call.answer()


@router.callback_query(F.data == "security1")
async def func_50(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.complex(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.security(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('sec_dialogue'))
    await call.answer()


@router.callback_query(F.data == "security2")
async def func_51(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.complex_without_alice(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.security(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('sec_dialogue'))
    await call.answer()


@router.callback_query(F.data == "security3")
async def func_52(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.complex(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.security(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('sec_dialogue'))
    await call.answer()


@router.callback_query(F.data == "sec_dialogue")
async def func_53(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.security(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.dialogue(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('dark'))
    await call.answer()


@router.callback_query(F.data == "dark")
async def func_54(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.dialogue(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.trap(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('trap'))
    await call.answer()


@router.callback_query(F.data == "trap")
async def func_55(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.trap(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.question(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice2_2())
    await call.answer()


@router.callback_query(F.data.startswith('choice2_2'))
async def func_56(call: callback_query):
    username = call.from_user.username
    part = call.data.split(':')[1]

    if part == 'fair':
        await call.message.edit_text(text=ThirdChapterText.question(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.fair(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('aftermath'))

    elif part == 'lie':
        await call.message.edit_text(text=ThirdChapterText.question(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.lie(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('lied'))
    await call.answer()


@router.callback_query(F.data == "lied")
async def func_57(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.lie(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.gas(username),
                              parse_mode=ParseMode.HTML)
    await state.clear()
    await call.answer()


@router.callback_query(F.data == "aftermath")
async def func_58(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.fair(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.aftermath(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('scientists'))
    await call.answer()


@router.callback_query(F.data == "scientists")
async def func_59(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.aftermath(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.scientists(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice2_3())
    await call.answer()


@router.callback_query(F.data.startswith('choice2_3'))
async def func_60(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]

    if part == 'yes':
        await call.message.edit_text(text=ThirdChapterText.scientists(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.agree(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('syringe'))

    elif part == 'no':
        await call.message.edit_text(text=ThirdChapterText.scientists(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.disagree(username),
                                  parse_mode=ParseMode.HTML)
        await state.clear()
    await call.answer()


@router.callback_query(F.data == "syringe")
async def func_61(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.agree(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.syringe(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('guess'))
    await call.answer()


@router.callback_query(F.data == "guess")
async def func_62(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.syringe(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.guess(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('solution'))
    await call.answer()


@router.callback_query(F.data == "solution")
async def func_63(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.guess(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.solution(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('destruction'))
    await call.answer()


@router.callback_query(F.data == "destruction")
async def func_64(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.solution(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.destruction(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice2_4())
    await call.answer()


@router.callback_query(F.data.startswith('choice2_4'))
async def func_65(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]

    if part == 'kill':
        await call.message.edit_text(text=ThirdChapterText.destruction(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.kill(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('gen_kill'))
        await state.update_data(kill=True)

    elif part == 'life':
        await call.message.edit_text(text=ThirdChapterText.destruction(username),
                                     parse_mode=ParseMode.HTML)
        await call.message.answer(text=ThirdChapterText.life(username),
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=continue_keyboard('gen_life'))
    await call.answer()


@router.callback_query(F.data == "gen_kill")
async def func_66(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.kill(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.generator(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('final'))
    await call.answer()


@router.callback_query(F.data == "gen_life")
async def func_67(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.life(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.generator(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=continue_keyboard('final'))
    await call.answer()


@router.callback_query(F.data == "final")
async def func_68(call: callback_query):
    username = call.from_user.username
    await call.message.edit_text(text=ThirdChapterText.generator(username),
                                 parse_mode=ParseMode.HTML)
    await call.message.answer(text=ThirdChapterText.final(username),
                              parse_mode=ParseMode.HTML,
                              reply_markup=choice2_5())
    await call.answer()


@router.callback_query(F.data.startswith('choice2_5'))
async def func_69(call: callback_query,
                  state: FSMContext):
    username = call.from_user.username
    part = call.data.split(':')[1]
    data = await state.get_data()

    await call.message.edit_text(text=ThirdChapterText.final(username),
                                 parse_mode=ParseMode.HTML)

    if part == 'yes':
        if username == 'Xarenn':
            await call.message.answer(text=ThirdChapterText.xarenn(username),
                                      parse_mode=ParseMode.HTML)
        else:
            await call.message.answer(text=ThirdChapterText.sad_final(username),
                                      parse_mode=ParseMode.HTML)

    elif part == 'no':
        if username == 'Xarenn':
            await call.message.answer(text=ThirdChapterText.xarenn(username),
                                      parse_mode=ParseMode.HTML)
        elif data['kill']:
            await call.message.answer(text=ThirdChapterText.middle_final(username),
                                      parse_mode=ParseMode.HTML)

        else:
            await call.message.answer(text=ThirdChapterText.happy_final(username),
                                      parse_mode=ParseMode.HTML)
    await state.clear()
    await call.answer()
