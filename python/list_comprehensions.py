# 𝗗𝘂𝗻𝗸𝗲𝗹 𝗜𝗧 𝗦𝘁𝘂𝗱𝗶𝗼𝘀

# 🄻🄸🅂🅃 🄲🄾🄼🄿🅁🄴🄷🄴🄽🅂🄸🄾🄽🅂

# Generación de una lista de 1 millón de números para
# comparar estilos / sintáxis y velocidades usando:
#   - Ciclo «for» y el método «append»
#   - «List comprehensions»

# =============================================================================
# Capacitación en tecnologías como .Net, Python, Java, desarrollo para
# móviles (Android, iOS, Flutter, Xamarin), Bases de Datos y muchas más.

# También brindamos instrucción en Ciencia de Datos (Data Science),
# Estadística, Matemáticas y Física.

# Nos respalda nuestra sólida formación en Ciencias Matemáticas y Físicas, en
# conjunto con la gran experiencia en el área de las Tecnologías de la
# Información.

# Website: https://dunkel.studio/go2/website
# Facebook: https://dunkel.studio/go2/facebook
# Instagram: https://dunkel.studio/go2/instagram
# Youtube: https://dunkel.studio/go2/youtube
# Github: https://dunkel.studio/go2/github
# =============================================================================

# Importamos la función para contar el tiempo
from time import perf_counter_ns as pcn

# Vamos a llegar hasta 1 millón
numero_maximo = int(1e6)

# Definimos una lista vacía para guardar los números
lista = []

# Guardamos el tiempo de inicio
tiempo_inicio = pcn()
for i in range(numero_maximo):
    # Agregamos el número «i» a la lista
    lista.append(i)

# Aquí hemos terminado el ciclo, guardamos el tiempo
# de término.
tiempo_fin = pcn()

# Calculamos el tiempo que tardó el proceso
tiempo_for = tiempo_fin - tiempo_inicio

print(f'Duración del «for»: {tiempo_for} nanosegundos')

# Reiniciamos la lista
# (este paso no es necesario, la «list comprehension»
#  sustituye el valor de la variable)
lista = []

# Guardamos el tiempo de inicio
tiempo_inicio = pcn()

# Ejecutamos la list_comprehension
lista = [ i for i in range(numero_maximo) ]

# Guardamos el tiempo de término del proceso
tiempo_fin = pcn()

# Calculamos el tiempo que tardó el proceso
tiempo_comprehension = tiempo_fin - tiempo_inicio

print(f'Duración de la «list-comprehension»: {tiempo_comprehension} nanosegundos')

print(f'\nLa «list comprehension» es {100 * (1 - tiempo_comprehension / tiempo_for):.2f}% más rápida que el ciclo «for»')
