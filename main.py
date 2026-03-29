from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def firstday():
    return {"Message":"it works API"}

@app.get("/2ndday")
def secondday():
    return{"message":"i learned the same thing "}

