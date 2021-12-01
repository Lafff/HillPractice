from fastapi import FastAPI
from fastapi import Form
from fastapi.responses import HTMLResponse, Response

import Hill4
import Hill3

import generator3
import generator4

app = FastAPI()



@app.get("/")
async def root():
    with open('index.html','r',encoding='utf-8') as file:
        html = file.read()
    return Response(content=html,media_type='text/html')


@app.post("/Hill")
async def solve(song: str = Form(...), keymatrix :str = Form(...)):
   keymatrix = list(map(int,keymatrix.split()))

   if len(keymatrix) == 9 :
       answer = Hill3.solve(song,keymatrix)
       return HTMLResponse(answer,media_type='text/html')
   if len(keymatrix) == 16 :
       answer = Hill4.solve(song,keymatrix)
       return HTMLResponse(answer,media_type='text/html')
   else:
       return HTMLResponse(content='Твоя матрица не 3 на 3 и не 4 на 4. Попробуй ввести заново.',media_type='text/html')

@app.post("/generate")
async def generate_matrix(size: str = Form(...)):
    if int(size) ==3:
       answer = await generator3.generate()
       result = 'Матрица в виде строки:' + answer
       return HTMLResponse(content=result,media_type='text/html')
    elif int(size) == 4:
        answer = await generator4.generate()
        result = 'Матрица в виде строки:' + answer
        print(result)
        return HTMLResponse(content=result,media_type='text/html')
    else:
        return Response(content='Ты ввел неверный размер',media_type='text/html')
