# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.

# Primero, debes abrir el folder donde se encuentra tu archivo de Python en la terminal de tu computadora.
# Para hacerlo, debes escribir el siguiente comando en la terminal de tu computadora
# cd ruta_de_tu_carpeta
# o desde Visual Studio Code, seleccionas Open Folder y seleccionas la carpeta 
# donde se encuentra tu archivo de Python

# Segundo, debes instalar un entorno virtual en tu computadora.
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta actual con el nombre .venv.

# Para activar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# .venv\Scripts\activate
# Para desactivar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# deactivate

# Tercero, debes instalar Streamlit en tu entorno virtual.
# pip install Streamlit 

# Cuarto, puedes abrir el tutorial de Streamlit en tu navegador.
# streamlit hello o python -m streamlit hello

# Quinto, debes abrir el archivo de Python en la terminal de tu computadora.
# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py o python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Blog Final Semestre 2024-02</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("IMG_8167.PNG", caption='Aquí puedes escribir una tiqueta debajo de la imagen', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Mi nombre es Ari Salas y estudio la carrera de Comunicación Audiovisual en la Pontificia Universidad Católica del Perú. Respecto a mi carrera, me gustaría ser capaz de comunicar efectivamente mis historias, ya que me especializo más en el área creativa. Quisiera que las audiencias pudieran sentirse identificadas con dichas historias. Considero que tener nociones de programación básicas es necesario para la promoción de dichos productos audiovisuales. En mi tiempo libre, me gusta mucho dibujar, por lo que me gustaría hacer un proyecto animado alguna vez. 

"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.

# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Al principio las funciones que utilizamos eran sencillas y eso hizo que el proceso de aprendizaje fuera más sencillo. Sin embargo, cometí errores puntuales en las prácticas ya que una de las dificultades para aprender a programar es que todo debe ser escrito de forma precisa y puesto de manera estratégica. Con el tiempo el proceso de programar se complejizó, pero considero que no me ha ido tan mal. Pienso que si hubiera notado mejor esos detalles que realmente sirven a la hora de escribir un código, los resultados obtenidos hubieran sido más óptimos. Programar me ha enseñado a conocer todo este mundo detrás de los programas que usamos siempre. Tener la capacidad de operarlos desde dentro es entretenido e interesante. Tener la habilidad de programar es un “plus” para el mundo tecnológico del que estamos rodeados actualmente, pues es una habilidad que necesitamos los futuros comunicadores. Por mi parte, voy a especializarme más en esta área puesto que considero que es una práctica que ayuda a solucionar problemas de forma efectiva. Esta es una complicación personal mía porque siempre he tenido el problema de fijarme bien en los detalles por lo que esto se refleja claramente en este campo. Lo que sí me gusta es que uno se siente capaz de crear todo tipo de códigos y ver cómo se construyen las cosas desde cero solo usando lenguaje informático. En el curso de Pensamiento Computacional me he especializado en Python y quisiera mejorar mis trabajos de programación en el futuro para tener la capacidad de lanzar páginas webs funcionales que pudieran tener una utilidad en el mercado actual. Considero que tener nociones de programación básicas es necesario para la promoción de dichos productos audiovisuales que quisiera realizar a futuro. En mi tiempo libre, me gusta mucho dibujar, por lo que me gustaría hacer un proyecto animado alguna vez. 

"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Explicación de un tema de las clases 📚") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)
st.video("video1578897823.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.


# Agregamos un enlace a la página web donde está el video.
enlace = f'<a href="https://drive.google.com/file/d/1y5zFUZ_tnaWSIw5HIc5b41uYXRUyj5fo/view?usp=sharing" target="_blank"><button>Nombre creativo para el botón</button></a>'
st.markdown(enlace, unsafe_allow_html=True)
# f'<a href="URL" target="_blank"><button>Nombre</button></a>':
# La etiqueta <a> se utiliza para crear un enlace en HTML.
# El atributo href se utiliza para especificar la URL de destino del enlace.
# El atributo target="_blank" se utiliza para abrir el enlace en una nueva pestaña del navegador.
# La etiqueta <button> se utiliza para crear un botón en HTML.
# El texto dentro de las etiquetas <button> ("Nombre creativo para el botón") es el contenido del botón.
# La variable enlace contiene la cadena de código HTML para el enlace y el botón.


# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Gráficos</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['Lenguas aisladas', 'Familias lingüísticas', 'Mapa de las lenguas sudamericanas']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Lenguas aisladas':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    sidebar.image("aisladas_base_datos.png", caption='Lenguas aisladas', width=500)
    pass
elif grafico_seleccionado == 'Familias lingüísticas':
    sidebar.markdown("<div style='text-align: justify'>Texto para la opción 2.</div>", unsafe_allow_html=True)
    sidebar.image("lengua_familia_GB.png", caption='Familias lingüísticas', width=500)
    pass
elif grafico_seleccionado == 'Mapa de las lenguas sudamericanas':
    sidebar.markdown("<div style='text-align: justify'>Texto para la opción 3.</div>", unsafe_allow_html=True)
    sidebar.image("mapa_familias_aisladas_S.jpg", caption='Mapa de las lenguas sudamericanas', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas': Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
