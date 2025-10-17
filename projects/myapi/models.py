# 파이보 프로젝트는 ORM을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다.
# SQLAlahemy는 모델 기반으로 데이터베이스를 처리한다. 

# 데이터가 생성되고 이를 저장하거나 조회 수정하는 등의 기능을 구현해야 한다.
# 웹 서비스는 데이터를 처리할 때 대부분 데이터 베이스를 사용한다.
# 데이터베이스를 사용하려면 SQL 쿼라문을 작성하고 실행하는 복잡한 과정이 필요하다.
# 그런데 ORM을 이용하면 파이썬 문법만으로도 데이터베이스를 다룰 수 있다.



from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# 질문 모델과 속성들
# __tablename__은 모델에 의해 관리되는 테이블의 이름
class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


# primary_key는 기본키임
# nullable는 null 값을 허용할건지 설정하는 값, False는 허용 안함
# relationship의 첫번째 파라미터는 참조할 모델명이고 두번째 파라미터는 역참조 설정이다.
class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # 데이터베이스에서는 기존 모델과 연결된 속성을 외부키(foreign key)라고 한다.
    question = relationship("Question", backref="answers")



