import requests # Librería necesaria para hacer peticiones

# Librerías de telegram
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler, Filters

# Updater que contiene el token de nuestro bot
updater = Updater(token='5064607143:AAHCtxEU16d91aQkqyTbznmmDfIc4VetHVc', use_context=True)
dispatcher = updater.dispatcher

def echo(update: Update, context: CallbackContext):
    mensajeRecibido = update.message.text # Mensaje introducido por el usuario en telegram
    datosRecibidos = mensajeRecibido.split(",") # Convertimos el mensaje en un array separando sus campos por cada coma
    operacion = datosRecibidos[0].lower() # Obtenemos la operación que el usuario desea realizar

    # Según la opción elegida por el usuario realizaremos unas acciones u otras
    if(operacion == "crear"):
        operacionCrear(context, update, datosRecibidos) # Función usada para crear socios
    elif(operacion == "modificar"):
        operacionModificar(context, update, datosRecibidos) # Función usada para modificar socios
    elif(operacion == "consultar"):
        operacionConsultar(context, update, datosRecibidos) # Función usada para consultar socios
    elif(operacion == "borrar"):
        operacionBorrar(context, update, datosRecibidos) # Función usada para eliminar socios
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error: el comando introducido no existe")

# Activamos nuestro bot
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()

# Función encargada de la operación de crear socio
def operacionCrear(context, update, datosRecibidos):
    if(len(datosRecibidos) != 4): # Si no disponemos de 4 datos informaremos de ello al usuario
        # El mensaje que verá el usuario en Telegram será el siguiente
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error: el número de datos introducidos es incorrecto")
    else:
        # Disponemos de 4 campos, el nombre de la operación y los tres siguientes
        nombreCampos = ["nombre","apellidos","num_socio"] # Nombre de los campos del socio
        valoresRecibidos = [] # Valores de los campos introducidos por el usuario
        valoresFormateados = [] # Valores formateados correctamente, quitando comillas a los campos
        datosCorrectos = True # Variable que nos indica si los datos son correctos, en caso de error cambiará a False

        for dato in datosRecibidos: # Foreach para comprobar cada uno de los datos recibidos
            if dato != datosRecibidos[0]: # El campo 0 es el nombre de la operación, queremos comprobar el resto
                datoSeparado = dato.split("=") # Separamos cada dato por el igual para obtener su valor
                if(len(datoSeparado) == 2): # Si tenemos dos datos uno será la clave y otro el valor
                    valoresRecibidos.append(datoSeparado[0]) # Añadimos el dato a nuestro array de valores
                    valorReal = datoSeparado[1].split('"') # Separamos las comillas del valor
                    if(len(valorReal) != 3): # El formato es incorrecto
                        datosCorrectos = False
                    else:
                        # Si tenemos comillas antes y después del valor, es correcto
                        if(valorReal[0]=="" and valorReal[1]!="" and valorReal[2]==""):
                            valoresFormateados.append(valorReal[1]) # Añadimos 1 valor correcto
                        else:
                            datosCorrectos = False # Datos incorrectos
                else:
                    datosCorrectos = False # Datos incorrectos
        
        # Si los datos son correctos enviaremos el valor a la API
        if(datosCorrectos): # Si no hemos detectado ningún fallo procederemos a la petición
            if(len(valoresRecibidos)== 3): # Para el POST necesitaremos 3 campos correctos
                # Comprobamos que la posición de ellos es la correcta
                if(valoresRecibidos[0] == nombreCampos[0] and valoresRecibidos[1] == nombreCampos[1] 
                and valoresRecibidos[2] == nombreCampos[2]):
                    try:
                        # Realizamos la petición
                        requests.post('http://localhost:8069/gestion/apirest/socio?data={"num_socio":"'
                        + valoresFormateados[2] + '", "nombre":"' + valoresFormateados[0] + '","apellidos":"' + 
                        valoresFormateados[1] + '"}' )

                        # Informamos de ello al usuario
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Socio creado satisfactoriamente.")
                    except:
                        # Si ha sucedido un error informaremos de ello al usuario
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Error: no se pudo crear el socio")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error: revise el mensaje introducido")

# Función encargada de la operación de modificar socio
def operacionModificar(context, update, datosRecibidos):
    if(len(datosRecibidos) != 4): # Si no disponemos de 4 datos informaremos de ello al usuario
        # El mensaje que verá el usuario en Telegram será el siguiente
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error: el número de datos introducidos es incorrecto")
    else:
        # Disponemos de 4 campos, el nombre de la operación y los tres siguientes
        nombreCampos = ["nombre","apellidos","num_socio"] # Nombre de los campos del socio
        valoresRecibidos = [] # Valores de los campos introducidos por el usuario
        valoresFormateados = [] # Valores formateados correctamente, quitando comillas a los campos
        datosCorrectos = True # Variable que nos indica si los datos son correctos, en caso de error cambiará a False

        for dato in datosRecibidos: # Foreach para comprobar cada uno de los datos recibidos
            if dato != datosRecibidos[0]: # El campo 0 es el nombre de la operación, queremos comprobar el resto
                datoSeparado = dato.split("=") # Separamos cada dato por el igual para obtener su valor
                if(len(datoSeparado) == 2): # Si tenemos dos datos uno será la clave y otro el valor
                    valoresRecibidos.append(datoSeparado[0]) # Añadimos el dato a nuestro array de valores
                    valorReal = datoSeparado[1].split('"') # Separamos las comillas del valor
                    if(len(valorReal) != 3): # El formato es incorrecto
                        datosCorrectos = False
                    else:
                        # Si tenemos comillas antes y después del valor, es correcto
                        if(valorReal[0]=="" and valorReal[1]!="" and valorReal[2]==""):
                            valoresFormateados.append(valorReal[1]) # Añadimos 1 valor correcto
                        else:
                            datosCorrectos = False # Datos incorrectos
                else:
                    datosCorrectos = False # Datos incorrectos
        
        # Si los datos son correctos enviaremos el valor a la API
        if(datosCorrectos): # Si no hemos detectado ningún fallo procederemos a la petición
            if(len(valoresRecibidos)== 3): # Para el PUT necesitaremos 3 campos correctos
                # Comprobamos que la posición de ellos es la correcta
                if(valoresRecibidos[0] == nombreCampos[0] and valoresRecibidos[1] == nombreCampos[1] 
                and valoresRecibidos[2] == nombreCampos[2]):
                    try:
                        # Realizamos la petición
                        requests.put('http://localhost:8069/gestion/apirest/socio?data={"num_socio":"'
                        + valoresFormateados[2] + '", "nombre":"' + valoresFormateados[0] + '","apellidos":"' + 
                        valoresFormateados[1] + '"}' )

                        # Informamos de ello al usuario
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Socio modificado satisfactoriamente.")
                    except:
                        # Si ha sucedido un error informaremos de ello al usuario
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Error: no se pudo modificar el socio")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error: revise el mensaje introducido")

# Función encargada de obtener los datos de un socio
def operacionConsultar(context, update, datosRecibidos):
    if(len(datosRecibidos) != 2): # Si no disponemos de 2 datos informaremos
        # El mensaje que verá el usuario en Telegram será el siguiente
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error: el número de datos introducidos es incorrecto")
    else:
        nombreCampo = None # Nombre del campo introducido
        valorCampo = None # Valor introducido por el usuario
        datosCorrectos = True # Variable que nos indica si los datos son correctos
        
        for dato in datosRecibidos: # Foreach para comprobar cada uno de los datos recibidos
            if dato != datosRecibidos[0]: # El campo 0 es el nombre de la operación, queremos comprobar el resto
                datoSeparado = dato.split("=") # Separamos cada dato por el igual para obtener su valor
                if(len(datoSeparado) == 2): # Si tenemos dos datos uno será la clave y otro el valor
                    nombreCampo = datoSeparado[0] # Actualizamos el nombre del campo
                    valorReal = datoSeparado[1].split('"')  # Separamos las comillas del valor
                    if(len(valorReal) != 3): # El formato es incorrecto
                        datosCorrectos = False # Datos incorrectos
                    else:
                        if(valorReal[0] == "" and valorReal[1] != "" and valorReal[2] == ""):
                            valorCampo = valorReal[1] # Actualizamos el valor del campo
                        else:
                            datosCorrectos = False # Datos incorrectos
                else:
                    datosCorrectos = False # Datos incorrectos

        # Si los datos son correctos enviaremos el valor a la API        
        if(datosCorrectos):
            if(nombreCampo == "num_socio"):
                try:
                    # Realizamos la petición
                    response = requests.get('http://localhost:8069/gestion/apirest/socio?data={"num_socio": "' + valorCampo + '"}')
                    jsonSocio = response.json() # JSON que contendrá los datos del socio
                    context.bot.send_message(chat_id=update.effective_chat.id, text=jsonSocio) # Mostramos el mensaje en telegram
                except:
                    # Si ha sucedido un error informaremos de ello al usuario
                    context.bot.send_message(chat_id=update.effective_chat.id, text="Error: no se ha localizado el número de socio introducido")                    
            else:
                # Si ha sucedido un error informaremos de ello al usuario
                context.bot.send_message(chat_id=update.effective_chat.id, text="Error: revise el mensaje introducido")
        else:
            # Si ha sucedido un error informaremos de ello al usuario
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error: revise el mensaje introducido")

# Función encargada de borrar de un socio
def operacionBorrar(context, update, datosRecibidos):
    if(len(datosRecibidos) != 2): # Si no disponemos de 2 datos informaremos
        # El mensaje que verá el usuario en Telegram será el siguiente
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error: el número de datos introducidos es incorrecto")
    else:
        nombreCampo = None # Nombre del campo introducido
        valorCampo = None # Valor introducido por el usuario
        datosCorrectos = True # Variable que nos indica si los datos son correctos
        
        for dato in datosRecibidos: # Foreach para comprobar cada uno de los datos recibidos
            if dato != datosRecibidos[0]: # El campo 0 es el nombre de la operación, queremos comprobar el resto
                datoSeparado = dato.split("=") # Separamos cada dato por el igual para obtener su valor
                if(len(datoSeparado) == 2): # Si tenemos dos datos uno será la clave y otro el valor
                    nombreCampo = datoSeparado[0] # Actualizamos el nombre del campo
                    valorReal = datoSeparado[1].split('"')  # Separamos las comillas del valor
                    if(len(valorReal) != 3): # El formato es incorrecto
                        datosCorrectos = False # Datos incorrectos
                    else:
                        if(valorReal[0] == "" and valorReal[1] != "" and valorReal[2] == ""):
                            valorCampo = valorReal[1] # Actualizamos el valor del campo
                        else:
                            datosCorrectos = False # Datos incorrectos
                else:
                    datosCorrectos = False # Datos incorrectos
        
        if(datosCorrectos):
            if(nombreCampo == "num_socio"):
                try:
                    # Realizamos la petición
                    response = requests.delete('http://localhost:8069/gestion/apirest/socio?data={"num_socio": "' + valorCampo + '"}')
                    jsonSocio = response.json() # JSON que contendrá los datos del socio
                    context.bot.send_message(chat_id=update.effective_chat.id, text=jsonSocio) # Mostramos el mensaje en telegram
                except:
                    # Si ha sucedido un error informaremos de ello al usuario
                    context.bot.send_message(chat_id=update.effective_chat.id, text="Error: no se ha localizado el número de socio introducido")                    
            else:
                # Si ha sucedido un error informaremos de ello al usuario
                context.bot.send_message(chat_id=update.effective_chat.id, text="Error: revise el mensaje introducido")
        else:
            # Si ha sucedido un error informaremos de ello al usuario
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error: revise el mensaje introducido")