from config import create_app
from db import db

app = create_app()

# before_first_request
with app.app_context():
    db.init_app(app)

if __name__ == '__main__':
    app.run()
