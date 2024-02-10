
#     
#|      |
#|      |  
#+------+ fill=60%
#|      |
#|      |
#|      |
#+------+
fill=80
import os
os.system("cls")

for n in range(10):
    if int((100-fill)/10)==n:
        print(f"+-----+  >>> {fill}%")
    print("|     |")

print(("+-----+"))