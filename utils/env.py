from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ADMIN = env('ADMIN')
CHANNEL = env('CHANNEL')

BASE_URL = env('BASE_URL')
