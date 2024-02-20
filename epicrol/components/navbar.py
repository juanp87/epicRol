import reflex as rx
from epicrol.styles.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico",
                     height ="1.5em"),
            rx.text("Epic Rol APP"),
            padding ="0.5em",
            width="100%",


            
        ),
        background_color = Color.MID_VIOLET.value,
        width="100%",
        position="fixed",
        top= "0px",
        z_index= "999"
        
    )