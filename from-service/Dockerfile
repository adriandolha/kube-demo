FROM python:3.6

RUN useradd demo

WORKDIR /home/demo
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt requirements.txt

COPY . .
RUN pip install /home/demo/
#COPY config /home/demo/.kube/config

ENV FLASK_APP app.py
COPY config .kube/config
RUN chown -R demo:demo /home/demo
USER demo

EXPOSE 8000
CMD ["gunicorn","-w","2","-b","0.0.0.0:8000","app:app","--log-level","debug",\
"--access-logfile","-",\
"--access-logformat", "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s %(f)s %(a)s","--log-syslog"]
