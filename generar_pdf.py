from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12)
pdf.set_font("helvetica", style="B", size=18)
pdf.cell(200, 10, text="Fantastic_World - Catalogo Oficial", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.output("catalogo_fantastic_world.pdf")
print("¡PDF CREADO EXITOSAMENTE!")
