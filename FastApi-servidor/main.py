from fastapi import FastAPI
from funciones import developer
from funciones import userdata


app = FastAPI()

@app.get('/developer/{desarrollador}')
def get_developer(desarrollador: str):
    resultado = developer(desarrollador)
    return resultado

@app.get('/userdata/{user_id}')
def get_userdata(user_id: str):
    resultado = userdata(user_id)
    return resultado

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)