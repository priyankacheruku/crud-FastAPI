from fastapi import FastAPI

# from books 'package' imported  books 'file'/'APIRouter'
from book_store.books.books import router as books_router
from book_store.person.person_weight import router as person_router
from book_store.person.user import router as user_router
from book_store import login_router 
app = FastAPI()

app.include_router(books_router)
app.include_router(person_router)
app.include_router(user_router)
app.include_router(login_router)