import sqlalchemy as sa
import sqlalchemy.orm as saorm
import sqlalchemy.ext.declarative
import config

from sqlalchemy.orm import scoped_session

Base = sqlalchemy.ext.declarative.declarative_base()
db_engine = sa.create_engine(config.DATABASE_CONFIG['dburl'], echo=True, encoding='utf-8', pool_recycle=3600)
Session = saorm.sessionmaker(bind=db_engine)

session = Session()


class File(Base):
	__tablename__ = 'file'
	id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
	name = sa.Column(sa.String(256))
	target = sa.Column(sa.String(256))
	setting = sa.Column(sa.Text())
	content = sa.Column(sa.Text())


class Sentence(Base):
    __tablename__ = 'sentence'
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    text = sa.Column(sa.String(1024))
    file_id = sa.Column(sa.Integer(), sa.ForeignKey('file.id'))


class Ptask(Base):
    __tablename__ = 'ptask'
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    T = sa.Column(sa.String(64))
    V = sa.Column(sa.String(64))
    N = sa.Column(sa.String(64))
    D = sa.Column(sa.String(64))
    D1 = sa.Column(sa.String(64))
    D2 = sa.Column(sa.String(64))
    step = sa.Column(sa.String(1024))
    sentence_id = sa.Column(sa.Integer(), sa.ForeignKey('sentence.id'))


class Scenarios(Base):
	__tablename__ = 'scenarios'
	id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
	name = sa.Column(sa.String(256))
	envt = sa.Column(sa.String(64))


class Testruns(Base):
    __tablename__ = 'testruns'
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    extid = sa.Column(sa.String(256))
    scenario_id = sa.Column(sa.Integer(), sa.ForeignKey('scenarios.id'))
    date = sa.Column(sa.Date())

class Execdetails(Base):
    __tablename__ = 'execdetails'
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    T = sa.Column(sa.String(64))
    N = sa.Column(sa.String(64))
    D2 = sa.Column(sa.String(64))
    step = sa.Column(sa.String(1024))
    passfail = sa.Column(sa.String(2))
    comments = sa.Column(sa.String(1024))
    file_id = sa.Column(sa.Integer(), sa.ForeignKey('File.id'))
    testrun_id = sa.Column(sa.Integer(), sa.ForeignKey('testruns.id'))

class Scripts(Base):
    __tablename__ = 'scripts'
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    name = sa.Column(sa.String(256))
    webapp = sa.Column(sa.String(6))
    base_url = sa.Column(sa.String(256))
    file_id = sa.Column(sa.Integer(), sa.ForeignKey('File.id'))
