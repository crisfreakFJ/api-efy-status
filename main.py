from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import resultados_correo
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]    
)

@app.get("/")
async def root():
    return {"message": "Hello Word!"}
   
app.include_router(resultados_correo.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5002, reload=True)