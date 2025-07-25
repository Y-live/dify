from celery import states  # type: ignore

from libs.datetime_utils import naive_utc_now
from models.base import Base

from .engine import db


class CeleryTask(Base):
    """Task result/status."""

    __tablename__ = "celery_taskmeta"

    id = db.Column(db.Integer, db.Sequence("task_id_sequence"), primary_key=True, autoincrement=True)
    task_id = db.Column(db.String(155), unique=True)
    status = db.Column(db.String(50), default=states.PENDING)
    result = db.Column(db.PickleType, nullable=True)
    date_done = db.Column(
        db.DateTime,
        default=lambda: naive_utc_now(),
        onupdate=lambda: naive_utc_now(),
        nullable=True,
    )
    traceback = db.Column(db.Text, nullable=True)
    name = db.Column(db.String(155), nullable=True)
    args = db.Column(db.LargeBinary, nullable=True)
    kwargs = db.Column(db.LargeBinary, nullable=True)
    worker = db.Column(db.String(155), nullable=True)
    retries = db.Column(db.Integer, nullable=True)
    queue = db.Column(db.String(155), nullable=True)


class CeleryTaskSet(Base):
    """TaskSet result."""

    __tablename__ = "celery_tasksetmeta"

    id = db.Column(db.Integer, db.Sequence("taskset_id_sequence"), autoincrement=True, primary_key=True)
    taskset_id = db.Column(db.String(155), unique=True)
    result = db.Column(db.PickleType, nullable=True)
    date_done = db.Column(db.DateTime, default=lambda: naive_utc_now(), nullable=True)
