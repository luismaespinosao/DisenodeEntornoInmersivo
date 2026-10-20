#!/usr/bin/env python3
"""Genera datos/resumen_agregado.csv a partir de los registros por participante (Excel).

Los Excel con datos por participante NO se publican en este repositorio (el consentimiento
informado no contempla compartir datos individuales). Este script se incluye para que el
procedimiento sea reproducible por quien tenga acceso a los registros originales.

Uso:  python3 generar_resumen_agregado.py Registro_Encuestas_Usabilidad_1.xlsx Resultados_Prueba_Usabilidad_2.xlsx
"""
import csv, statistics as st, sys, openpyxl

def col(ws, header_row, first_data_row, col_idx, n):
    vals = []
    for r in range(first_data_row, first_data_row + n):
        v = ws.cell(r, col_idx).value
        vals.append(float(v))
    return vals

def fila(prueba, indicador, vals):
    return [prueba, indicador, len(vals), round(st.mean(vals), 2), round(st.median(vals), 2),
            round(st.stdev(vals), 2) if len(vals) > 1 else "", round(min(vals), 2), round(max(vals), 2)]

def main(f1, f2):
    out = []
    wb1 = openpyxl.load_workbook(f1, data_only=True)
    sus = wb1["SUS"]; vr = wb1["VRSUQ"]
    out.append(fila("Prueba 1", "SUS (0-100)", col(sus, 4, 5, 12, 5)))
    out.append(fila("Prueba 1", "VRSUQ promedio (1-5)", col(vr, 4, 5, 14, 5)))
    wb2 = openpyxl.load_workbook(f2, data_only=True)
    sus = wb2["SUS"]; vr = wb2["VRSUQ"]; cp = wb2["Comprensión"]
    out.append(fila("Prueba 2", "SUS (0-100)", col(sus, 1, 2, 12, 10)))
    out.append(fila("Prueba 2", "VRSUQ promedio (1-5)", col(vr, 1, 2, 11, 10)))
    out.append(fila("Prueba 2", "Aciertos comprension digital/VR (0-5)", col(cp, 1, 2, 3, 10)))
    out.append(fila("Prueba 2", "Aciertos comprension fisico (0-5)", col(cp, 1, 2, 6, 10)))
    with open("resumen_agregado.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["prueba", "indicador", "n", "media", "mediana", "desv_est", "min", "max"])
        w.writerows(out)
    print("resumen_agregado.csv generado")

if __name__ == "__main__":
    main(*sys.argv[1:3])
