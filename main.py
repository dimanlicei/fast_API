from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO": "Березиков Дмитрий Алексеевич"}

@app.get('/users')
async def f_indexU():
    return {"+7": "9627931429"}

@app.get('/tools')
async def f_indexU():
    return {"Навыки": "С# c++ python html php java unity"}