# Librerías de kivy, la liberría encargada de mostrar la interfaz de usuario
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

import hashlib # Importamos la librería que nos va a permitir cambiar la contraseña a formato Hash

import os # Importamos la librería necesaria para trabajar con los ficheros y directorios del sistema operativo

import pandas as pd # Liberaría para leer ficheros csv

# Función encargada de leer los datos del fichero csv
def cargarUsuarios():
    df2 = pd.read_csv("users.csv", header=None) 
    return df2

# Codificamos una contraseña a sha1
def encriptar(password):
    sha1 = hashlib.sha1()
    key = password.encode('utf-8')
    sha1.update(key)
    return sha1.hexdigest()

datosCsv = cargarUsuarios() # Cargamos los usuarios y contraseñas de nuestro fichero csv
listadoUsuarios = datosCsv[0] # La primera columna contiene las usuarios
listadoContrasenas = datosCsv[1] # La segunda columna contiene las contraseñas


class Login(Screen):
    def do_login(self, loginText, passwordText, resultadoLogin):
        app = App.get_running_app()

        # Usuario y contraseña introducidos en la interfaz gráfica
        app.username = loginText
        app.password = encriptar(passwordText)

        # Antes de comprobar si el usuario y la contraseña son válidos comprobamos que han sido rellenados
        if(app.username != "" and app.password != ""):
            # Bucle for que se encarga de recorrer la lista de usuarios, asumimos que tendremos el mismo número de usuarios y contraseñas en el CSV
            for i in range(len(listadoUsuarios)):
                # Valores que contendrán el usuario y la contraseña de cada línea del fichero csv
                usuario = listadoUsuarios[i]
                contrasena = listadoContrasenas[i]

                # Comprobamos si el usuario y la contraseña introducidos coinciden con los de la itineración
                if(app.username == usuario and app.password == contrasena):
                     resultadoLogin.text = "OK"

                     '''
                        Usamos break para detener el bucle for. Esto es debido a que si, por ejemplo, tenemos varios usuarios
                        y los datos coinciden con el primero, indicaríamos que la operación ha ido correctamente, pero inmediatamente
                        después, compararíamos los datos con los siguientes usuarios y marcaríamos un error, machacando el resultado correcto.
                     '''
                     break
                else:
                    resultadoLogin.text = "ERROR: Revise su usuario y contraseña" # Si los datos no coinciden con los almacenados informaremos
        else:
            # Si el usuario y la contraseña no han sido rellenados lo indicaremos
            resultadoLogin.text = "ERROR: Indique un usuario y una contraseña"

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()