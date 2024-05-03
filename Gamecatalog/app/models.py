from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
class Publisher(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64),index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120),index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128))
    posts: so.WriteOnlyMapped['Game'] = so.relationship(back_populates='author')
    def __repr__(self):
        return '<User {}>'.format(self.username)
class Game(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(140))
    releasedate: so.Mapped[str] = so.mapped_column(sa.String(150))
    user_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey(Publisher.id), index=True)
    gamename: so.Mapped[str] = so.mapped_column(sa.String(140))
    def __repr__(self):
        return '<Post {}>'.format(self.description) 