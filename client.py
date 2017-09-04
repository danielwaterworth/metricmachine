import itertools
import math
import requests
import time

class Metric:
    def __init__(self, url, run_id, metric_name):
        self.url = url
        self.run_id = run_id
        self.metric_name = metric_name

    def __setitem__(self, key, value):
        path = \
            "%s/run/%d/metric/%s/data" % (self.url, self.run_id, self.metric_name)
        requests.post(
            path,
            json={'samples': [[key, value]]}
        )

class Run:
    def __init__(self, url, run_id):
        self.url = url
        self.run_id = run_id

    def __getitem__(self, metric_name):
        return Metric(self.url, self.run_id, metric_name)

    def new_metric(self, metric_name):
        requests.post("%s/run/%d/metric/%s/initialize" % (self.url, self.run_id, metric_name))
        return self[metric_name]

class Client:
    def __init__(self, url):
        self.url = url

    def __getitem__(self, run_id):
        return Run(self.url, run_id)

    def new_run(self):
        run_id = requests.post("%s/run/new" % self.url).json()['run_id']
        return Run(self.url, run_id)

if __name__ == '__main__':
    client = Client('http://localhost:5000')
    run = client.new_run()
    metric = run.new_metric('foo')
    for i in itertools.count():
        metric[i] = math.sin(float(i)/10)
        time.sleep(1)
