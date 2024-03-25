import os
import tools
import printf
import terminal
coldefault = "\033[0;1m"
colred = "\033[31;1m"
colgreen = "\033[32;1m"
colyellow = "\033[33;1m"
colblue = "\033[34;1m"
colpueple = "\033[35;1m"
colcyan = "\033[36;1m"
kernel = os.name
if kernel == "nt":
    clear = "cls"
if kernel == "posix":
    clear = "clear"
print(coldefault)
os.system(clear)


