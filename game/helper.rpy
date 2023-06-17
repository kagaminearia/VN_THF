init python:
    config.keymap['dismiss'].append('mousedown_5')

init python:
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False

init python:
    # change punch variable
    hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
    vpunch = Move((0, 30), (0, -30), .50, bounce=True, repeat=True, delay=.275)


transform char_mid:
    zoom 0.2
    xalign 0.5
    yalign 0.27

transform char_left:
    zoom 0.2
    xalign 0.2
    yalign 0.27

transform char_right:
    zoom 0.2
    xalign 0.8
    yalign 0.27

transform large:
    xalign 0.5
    yalign 0.85

transform cg0:
    zoom 0.5

transform cg1:
    zoom 0.8
    xalign 0.4
    yalign 0.53