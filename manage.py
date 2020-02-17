from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from model_user import User
from model_comment import Comment


app = create_app()

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    '''
    It will run the unit test
    '''
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager .shell
def make_shell_context():
    return dict(app=app, db=db, User=user, Comment=comment, PitchCategory=PitchCategory, Pitches=Pitches)
    pass

if __name__ == '__main__':
    manager.run()