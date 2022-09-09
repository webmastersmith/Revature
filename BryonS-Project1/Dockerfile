FROM python:3.11.0b3-slim-bullseye

WORKDIR /flask-app
COPY ./requirements.txt /flask-app/requirements.txt

COPY ./app/* /flask-app/

# create venv environment
# RUN python3 -m venv .venv
# RUN . .venv/bin/activate
# install all requirements
RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]