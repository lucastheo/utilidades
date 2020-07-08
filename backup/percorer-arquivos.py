import os 
import sys
import fora_da_lei
import z_backup


def percorrer_arquivos_com_zip( path_base ):    
    
    print("Parte zip")
    cont_0 = 0
    #for (dirpath, dirnames, filenames) in os.walk(path_base):
    #    for f in filenames:
    #        path = os.path.join(dirpath, f)
    #        if os.path.isdir( path ) == False:
    #            
    #            if path.endswith( ".zip"):
    #                fora_da_lei.unzip_para_padrao( dirpath , path )
    #                os.remove( path )
    #                cont_0 += 1
    #                print( cont_0 )
    
    print("Parte arquivos")
    cont_0 = 0  
    for (dirpath, dirnames, filenames) in os.walk(path_base):
        for f in filenames:
            path = os.path.join(dirpath, f)
            if os.path.isdir( path ) == False:
                if path.endswith( z_backup.EXTENCAO) == False and path.endswith(".zip") == False:
                    try:
                        fora_da_lei.file_para_padrao( path )
                        os.remove( path )
                    except:
                        print("Erro em" , path )
            cont_0 += 1
            if cont_0 % 5000 == 0:
                print( cont_0 , path )

if __name__ == "__main__":
    percorrer_arquivos_com_zip( "/run/media/lucathe/teste/backupHdExterno/regu-algo/regulacaoAlgoritmo")