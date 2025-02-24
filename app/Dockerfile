FROM python:3.13.0
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/app
WORKDIR /var/www
ADD requirements.txt /var/www
RUN pip install -r requirements.txt
CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000"]