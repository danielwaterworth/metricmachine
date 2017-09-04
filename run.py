#!env/bin/python
from app import app
app.jinja_env.auto_reload = True
app.run(debug=True)
