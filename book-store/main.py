from fastapi import FastAPI

# from books 'package' imported  books 'file'/'APIRouter'
from app.books.books import router as books_router
from app.person.person_weight import router as person_router
app = FastAPI()

app.include_router(books_router)
app.include_router(person_router)