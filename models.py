from database import Base
from sqlalchemy import Integer, String, TIMESTAMP, Column, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    id = Column(Integer, primary_key=True)
    os = Column(String)
    source = Column(String)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)


class Feed(Base):
    __tablename__ = "feed_action"
    action = Column(String)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    time = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user = relationship("User")
    post = relationship("Post")
