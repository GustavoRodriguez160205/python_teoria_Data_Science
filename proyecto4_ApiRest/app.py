from typing import List, Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Definimos el modelo de datos para los cursos
class Curso(BaseModel):
    id: str 
    nombre: str  
    descripcion: Optional[str] = None  
    nivel: str  
    duracion: int 

# Simulamos una base de datos de cursos como una lista vacía
db_cursos: List[Curso] = []  # Añadimos el tipo a la lista para mayor claridad

# GET para obtener la lista completa de cursos
@app.get('/cursos/', response_model=List[Curso])
def obtener_cursos():
    return db_cursos

# POST para agregar un nuevo curso
@app.post('/cursos/', response_model=Curso)
def crear_curso(curso: Curso):
    # Asignamos un ID único al curso
    curso.id = str(uuid.uuid4())  # Llamamos a uuid.uuid4() correctamente
    db_cursos.append(curso)
    return curso

# GET para obtener un curso específico por su ID
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    # Buscamos el curso por su ID
    curso = next((curso for curso in db_cursos if curso.id == curso_id), None)
    if curso is None:
        # Si no se encuentra, lanzamos una excepción 404
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

# PUT para actualizar un curso existente por su ID
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    # Buscamos el curso por su ID
    curso = next((curso for curso in db_cursos if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    # Mantenemos el mismo ID y actualizamos los datos
    curso_actualizado.id = curso_id
    # Buscamos el índice del curso en la base de datos para reemplazarlo
    index = db_cursos.index(curso)
    db_cursos[index] = curso_actualizado
    return curso_actualizado

# DELETE para eliminar un curso por su ID
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):
    # Buscamos el curso por su ID
    curso = next((curso for curso in db_cursos if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    # Eliminamos el curso de la base de datos
    db_cursos.remove(curso)  # Asegúrate de usar remove() correctamente
    return curso
