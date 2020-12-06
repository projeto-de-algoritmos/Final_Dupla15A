FROM python:3.6
ENV PYTHONUNBUFFERED 1
# RUN mkdir -p /code
WORKDIR /code
ADD ./projeto_final /code
ADD ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt



EXPOSE 8000

CMD [ "bash entrypoint.sh" ]