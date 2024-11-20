from fastapi import FastAPI, HTTPException

app = FastAPI()

customers = [
    (0, "609-555-0124", "Karl"),
    (1, "609-555-1234", "Mike"),
    (3, "609-555-4302", "Ryan"),
]

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application. Use /customers/{id} to fetch customer data."}

@app.get("/customers/{id}")
async def get_customer(id: int):
    for customer in customers:
        if customer[0] == id:
            return {"id": customer[0], "phone": customer[1], "name": customer[2]}
    raise HTTPException(status_code=404, detail="Customer not found")