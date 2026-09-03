import reflex as rx
from typing import List, Dict, Optional

class ComicsState(rx.State):
    comics_list: List[Dict[str, str]] = [
        {
            "id": "1",
            "titulo": "X-Men: Kraven's Last Hunt",
            "editorial": "MARVEL",
            "precio": "$29.99",
            "portada": "/images/spider.jpeg",
            "badge": "Nuevo",
            "sinopsis": "Una de las historias más oscuras y aclamadas. "
            "Kraven el Cazador rastrea a su presa definitiva en una cacería sin precedentes.",
            "autor": "J.M. DeMatteis"
        },
        {
            "id": "2",
            "titulo": "Batman: Vol. 1",
            "editorial": "DC",
            "precio": "$29.99",
            "portada": "/images/BatmanVolumen1.jpeg",
            "badge": "Colección",
            "sinopsis": "El inicio de una nueva era en Gotham City. El Caballero de la Noche enfrenta la misteriosa red de la Corte de los Búhos.",
            "autor": "Scott Snyder"
        },
        {
            "id": "3",
            "titulo": "Amalgam Comics: Dark Claw",
            "editorial": "COLABORACIONES",
            "precio": "$35.00",
            "portada": "/images/wolverineBat.jpeg",
            "badge": "Edición Especial",
            "sinopsis": "La icónica fusión entre Marvel y DC que dio origen al héroe híbrido definitivo: Dark Claw.",
            "autor": "Larry Hama"
        },
        {
            "id": "4",
            "titulo": "The Amazing Spider-Man #300",
            "editorial": "MARVEL",
            "precio": "$34.99",
            "portada": "/images/spi.jpeg",
            "badge": "Joyita",
            "sinopsis": "La primera aparición completa de Venom. Un hito histórico en la trayectoria de Peter Parker.",
            "autor": "David Michelinie"
        },
        {
           "id": "5",
            "titulo": "Zero War",
            "editorial": "COLABORACIONES",
            "precio": "$35.00",
            "portada": "/images/fort1.jpeg",
            "badge": "Edición Especial",
            "sinopsis": "La Isla de Fortnite está atrapada en un conflicto sin fin y la única forma de salvar la realidad es recuperar un fragmento del Punto Cero que cayó en el Universo Marvel. El Agente Jones y La Imaginada viajan a la Tierra-616 para hacer equipo con Spider-Man, Wolverine, Iron Man y Shuri. Juntos inician una búsqueda interdimensional contra reloj para recuperar el fragmento antes de que la Orden Imaginada destruya ambos universos.",
            "autor": "Christos Gage y Donald Mustard (Guion); Sergio Dávila (Dibujo)."
        },
        {
            "id": "6",
            "titulo": "Zero War 2",
            "editorial": "COLABORACIONES",
            "precio": "$35.00",
            "portada": "/images/fort2.jpeg",
            "badge": "Edición Especial",
            "sinopsis": "Corresponde específicamente al cuarto ejemplar de la saga (portada en portugués Guerra do Ponto Zero). En esta entrega, los héroes viajan a la Luna Helada de la Isla para reactivar al meca gigante Mecha Strike Commander. Al necesitar una fuente de energía masiva para encender el robot y enfrentar la amenaza inminente, el equipo se ve obligado a realizar un peligroso e inestable pacto con el Doctor Doom.",
            "autor": "Christos Gage y Donald Mustard (Guion); Sergio Dávila (Dibujo)."
            },
        {
            "id": "6",
            "titulo": "NIGHTWING",
            "editorial":"DC",
            "precio": "$35.00",
            "portada": "/images/DC1.jpeg",
            "badge": "DC",
            "sinopsis": "Se trata de un número especial tipo art book que celebra el apartado visual de la aclamada etapa moderna de Nightwing. El ejemplar reúne las portadas variantes más representativas, bocetos de desarrollo de personajes, arte inédito y estudios de diseño creados por los ilustradores que le dieron una nueva identidad estética a Dick Grayson y a la ciudad de Blüdhaven.",
            "autor": "Tom Taylor (Guion/Notas); Dan Mora (Artista de esta portada); Bruno Redondo, Jamal Campbell, Javier Fernández, Travis Moore y varios artistas (Ilustración)."
        },
        {
            "id": "8",
            "titulo": "Gael_de_Jesus",
            "editorial":"COLABORACIONES",
            "precio": "$999",
            "portada": "/images/GAEL1.jpeg",
            "badge": "Edición Especial",
            "sinopsis":"Guapo, alto y bronceado",
            "autor":"Enigma."
        },
        {
            "id": "9",
            "titulo": "X-MEN",
            "editorial":"MARVEL",
            "precio": "$29.00",
            "portada": "/images/x.jpeg",
            "badge": "Coleccion ",
            "sinopsis":"Esta aprendiendo a ocupar Reflex",
            "autor":"Enigma."
         },

    ]

    selected_editorial: str = "TODOS"
    search_query: str = ""

    # Control del Modal de Detalles
    selected_comic: Dict[str, str] = {}
    is_modal_open: bool = False

    def select_editorial(self, ed: str):
        if self.selected_editorial == ed:
            self.selected_editorial = "TODOS"
        else:
            self.selected_editorial = ed

    def set_search_query(self, query: str):
        self.search_query = query

    def open_comic_details(self, comic: Dict[str, str]):
        """Guarda el cómic clickeado y abre el modal."""
        self.selected_comic = comic
        self.is_modal_open = True

    def close_modal(self):
        """Cierra el modal de detalles."""
        self.is_modal_open = False

    @rx.var
    def filtered_comics(self) -> List[Dict[str, str]]:
        return [
            comic for comic in self.comics_list
            if (self.selected_editorial == "TODOS" or comic["editorial"] == self.selected_editorial)
            and (self.search_query.lower() in comic["titulo"].lower())
        ]