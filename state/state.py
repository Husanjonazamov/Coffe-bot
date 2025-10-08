# state.py fayli

from aiogram.dispatcher.filters.state import State, StatesGroup



class UserState(StatesGroup):
    lang = State()


class CoffeState(StatesGroup):
    coffe = State()
    category = State()
    quantity = State()
    
    # order
    order = State()
    name = State()
    phone = State()
    comment = State()
    payment = State()
    confirm = State()
    check = State()
    
    
class LangUpdate(StatesGroup):
    lang = State()
    