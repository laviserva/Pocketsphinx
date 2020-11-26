from ppf.Punctuation import *
from pocketsphinx import *
import os


"""
1.- Traducir el texto de pocketsphinx al ingles
2.- Puntuarlo
3.- Regresarlo al español

"""
class Puntuar:
    def __init__(self,filename="output"):
        self.path = get_data_path() + "/" + filename
        print("El nombre del path es :",self.path)
                
    def run(self):
        reading_file = open(self.path, "r",encoding='utf-8')
        print(reading_file)
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_file_content += stripped_line +"\n"
            new_file_content = new_file_content.replace("(0)", "")
            new_file_content = new_file_content.replace("(1)", "")
            new_file_content = new_file_content.replace("(2)", "")
            new_file_content = new_file_content.replace("(3)", " ")
            new_file_content = new_file_content.replace("(4)", "")
            new_file_content = new_file_content.replace("(5)", "")
            new_file_content = new_file_content.replace("(6)", "")
            new_file_content = new_file_content.replace("(7)", "")
            new_file_content = new_file_content.replace("(8)", "")
            new_file_content = new_file_content.replace("(9)", "")
            new_file_content = new_file_content.replace("<sil>", "")
            new_file_content = new_file_content.replace("<s>", "")
            new_file_content = new_file_content.replace("  ", " ")

            if new_file_content[0] == " ":
                new_file_content = new_file_content[1:]
        
        texto = Traduction('es','en',new_file_content)
        print("\nConversión de texto a inglés")
        print(str(texto))
        
        self.path_2 = self.path
        
        writing_file = open(self.path_2+"2", "w",encoding='utf-8')
        writing_file.write(texto)
        writing_file.close()
        
        print("Direccion de self.path_2+2:\n",self.path_2+"2")
        
        punctuation()
        
        reading_file = open(get_data_path() + "/output2.output", "r",encoding='utf-8')
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_file_content += stripped_line +"\n"
            new_file_content = new_file_content.replace("  ", " ")

            if new_file_content[0] == " ":
                new_file_content = new_file_content[1:]
        print("New file content: \n",new_file_content)
        texto = Traduction('en','es',new_file_content)
        print("\nConversión de texto a español\n")
        print(str(texto))
        
        reading_file.close()
        
        writing_file = open(get_data_path() + "/output2.output", "w",encoding='utf-8')
        writing_file.write(texto)
        writing_file.close()
        
        print("Se iniciará asistente\n")
        asistente()
        print("Se finalizó asistente")
        return
