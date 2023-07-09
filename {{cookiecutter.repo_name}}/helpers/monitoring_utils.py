from datetime import datetime

from dbconfig.sqlite3_script import create_user_logs


# █▀▀ ▄▀█ █░░ █░░ █▄▄ ▄▀█ █▀▀ █▄▀  ==
# █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▀█ █▄▄ █░█  ==

###################################################
# Functions for callbacks
###################################################


def user_logs(username, pathname):
    ct = datetime.now()
    user_logs = [
        {
            "username": username,
            "timestamp_recorded": ct,
            "trigger": pathname,
        }
    ]
    create_user_logs(user_logs)
    return None
