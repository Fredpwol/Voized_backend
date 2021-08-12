import os
from flask_script import  Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv

load_dotenv()

from voized import app, db
from voized.config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)

manager = Manager(app)
migrate = Migrate(app=app, db=db)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()