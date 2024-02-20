import reflex as rx
from epicrol.styles.colors import Color

def message(avatar:str, name:str, text_m: str) -> rx.Component:
    return rx.hstack(
        rx.avatar(src=avatar,
                    radius= "full",
                    size="7",
                    margin_x ="0.2em"),
        rx.vstack(
            rx.heading(name,
                        size="3"),
            rx.text(text_m),
                        
    ),
    bg = Color.LIGHT_VIOLET.value,
    padding ="1em",
    margin_x ="2em",
    border_radius = "1em",
    
    )

