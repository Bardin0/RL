#!/usr/bin/env python3
import traceback

import tcod

import color
import time

import exceptions
import input_handlers # This
import setup_game

GAME_SPEED = 500

def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")

flags = tcod.context.SDL_WINDOW_FULLSCREEN_DESKTOP # Sets window to full screen on launch

def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(  # loads the tile sheet 
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # handler: input_handlers.BaseEventHandler = setup_game.MainMenu()
    handler = input_handlers.MainGameEventHandler(setup_game.new_game())

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Tomb of The Ancient Kings",
        vsync=True,
        sdl_window_flags=flags,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        try:

            move_cooldown = 20/GAME_SPEED
            last_move = 0.0
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                current_time = time.time()

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        if current_time - last_move >= move_cooldown:
                            new_handler = handler.handle_events(event)
                
                            # If the handler changes (e.g., game state changes), reset the clock
                            if new_handler is not handler:
                                last_move = current_time

                            handler = new_handler
                        else:
                            pass  # Input is ignored due to cooldown
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            pass
            raise
        except BaseException:  # Save on any other unexpected exception.
            pass
            raise

            


if __name__ == "__main__":
    main()