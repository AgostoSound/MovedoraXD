#______________ LIBRERIAS _________________________________
import os
import shutil

#______________ HARD CODE _________________________________
dir_input = 'C:/Users/Agosto/Desktop/Patin2021/Disney'
vec_direct = os.listdir(dir_input)
dir_output = 'C:/Users/Agosto/Desktop/Patin2021'

#______________ FUNCIONES _________________________________


#______________ PRINCIPAL _________________________________
def main():
    lista_temas = []
    for carpeta in vec_direct:
        intermedia = dir_input + '/' + carpeta
        sub = os.listdir(intermedia)
        contenedora = intermedia + '/' + sub[0]
        lista_temas.append(os.listdir(contenedora))

    for tracks in lista_temas:
        for t in tracks:
            dir_a_mover = contenedora + '/' + t
            dir_final = dir_output + '/'  + t
            shutil.move(dir_a_mover, dir_final)

main()

