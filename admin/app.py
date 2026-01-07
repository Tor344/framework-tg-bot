from fastapi import FastAPI
from sqladmin import Admin

# ✅ импортируй из своего проекта
# Подставь реальные пути/имена:
from bot.database.session import engine, SessionMaker  # например

from admin.auth import AdminAuth
from admin.views import UserAdmin  # добавь свои ModelView


def create_admin_app() -> FastAPI:
    app = FastAPI(title="Admin Panel")

    auth = AdminAuth(secret_key="CHANGE_ME")  # лучше взять из config/.env

    admin = Admin(
        app=app,
        engine=engine,
        authentication_backend=auth,
        session_maker=SessionMaker,  # ⭐ ключевое для async
    )

    # регистрируешь модели
    admin.add_view(UserAdmin)

    return app


app = create_admin_app()
