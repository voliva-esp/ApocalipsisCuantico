# Apocalipsis Cuántico
Este repositorio está relacionado con la charla divulgativa "Apocalipsis cuántico", 
que tiene por objetivo repasar algunos de los métodos criptográficos más utilizados
a lo largo de la historia hasta llegar a los más modernos, resistentes a los nuevos
ordenadores cuánticos.

## Contenidos ejecutables
Implementaciones completas de los algoritmos de cifrados que representan. No necesitan
ninguna dependencia para ser ejecutados
```
cesar.py
vigenere.py
```

Implementaciones prácticas de los algoritmos en cuestión. Los algoritmos están implementados
en librerías externas, que son las más utilizadas en la industria. Lo que se muesta en estos
ficheros es cómo utilizarlos.
```
post_cuantico.py
```

## Instrucciones de instalación

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