# date_f.py
# Getting local datetime
# from requests import Response
from datetime import date
import datetime


def comic_date(gcck=True, dj=0):

    # gcck == True if gocomics, False if commicskingdom
    # dj == days from todaqy

    # get todays date
    today = date.today()
    assert isinstance(today, object)

    # days from today

    date_adj = str(today - datetime.timedelta(days=dj))

    # format date_adj
    if gcck == True:
        date_adj = date_adj.replace('-', '/')

    comic_date_str = date_adj
    return comic_date_str
