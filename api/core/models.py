from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy_serializer import SerializerMixin

class Base(DeclarativeBase, SerializerMixin):
    pass

class Board(Base):
    __tablename__ = "board"

    # See if this can be made into composite PK
    board_id: Mapped[str] = mapped_column(String(8), primary_key=True, nullable=True)
    board_name: Mapped[str] = mapped_column(String(50))


class PostIdTracker(Base):
    __tablename__ = "post_id_tracker"

    internal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    board_id: Mapped[str] = mapped_column(ForeignKey("board.board_id"))
    next_post_id: Mapped[int]

class Thread(Base):
    __tablename__ = "thread"

    # Required because post_id can overlap between boards
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

    # Required because post_id can overlap between boards
    internal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    post_id: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey("board.board_id")) #FK Thread.board_id not null
    thread_id: Mapped[int] = mapped_column(ForeignKey("thread.post_id")) #FK Thread.post_id not null
    comment: Mapped[str] = mapped_column(String(2000))
    created_at: Mapped[str] = mapped_column(DateTime(), server_default="func.now()")

class Image(Base):
    __tablename__ = "image"

    internal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    image_binary: Mapped[str] = mapped_column(String(1000))
