from fastapi import FastAPI, HTTPException
from app.domain.models import Paciente, Doctor
from app.application.service import ClinicaService

app = FastAPI(title="Sistema Central de la Clínica")
servicio = ClinicaService()

app_pacientes = FastAPI(title="Módulo de Gestión de Pacientes")

@app_pacientes.post("/", tags=["Gestión de Pacientes"])
def crear_paciente(p: Paciente):
    return servicio.registrar_paciente(p)

@app_pacientes.get("/", tags=["Gestión de Pacientes"])
def listar_pacientes():
    return servicio.obtener_pacientes()

@app_pacientes.put("/{p_id}", tags=["Gestión de Pacientes"])
def editar_paciente(p_id: int, p: Paciente):
    res = servicio.actualizar_paciente(p_id, p)
    if not res: raise HTTPException(status_code=404, detail="No encontrado")
    return res

@app_pacientes.delete("/{p_id}", tags=["Gestión de Pacientes"])
def eliminar_paciente(p_id: int):
    if not servicio.eliminar_paciente(p_id):
        raise HTTPException(status_code=404, detail="ID no existe")
    return {"status": "Eliminado"}

app_doctores = FastAPI(title="Módulo de Gestión de Doctores")

@app_doctores.post("/", tags=["Gestión de Doctores"])
def crear_doctor(d: Doctor):
    return servicio.registrar_doctor(d)

@app_doctores.get("/", tags=["Gestión de Doctores"])
def listar_doctores():
    return servicio.obtener_doctores()

@app_doctores.put("/{d_id}", tags=["Gestión de Doctores"])
def editar_doctor(d_id: int, d: Doctor):
    res = servicio.actualizar_doctor(d_id, d)
    if not res: raise HTTPException(status_code=404, detail="No encontrado")
    return res

@app_doctores.delete("/{d_id}", tags=["Gestión de Doctores"])
def eliminar_doctor(d_id: int):
    if not servicio.eliminar_doctor(d_id):
        raise HTTPException(status_code=404, detail="ID no existe")
    return {"status": "Eliminado"}

app.mount("/pacientes_modulo", app_pacientes)
app.mount("/doctores_modulo", app_doctores)