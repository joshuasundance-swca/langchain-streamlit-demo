FROM python:3.11-slim-buster

RUN adduser --uid 1001 --disabled-password --gecos '' appuser
USER 1001

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --user --upgrade pip
COPY ./requirements.txt /home/appuser/app/requirements.txt
RUN pip install --user -r /home/appuser/app/requirements.txt

CMD ["/bin/bash"]
