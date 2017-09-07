from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oneuadnoehudaounelg'
Bootstrap(app)
from metricmachine.app import views
