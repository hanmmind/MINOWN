from sqlalchemy import create_engine,MetaData
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sql_configue import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


database = "sakila"
#连接到mysql数据库
engine = create_engine(f'mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}',encoding='utf-8')
metadata = MetaData()

Base = automap_base(metadata=metadata)
Base.prepare(engine, reflect=True)
Country = Base.classes.country
# 创建会话对象
Session = sessionmaker(bind=engine)
session = Session()

# 查询users表的所有数据
data = session.query(Country).all()
for result in data:
    print(result)