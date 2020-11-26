#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wav_2_text import *
from text_cleaner import *

"""
Paso 1, convertir de voz a texto
"""
filename = "untitled.wav"
sd = SpeechDetector(filename)

try:
    texto = sd.run()
    
    """
    Paso 2, limpiar el texto
    """
    paso2 = Puntuar()
    paso2.run()
except (KeyboardInterrupt):
    print('\nGoodbye.')
    sys.exit()
except Exception as e:
    exc_type, exc_value, exc_tranceback = sys.exe_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2,
                              file=sys.stdout)
    sys.exit()