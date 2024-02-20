import reflex as rx


def send_bar() -> rx.Component:
    return rx.text_area(
        placeholder="Type your message...",
        position ="fixed",
        bottom ="0px",
        width ="100%"

    )