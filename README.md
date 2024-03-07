# Prometheus metrics examples

Built with:
- Python (Flask)
- Prometheus Flask Exporter (https://pypi.org/project/prometheus-flask-exporter/)

## Local istallation

### Virtual environment
```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### Running the app
```commandline
cd prometheus-metrics-example
pip install -r requirements.txt
mkdir tmp
export prometheus_multiproc_dir=tmp
gunicorn -c config.py -b 0.0.0.0:8000 server:application
```

### Deactivate the venv
```commandline
deactivate
```
