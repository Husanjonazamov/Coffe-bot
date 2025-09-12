# state.py fayli

from aiogram.dispatcher.filters.state import State, StatesGroup




class CoffeState(StatesGroup):
    coffe = State()
    category = State()
    quantity = State()
    
    # order
    order = State()
    name = State()
    phone = State()
    comment = State()
    confirm = State()
    