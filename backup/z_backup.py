import json
import zipfile
import arquivos 

ZIP_PATH_INFO = "info.json"
ZIP_PATH_FILE = "file"
EXTENCAO = ".zbackup"

def gerando_arquivo_info( file_name:str ):
    var1 = dict()
    var1["name"] = file_name
    objJ = json.dumps( var1 )
    return objJ

def verica_caminho( path_base:str , file_name:str ):
    if len( file_name ) > 100:
        var = file_name[:100] + EXTENCAO
    else:
        var = file_name + EXTENCAO
    return path_base[:len( path_base ) - len( file_name )] + var

def extraindo( path_base:str )->None:
    file_name = arquivos.get_file_name( path_base )
    file_name_zip = verica_caminho( path_base , file_name )
    objZ = zipfile.ZipFile(  file_name_zip , "r" , compression=zipfile.ZIP_BZIP2 , compresslevel=9)
    objZ.write( path_base , ZIP_PATH_FILE )
    objZ.writestr(ZIP_PATH_INFO, gerando_arquivo_info( file_name ) )
    objZ.close()

def formatar( path_base:str )->None:
    file_name = arquivos.get_file_name( path_base )
    file_name_zip = verica_caminho( path_base , file_name )
    objZ = zipfile.ZipFile(  file_name_zip , "w" , compression=zipfile.ZIP_BZIP2 , compresslevel=9)
    objZ.write( path_base , ZIP_PATH_FILE )
    objZ.writestr(ZIP_PATH_INFO, gerando_arquivo_info( file_name ) )
    objZ.close()

