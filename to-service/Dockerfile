FROM python:3.6

RUN useradd demo

WORKDIR /home/demo

COPY requirements.txt requirements.txt

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install /home/demo/

ENV FLASK_APP app.py
RUN chown -R demo:demo /home/demo
USER demo

EXPOSE 8000
CMD ["gunicorn","-w","2","-b","0.0.0.0:8000","app:app","--log-level","debug",\
"--access-logfile","-",\
"--access-logformat", "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s %(f)s %(a)s","--log-syslog"]
