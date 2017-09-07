#!env/bin/python
from metricmachine.app import app
app.jinja_env.auto_reload = True
app.run(debug=True)
