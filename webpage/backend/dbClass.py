from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AboutMe(Base):
    __tablename__ = 'about_me'
    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey('user.id'))
    text = Column("text", String)


class ContactInfo(Base):
    __tablename__ = 'contact_info'
    id = Column("id", Integer, primary_key=True)
    github = Column("github", String)
    linkedin = Column("linkedin", String)
    website = Column("website", String)
    skype = Column("skype", String)
    email = Column("email", String)
    phone = Column("phone", String)
    address = Column("address", String)


class Education(Base):
    __tablename__ = 'education'
    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey('user.id'))
    title = Column("title", String)
    school = Column("school", String)
    startdate = Column("startdate", String)
    enddate = Column("enddate", String)
    user = relationship('User')


class Experience(Base):
    __tablename__ = 'experience'
    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey('user.id'))
    title = Column("title", String)
    company = Column("company", String)
    tasks = Column("tasks", String)
    startdate = Column("startdate", String)
    enddate = Column("enddate", String)
    user = relationship('User')


class Skills(Base):
    __tablename__ = 'skills'
    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey('user.id'))
    skill = Column("skill", String)
    level = Column("level", String)
    user = relationship('User')


class User(Base):
    __tablename__ = 'user'
    id = Column("id", Integer, primary_key=True)
    full_name = Column("full_name", String)
    title = Column("title", String)
    contact_info = Column("contact_info", String)
    contact = relationship('ContactInfo')
