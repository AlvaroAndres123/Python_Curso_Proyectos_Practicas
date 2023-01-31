from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "!Hola Alvaro!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url":"https://almasoft.com.ni/"}

# Inicia el server: python -m uvicorn main:app --reload
# Detiene el server CTRL+C

# Documetacion con Swagger: http://127.0.0.1:800/docs
# Documetacion con Redocly: http://127.0.0.1:800/redoc
