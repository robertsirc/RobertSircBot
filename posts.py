import xml.etree.ElementTree
import datetime
from dataclasses import dataclass
from configuration import *
import requests


@dataclass
class Post:
    title: str
    link: str
    date: str


def get_all_post():
    response = requests.get(URL)
    return response.content.decode('utf-8')


def get_post_by_date(date):
    response = get_all_post()
    tree = xml.etree.ElementTree.fromstring(response)
    for item in tree.iter('item'):
        if date == datetime.datetime.strptime(item[2].text, DATE_FORMAT).date():
            return Post(item[0].text, item[1].text, item[2].text)
    return Post('', '', '')


def get_todays_post():
    current_date = datetime.datetime.today().date()
    return get_post_by_date(current_date)
