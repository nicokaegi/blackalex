FROM python:latest
RUN mkdir -p firekeeper/
RUN mkdir /blackalex
WORKDIR firekeeper/
COPY ./firekeeper .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["bash","start.sh"]
