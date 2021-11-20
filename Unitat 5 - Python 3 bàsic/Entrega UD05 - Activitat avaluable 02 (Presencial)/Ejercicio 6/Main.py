import db
from Alumno import Alumno
from Profesor import Profesor
from Escuela import Escuela

def run():
    p1 = Profesor(nombre="Sebastián Rodríguez", tipo="otros")
    db.session.add(p1)
    db.session.commit()
    a1 = Alumno(nombre="Diego Fernández", curso="2ºDAM", profesor=p1.id, escuela=None)
    db.session.add(a1)
    e1 = Escuela(nombre="Serra Perenxisa", localidad="Torrent", responsable=p1.id)
    db.session.add(e1)
    db.session.commit()
    pass


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()

