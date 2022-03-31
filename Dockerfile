FROM python:3.9-alpine
COPY . /CRUD
RUN pip install -r /CRUD/stocks_products/requirements.txt
EXPOSE 80
