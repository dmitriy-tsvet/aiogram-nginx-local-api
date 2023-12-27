from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
TELEGRAM_API_URL = env.str("TELEGRAM_API_URL")
NGINX_API_URL = env.str("NGINX_API_URL")

