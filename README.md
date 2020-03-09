# ngspice Parser

`NgspiceParser v0.0.1`

### NgspiceParser

This python and Antlr project is part of a Master´s Final Project that specified the whole project in the About Section
(in Spanish cause is copied directly from the campus web). 

With the help of Antlr4 we have to develop a parser of SPICE, more precisely ngspice, in Python3. This parser it should
not just a syntax lexer, but also analog circuits analyzer. The python generated files of Antlr will do syntax analysis,
 and later with python analyses the results and verify the composition and structure of the electronic circuit.  
 
Unless this like first part, ngspice parser. Later when we get will pass to the next parts of the whole projects and 
convert this start to his final purpose.

### Version

First time NgspiceParser.py executes, so this is first step. Can execute and now we can start to verify the grammar 
rules, identifiers, parse tree, etc. is well done. In other words, now we can check our .g4 file and the manipulations 
we made to the files generate from this file and improve our and resolve the parser.

Also, runs but wrong. The next step is solve why the why top rule of NgspiceGrammar.g4, `code` says it's an unused rule.
How will run a parser if the top rule can not be reached?

### About

***Autor: Samu Gonzalez***\
***Coordinador: Antonio Martinez***\
***Tutores: Antonio Martinez, Sergio Cuenca***

#### Trabajo Fin de Máster

##### Título del trabajo
Diseño de un simulador de inyección de fallos inducidos por radiación en circuitos
analógicos definidos con SPICE: aplicación al sector aeroespacial

##### Resumen

El estudio de la tolerancia frente a fallos inducidos por radiación en sistemas electrónicos es una tarea que cada vez demanda más la atención de la industria aeroespacial.
En este proyecto se diseñará y evaluará un inyector de fallos inducidos por radiación orientado a sistemas electrónicos analógicos definidos en SPICE.

##### Objetivos concretos

- Diseñar un analizador de esquemas circuitales analógicos definidos con SPICE.
- Dotar a dicho analizador de la habilidad de simular la inyección de fallos inducidos por radiación.
- Diseñar un director de campañas de inyección de fallos para automatizar la experimentación.
- Evaluar la herramienta con varios casos de estudio reales del entorno aeroespacial.


##### Metodología a emplear

- Estudio de cómo realizar un analizador (parser) empleando herramientas como ANTLR o similares.
- Estudio de Python para automatizar la interoperabilidad entre varias aplicaciones (inyector de fallos y SPICE).
- Estudio en profundidad de ngspice.
- Diseño de una campaña de inyección de fallos que valide el simulador de inyección de fallos.

##### Relación con asignaturas cursadas y/o itinerario relacionado

- Este proyecto está directamente relacionado con la asignatura "Diseño de Circuitos y Sistemas Integrados" (DCSI) del Máster en Ingeniería de Telecomunicación.

##### Bibliografía o fuentes de información

- https://www.antlr.org/
- http://ngspice.sourceforge.net/
- https://www.python.org/doc

###### *Universidad de Alicante*
###### *Máster en Ingeniería de Telecomunicación*

