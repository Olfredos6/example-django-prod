FROM python:3.10-slim
RUN apt update && apt upgrade
COPY ./requirements/local.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt
WORKDIR /app
# CMD tail -F x
CMD chmod +x run.sh && ./run.sh