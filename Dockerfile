FROM python:3.7

RUN pip install request
RUN pip install tweepy
RUN pip install schedule

RUN mkdir -p /var/RobertSircBot

WORKDIR /var/RobertSircBot

COPY ./ /var/RobertSircBot

ENTRYPOINT python /var/RobertSircBot/bot.py