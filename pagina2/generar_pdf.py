from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12)

pdf.set_font("helvetica", style="B", size=18)
pdf.cell(200, 10, text="Fantastic_World - Catálogo Oficial", align="C", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("helvetica", size=10)
pdf.cell(200, 10, text="Ubicación: Av. Geek #404, Col. Centro, Ciudad Ficticia", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(10)

contenido = """
Bienvenido a Fantastic_World, tu tienda geek especializada en cómics, mangas, videojuegos y tecnología.

--- CATÁLOGO ---
1. CÓMICS: Batman: The Dark Knight Returns ($350), Spider-Man: Blue ($290).
2. MANGAS: One Piece Vol. 105 ($180), Chainsaw Man Vol. 1 ($150).
3. VIDEOJUEGOS: Elden Ring PS5 ($1,199), Zelda Tears of the Kingdom ($1,299).
4. TECNOLOGÍA: Teclado Mecánico RGB ($850), Mouse Ergonómico ($599).
"""

pdf.set_font("helvetica", size=11)
pdf.multi_cell(0, 8, text=contenido)
pdf.output("catalogo_fantastic_world.pdf")
print("¡PDF generado con éxito!")