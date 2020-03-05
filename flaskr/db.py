import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
		#tell Flask call function when cleaning up after return response
    app.teardown_appcontext(close_db)
    #add new comment can be called with flask (VD:flask init-data)
    app.cli.add_command(init_db_command)

def init_db():
    db = get_db()
		#open file relative to flaskr package
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8')) 


def get_db():
		#g: special object is unique for each request, store data, connect
    if 'db' not in g: 
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db
      
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


#define a command line called init-db
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

    

