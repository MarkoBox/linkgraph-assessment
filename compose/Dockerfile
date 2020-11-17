FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
# copied requirements
COPY requirements.txt /code/
RUN pip install -r requirements.txt
