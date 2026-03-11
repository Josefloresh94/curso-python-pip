FROM python:3.14
#Le estamos indicando que queremos que todo el archivo se ejecute con esa versión

WORKDIR /app
#WORKDIR /app estamos creando la carpeta dentro del contenedor
COPY requirements.txt /app/requirements.txt

#Una buena práctica es copiar los archivos, el archivo de las dependencias,
#en este caso los archivos .txt, el cual vamos a pasar de local al entorno en el que estamos trabajando,
#Para eso usamos COPY. Seguidamente indicamos el archivo que queremos copiar y en donde lo queremos copiar (en el contenedor)


#En el campo del software una dependencia es una aplicación o una biblioteca requerida por otro programa
#para poder funcionar correctamente. Por ello se dice que dicho programa depende de tal aplicación o biblioteca.


RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#Con esto dejamos listo el archivo para su ejecución ya que instala las dependencias necesarias, las cuales se encuentran en requirement
#Si le agregas --no-cache-dir le dices que no agregue el caché
#Con --upgrade le dices que actualice las aplicaciones si encuentra alguna actualización, es buena práctica

COPY . /app
#Le pedimos que copie todo lo que está en la carpeta actual y que lo lleve al entrono que estamos creando.
CMD bash -c "while true; do sleep 1; done"
#Esto sirve para que el contenedor esté corriendo continuamente y o podamos conectar con el archivo docker