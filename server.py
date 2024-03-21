from flask import Flask, render_template
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
import time
import random
from prometheus_client import Gauge

application = Flask(__name__, static_folder="./public", template_folder="./templates")
metrics = GunicornInternalPrometheusMetrics(application, export_defaults=False)


# Counter metric example
@application.route("/count", methods=["POST"])
@metrics.counter("demo_clicks_counter", "Number of button clicks by user")
def count_clicks():
    return {}


# Gauge metric example
# Define the gauge metric
current_value_gauge = Gauge('demo_request_duration_gauge', 'Gauge metric example')


@application.route('/gauge', methods=['POST'])
def gauge():
    # Start time
    start_time = time.time()

    # Simulate some processing or just wait for the request handling
    time.sleep(random.uniform(0.1, 0.5))  # Simulating processing time

    # End time
    end_time = time.time()

    # Calculate request duration
    duration = end_time - start_time

    # Set the gauge to the duration of this request
    current_value_gauge.set(duration)

    # Return response with the measured duration
    return {'status': 'success', 'request_duration': duration}, 200


# Histogram metric example
# custom_buckets = [0.1, 0.5, 1.0, 1.5, 2.0]  # Define your own bucket boundaries here
# @metrics.histogram('demo_click_duration_seconds', 'Duration of button click processing in seconds', buckets=custom_buckets)

@application.route("/histogram", methods=["POST"])
@metrics.histogram('demo_click_duration_seconds', 'Duration of button click processing in seconds')
def histogram():
    processing_time = random.uniform(0.1, 2.0)  # Adjust the range as needed
    time.sleep(processing_time)

    return {}


# Summary metric example
@application.route("/summary", methods=["POST"])
@metrics.summary('demo_seconds_summary', 'Summary of button click processing durations in seconds')
def summary():
    processing_time = random.uniform(0.1, 2.0)  # Adjust the range as needed
    time.sleep(processing_time)

    return {}
