def path_calculate( path:str , file:str )->str:
    return path + file

def get_file_name( path:str )->str:
    var = -1
    for i in reversed( range( 0 , len( path) ) ):
        if path[ i ] == "/":
            return path[ i + 1: ]
    
    return path