print("033[0;1m")
ver = "VERSION:1.0 GUI:FALSE LANG:ENGLISH"
import os
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
os.system(clear)