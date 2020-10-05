from peewee import *
import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath
import shutil
from datetime import datetime
import logging

db = SqliteDatabase('files.db')

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)


class File(Model):
    datetime = DateTimeField()
    name = TextField()

    class Meta:
        database = db


db.connect()
db.create_tables([File])

first_path = "first"
second_path = "second"

if __name__ == "__main__":
    try:
        for i in listdir(first_path):
            if isfile(joinpath(first_path, i)):
                shutil.move(f'{first_path}/{i}', f'{second_path}/{i}')
                datetime_now = datetime.now()
                File(datetime=datetime_now, name=f'{second_path}/{i}').save()
                logging.info(f'file "{i}" moved from folder "{first_path}" to folder "{second_path}",'
                             f' time {datetime_now}')
    except Exception as ex:
        logging.error(f'{str(ex)} - {datetime.now()}')
