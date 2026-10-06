import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def pagina_inicial(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

# Rotas para servir os arquivos de PWA
@app.get("/manifest.json")
def get_manifest():
    return FileResponse("templates/manifest.json", media_type="application/json")

@app.get("/sw.js")
def get_sw():
    return FileResponse("templates/sw.js", media_type="text/javascript")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)