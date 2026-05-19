# Apocalipsis Cuántico
Este repositorio está relacionado con la charla divulgativa "Apocalipsis cuántico", 
que tiene por objetivo repasar algunos de los métodos criptográficos más utilizados
a lo largo de la historia hasta llegar a los más modernos, resistentes a los nuevos
ordenadores cuánticos.

## Contenidos ejecutables
### Algoritmos criptográficos clásicos
Todas las implementaciones se encuentran dentro de la carpeta `criptografia`

Implementaciones completas de los algoritmos de cifrados que representan. No necesitan
ninguna dependencia para ser ejecutados
```
# Implementación del cifrado Cesar
cesar.py
# Implementacion del cifrado Vigenere
vigenere.py
```

Implementaciones prácticas de los algoritmos en cuestión. Los algoritmos están implementados
en librerías externas, que son las más utilizadas en la industria. Lo que se muesta en estos
ficheros es cómo utilizarlos.
```
post_cuantico.py
```

### Algoritmos cuánticos
Todas las implementaciones se encuentran dentro de la carpeta `computacion_cuantica`. Estas
implementaciones dependen de la libreria `qiskit` para construir los circuitos cuánticos y
`qiskit_aer` para simular los circuitos. Los circuitos son simulados en nuestro ordenador, 
no son ejecutados en un ordenador cuántico real. Para utilizar un ordenador cuántico real,
consultar https://www.ibm.com/quantum/qiskit

```
# Implementación del algoritmo de Deutsch
deutsch.py
```

## Instrucciones de instalación

Primero necesitaremos todas las dependencias listadas en `requirements.txt`

```
pip install -r requirements.txt 
```

Necesitaremos compilar la librería oqs, la más utilizada del mercado. Está escrita en
C, que suele ser el estándar para las empresas. Podéis seguir las instrucciones para
instalarlas de su propio repositorio:
https://github.com/open-quantum-safe/liboqs.git

Una vez hecho, necesitaremos también instalar la interfaz de python para poder
utilizarla en nuestros ejemplos. Para ello, usaremos los siguientes comandos

```
cd ~
git clone https://github.com/open-quantum-safe/liboqs-python.git
cd liboqs-python
pip install .
```