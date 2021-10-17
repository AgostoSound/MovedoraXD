#______________ LIBRERIAS _________________________________
import os

#______________ HARD CODE _________________________________
dir_input = 'C:/Users/Agosto/Desktop/Patin2021/Disney'
vec_direct = os.listdir(dir_input)
dir_output = 'C:/Users/Agosto/Desktop/Patin2021'

#______________ FUNCIONES _________________________________

#______________ PRINCIPAL _________________________________
def main():
    for carpeta in vec_direct:
        print(carpeta)


main()

