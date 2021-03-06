FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN mkdir -p /home/nginx/.cloudvolume/secrets && chown -R nginx /home/nginx && usermod -d /home/nginx -s /bin/bash nginx
COPY requirements.txt /app/.
RUN pip install numpy && \
    pip install -r requirements.txt
COPY timeout.conf /etc/nginx/conf.d/
COPY . /app
