from fastapi import FastAPI, HTTPException
from app.domain.models import Doctor
from app.application.service import ClinicaService

app = FastAPI(title="Módulo de Gestión de Doctores")
servicio = ClinicaService()

@app.post("/", tags=["Doctores"])
def crear(d: Doctor):
    return servicio.registrar_doctor(d)

@app.get("/", tags=["Doctores"])
def listar():
    return servicio.obtener_doctores()

@app.put("/{d_id}", tags=["Doctores"])
def editar(d_id: int, d: Doctor):
    res = servicio.actualizar_doctor(d_id, d)
    if not res: raise HTTPException(status_code=404, detail="No encontrado")
    return res

@app.delete("/{d_id}", tags=["Doctores"])
def borrar(d_id: int):
    if not servicio.eliminar_doctor(d_id):
        raise HTTPException(status_code=404, detail="No existe")
    return {"status": "Eliminado"}