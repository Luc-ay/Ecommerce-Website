from fastapi import FastAPI
from models import user_model, items_model
from config import database


app = FastAPI()


database.Base.metadata.create_all(bind=database.engine)
