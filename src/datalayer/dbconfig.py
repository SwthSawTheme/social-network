from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

def configure_db(app: FastAPI):
    register_tortoise(
        app=app,
        config={
             'connections': {
                # 'default': 'postgres://postgres:qwerty123@localhost:5432/events',
                "default": 'sqlite://db.sqlite3'
             },
             'apps': {
                'models': {
                    'models': [
                        "src.datalayer.models.user"
                    ],
                    # If no default_connection specified, defaults to 'default'
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )