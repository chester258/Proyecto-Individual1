# Proyecto-Individual1

Este es el primer proyecto individual de Henry, donde llevare acabo el rol del data engineer, en el mismo realizare ciertas tareas requeridas, desarrolare una API, 
entre otros. En este readme explicare brevemente cada archivo que contiene el proyecto.

DATASET: En esta carpeta encontraremos los archivos csv de las 4 plataformas con las que trabajaremos

RATING: Esta carpeta contiene varios archivos con las reseñas de los usuarios, aparte contiene un jupiter notbook en donde se busco concatenarlos todas estas reseñas 
        en un csv en comun y se creo el csv 'score' donde calculamos el promedio del rating de cada pelicula basada en el promedio de las puntuaciones de cada pelicula 
        de los distintos usuarios, esto lo hicimos con el fin de cumplir los requisitos que se explicaran mas adelante.
        

ETL : En este jupiter notbook cargamos los csv de las plataformas, nos dimos una breve idea de lo que contienen y procedimos a hacer las transformaciones 
      requeridas, las mismas son las siguientes:
      
      Transformación de los datos:
      1- Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets 
         (ejemplo para títulos de Amazon = as123)

      * Despues de este primer paso se procedio a concatener todos los csv en el dataframe 'Peliculas-F(Final)' para hacer las siguiente transformaciones
        mas rapido y eficiente
      

      2- Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

      3- De haber fechas, deberán tener el formato AAAA-mm-dd

      4- Los campos de texto deberán estar en minúsculas, sin excepciones

      5- El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) 
          o season (temporadas)
      
      * Cada una de las transformaciones esta explicada paso a paso en el codigo
      
      -Finalmente se concateno al al csv 'Peliculas-F' la columna score( promedio de cada pelicula) del csv 'score', aca hubo varios problemas con los cambios de nombre 
      de esta carpeta, en el codigo se lo ve con el nombre de 'rating-final', pero el csv de la carpeta rating y el mostrado en primer plano, se llaman 'score' y 'rg_promedio'
      (obviamente me di cuenta de esto despues de cargarlo a git hub y poco antes del cierre de entrega)
      
      
EDA : En este jupiter estudiaremos el csv 'Peliculas final' mas en profundidad, donde nos damos una idea del contenido del csv, revisamos si tienen valores nulos 
      y cuales columnas las contienen; Estudiamos distintas variables como el 'type' donde hacemos distintas comparaciones de las peliculas con las series, estudiamos
      el  'score'(Rating de cada pelicula y serie), la correlacion de las variables numericas, la duracion de las peliculas, un top20 de las series con mas temporadas.
      Cada una de la misma trae consigo una conclusion.


csv Principales: Estos csv se dejaron en primer plano dado que son los csv principales con los que se trabaja luego para hacer la API, recuendo que hubo 
                 un error al nombrar el csv de rating


main.py: En este archivo.py llevaremos a cabo nuestra API, que busca disponibilizar los datos de la empresa usando el framework FastAPI. 
         Las consultas que se pueden hacer son:
          
          -get_max_duration : Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

          -get_score_count: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año 

          -get_count_platform: Cantidad de películas por plataforma con filtro de PLATAFORMA.

          -get_actor: Actor que más se repite según plataforma y año.


          * El Deployment esta hecho en deta


Este es el final del readme, espero que les haya gustado.
