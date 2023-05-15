from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Board(Base):
    __tablename__ = "board"

    board_id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    board_name: Mapped[str] = mapped_column(String(50))


class PostIdTracker(Base):
    __tablename__ = "post_id_tracker"

    internal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    board_id: Mapped[int] = mapped_column(ForeignKey("board.board_id")) #FK Boards.board_id
    next_post_id: Mapped[int]

class Thread(Base):
    __tablename__ = "thread"

    internal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    post_id: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey("board.board_id")) #FK Boards.board_id
    subject: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(25))
    options: Mapped[str] = mapped_column(String(100))
    comment: Mapped[str] = mapped_column(String(2000))
    created_at: Mapped[str] = mapped_column(DateTime(), server_default="func.now()")

class Reply(Base):
    __tablename__ = "reply"

    internal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    post_id: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey("board.board_id")) #FK Thread.board_id not null
    thread_id: Mapped[int] = mapped_column(ForeignKey("thread.post_id")) #FK Thread.post_id not null
    comment: Mapped[str] = mapped_column(String(2000))
    created_at: Mapped[str] = mapped_column(DateTime(), server_default="func.now()")

"""
db = SQLAlchemy()

class Thread(db.Model):
    postID = db.Column(db.Integer)
    boardID = db.Column(db.Integer) FK Boards.boardID
    subject = db.Column(db.String(100))
    author = db.column(db.String(25))
    options = db.column(db.String(100))
    comment = db.column(db.String(2000))
    createdAt = db.column(db.DateTime(timezone=True), server_default=func.now())


class Reply(db.Model):
    postID = db.Column(db.Integer, nullable=False) 
    boardID = db.Column(db.Integer, nullable=False) FK Boards.boardID
    threadID = db.Column(db.Integer, nullable=False) FK Thread.postID
    comment = db.column(db.String(2000))
    createdAt = db.column(db.DateTime(timezone=True), server_default=func.now())


class PostIds(db.Model):
    boardID = db.column(db.Integer)
    nextPostID = db.column(db.Integer)


class Boards(db.Model):
    boardID = db.column(db.Integer)
    boardName = db.column(db.String(50))
"""