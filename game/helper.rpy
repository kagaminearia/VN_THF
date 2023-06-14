init python:
    # change punch variable
    hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
    vpunch = Move((0, 20), (0, -20), .10, bounce=True, repeat=True, delay=.275)


transform char_mid:
    zoom 0.25
    xalign 0.5
    yalign 0.27

transform char_left:
    zoom 0.25
    xalign 0.2
    yalign 0.27

transform char_right:
    zoom 0.25
    xalign 0.8
    yalign 0.27

transform large:
    xalign 0.5
    yalign 0.85