import os
import flask
from sqlalchemy import create_engine, select

from webpage.backend.dbClass import *

template_dir = os.path.abspath('../frontend')
# Create the application.
APP = flask.Flask(__name__, template_folder=template_dir)

# PyMySQL (dialect[+driver]://user:password@host/dbname)
engine = create_engine('mysql://root:my_sql_password@localhost:3306/resume')

# create session and add objects
with engine.connect() as conn:
    with conn.begin():
        q1 = select([User, ContactInfo, AboutMe],
                    User.id == 1 and AboutMe.user_id == User.id and ContactInfo.id == User.contact_info)
        q2 = select([Education], User.id == 1)
        q3 = select([Experience], User.id == 1)
        q4 = select([Skills], User.id == 1)
        r1 = conn.execute(q1)
        r2 = conn.execute(q2)
        r3 = conn.execute(q3)
        r4 = conn.execute(q4)

d, userInfo = {}, []
for row in r1:
    for column, value in enumerate(row):
        # build up the dictionary
        d = {**d, **{column: value}}
    userInfo.append(d)
print(userInfo)

d, educ = {}, []
for row in r2:
    for column, value in enumerate(row):
        # build up the dictionary
        d = {**d, **{column: value}}
    educ.append(d)
educ.reverse()
print(educ)

d, exp = {}, []
for row in r3:
    for column, value in enumerate(row):
        # build up the dictionary
        d = {**d, **{column: value}}
    exp.append(d)
exp.reverse()
print(exp)

d, skill = {}, []
for row in r4:
    for column, value in enumerate(row):
        # build up the dictionary
        d = {**d, **{column: value}}
    skill.append(d)
print(skill)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html', userInfo=userInfo, educ=educ, exp=exp, skill=skill)


if __name__ == '__main__':
    APP.debug = True
    APP.run()
