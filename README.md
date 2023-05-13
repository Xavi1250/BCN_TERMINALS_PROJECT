![Imagen puerto de BCN](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/Puerto-BCN.jpg)
# EFICIENCIA DE LAS TERMINALES DE CONTENEDORES DEL PUERTO DE BARCELONA


## INTRODUCCIÓN

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


Como se puede observar en el siguiente gráfico, sorprende que lleguen muchos más buques en la primera mitad de año que en verano, por ejemplo:

![Llegadas por meses](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/Llegadas_buques_meses.png)


A continuación se puede ver a qué terminales llegan más buques por mes:

![Buques por mes y terminal](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/Llegadas_buques_meses_terminal.png)

- La probabilidad de que un buque vaya a APMT es de: **38.15%**
- La probabilidad de que un buque vaya a BEST es de: **61.85%**

&nbsp;

## 2. Análisis de tiempo e operaciones de buques llegados a cada terminal por eslora
En este apartado, se va a determinar el tamaño de los buques que llegan y la probabilidad de que vayan a una u otra terminal.

En los siguientes gráficos, se representa la distribución de buques que atracan en cada terminal según la Eslora y el tiempo que tardan en operar los buques:

![Eslora_tiempo_4](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/eslora_tiempo.png)

Pero para determinar si una terminal opera los buques más eficientemente que otra, se ha obtenido la equivalencia en horas de cada escala a la carga de un buque de 100 m. Resultado:

- APMT BARCELONA:    **9.15 horas**
- BEST:              **8.18 horas**

&nbsp;


Para seguir con los cálculos, se ha calculado media y mediana de Eslora y Calado:

- La media de eslora de buques es: **216.79 metros**
- La mediana de eslora de buques es: **198.6 metros**
- La media de calado de buques es: **11.12 metros**
- La mediana de calado de buques es: **11.15 metros**

&nbsp;

Se considerará a partir de ahora buque de gran Eslora, a aquél que supere la media de eslora de buques que han llegado a BCN. Se calculan a continuación las probabilidades relacionadas con estos buques:

- La probabilidad de que lleguen buques de gran Eslora a BCN es de: **38.84%**
- La probabilidad de que, si llega un buque de gran Eslora, atraque en APMT es de: **39.35%**
- La probabilidad de que, si llega un buque de gran Eslora, atraque en BEST es de: **60.65%**
- La probabilidad de que llegue un buque de gran Eslora a APMT es de: **15.29%**
- La probabilidad de que llegue un buque grande a BEST es de: **23.56%**

&nbsp;

## 3. Análisis de los tiempos de acceso por camión a cada terminal
En este apartado se calcula lo que tarda cada terminal en dar acceso a un camión a sus instalaciones, ya sea para soltar o recoger un contenedor.
Para ello, se obtienen los datos anuales de tiempos de acceso, se limpian mediante una función llamada **transformacion_tiempos_camion** y se concatenan. 

Primero, se obtienen las medias de tiempo de acceso en total para BCN y para cada terminal:

- La media de minutos de espera para acceder en camion es: **19.21 minutos**
- La media de minutos de espera para acceder en camion a APMT es de: **18.45 minutos**
- La media de minutos de espera para acceder en camion a BEST es de: **19.89 minutos**

&nbsp;

Ya con estos datos, se determina la probabilidad de sufrir retrasos en cada terminal, tomando como referencia que se considera retraso a todo tiempo mayor a la media de acceso a cada terminal:

- La probabilidad de tardar más de la media en acceder a APMT es de: **22.81%**
- La probabilidad de tardar más de la media en acceder a BEST es de: **32.58%**

&nbsp;

Segundo, se realiza el análisis por meses para determinar en qué meses se sufren más retrasos. Observemos el siguiente gráfico:

![Tiempo acceso por meses y terminales](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/tiempo_acceso_terminal.png)


Tercero, se va a realizar el análisis por día de la semana:

![Retrasos por día](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/tiempo_acceso_dia_terminal.png)

&nbsp;

Y por último, y posiblemente más importante, se analiza por horas:

![Retrasos por horas](https://github.com/Xavi1250/BCN_terminals_project/blob/main/Imagenes/tiempo_acceso_hora_terminal.png)


Para calcular probabilidades, se han dividido las horas del día en 4 franjas:

- franja 1 = 00:00 - 6:00
- franja 2 = 6:00 - 12:00
- franja 3 = 12:00 - 18:00
- franja 4 = 18:00 - 00:00

Los resultados obtenidos para APMT son:

- La probabilidad de sufrir retrasos en APMT de 0h a 6h es de: **5.46%**
- La probabilidad de sufrir retrasos en APMT de 6h a 12h es de: **15.32%**
- La probabilidad de sufrir retrasos en APMT de 12h a 18h es de: **37.96%**
- La probabilidad de sufrir retrasos en APMT de 18h a 24h es de: **12.15%**

Los resultados obtenidos para BEST son:

- La probabilidad de sufrir retrasos en BEST de 0h a 6h es de: **4.48%**
- La probabilidad de sufrir retrasos en BEST de 6h a 12h es de: **22.08%**
- La probabilidad de sufrir retrasos en BEST de 12h a 18h es de: **53.17%**
- La probabilidad de sufrir retrasos en BEST de 18h a 24h es de: **32.31%**


