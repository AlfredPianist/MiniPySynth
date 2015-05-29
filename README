MiniPySynth: Un interpretador para el módulo pyo para Python 2.7.
=================================================================

Requerimientos:
---------------

* Python 2.7

* `parsimonious <https://github.com/erikrose/parsimonious>`_
  librería para parsing usando Parsing Expression Grammar (PEG).

* `pyo <http://ajaxsoundstudio.com/software/pyo/>`_
  módulo para DSP escrito en C.

Pequeño manual de usuario:
---------------------------

- Las notas tienen la forma "nombre de nota" "alteración" "octava" "duración" y "puntillo". Ejemplos pueden ser "do#8'" o "mi,32.".
	- Nombre de nota (obligatoria). Su entrada es en el sistema solfeo traducido al español, es decir: "do", "re", "mi", etc.
	- Alteración (opcional). Sostenido (#) o bemol (b). ** EN DESARROLLO **
	- Octava (opcional). Si se quiere que la nota suene una octava más arriba (') o más abajo (,). ** EN DESARROLLO **
	- Duración (obligatoria). En números enteros, representando la fracción relativa a la entera o redonda ("1"). Así, las blancas son "2", las negras "4", las corcheas "8", y así sucesivamente en potencias de 2.
	- Puntillo (opcional). Si se quiere añadir uno o más puntillos a la duración asignada. ** EN DESARROLLO **

- Se pueden asignar variables a las notas, y así ahorrar tiempo al digitar, por ejemplo:
	escala = do8 re8 mi8 fa8 sol8

- Los condicionales se digitan, como ejemplo, así:
  	si a == 2:
  	{ do8 re4 mi1 }
  	si no:
  	{ la16 si2 }
  Por el momento solo soporta una expresión bajo los condicionales.

- Para repetir una sección se puede usar el siguiente ejemplo:
	repita i -> (0,1):
	{ do8 fa16 sol32 }

