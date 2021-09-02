from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

# from books 'package' imported  books 'file'/'APIRouter'
from book_store.books.books import router as books_router
from book_store.person.person_weight import router as person_router
from book_store.person.user import router as user_router
from book_store import login_router 

from logging.config import dictConfig
from book_store.log_config import log_config
import logging


dictConfig(log_config)
logger = logging.getLogger("foo-logger")
# logging.config.fileConfig("log.log")

logger.info("Dummy Info")
logger.error("Dummy Error")
logger.debug("Dummy Debug")
logger.warning("Dummy Warning")

app = FastAPI()


app.include_router(books_router)
app.include_router(person_router)
app.include_router(user_router)
app.include_router(login_router)

import time



@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    response.headers["X-Process-Time"] = str(process_time)

    logger.info("url: "+ str(request.url)+"-->"+str(response.status_code))

    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

