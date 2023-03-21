from fastapi import FastAPI
import pandas as pd


app = FastAPI(title='API',
              description='Estoy haciendo mi primera API')

df = pd.read_csv("Peliculas-F.csv")


@app.get("/")
def presentacion():
    return "Mi décima tercera api"


@app.get("/menu")
def menu():
    return ("Funciones de mi API: get_longest, get_score_count, get_count_platform, get_actor ")

#--------------------------------------------------

#Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y 
#TIPO DE DURACIÓN

@app.get("/get_longest/{plataforma}/{duration_type}/{ano}")
async def get_longest(plataforma: str, duration_type: str, ano: int):
    #lectura de la base de datos:
    df = pd.read_csv("Peliculas-F.csv")
    
    if plataforma == "amazon":
        plat = "a"
    elif plataforma == "disney":
        plat = "d"
    elif plataforma == "hulu":
        plat = "h"
    elif plataforma == "netflix":
        plat = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
        

    if  duration_type == 'min':
        dt = 'min'
    elif duration_type =='season' or 'seasons':
        dt = 'season'
    
    else:
        return  'El duration_type es invalido, las posibles opciones son:min, season/s' 

    

    mascara =(df['release_year']==ano) & (df['duration_type'].str.contains(dt)) & (df['id'].str.contains(plat))

    rta = df[mascara]

    if rta.empty:
        return ("No se han encontrado peliculas.")
    else:
        return rta[['title','duration_int','duration_type']].max().to_dict()
    
    
#--------------------------------------------------


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

@app.get('/get_score_count/{plataforma}/{scored}/{ano}')
async def get_score_count(platform:str, scored:float, ano:int):

    df = pd.read_csv("Peliculas-F.csv")
    
    if platform == "amazon":
        plat = "a"
    elif platform == "disney":
        plat = "d"
    elif platform == "hulu":
        plat = "h"
    elif platform == "netflix":
        plat = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")

    
    mascara =(df['release_year']== ano) & (df['score'] > scored) & (df['id'].str.contains(plat))
    rta = df[mascara].shape[0]

    return f"La cantidad de series/peliculas en {platform} con un puntaje mayor a {scored} en el año {ano} son en total {rta} "

#--------------------------------------------------

#Cantidad de películas por plataforma con filtro de PLATAFORMA.

@app.get('/get_count_platform/{plataforma}')

async def get_count_platform(platform:str):
    df = pd.read_csv("Peliculas-F.csv")
    
    if platform == "amazon":
        plat = "a"
    elif platform == "disney":
        plat = "d"
    elif platform == "hulu":
        plat = "h"
    elif platform == "netflix":
        plat = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
    

    mascara = df['id'].str.contains(plat)
    rta = df[mascara].shape[0]
    
    return f'La cantidad de series/peliculas que tiene {platform} es de: {rta}'



#--------------------------------------------------


#Actor que más se repite según plataforma y año

@app.get('/get_actor/{plataforma}/{year}')
async def get_actor(platform:str, year:int):
    df = pd.read_csv("Peliculas-F.csv")

    if platform == "amazon":
        plat = "a"
    elif platform == "disney":
        plat = "d"
    elif platform == "hulu":
        plat = "h"
    elif platform == "netflix":
        plat = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
    
    
        
    mascara = (df['id'].str.contains(plat)) & (df['release_year'] == year)

    df2 = df[mascara]

    df2 = df2[df2['cast'].isna() == False]

    listaR = df2['cast'].str.split(',')


    lista_actores_ind = []
    lista_actores_total = []
    lista_final = []


    for lista in listaR:
        for actor in lista:
            if actor not in lista_actores_ind:
                lista_actores_ind.append((actor))
            lista_actores_total.append(actor)
        

    for i in lista_actores_ind:
        lista_final.append([i,lista_actores_total.count(i)])

    
    df_actores = pd.DataFrame(lista_final,columns=['actor','repeticiones'])

    rta = df_actores.max()
    if df_actores.empty:
        return ("No se han encontrado registro de actores ese año.")
    else:
        return rta.to_dict()
    
#--------------------------------------------------


