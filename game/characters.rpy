define na = Character(None)
define na1 = Character(None,what_font="fonts/江城正君体_600W.ttf")
define red = Character(None,what_color="#9d2525",what_font="fonts/江城正君体_600W.ttf")
define horr = Character(None,what_font="fonts/恐怖明朝体.otf")

# main characters
define unknown = Character("？",what_prefix="“",what_suffix="”")
define unknown_inn = Character("？")
define qian = Character("时茜")
define qian_speaking = Character("时茜",what_prefix="“",what_suffix="”")
define chi_speaking = Character("迟玉",what_prefix="“",what_suffix="”")
define ying_speaking = Character("莺莺",what_prefix="“",what_suffix="”")
define li_speaking = Character("黎沙",what_prefix="“",what_suffix="”")

define bfem = Character("黑衣女人")
define bfem_speaking = Character("黑衣女人",what_prefix="“",what_suffix="”")
define off_speaking = Character("工作人员",what_prefix="“",what_suffix="”")
define thin_speaking = Character("瘦小女人",what_prefix="“",what_suffix="”")
define short_speaking = Character("短发女人",what_prefix="“",what_suffix="”")

define boss_speaking = Character("老板",what_prefix="“",what_suffix="”")
define jun_speaking = Character("君和",what_prefix="“",what_suffix="”")
define stf_speaking = Character("工作人员",what_prefix="“",what_suffix="”")

# place holders
define place_holder = Character("制服女人",what_prefix="“",what_suffix="”")
define lan_speaking = Character("蓝石",what_prefix="“",what_suffix="”")
define coworker_speaking = Character("同事",what_prefix="“",what_suffix="”")
define white_speaking = Character("白衣女人",what_prefix="“",what_suffix="”")
define doctor_speaking = Character("医生",what_prefix="“",what_suffix="”")

define nvl_mode = Character('', kind=nvl)
define qian_msg = Character("时茜：",color="#fff",kind=nvl,what_prefix="【",what_suffix="】")
define chi_msg = Character("迟玉：",color="#fff",kind=nvl,what_prefix="【",what_suffix="】")


# images for characters
init:
    layeredimage qianimg:
        group body:
            attribute pajama default:
                "images/char/qian/pajama.png"
            attribute pajama_red:
                "images/char/qian/pajama_red.png"
            attribute black:
                "images/char/qian/black.png"
            attribute shirt:
                "images/char/qian/shirt.png"
            attribute coat:
                "images/char/qian/coat.png" 
            attribute white:
                "images/char/qian/white.png" 

        group expressions:
            attribute neutral default:
                "images/char/qian/neutual.png"
            attribute close:
                "images/char/qian/close.png"
            attribute shock:
                "images/char/qian/shock.png"
            attribute shout:
                "images/char/qian/shout.png"
            attribute closecalm:
                "images/char/qian/closecalm.png"
            attribute closesad:
                "images/char/qian/closesad.png"
            attribute o:
                "images/char/qian/o.png"
            attribute smile:
                "images/char/qian/smile.png"
            attribute sad:
                "images/char/qian/sad.png"
            attribute still:
                "images/char/qian/still.png"

        group mask:
            attribute mask:
                "images/char/qian/mask.png"


    layeredimage chiimg:
        group body:
            attribute body default:
                "images/char/chi/body.png"

        group expressions:
            attribute o default:
                "images/char/chi/o.png"
            attribute black:
                "images/char/chi/black.png"
            attribute close:
                "images/char/chi/close.png"
            attribute closesmile:
                "images/char/chi/closesmile.png"
            attribute sad:
                "images/char/chi/sad.png"
            attribute sadask:
                "images/char/chi/sadask.png"
            attribute warm:
                "images/char/chi/warm.png"
            attribute laugh:
                "images/char/chi/laugh.png"
            attribute afraid:
                "images/char/chi/afraid.png"

    
    layeredimage liimg:
        group body:
            attribute coat default:
                "images/char/li/coat.png"
            attribute black:
                "images/char/li/black.png"
            attribute white:
                "images/char/li/white.png"

        group expressions:
            attribute neutral default:
                "images/char/li/neutual.png"
            attribute o:
                "images/char/li/o.png"
            attribute ask:
                "images/char/li/ask.png"
            attribute closeask:
                "images/char/li/closeask.png"
            attribute laugh:
                "images/char/li/laugh.png"
            attribute smile:
                "images/char/li/smile.png"
            attribute laugh:
                "images/char/li/laugh.png"


    layeredimage yingimg:
        group body:
            attribute coat default:
                "images/char/ying/coat.png"
            attribute shirt:
                "images/char/ying/shirt.png"

        group expressions:
            attribute neutral default:
                "images/char/ying/calm.png"
            attribute o:
                "images/char/ying/o.png"
            attribute close:
                "images/char/ying/close.png"
            attribute closeo:
                "images/char/ying/closeo.png"
            attribute still:
                "images/char/ying/still.png"
            attribute stillo:
                "images/char/ying/stillo.png"
            attribute smile:
                "images/char/ying/smile.png"
            attribute shock:
                "images/char/ying/shock.png"