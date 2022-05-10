FROM python:latest
RUN mkdir -p firekeeper/
WORKDIR firekeeper/
COPY ./firekeeper .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "firekeeper.wsgi","--bind 0.0.0.0:8000","--timeout 500"]
