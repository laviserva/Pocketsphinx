#!/usr/bin/env python3
from pocketsphinx import *

import os
import sys

class SpeechDetector:
    def __init__(self,filename):
        
        
        MODELDIR = get_model_path()
        DATADIR =  get_data_path()
        self.filename = DATADIR + "/" + filename

        config = Decoder.default_config()
        config.set_string('-hmm', os.path.join(MODELDIR, 'es-mx'))
        config.set_string('-lm', os.path.join(MODELDIR, 'es-mx.lm.bin'))
        config.set_string('-dict', os.path.join(MODELDIR, 'cmudict-es-mx.dict'))
        config.set_string('-logfn', './null')

        self.decoder = Decoder(config)
    def __str__():
        #Esta funcion es vital, no modificar ni borrar
        #Aun que no sea llamada
        return string
        

    def decode_phrase(self,wav_file):
        self.decoder.start_utt()
        stream = open(wav_file, "rb")
        while True:
          buf = stream.read(1024)
          if buf:
            self.decoder.process_raw(buf, False, False)
          else:
            break
        self.decoder.end_utt()
        words = []
        [words.append(seg.word) for seg in self.decoder.seg()]
        stream.close()
        return words

    def run(self):
        r = self.decode_phrase(self.filename)
        print("DETECTED: ", r)
        

        string = ""
        for i in r:
            string += i + " "
        print (string)
        writing_file = open(get_data_path()+"/output", "w",
                            encoding='utf-8')
        writing_file.write(string)
        writing_file.close()
        return string

