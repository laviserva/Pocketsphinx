#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:05:54 2020
@author: lavi

This code was made for punctuation in pocketsphinx lib.

1.- Traslation from spanish to english and then add the punctuation
    Done
2.- Use gutemberg.DMP for punctuation
    
3.- Traslate back from english to spanish with the punctuation added

"""
from pocketsphinx import get_data_path

def Traduction(source, target, text):
    import requests
    """
    
    Traduce de un texto a otro.
    
    Parametros
    ----------
    source : Entrada
    target : Salida
    text : Texto
        
    Return
    -------
    
        español = 'es'
        ingles = 'en'
        
    ejemplo
    -------
    
        Traduccion('es','en',text)
        Traduce el string texto de español a ingles

    """
    parametros = {'sl': source, 'tl': target, 'q': text}
    cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
    url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
    response = requests.post(url, data=parametros, headers=cabeceras)
    if response.status_code == 200:
        for x in response.json()['sentences']:
            return x['trans']
    else:
        return "Error de parámetros (I,O,txt)"
    

def punctuation():

    import platform,os
    from pocketsphinx import get_data_path
    
    sistema = platform.system()
    
    if sistema == "Linux":
        print("Iniciando la puntuación")
        act_path = os.getcwd()
        os.chdir(get_data_path())
        
        try:
            actual_path = os.getcwd()
            print("\n\nActual path: ",actual_path)
            new_path = os.path.join(get_data_path() + "/ppf")
            print("\nnew_path: ",new_path)
            input_file = "'" + actual_path + "/output2" + "'"
            print("\ninput_file: ",input_file)
            lm_file = "'" + new_path + "/gutenberg.DMP" + "'"
            print("\nlm_file: ",lm_file)
            command = "sh ./postprocess.sh -input_file " + input_file + " -lm " + lm_file
            print("\n\nEl path del comando es : ",os.getcwd())
            os.chdir("ppf")
            print("\ncommand: ",command)
            
            os.system(command)
            os.chdir(act_path)
            print("\n\nTexto puntuado con exito")
        except:
            print("Error en el orden de archivos")
            
def asistente():
    nombres = ["rachael","siri","alexa","cortana","xochitl"]
    print(get_data_path() + "/output2.output")
    with open(get_data_path() + "/output2.output","r",encoding='utf-8') as f:
        first_line = f.readline()
        print(first_line)
        new_file_content = ""
        for line in f:
            stripped_line = line.strip()
            new_file_content += stripped_line +"\n"
        
        for i in nombres:
            if i in first_line.lower():
                #out_name ="{}/{}".format(os.getcwd(),i)
                out_name ="{}/{}".format(get_data_path(),i)
                print("Texto salida de asistente:\n",out_name)
                writing_file = open(out_name, "w",encoding='utf-8')
                writing_file.write(new_file_content)
                writing_file.close()
                break