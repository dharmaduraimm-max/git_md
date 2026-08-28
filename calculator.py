from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
	title="Calculator API",
	description="A simple calculator API using FastAPI",
	version="1.0.0",
)


class Calculation(BaseModel):
	num1: float
	num2: float
	operation: str


@app.get("/")
def home():
	return {
		"message": "Welcome to Calculator API",
		"docs": "/docs",
	}


@app.post("/calculate")
def calculate(data: Calculation):
	num1 = data.num1
	num2 = data.num2
	operation = data.operation.lower()

	if operation == "add":
		result = num1 + num2
	elif operation == "subtract":
		result = num1 - num2
	elif operation == "multiply":
		result = num1 * num2
	elif operation == "divide":
		if num2 == 0:
			raise HTTPException(status_code=400, detail="Cannot divide by zero")
		result = num1 / num2
	elif operation == "modulus":
		if num2 == 0:
			raise HTTPException(
				status_code=400,
				detail="Cannot calculate modulus with zero",
			)
		result = num1 % num2
	elif operation == "power":
		result = num1**num2
	else:
		raise HTTPException(
			status_code=400,
			detail=(
				"Invalid operation. Use add, subtract, multiply, divide, "
				"modulus, or power."
			),
		)

	return {
		"num1": num1,
		"num2": num2,
		"operation": operation,
		"result": result,
	}


if __name__ == "__main__":
	import uvicorn

	uvicorn.run(
		"calculator:app",
		host="127.0.0.1",
		port=8000,
		reload=True,
	)
