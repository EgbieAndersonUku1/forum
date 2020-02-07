from flask_security import SQLAlchemyUserDatastore, Security

from create_app import db
from create_app import create_app
from registeration.form import RegistrationForm

from users.models import User, Role


app = create_app()

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=RegistrationForm)


if __name__ == "__main__":
    app.run()