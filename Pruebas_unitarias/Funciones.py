import re


def eliminar_por_id(lista, id_buscado, i=0):
    if i >= len(lista):
        return lista
    if lista[i]['ID'] == id_buscado:
        lista.pop(i)
        return lista
    return eliminar_por_id(lista, id_buscado, i + 1)
