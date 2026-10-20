#!/usr/bin/env python3
"""Quita de un registro Excel las columnas y hojas que pueden identificar a una persona
(nombre, carrera, semestre, notas libres) y guarda una copia *_anonimizado.xlsx.

IMPORTANTE: este script reduce el riesgo, no lo elimina. Antes de publicar datos por
participante, confirma que el consentimiento informado lo permite y revisa el resultado a mano.

Uso:  python3 anonimizar_excel.py registro.xlsx
"""
import sys, openpyxl

COLUMNAS = ("nombre", "carrera", "semestre", "edad", "correo", "email", "observaciones", "notas")
HOJAS = ("notas cualitativas", "perfil y retro", "instrucciones")

def main(ruta):
    wb = openpyxl.load_workbook(ruta)
    for nombre in list(wb.sheetnames):
        if nombre.strip().lower() in HOJAS:
            del wb[nombre]; continue
        ws = wb[nombre]
        borrar = []
        for fila in ws.iter_rows(min_row=1, max_row=6):
            for c in fila:
                if isinstance(c.value, str) and any(c.value.strip().lower().startswith(k) for k in COLUMNAS):
                    borrar.append(c.column)
        for idx in sorted(set(borrar), reverse=True):
            ws.delete_cols(idx)
    salida = ruta.rsplit(".", 1)[0] + "_anonimizado.xlsx"
    wb.save(salida)
    print("Guardado:", salida)

if __name__ == "__main__":
    main(sys.argv[1])
