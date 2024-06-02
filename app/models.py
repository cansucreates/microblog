from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# The User class is a subclass of db.Model, a base class for all models from Flask-SQLAlchemy.
class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(128))
    
    # not a column, but a relationship to the Post class
    # The line `posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')` in the
    # `User` class is defining a relationship between the `User` and `Post` models in SQLAlchemy.
    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author') # This is a one-to-many relationship, as one user can have many posts.

    # The __repr__ method tells Python how to print objects of this class.
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)

    # not a column, but a relationship to the User class
    author: so.Mapped[User] = so.relationship(back_populates='posts') # This is a many-to-one relationship, as many posts can have one author.

    def __repr__(self):
        return '<Post {}>'.format(self.body)