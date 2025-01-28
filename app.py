from flask import Flask, Response
import random
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

# Create Prometheus Gauges
acme_value = Gauge("acme_value", "Description of acme_value", ["pod"])
acme_value2 = Gauge("acme_value2", "Description of acme_value2", ["persistentvolumeclaim"])

@app.route("/metrics")
def metrics():
    # Update metrics with random values
    acme_value.labels(pod="cc3-testnet").set(random.randint(1, 5))
    acme_value2.labels(persistentvolumeclaim="node-storage-cc3-testnet").set(random.randint(1, 10))
    acme_value.labels(pod="cc3-mainnet").set(random.randint(1, 5))
    acme_value2.labels(persistentvolumeclaim="node-storage-cc3-mainnet").set(random.randint(1, 10))
    
    # Return the metrics
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
