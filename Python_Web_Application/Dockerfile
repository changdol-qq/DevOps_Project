FROM ubuntu:jammy-20240405
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip install Flask  Flask-Bcrypt wtforms_alchemy Flask-Login Flask-WTF WTForms Flask-SQLAlchemy psycopg2-binary pytest
RUN apt-get install -y locales \
    && locale-gen ko_KR.UTF-8 \
    && update-locale LANG=ko_KR.UTF-8
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR:ko
ENV LC_ALL ko_KR.UTF-8
ENV FLASK_APP=run.py
COPY . /opt/
EXPOSE 5000
CMD ["python3", "/opt/run.py", "--host=0.0.0.0"]

