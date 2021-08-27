from fastapi import FastAPI

# from books 'package' imported  books 'file'/'APIRouter'
from book_store.books.books import router as books_router
from book_store.person.person_weight import router as person_router
app = FastAPI()

app.include_router(books_router)
app.include_router(person_router)