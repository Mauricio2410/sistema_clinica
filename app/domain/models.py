from pydantic import BaseModel

class Paciente(BaseModel):
    id: int
    nombre: str
    email: str

class Doctor(BaseModel):
    id: int
    nombre: str
    especialidad: str