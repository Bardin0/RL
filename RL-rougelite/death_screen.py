
import color

def on_render(console)-> None:
    "Renders the screen when death occurs"

    console.draw_frame(
        x= console.width//2,
        y= console.height//2,
        width= console.width,
        height= 4,
        string= "YOU DIED",
        fg = color.black,
        bg = color.red
    )

    return None
