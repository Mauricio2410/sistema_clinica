import json
import os
# Importamos los modelos desde la capa de dominio
from app.domain.models import Paciente, Doctor

class ClinicaService:
    def __init__(self):
        self.archivo = "datos.json"
        # Si el archivo no existe, lo creamos con estructura básica
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump({"pacientes": [], "doctores": []}, f)

    def _guardar(self, data):
        with open(self.archivo, 'w') as f:
            json.dump(data, f, indent=4)

    def _leer(self):
        with open(self.archivo, 'r') as f:
            return json.load(f)

    def registrar_paciente(self, p: Paciente):
        data = self._leer()
        data["pacientes"].append(p.dict())
        self._guardar(data)
        return p

    def registrar_doctor(self, d: Doctor):
        data = self._leer()
        data["doctores"].append(d.dict())
        self._guardar(data)
        return d

    def obtener_pacientes(self):
        return self._leer()["pacientes"]

    def obtener_doctores(self):
        return self._leer()["doctores"]