from fastapi import FastAPI
from funciones import developer
from funciones import userdata
from funciones import UserForGenre
from funciones import best_developer_year


app = FastAPI()

@app.get('/developer/{desarrollador}')
def get_developer(desarrollador: str):
    resultado = developer(desarrollador)
    return resultado

@app.get('/userdata/{user_id}')
def get_userdata(user_id: str):
    resultado = userdata(user_id)
    return resultado

@app.get('/UserForGenre/ {genero}')
def get_UserForGenre(genero:str):
    resultado = UserForGenre(genero)
    return resultado

@app.get('/best_developer_year/ {year}')
def get_best_developer_year(year:int):
    resultado = best_developer_year(year)
    return resultado

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)