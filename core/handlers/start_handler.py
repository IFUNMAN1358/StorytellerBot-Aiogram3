from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from core.keyboards.chapter_1_keyboard import continue_keyboard
from core.texts.chapter_1_text import FirstChapterText


router = Router()


@router.message(F.text == '/start')
async def get_start(message: Message,
                    state: FSMContext):
    username = message.from_user.username
    await state.update_data(actions=0)
    await state.update_data(history=0)
    await state.update_data(numbers_for_delete=list())
    await state.update_data(attempts=2)
    await state.update_data(items={'knife': False,
                                   'bandage': False})
    await state.update_data(kill=False)
    await message.answer(text=FirstChapterText.start(username),
                         reply_markup=continue_keyboard('start'))
