from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from model_user import User
from model_comment import Comment


app = create_app()

manager = Manager(app)
manager.add_command('server', Server)

@manager .shell
def make_shell_context():
    return dict(app)ict(app)