FROM python:3.8.0-alpine

ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/instagram_api_endpoints/

WORKDIR /usr/src/app/instagram_api_endpoints/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

#CMD ["python", "instagram_api.py"]