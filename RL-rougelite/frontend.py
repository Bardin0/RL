import subprocess
import streamlit as st

st.header("Tomb of the Ancient Kings", divider="rainbow")
st.subheader("What is Tomb of the Ancient Kings?")

st.markdown('''
    Tomb of the Ancient Kings is an old-school 2D rogue-lite game built entirely in python.
    It's a small project I created to help me learn python in a fun way.
            
    Cool features of Tomb of the Ancient Kings
    - Randomly generated dungeons, no 2 dungeons will be the same!
    - various monsters and items found within the world.
    - Infinite Levels! (Obviously)
            
    To try out the game simply hit the run button below (It will open a new window).

''')

if st.button("Run Game"):
    subprocess.run(["python3", "main.py"])

st.markdown('''

    Creator: Michael Giovannini
            
    [Source Code](https://github.com/Bardin0/rougue-lite)

''')

st.header("How to Play", divider="rainbow")
st.markdown('''

    Objective:
    There is no real objective, just see how far you can go!
            
    Controls:
            
    Up: j or up arrow

    Down: k or down arrow

    Left: h or left arrow

    Right l or right arrow

    Diagonal up and left: y or home

    Diagonal up and right: u or page up

    Diagonal down and left: b or end 

    Diagonal down and right: n or page down

            
    Inventory: i

    Character Menu: c

    Pickup: g

    Drop Menu: d

    Close Menu / Select: Enter

    Tile selector: Forward slash (/)

    Descend Floors: >

    View Message History: v

            
            
    Quit: Escape
            
    How do you attack you might ask?

    Just walk into the enemies!

    Have Fun!


''')