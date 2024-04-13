from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola desde FastAPI"}

@app.get("/sumar")
def sumar_numeros(numero1: int, numero2: int):
    resultado = numero1 + numero2
    return {"resultado": resultado}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


