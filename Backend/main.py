from fastapi import FastAPI # type: ignore

app = FastAPI(
	title="Shunya",
	description="Shunya is a smart data preprocessing tool that fills missing values in datasets using algorithms like regression and interpolation, ensuring clean and reliable data for analysis and machine learning.",
	version="1.0.0"
)

# Example root endpoint
@app.get("/")
def read_root():
	return {"message": "Welcome to Shunya - Smart Data Preprocessing Tool"}

# command to run the app: uvicorn main:app --reload