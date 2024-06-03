from pydantic import BaseModel
from datetime import datetime

class GuestEntry(BaseModel):
    name: str
    message: str

class GuestEntryDB(GuestEntry):
    id: int
    timestamp: datetime
