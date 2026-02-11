import json
import os
from app.domain.models import Paciente, Doctor

class ClinicaService:
    def __init__(self):
        self.archivo = "datos.json"
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

    def obtener_pacientes(self):  
        return self._leer()["pacientes"]

    def actualizar_paciente(self, p_id: int, p_nuevo: Paciente): 
        data = self._leer()
        for i, p in enumerate(data["pacientes"]):
            if p["id"] == p_id:
                data["pacientes"][i] = p_nuevo.dict()
                self._guardar(data)
                return p_nuevo
        return None

    def eliminar_paciente(self, p_id: int):
        data = self._leer()
        original_len = len(data["pacientes"])
        data["pacientes"] = [p for p in data["pacientes"] if p["id"] != p_id]
        if len(data["pacientes"]) < original_len:
            self._guardar(data)
            return True
        return False
    
    