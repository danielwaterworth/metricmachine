from app import app
from flask import render_template, request, abort, Response

class Metric:
    def __init__(self):
        self.samples = {}

class Run:
    def __init__(self):
        self.metrics = {}

    def __getitem__(self, metric_name):
        return self.metrics[metric_name]

class RunCollection:
    def __init__(self):
        self.runs = []

    def __getitem__(self, run_id):
        return self.runs[run_id]

runs = RunCollection()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/run/<int:run_id>/', methods=['GET'])
def run_index(run_id):
    run = runs[run_id]
    raise NotImplementedError()

@app.route('/run/<int:run_id>/metric/<string:metric_name>', methods=['GET'])
def metrix_index(run_id, metric_name):
    run = runs[run_id]
    metric = run[metric_name]
    raise NotImplementedError()

@app.route('/run/<int:run_id>/metric/<string:metric_name>/data.json', methods=['GET'])
def metrix_data(run_id, metric_name):
    run = runs[run_id]
    metric = run[metric_name]
    raise NotImplementedError()

@app.route('/run/new', methods=['POST'])
def index():
    raise NotImplementedError()

@app.route('/run/<int:run_id>/metric/<string:metric_name>/initialize', methods=['POST'])
def index(run_id, metric_name):
    run = runs[run_id]
    metric = run[metric_name]
    raise NotImplementedError()

@app.route('/run/<int:run_id>/metric/<string:metric_name>/data', methods=['POST'])
def index(run_id, metric_name):
    run = runs[run_id]
    metric = run[metric_name]
    raise NotImplementedError()
