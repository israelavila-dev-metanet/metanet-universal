from fastapi import FastAPI
import uvicorn
import routeros_api
from fastapi.middleware.cors import CORSMiddleware
from mikrotik.maneger import MikrotikManager 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
manager = MikrotikManager("credenciales.json")


@app.on_event("startup")
def startup():

    manager.connect_all()
############################################################## get indentity of the router ##################################





@app.get("/")
def root():

    return {
        "status": "API funcionando"
    }

# @app.get("/mikrotik")
# def get_mikrotik():
#     return {
#         "mensaje": "OK"
#     }

@app.get("/mikrotik")
def get_mikrotik_connections():
    resultado = {}
    for router in manager.connections.keys():
        connection = manager.get_connection(router)
        resultado[router] = {
            "host": manager.routers[router]["host"],
            "username": manager.routers[router]["username"],
            "api_port": manager.routers[router].get("api_port", 8728),
            "ssl": manager.routers[router].get("ssl", False),
            "identity": connection.get_identity(),
            "version": connection.get_version(),
            "pppoe_users": connection.get_users_pppoe()      
        }

    return {
        "resultado": resultado
    }





if __name__ == "__main__":
    if uvicorn is None:
        raise RuntimeError("uvicorn is not installed. Please install it with: pip install uvicorn")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

