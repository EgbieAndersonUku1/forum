from flask import Blueprint, render_template, request, url_for, abort
from flask_login import current_user
from sqlalchemy import desc
from werkzeug.utils import redirect

from create_app import db
from reply.form import ReplyForm
from reply.model import Reply
from thread.model import Thread
from utils.secure_redirect import is_safe_url

thread_app = Blueprint("thread_app", __name__)
_REPLIES_PER_PAGE = 3


@thread_app.route("/thread/<int:thread_id>/<int:page_number>", methods=["GET"])
@thread_app.route("/thread/<int:thread_id>", methods=["GET"])
def main_thread(thread_id, page_number=1):

    thread = Thread.query.get_or_404(thread_id)
    form = ReplyForm()

    replies = Reply.query.filter_by(thread_id=thread_id).order_by(desc(Reply.id)) \
        .paginate(per_page=_REPLIES_PER_PAGE, page=page_number, error_out=True)

    return render_template("/thread/thread.html", thread=thread, replies=replies, form=form, page_number=page_number)


@thread_app.route("/thread/<int:thread_id>/<int:page_number>", methods=["POST"])
@thread_app.route("/thread/<int:thread_id>", methods=["POST"])
def new_thread(thread_id, page_number=1):

    form = ReplyForm()

    if current_user.is_active and request.method == "POST" and form.validate_on_submit():
        new_thread = Thread.query.get_or_404(thread_id)
        _save_to_thread(form, new_thread, thread_id)

    if not is_safe_url(url_for('thread_app.main_thread',  thread_id=thread_id, page_number=page_number)):
        abort(404)
    return redirect(url_for('thread_app.main_thread', thread_id=thread_id, page_number=page_number))


def _save_to_thread(form, thread, thread_id):
    reply = Reply(thread_id=thread_id, user_id=current_user.id, message=form.message.data)
    thread.replies.append(reply)
    db.session.commit()
