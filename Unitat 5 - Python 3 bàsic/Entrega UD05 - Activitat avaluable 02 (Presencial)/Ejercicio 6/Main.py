import db
from Alumno import Alumno
from Profesor import Profesor
from Escuela import Escuela

def run():
    a1 = Alumno(nombre="Diego Fernández", curso="2ºDAM")
    db.session.add(a1)
    db.session.commit()
    pass


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()

