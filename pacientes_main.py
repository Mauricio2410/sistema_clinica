from fastapi import FastAPI, HTTPException
from app.domain.models import Paciente
from app.application.service import ClinicaService

app = FastAPI(title="Módulo de Gestión de Pacientes")
servicio = ClinicaService()

@app.post("/", tags=["Pacientes"])
def crear(p: Paciente):
    return servicio.registrar_paciente(p)

@app.get("/", tags=["Pacientes"])
def listar():
    return servicio.obtener_pacientes()

@app.put("/{p_id}", tags=["Pacientes"])
def editar(p_id: int, p: Paciente):
    res = servicio.actualizar_paciente(p_id, p)
    if not res: raise HTTPException(status_code=404, detail="No encontrado")
    return res

@app.delete("/{p_id}", tags=["Pacientes"])
def borrar(p_id: int):
    if not servicio.eliminar_paciente(p_id):
        raise HTTPException(status_code=404, detail="No existe")
    return {"status": "Eliminado"}