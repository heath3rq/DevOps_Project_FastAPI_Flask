#!/usr/bin/env python3
from fastapi import FastAPI
import uvicorn
from menu import generatemenu 

app = FastAPI()

@app.get("/")
def root():
    """Returns default values when no input is given"""
    return generatemenu()


@app.get("/get_menu/{tip_percentage}/{tax_percentage}")
def search_return_price(tip_percentage: int, tax_percentage: int):
    """Returns commodity price based on commodity type and date"""
    result = generatemenu((tip_percentage/100),(tax_percentage/100))
    return result

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
