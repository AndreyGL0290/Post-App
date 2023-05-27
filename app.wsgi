from dotenv import load_dotenv
from os import getenv

import sys
working_directory = '/var/www/Post-App'
sys.path.insert(0, working_directory)
load_dotenv(working_directory + '/.env')

activate_this = f"{working_directory}{getenv('ENV_ACT_FILE')}"
with open(activate_this) as file:
        exec(file.read(), dict(__file__=activate_this))

from app import app as application
