![Imagen puerto de BCN](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/Puerto-BCN.jpg)
# EFICIENCIA DE LAS TERMINALES DE CONTENEDORES DEL PUERTO DE BARCELONA


## INTRODUCCION

El puerto de BCN es el 3er puerto más importante de España en cuanto a volumen de contenedores movidos, por detrás de Algeciras y Valencia.

A día de hoy, cuenta con dos grandes terminales de contenedores, **APMT** y **BEST**:
          
![Terminales](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/Terminales.jpeg)

https://www.google.es/maps/@41.3312633,2.1588127,13.46z

Gracias a la open data del puerto de Barcelona, hemos podido acceder a muchos datos relevantes sobre la operativa de estas dos terminales, y aun no haber podido acceder a otros datos de carácter confidencial, se ha podido realizar un estudio de quan eficientes son cada una de las dos terminales.

&nbsp;

## OBJETIVOS

1. Análisis general de llegadas de buques a ambas terminales.
2. Análisis de tiempos de operaciones de buques llegados a cada terminal.
3. Análisis de los tiempos de acceso en camión para cada terminal.

&nbsp;

## 1. Análisis general de llegadas de buques a ambas terminales.
En open data BCN se ha obtenido datos de las escalas de buques en BCN por años, desde 2020 en adelante. Lo primero que se ha conseguido es limpiar y concatenar todos los dataframes en uno mediante la creación de una función llamada **transformacion_escalas**. De esta forma se ha obtenido un dataframe limpio y filtrado únicamente por terminales APMT y BEST, objeto de este estudio.


- Como se puede observar en el siguiente gráfico, sorprende que lleguen muchos más buques en la primera mitad de año que en verano, por ejemplo:

![Llegadas por meses](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/Llegadas_buques_meses.png)


- A continuación se puede ver a qué terminales llegan más buques por mes:

![]()

- La probabilidad de que un buque vaya a APMT es de: **38.15%**
- La probabilidad de que un buque vaya a BEST es de: **61.85%**

&nbsp;

## 2. Análisis por Eslora de buques llegados a cada terminal
En este apartado, se va a determinar el tamaño de los buques que llegan y la probabilidad de que vayan a una u otra terminal.

- En los siguientes gráficos, se representa la distribución de buques que atracan en cada terminal según la Eslora y el tiempo que tardan en operar los buques:

![Eslora_tiempo_4]()

- Pero para determinar si una terminal opera los buques más eficientemente que otra, se ha obtenido la equivalencia en horas de cada escala a la carga de un buque de 100 m. Resultado:

APMT BARCELONA:    **9.15 horas**

BEST:              **8.18 horas**

- Para seguir con los cálculos, se ha calculado media y mediana de Eslora y Calado:

La media de eslora de buques es: **216.79 metros**

La mediana de eslora de buques es: **198.6 metros**

La media de calado de buques es: **11.12 metros**

La mediana de calado de buques es: **11.15 metros**






