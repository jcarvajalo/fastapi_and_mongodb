print("Hello Word")
from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API with FastaApi and mongodb",
    
    description='<img alt="Example" src="https://miro.medium.com/max/1400/1*NjrRKp89LuN5oIzNHBrvkQ.png"/> <h1>By: Jairo Alonso Carvajal Ochoa </h1>',
    version="0.0.1",
    terms_of_service="https://dsinno.io",
    contact={
        "name": "Desing System Inno",
        "url": "https://dsinno.io",
        "email": "desingsystem2020@gmail.com",
    },
    license_info={
        "name": "DSI 2.0",
        "url": "https://dsinno.io",
    },
    by = "Jairo Alonso Carvajal"
)
app.include_router(user)