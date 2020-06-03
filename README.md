# Usure

La herramienta USURE permite la creación de las representaciones, la experimentación y evaluación de ellas en diferentes tipos de clasificadores.

Esta herramienta brinda una facilidad para el desarrollo de la experimentación, permitiendo ahorrar tiempo y recursos. Se espera que pueda servir y agregar valor en trabajos futuros de estudiantes o cualquier otra persona interesada en el tema.  

El nombre clave del proyecto o herramienta es \say{Usure} (Úsure) y como dato curioso, representa la casa cósmica de los aborígenes Bribri de Costa Rica.


## Descripción de la aplicación Usure

La aplicación Usure se encuentra dividida en tres paquetes (Python) principales, pero la conceptualización lógica que se le da a estos paquetes para efectos del proyecto es de aplicación. Las tres aplicaciones son \textit{preprocessing, wordvectors} y  _classification_. Estas aplicaciones cuentan con responsabilidades específicas que se mencionan a continuación.

La aplicación de preprocesamiento **_preprocessing_** se encarga de transformar los corpus existentes.  Esta aplica funciones de transformación a cada uno de los comentarios de un corpus.  Además, almacena en forma persistente el resultado de estas transformaciones en archivos con extensión ".usu".  

La aplicación **_wordvectors_**, recibe como insumo los archivos ".usu", los cuales representan el corpora preprocesado. Se encarga de crear las representaciones vectoriales de las palabras y persistirlas, por medio del _framework_ Gensim, que a su vez es el en cargado de generar estas representaciones. Cabe destacar que la arquitectura permite desacoplar el _framework_ de vectorización de forma fácil. En este caso se utilizó Gensim pero este puede ser sustituido por otro, como por ejemplo fastText.  

La aplicación **_classification_**, es la encargada de generar y evaluar los modelos, teniendo como insumo cualquier corpus (en este proyecto el corpus InterTASS\_CR) y las representaciones vectoriales generadas por la aplicación _wordvectors_.

El paquete _classification_, sirve como punto de referencia para describir la estructura interna de las tres aplicaciones. Los principales paquetes que se pueden encontrar en estas aplicaciones son: el _core_, donde reside la lógica del negocio, _infrastructure_, que representa los accesos a recursos externos o ajenos a la lógica del negocio, como por ejemplo la persistencia; y por último se tiene _ui_ que representa el paquete de interfaz de usuario. Utilizándose aquí Jupyter, una aplicación HTML para visualización y ejecución de código.   
