import zipfile
import os
import arquivos as util_arq
import z_backup as util_zbackup

def unzip_para_padrao( pathBase , pathZip ):
    objZ = zipfile.ZipFile( pathZip , "r") 
    objZ.extractall( pathBase )
    objZ.close()
    


def file_para_padrao( pathBase ):
    util_zbackup.formatar( pathBase )

