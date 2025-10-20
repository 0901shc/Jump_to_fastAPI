#main.py 파일에서 생성한 app 객체는 FastAPI 클래스의 인스턴스입니다.
#app 객체를 통해 FastAPI 애플리케이션의 다양한 설정과 기능을 사용할 수 있습니다.
#main.py는 FastAPI 프로젝트의 전체적인 환경을 설정하는 파일임

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173", "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(question_router.router)
app.include_router(answer_router.router)
