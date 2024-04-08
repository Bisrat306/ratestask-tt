import os
import unittest

from flask.cli import FlaskGroup
from flask_migrate import Migrate
from dotenv import load_dotenv

from app import create_app
from app.database import db

# Load environment variables 
load_dotenv()

config_name = os.getenv('ENV') or 'dev'
app = create_app(config_name)

migrate = Migrate(app, db)
cli = FlaskGroup(app)

@cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('tests', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
