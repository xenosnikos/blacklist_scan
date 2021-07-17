from datetime import datetime
from helpers import common_strings
from helpers.mongo_connection import db


def blacklist_db_addition(value, output):
    db.blacklist.find_one_and_update({common_strings.strings['mongo_value']: value},
                                     {'$set': {'status': common_strings.strings['status_finished'],
                                               'timeStamp': datetime.utcnow(), 'output': output}})

