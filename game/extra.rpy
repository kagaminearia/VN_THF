# ending lists
define ending_1 = "ENDING: 死寂" # python index starts at 0
define ending_2 = "ENDING: 安心"
define ending_3 = "ENDING: 突刺"
define ending_4 = "ENDING: 麻痹"
define ending_5 = "ENDING: 可惜"
define ending_6 = "ENDING: 紧急"
define ending_7 = "ENDING: 绽放"
define ending_8 = "ENDING: 晕眩"
define ending_9 = "ENDING: 美梦"
define ending_10 = "ENDING: 窒息"
define ending_11= "ENDING: 惊疑"
define ending_12 = "ENDING: 秘密"
define ending_13 = "ENDING: 逃亡"
define ending_14 = "ENDING: 荆棘"
define ending_15 = "ENDING: 风沙"
define ending_16 = "ENDING: 空荡"
define ending_17 = "ENDING: 噩梦"
define ending_18 = "ENDING: 沉默"
define ending_19 = "ENDING: 陌生"
define ending_20 = "ENDING: 尘埃"





## extra screens
screen extra_navi():
    hbox:
        style_prefix "navigation"
        xalign 0.5
        yalign 0.95
        spacing 60
        textbutton _("返回") action Return()
        textbutton _("画廊") action ShowMenu("gallary")
        textbutton _("结局") action ShowMenu("ending")
        textbutton _("概览") action ShowMenu("outline")
        textbutton _("制作") action ShowMenu("credits")


screen gallary():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi



screen ending():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi

    hbox:
        xalign 0.5
        yalign 0.5

        grid 5 4:
            for i in range(20): 
                if persistent.ending[i] == 1:
                    add im.Scale(f"gui/ending/ending{i+1}.jpg",180,180)
                else:
                    add im.Scale("gui/ending/locked_end.jpg",180,180)

            spacing 15
            


screen outline():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi


screen credits():
    tag menu
    add "gui/extra_menu.png"
    add "gui/overlay/bg_transparent.png"
    use extra_navi