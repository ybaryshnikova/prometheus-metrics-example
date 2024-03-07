FROM nikolaik/python-nodejs:python3.8-nodejs14

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
#RUN npm install --prefix /app/demo_app/src --no-package-lock
#RUN npm run-script build --prefix /app/demo_app/src

ENV prometheus_multiproc_dir /tmp
EXPOSE 8000
CMD [ "gunicorn", "-c", "config.py", "-w", "4", "-b", "0.0.0.0:8000", "server"]
