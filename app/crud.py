from sqlalchemy.orm import Session
from . import models, schemas

def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote
