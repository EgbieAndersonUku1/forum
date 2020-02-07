from flask import Blueprint, request, render_template
from flask_login import current_user
from sqlalchemy import desc

from create_app import db
from home.error import THREAD_CREATION_ERROR
from thread.form import NewThreadForm
from thread.model import Thread


home_app = Blueprint("home_app", __name__)
_THREAD_PER_PAGE = 5


@home_app.route("/<int:page_number>", methods=['GET', 'POST'])
@home_app.route("/", methods=['GET', 'POST'])
def home(page_number=1):
    """home(int) -> returns a render template

       When called takes the user to the main thread page

       :parameter
            page_number (int): Takes a page number and goes to that page number.
                               Default page number 1
    """
    form = NewThreadForm()
    error = None

    if current_user.is_active:
        submit = form.validate_on_submit()

        if request.method == "POST":
            if submit:
                _save_to_thread(form)
            else:
                error = THREAD_CREATION_ERROR

    threads = Thread.query.order_by(desc(Thread.id)).paginate(per_page=_THREAD_PER_PAGE, page=page_number, error_out=True)

    return render_template("index.html", form=form, error=error, threads=threads, current_user=current_user)


def _save_to_thread(form):
    """_save_to_thread(form obj) -> return None

    A private helper function that takes a flask form object and saves the data
    from that form thread object database.

    :parameter
        form: The flask-WTF form objects that contains the user data
    """
    new_thread = Thread(title=form.title.data, description=form.description.data,
                        created_by=current_user.username.title())
    db.session.add(new_thread)
    db.session.commit()
