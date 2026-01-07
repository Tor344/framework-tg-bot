from sqladmin import ModelView
from bot.database.models import User  # <-- твоя модель

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.telegram_id]
    column_telegram_id= [User.telegram_id]
