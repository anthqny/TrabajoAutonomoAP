from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List

app = FastAPI()

sqlite_file_name = "database.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}")

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: Usuario):
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    with Session(engine) as session:
        return session.exec(select(Usuario)).all()

@app.get("/usuarios/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario

@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def actualizar_usuario(usuario_id: int, datos: Usuario):
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        usuario.nombre = datos.nombre
        usuario.email = datos.email
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        session.delete(usuario)
        session.commit()
        return {"mensaje": "Usuario eliminado"}

@app.post("/libros/", response_model=Libro)
def crear_libro(libro: Libro):
    with Session(engine) as session:
        session.add(libro)
        session.commit()
        session.refresh(libro)
        return libro

@app.get("/libros/", response_model=List[Libro])
def listar_libros():
    with Session(engine) as session:
        return session.exec(select(Libro)).all()

@app.get("/libros/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: int):
    with Session(engine) as session:
        libro = session.get(Libro, libro_id)
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return libro

@app.put("/libros/{libro_id}", response_model=Libro)
def actualizar_libro(libro_id: int, datos: Libro):
    with Session(engine) as session:
        libro = session.get(Libro, libro_id)
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        libro.titulo = datos.titulo
        libro.autor = datos.autor
        session.add(libro)
        session.commit()
        session.refresh(libro)
        return libro

@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    with Session(engine) as session:
        libro = session.get(Libro, libro_id)
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        session.delete(libro)
        session.commit()
        return {"mensaje": "Libro eliminado"}