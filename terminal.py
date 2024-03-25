coldefault = "\033[0;1m"
colred = "\033[31;1m"
colgreen = "\033[32;1m"
colyellow = "\033[33;1m"
colblue = "\033[34;1m"
colpueple = "\033[35;1m"
colcyan = "\033[36;1m"

import os
import printf

def log(message = "", access = 0, color = coldefault, back = coldefault): 
    if access == 0:
        print(color, "LOG MESSAGE:", message, back)
    else:
        print(color, "LOG MESSAGE:", message, "LEVEL:", access,  back)

def warn(message, access = 0, color = colyellow, back = coldefault):
    if access == 0:
        print(color, "WARNING:", message, back)
    else:
        print(color, "WARNING:", message, "LEVEl:", access, back)

def error(message, access = 0, color = colred, back = coldefault):
    if access == 0:
        print(color, "ERROR:", message, back)
    else:
        print(color, "ERROR:", message, "LEVEl:", access, back)

def tell(message, access = 0, color = coldefault, back = coldefault):
    if access == 0:
        print(color, message, back)
    else:
        print(color, message, "LEVEl:", access, back)

def tip(message, access = 0, color = colcyan, back = coldefault):
    if access == 0:
        print(color, "TIP:", message, back)
    else:
        print(color, "TIP:", message, "LEVEl:", access, back)

def message(message, access = 0, color = colcyan, back = coldefault):
    if access == 0:
        print(color, "MESSAGE:", message, back)
    else:
        print(color, "MESSAGE:", message, "LEVEl:", access, back)

warn("DETECTED THAT GRACE IS STUPID")