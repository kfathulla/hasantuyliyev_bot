from aiogram.fsm.state import StatesGroup, State


class MessageFormState(StatesGroup):
    AnonymousMessage = State()
