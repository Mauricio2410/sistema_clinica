from fastapi import FastAPI
from app.domain.models import Paciente, Doctor
from app.application.service import ClinicaService

app = FastAPI(title="Sistema de Gestión Clínica")
servicio = ClinicaService()

@app.post("/pacientes/", tags=["Pacientes"])
def crear_paciente(p: Paciente):
    return servicio.registrar_paciente(p)

@app.get("/pacientes/", tags=["Pacientes"])
def listar_pacientes():
    return servicio.obtener_pacientes()

@app.post("/doctores/", tags=["Doctores"])
def crear_doctor(d: Doctor):
    return servicio.registrar_doctor(d)

@app.get("/doctores/", tags=["Doctores"])
def listar_doctores():
    return servicio.obtener_doctores()