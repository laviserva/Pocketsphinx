# pocketsphinx  
Algoritmo de voz a texto realizado en python3

pasos para que funcione.  

1: instalar dependencias y pócketsphix.  
    -sudo apt-get install gcc automake autoconf libtool bison swig python-dev libpulse-dev.  
    <br>-python -m pip install --upgrade pip setuptools wheel<br/>
    <br>-pip install --upgrade pocketsphinx<br/>
<br>2: Entrar a python y encontrar la carpeta de los modelos y data; el retorno del siguiente codigo es el path.  <br/>
    from pocketsphinx import *  
    Path_model = get_model_path()  
    Path_data = get_data_path()  
3: Descargar el modelo español mexicano y decomprimir en el path de modelo.  
    -https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Mexican%20Spanish/  
    -Renombra la carpeta como 'es-mx'  
    -Renombra el archivo '581HCDCONT10000SPA.dict' como 'cmudict-es-mx.dict'  
    -Renombra el archivo '581HCDCONT10000SPA.lm.bin' como 'es-mx.lm.bin'  
4: Descargar carpeta ppf y ubicarla dentro de 2 rutas  
    1: La carpeta ubicada en "get_data_path()"  
    2: Donde se vaya a colocar el archivo main  
5: Descargar el archivo gutenberg.DMP y ponerlo dentro de la carpeta ppf dentro del path de "get_data_path()"  
    -https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Archive/English%20Gutenberg%20Postprocessing/  
6: Descargar archivo "main.py", "text_cleaner.py" y "wav_2_text.py"  
    - Colocar estos 3 archivos en una carpeta acompañado de la carpeta ppf como se indicó previamente
      
        
          
          
Para que funcione se debe tener esto en orden  
La entrada será un archivo .wav ubicado en get_data_path() el nombre y path puede definirse al cambiar la linea 10 del archivo main.py  
La salida será un archivo sin extensión ubicado en get_data_path() cuyo nombre será "output2.output" Para cambiar el nombre y el path de salida se debe cambiar la linea 67 del archivo text_clearner.py
Si se detecta un asistente; siri, alexa, rachael, xochitl etc. Se generará un archivo con el nombre del asistente por ejemplo "Siri", sin extensión, para modificar el nombre, y directorio de salida ir al archívo "Punctuation.py" y modificar la línea 100

Nota: Todos los path de los archivos y funciones están relacionados cualquier fallo está relacionada a una modificación en el orden.
