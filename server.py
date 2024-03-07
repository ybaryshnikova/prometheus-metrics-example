from flask import Flask, render_template
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
import time
import random
from prometheus_client import Gauge

application = Flask(__name__, static_folder="./public", template_folder="./templates")
metrics = GunicornInternalPrometheusMetrics(application, defaults_enabled=False)


@application.route("/")
def index():
    return render_template("index.html")


# Counter metric example
@application.route("/count", methods=["POST"])
@metrics.counter("demo_clicks_counter", "Number of button clicks by user")
def count_clicks():
    return {}


# Gauge metric example
# Define the gauge metric
current_value_gauge = Gauge('demo_clicks_gauge', 'Gauge metric example')


@application.route("/increase-gauge-value", methods=["POST"])
def increase_value():
    current_value_gauge.inc()  # Decrease gauge by 1
    return {}


@application.route("/decrease-gauge-value", methods=["POST"])
def decrease_value():
    current_value_gauge.dec()  # Decrease gauge by 1
    return {}


# Histogram metric example
# custom_buckets = [0.1, 0.5, 1.0, 1.5, 2.0]  # Define your own bucket boundaries here
# @metrics.histogram('demo_click_duration_seconds', 'Duration of button click processing in seconds', buckets=custom_buckets)

@application.route("/histogram", methods=["POST"])
@metrics.histogram('demo_click_duration_seconds', 'Duration of button click processing in seconds')
def histogram():
    processing_time = random.uniform(0.1, 2.0)  # Adjust the range as needed
    time.sleep(processing_time)

    return {}


