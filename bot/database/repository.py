from tortoise import Tortoise

from bot.database.models import User


class Database:
    def __init__(self, db_url: str = "sqlite://db.sqlite3") -> None:
        self.db_url = db_url

    async def connect(self) -> None:
        """Конектимся к базе"""
        await Tortoise.init(db_url=self.db_url, modules={"models": ["bot.database.models"]})
        await Tortoise.generate_schemas()

    async def close(self):
        """Закрываем конект"""
        await Tortoise.close_connections()



class DB_users(Database):
    async def add_user(self, user_id: int, user_name: str, age: int) -> None:
        """добавляем пользователя"""
        if not User.filter(id=user_id).exists():
            await User.create(id=user_id, user_name=user_name, age=age)

    async def get_user(self, user_id: int):
        """получем данные пользователя"""
        return await User.get_or_none(id=user_id)

    async def update_user(self, user_id: int, user_name: str, age: int) -> None:
        """Изменяет или добавляет пользователя"""
        await User.update_or_create(id=user_id, user_name=user_name, age=age)

    async def delete_user(self, user_id: int) -> bool:
        """Удоляем пользователя True если удалили False если нет"""
        return bool(await User.filter(user_id=user_id).delete())


db = Database()

db_users = DB_users()