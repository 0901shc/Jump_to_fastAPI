#database.py 파일은 데이터베이스와 관련된 설정과 연결을 담당하는 파일입니다.
#데이터베이스를 사용하기 위한 변수, 함수등을 정의하고 접속할 데이터베이스의 주소와 사용자, 비밀번호 등을 관리함.
#데이터베이스 연결 설정, ORM 모델 정의, 데이터베이스 세션 관리 등의 기능을 포함할 수 있습니다.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#데이터베이스 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db" 

#데이터베이스에 접속하는 세션수 제어
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#데이터베이스에 접속하기 위해 필요한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
