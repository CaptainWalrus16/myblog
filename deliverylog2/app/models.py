from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64),index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120),index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128))
    deliveries: so.WriteOnlyMapped['Log'] = so.relationship(back_populates='worker')
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Log(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(300))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    worker: so.Mapped[User] = so.relationship(back_populates='deliveries')
    def __repr__(self):
        return '<Log {}>'.format(self.description)