
DB_HOST = '193.148.58.82'
DB_PORT = '5432'
MAIN_DB_NAME = 'just_ask_main_db'
LOCAL_DB_NAME = 'just_ask_local_db'
DB_USER = 'just_ask_user'
DB_PASS = 'zxcqwerty08!'

SQLALCHEMY_MAIN_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{MAIN_DB_NAME}"
ASYNC_SQLALCHEMY_MAIN_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{MAIN_DB_NAME}"

SQLALCHEMY_LOCAL_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{LOCAL_DB_NAME}"
ASYNC_SQLALCHEMY_LOCAL_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{LOCAL_DB_NAME}"

BOT_TOKEN = '8346862400:AAG0fWc3MEvmoyDpftL8Zv2ump_drDp1BPw'

add_group_link = f"https://t.me/@JustAskX_bot?startgroup=newgroups&admin=manage_chat+change_info+delete_messages+restrict_members+invite_users+promote_members"

BALANCER_PORT = 8030
BALANCER_URL = 'https://justask.tsyrulix.fit/webhook'

TELEGRAM_BOT_USERS_PORT = 8029
TELEGRAM_BOT_USERS_URL = 'https://personal.tsyrulix.fit/webhook'


TELEGRAM_BOT_GROUPS_PORT = 8031
TELEGRAM_BOT_GROUPS_URL = 'https://groups.tsyrulix.fit/webhook'

ENV_TYPE = 'prod'
