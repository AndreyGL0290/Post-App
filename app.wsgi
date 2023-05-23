from dotenv import load_dotenv
load_dotenv()

from os import getenv

import sys
sys.path.insert(0, getenv('WORKING_DIRECTORY'))

activate_this = f"{getenv('WORKING_DIRECTORY')}{getenv('ENV_ACT_FILE')}"
with open(activate_this) as file:
        exec(file.read(), dict(__file__=activate_this))
from app import app as application
