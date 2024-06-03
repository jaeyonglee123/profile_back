from fastapi import APIRouter, Path
from model import GuestEntry, GuestEntryDB
from datetime import datetime

guestbook_router = APIRouter()

guest_entries = []
entry_counter = 0

@guestbook_router.post("/guestbook")
async def add_entry(entry: GuestEntry) -> dict:
    global entry_counter
    entry_counter += 1
    new_entry = GuestEntryDB(id=entry_counter, timestamp=datetime.utcnow(), **entry.dict())
    guest_entries.append(new_entry)
    return {"msg": "Entry added successfully"}

@guestbook_router.get("/guestbook")
async def retrieve_entries() -> dict:
    return {"entries": guest_entries}

@guestbook_router.get("/guestbook/{entry_id}")
async def get_single_entry(entry_id: int = Path(..., title="The ID of the entry to retrieve")) -> dict:
    for entry in guest_entries:
        if entry.id == entry_id:
            return {"entry": entry}
    return {"msg": "No entry found with the given ID"}

@guestbook_router.delete("/guestbook/{entry_id}")
async def delete_entry(entry_id: int = Path(..., title="The ID of the entry to delete")) -> dict:
    for index, entry in enumerate(guest_entries):
        if entry.id == entry_id:
            del guest_entries[index]
            return {"msg": f"Entry with ID {entry_id} deleted successfully"}
    return {"msg": "No entry found with the given ID"}
