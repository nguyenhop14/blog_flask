import os
from flask import Flask

def create_app(test_config=None):
	#create instance Flask (__name__: name of current module, 2: has config file are relative to instance folder)
	app = Flask(__name__, instance_relative_config=True)
	#set some default config
	app.config.from_mapping(
		#keep data safe, should with random value
		SECRET_KEY='dev',
		#where save SQlite databases
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)
	
	if test_config is None:
		#overrides default config
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)
	
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
	
	@app.route('/hello')
	def hello():
		return 'Hello World'
	@app.route('/about')
	def about():
		return "About me"
	from . import auth
	from . import db
	from . import blog
  	db.init_app(app)
  	app.register_blueprint(auth.bp)
  	app.register_blueprint(blog.bp)
    
  	
    
 
    
	
	return app
	
