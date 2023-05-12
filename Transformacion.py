import pandas as pd
import numpy as np
import datetime

def calado_eslora_100m(df, columna_calado, columna_eslora, nueva_columna):
    """ Esta función nos creará una columna en un dataframe con la relación calado/eslora, para un buque medio de 100m. 
        Con este resultado podremos comparar estimaciones de quan cargados estan los buques """
    df[nueva_columna] = (df[columna_calado])/(df[columna_eslora])*100
    return df


def tiempo_eslora_100m(df, eslora, horas, nueva_columna):
    """ Esta función nos creará una columna en un dataframe con la relación tiempo de operaciones / eslora,
        para un buque medio de 100m. Con este resultado podremos comparar la rapidez de carga de cada terminal por 100m de eslora """
    df[nueva_columna] = (df[horas])/(df[eslora])*100
    return df


def transformacion_escalas(year):
    """ Esta función nos dará el dataframe que necesitamos por año de escala, 
        obteniendo los datos de todas las escalas en puerto de BCN durante ese año """

    path = (f"/Users/xavi/Documents/Ironhack/Projects/BCN_terminals_project/Escalas puerto BCN/Llegadas/escales_arribades_{year}.csv")
    df = pd.read_csv(path)
    
    # Eliminamos las columnas que no necesitamos
    columnas_a_eliminar = ["TERMINALCODI","MESINFO","ETAHORA","ETDHORA","ETADIA","MOLLCODI","ESCALAESTAT","ESTOPERATIUID","MOLLMODULS","ETDDIA","ETA", "ETD"]
    df.drop(columns=columnas_a_eliminar, inplace=True)
    
    # Convertimos a formato datetime las llegadas y salidas de los buques:
    df["ETDUTC"] = pd.to_datetime(df["ETDUTC"])
    df["ETAUTC"] = pd.to_datetime(df["ETAUTC"]) 
    
    # Obtenemos las horas de operaciones de los buques:
    segundos_operaciones = (df["ETDUTC"] - df["ETAUTC"]).dt.total_seconds()
    horas_operaciones = segundos_operaciones / 3600
 
    #añadimos al df la columna horas_operaciones:
    df["HORASOPERACIONES"] = horas_operaciones

    # Añadimos al dataframe el mes en que operó el buque:
    df["NUM_MES"] = df["ETAUTC"].dt.month.astype(int)

    df["MESESCALA"] =  df["NUM_MES"].map({
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    })

    # Extraemos el primer número del número de escalas:
    df["ESCALANUM"] = df["ESCALANUM"].str.extract('(\d+)')

    # Cambiamos a tipo int la columna MMSI:
    df["MMSI"] = df["MMSI"].fillna(0)
    df["MMSI"] = df["MMSI"].astype(int)

    # Cambiamos a tipo float las columnas ESLORA_METRES, CALAT_METRES, MANEGA_METRES:
    df["ESLORA_METRES"] = df["ESLORA_METRES"].str.replace(",",".").astype(float)
    df["CALAT_METRES"] = df["CALAT_METRES"].str.replace(",",".").astype(float)
    df["MANEGA_METRES"] = df["MANEGA_METRES"].str.replace(",",".").astype(float)

    # Reorganizamos las columnas del dataframe
    df = df[["ESCALANUM", "ANYESCALA", "NUM_MES","MESESCALA","VAIXELLNOM", "VAIXELLBANDERACODI", "VAIXELLBANDERANOM", "MMSI", "IMO","CALLSIGN", "ESLORA_METRES", "CALAT_METRES", "MANEGA_METRES", "VAIXELLTIPUS", "TERMINALNOM", "ETAUTC", "ETDUTC", "HORASOPERACIONES", "PORTORIGENCODI", "PORTORIGENNOM","PORTDESTICODI", "PORTDESTINOM"]]
    
    # Cambiamos el nombre a APM para que aparezca siempre igual:
    df['TERMINALNOM'] = df['TERMINALNOM'].replace('.*APM.*', 'APMT BARCELONA', regex=True)

    # Cambiamos en nombre de "TERMINAL CATALUNYA SA" por lo mismo:
    df['TERMINALNOM'] = df['TERMINALNOM'].replace('.*TERMINAL CATALUNYA SA*.', 'BEST', regex=True)
    return df


def Shipname(x):
    if len(x) == 1:
        result = x[0]
    elif len(x) == 2:
        result = f"{x[0]} {x[1]}"
    else:
        result = f"{x[0]} {x[1]} {x[2]}"
    
    return result


def filtro_terminales(lista_terminales, df, nombre_columna):
    """ Vamos a crear una función para filtrar un dataframe por nombre de terminal, que será una lista de terminales que queremos """

    df_filtro_terminales = df[df[nombre_columna].isin(lista_terminales)]

    return df_filtro_terminales


def transformacion_tiempos_camion(terminal, year):
    """ Vamos a crear una función que nos junte los dataframes de los tiempos que tardan en operar los camiones por franja horaria """
    
    path = (f'/Users/xavi/Documents/Ironhack/Projects/BCN_terminals_project/Tiempos_acceso/Tiempo_acceso_{terminal}/od_ta_{terminal}_{year}.csv')
    
    if year < 2022:
        df = pd.read_csv(path, sep=';', engine='python')
    else:
        df = pd.read_csv(path, sep=",")

    # Convertimos columna "Temps Accés" en float:
    df['Tiempo_acceso'] = df['Tiempo_acceso'].str.replace(",",".").astype(float)
    
    # Eliminamos la columna "Temps Accés Reserva":
    df = df.drop(columns=['Tiempo_acceso_reserva'])

    # Convertimos la columna "Data" en datetime:
    df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
    
    # Averiguamos qué día de la semana era para nuestro estudio:
    df['dia_semana'] = df['Data'].apply(lambda x: x.weekday())

    # Obtenemos los días de la semana en nombre, no en número como nos da weekday():
    dict_dias_semana = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'domingo'
    }
    df['dia_semana'] = df['dia_semana'].replace(dict_dias_semana)

    df["Hora"] = df["Rang_Data"].apply(lambda x: int(str(x)[:2]))
    
    # En este caso, vamos a eliminar las filas que no tengan valores en "Tiempo_acceso" pues no sabemos los tiempos de acceso para ellos:
    df = df.dropna(subset=['Tiempo_acceso']) 

    # Eliminamos tambien las filas con valores de "Tiempo_acceso" de 0:
    df = df = df.drop(df[df['Tiempo_acceso'] <= 0.2].index)

    return df
