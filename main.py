from fastapi import FastAPI, HTTPException
from app.domain.models import Paciente, Doctor
from app.application.service import ClinicaService

app = FastAPI(title="Sistema de Gestión Clínica - CRUD Completo")
servicio = ClinicaService()

@app.get("/")
def home():
    return {"mensaje": "Servidor Clínico en línea"}

@app.post("/pacientes/", tags=["Pacientes"])
def crear_paciente(p: Paciente):
    return servicio.registrar_paciente(p)

@app.get("/pacientes/", tags=["Pacientes"])
def listar_pacientes():
    return servicio.obtener_pacientes()

@app.put("/pacientes/{p_id}", tags=["Pacientes"])
def editar_paciente(p_id: int, p: Paciente):
    res = servicio.actualizar_paciente(p_id, p)
    if not res: raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return res

@app.delete("/pacientes/{p_id}", tags=["Pacientes"])
def borrar_paciente(p_id: int):
    if not servicio.eliminar_paciente(p_id): raise HTTPException(status_code=404, detail="ID no existe")
    return {"status": "Eliminado"}

@app.post("/doctores/", tags=["Doctores"])
def crear_doctor(d: Doctor):
    return servicio.registrar_doctor(d)

@app.get("/doctores/", tags=["Doctores"])
def listar_doctores():
    return servicio.obtener_doctores()

@app.put("/doctores/{d_id}", tags=["Doctores"])
def editar_doctor(d_id: int, d: Doctor):
    res = servicio.actualizar_doctor(d_id, d)
    if not res: raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return res

@app.delete("/doctores/{d_id}", tags=["Doctores"])
def borrar_doctor(d_id: int):
    if not servicio.eliminar_doctor(d_id): raise HTTPException(status_code=404, detail="ID no existe")
    return {"status": "Eliminado"}