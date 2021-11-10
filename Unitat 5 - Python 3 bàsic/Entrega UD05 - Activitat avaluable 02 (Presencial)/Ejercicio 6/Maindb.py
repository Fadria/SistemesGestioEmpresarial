import db
from Profesor import Profesor
from Alumno import Alumno
from Escuela import Escuela

def run():
    pass

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()