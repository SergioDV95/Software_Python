import re
import pywhatkit as kit
import tkinter as tk
from tkinter import messagebox as exito


class Datos:
   
   def __init__(self, nombre, apellido, edad, numero, sexo, correo):
      self.nombre = nombre.title()
      self.apellido = apellido.title()
      self.edad = edad
      self.numero = numero
      self.sexo = sexo
      self.correo = correo
      self.mensaje = self.crearMensaje()
      self.entregado = False
   
   def crearMensaje(self):
      match self.sexo:
         case "femenino":
            return f"Hola {self.nombre}, bienvenida al espectacular mundo de la programación web"
         case "masculino":
            return f"Hola {self.nombre}, bienvenido al espectacular mundo de la programación web"
          
   def __str__(self):
      return f"\nNombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nSexo: {self.sexo}\nNúmero de teléfono: {self.numero}\nCorreo electrónico: {self.correo}\n"

def crearUsuario():
   ventana = tk.Tk()
   ventana.title("Registro de usuarios")
   Marco = tk.Frame(ventana, width = 500, height = 500)
   Marco.pack()

   Nombre = tk.Label(Marco, text = "Ingrese su primer nombre: ", font = ("Arial", 12))
   Nombre.grid(row=0, column=0)
   entradaNombre = tk.Entry(Marco)
   entradaNombre.grid(row=1, column=0)

   Apellido = tk.Label(Marco, text = "Ingrese su primer apellido: ", font = ("Arial", 12))
   Apellido.grid(row=2, column=0)
   entradaApellido = tk.Entry(Marco)
   entradaApellido.grid(row=3, column=0)

   Edad = tk.Label(Marco, text = "Ingrese su edad: ", font = ("Arial", 12))
   Edad.grid(row=4, column=0)
   entradaEdad = tk.Entry(Marco)
   entradaEdad.grid(row=5, column=0)

   Numero = tk.Label(Marco, text = "Ingrese su número de teléfono: ", font = ("Arial", 12))
   Numero.grid(row=6, column=0)
   entradaNumero = tk.Entry(Marco)
   entradaNumero.grid(row=7, column=0)

   Sexo = tk.Label(Marco, text = "Ingrese su sexo: ", font = ("Arial", 12))
   Sexo.grid(row=8, column=0)
   entradaSexo = tk.Entry(Marco)
   entradaSexo.grid(row=9, column=0)

   Correo = tk.Label(Marco, text = "Ingrese su correo electrónico: ", font = ("Arial", 12))
   Correo.grid(row=10, column=0)
   entradaCorreo = tk.Entry(Marco)
   entradaCorreo.grid(row=11, column=0)

   Boton = tk.Button(Marco, text="Registrar", command=lambda:guardarUsuario(entradaNombre, entradaApellido, entradaEdad, entradaNumero, entradaSexo, entradaCorreo, Marco))
   Boton.grid(row=12, column=0)

   ventana.bind('<Return>', lambda event: guardarUsuario(entradaNombre, entradaApellido, entradaEdad, entradaNumero, entradaSexo, entradaCorreo, Marco))

   ventana.mainloop()

usuarios = []
Errores = []
def guardarUsuario(entradaNombre, entradaApellido, entradaEdad, entradaNumero, entradaSexo, entradaCorreo, Marco):
   if Errores:
      for err in Errores:
         err.destroy()
      Errores.clear()
   Nombre = entradaNombre.get()
   Apellido = entradaApellido.get()
   Edad = entradaEdad.get()
   Numero = entradaNumero.get()
   Sexo = entradaSexo.get()
   Correo = entradaCorreo.get()
   if not Nombre == "" or not Apellido == "" or not Edad == "" or not Numero == "" or not Sexo == "" or not Correo == "":
      if not Nombre == "":
         if not re.search(r"^[a-zA-Z]+$", Nombre):
            errorNombre = tk.Label(Marco, text=f"Nombre inválido", font = ("Arial", 8), fg="red")
            errorNombre.grid(row=1, column=1)
            Errores.append(errorNombre)
      elif Nombre == "":
         errorNombre = tk.Label(Marco, text="Debe indicar el nombre", font = ("Arial", 8), fg="red")
         errorNombre.grid(row=1, column=1)
         Errores.append(errorNombre)
      if not Apellido == "":
         if not re.search(r"^[a-zA-Z]+$", Apellido):
            errorApellido = tk.Label(Marco, text=f"Apellido inválido", font = ("Arial", 8), fg="red")
            errorApellido.grid(row=3, column=1)
            Errores.append(errorApellido)
      elif Apellido == "":
         errorApellido = tk.Label(Marco, text="Debe indicar el apellido", font = ("Arial", 8), fg="red")
         errorApellido.grid(row=3, column=1)
         Errores.append(errorApellido)
      if not Edad == "":
         if not re.search(r"^\d{2} ?(años)?$", Edad):
            errorEdad = tk.Label(Marco, text=f"Edad inválida", font = ("Arial", 8), fg="red")
            errorEdad.grid(row=5, column=1)
            Errores.append(errorEdad)
      elif Edad == "":
         errorEdad = tk.Label(Marco, text="Debe indicar la edad", font = ("Arial", 8), fg="red")
         errorEdad.grid(row=5, column=1)
         Errores.append(errorEdad)
      if not Numero == "":
         if not re.search(r"^\+\d{2}(0\d{10}|\d{10})$", Numero):
            errorNumero = tk.Label(Marco, text=f"Número de teléfono inválido", font = ("Arial", 8), fg="red")
            errorNumero.grid(row=7, column=1)
            Errores.append(errorNumero)
      elif Numero == "":
         errorNumero = tk.Label(Marco, text="Debe indicar el número de teléfono", font = ("Arial", 8), fg="red")
         errorNumero.grid(row=7, column=1)
         Errores.append(errorNumero)
      M = r"^(m|masculino|var[oó]n|chico|hombre)$"
      F = r"^(f|femenino|hembra|chica|mujer)$"
      if not Sexo == "":
         if re.search(M, Sexo, re.IGNORECASE):
            Sexo = re.sub(M, "masculino", Sexo, flags = re.IGNORECASE)
         elif re.search(F, Sexo, re.IGNORECASE):
            Sexo = re.sub(F, "femenino", Sexo, flags = re.IGNORECASE)
         elif not re.search(M, Sexo, re.IGNORECASE) and not re.search(F, Sexo, re.IGNORECASE):
            errorSexo = tk.Label(Marco, text=f"Sexo inválido", font = ("Arial", 8), fg="red")
            errorSexo.grid(row=9, column=1)
            Errores.append(errorSexo)
      elif Sexo == "":
         errorSexo = tk.Label(Marco, text="Debe indicar el sexo", font = ("Arial", 8), fg="red")
         errorSexo.grid(row=9, column=1)
         Errores.append(errorSexo)
      if not Correo == "":
         if not re.search(r"^[^\s]+@[\w-]+\.[a-z]+(\.[a-z]+)*$", Correo):
            errorCorreo = tk.Label(Marco, text=f"Correo electrónico inválido", font = ("Arial", 8), fg="red")
            errorCorreo.grid(row=11, column=1)
            Errores.append(errorCorreo)
      elif Correo == "":
         errorCorreo = tk.Label(Marco, text="Debe indicar el correo electrónico", font = ("Arial", 8), fg="red")
         errorCorreo.grid(row=11, column=1)
         Errores.append(errorCorreo)
   else:
      errorDatos = tk.Label(Marco, text="Debe indicar todos los campos", font = ("Arial", 8), fg="red")
      errorDatos.grid(row=13, column=0)
      Errores.append(errorDatos)
   if len(Errores) == 0:
      exito.showinfo("Registro exitoso", "Sus datos se han registrado con éxito")

      usuario = Datos(Nombre, Apellido, Edad, Numero, Sexo, Correo)
      usuarios.append(usuario)
      for persona in usuarios:
         if not persona.entregado:
            kit.sendwhatmsg_instantly(persona.numero, persona.mensaje, 15, True)
            kit.send_mail("correo", "contraseña", "Mensaje desde Python", persona.mensaje, persona.correo)
            persona.entregado = True
      Info = [entradaNombre, entradaApellido, entradaEdad, entradaNumero, entradaSexo, entradaCorreo]
      for x in Info:
         x.delete(0, 'end')
      with open("./usuarios.txt", "a", encoding='utf-8') as file:
         file.write(str(usuario))

crearUsuario()