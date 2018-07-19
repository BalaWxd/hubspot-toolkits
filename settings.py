from dotenv import load_dotenv
import click
import os

load_dotenv()

# OR, the same with increased verbosity:
# load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


API_KEY = os.getenv("API_KEY")
