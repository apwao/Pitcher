from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Pitch
from flask_migrate import Migrate, MigrateCommand

app = create_app('production')

# Creating an instance of Manager to create commands
# create command to run the application 
manager = Manager(app)
manager.add_command('server', Server)

# creating command to create a database migration
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    """
    make_shell_context function to make the python shell accessible
    for purposes of testing the database functionality
    """
    # passing the models and app instances to the shell
    return dict(app = app, db = db, User = User, Pitch = Pitch)

@manager.command
def test():
    """
    test function to run the tests 
    """
    
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity =2).run(tests)
    
if __name__ == '__main__':
        manager.run()
