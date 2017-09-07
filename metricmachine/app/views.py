from metricmachine.app import app
import flask
from flask import render_template, request, abort, Response

class Metric:
    def __init__(self, name):
        self.name = name
        self.samples = {}

    def get_data(self):
        return list(sorted(self.samples.items()))

    def __setitem__(self, key, value):
        self.samples[key] = value

class Run:
    def __init__(self, run_id):
        self.run_id = run_id
        self.metrics = {}

    def __getitem__(self, metric_name):
        return self.metrics[metric_name]

    def new_metric(self, metric_name):
        metric = Metric(metric_name)
        self.metrics[metric_name] = metric
        return metric

    def metric_names(self):
        return self.metrics.keys()

class RunCollection:
    def __init__(self):
        self.runs = []

    def __getitem__(self, run_id):
        return self.runs[run_id]

    def new_run(self):
        run_id = len(self.runs)
        self.runs.append(Run(run_id))
        return run_id

    def run_ids(self):
        return range(len(self.runs))

runs = RunCollection()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', runs=runs)

@app.route('/run/<int:run_id>/', methods=['GET'])
def run_index(run_id):
    run = runs[run_id]
    return render_template('run_index.html', runs=runs, run=run)

@app.route('/run/<int:run_id>/metric/<string:metric_name>', methods=['GET'])
def metrix_index(run_id, metric_name):
    run = runs[run_id]
    metric = run[metric_name]
    return render_template('metric_index.html', runs=runs, run=run, metric=metric)

@app.route('/run/<int:run_id>/metric/<string:metric_name>/data.json', methods=['GET'])
def metrix_data(run_id, metric_name):
    run = runs[run_id]
    metric = run[metric_name]
    return flask.json.jsonify({'samples': metric.get_data()})

@app.route('/run/new', methods=['POST'])
def new_run():
    return flask.json.jsonify({'run_id': runs.new_run()})

@app.route('/run/<int:run_id>/metric/<string:metric_name>/initialize', methods=['POST'])
def initialize_metric(run_id, metric_name):
    run = runs[run_id]
    run.new_metric(metric_name)
    return ''

@app.route('/run/<int:run_id>/metric/<string:metric_name>/data', methods=['POST'])
def add_data(run_id, metric_name):
    run = runs[run_id]
    metric = run[metric_name]
    for key, value in request.json['samples']:
        metric[key] = value
    return ''
