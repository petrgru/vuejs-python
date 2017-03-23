#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main import app_factory
from config import cmm
from flask_socketio import SocketIO
from flask_migrate import Migrate, MigrateCommand
from flask_script import (
    Server,
    Shell,
    Manager,
    prompt_bool,
)



from extensions.database import db

#from flask_social.providers.facebook import *


app = app_factory(cmm, cmm.project_name)


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0'))
manager.add_command('db', MigrateCommand)


@manager.command
@manager.option('-n', '--num_users', help='Number of users')
def create_db(num_users=5):
    """Creates data tables and populates them."""
    db.create_all()



@manager.command
@manager.option('-n', '--num_assoc', help='Number of associations')
def create_assoc(num_assoc=5):
    test_assoc()


@manager.command
def drop_db():
    """Drops data tables."""
    if prompt_bool('Are you sure?'):
        db.drop_all()


@manager.command
def recreate_db():
    """Same as running drop_db() and create_db()."""
    drop_db()
    create_db()


if __name__ == '__main__':
    socketio = SocketIO(app)
    socketio.run(app)

