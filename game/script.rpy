# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    window hide

    scene black_bg with fade
    na1 "“愿你我的生命如荆棘般不屈。”"
    na1 "——荆棘之城 城市印章"
    pause

    window show
    unknown "……醒醒……起来……注意——"

    show qian_close0 at char_mid with dissolve
    qian "有什么东西，好吵……无边的黑暗似乎在震动，但……"
    hide qian_close0
    show qian_shocked0 at char_mid
    qian "——啊！"
    hide qian_shocked0
    show qian_shocked0 at large
    qian "我倏地睁开眼睛，视线还很朦胧，于是一道鲜红色的光线格外显眼，带领我走到它的终点，指着我的心脏。"
    show qian_shocked0 at char_mid
    qian "……\n那不是梦……。"
    scene bg_prolo_01 with fade
    hide qian_shocked0
    show qian_worry0 at char_mid
    qian "我混沌的脑海顿时清醒，眼睛也适应了微弱的光线。\n四个装束严实的人站在床边，我的四周，把我紧紧围住。"
    qian "他们在说什么，被面罩遮住，我听不真切。\n相同的黑色着装，挺拔绷直的身姿，若隐若现的标识……这当然是城市管制局的人。"
    hide qian_worry0
    show qian_worry1 at char_mid
    qian_speaking "你……你们要做什么？"
    qian "我想让自己的语气显得冷静，但嘴唇却不受控地颤抖。\n不行，冷静……她们是根据规定，不会乱来的。"
    show bfem_0r at char_right with dissolve
    bfem_speaking "时茜小姐，你被逮捕了。"
    qian "我刚刚才建立起的心理防线马上破碎。"
    qian_speaking "……什么？你们弄错了吧！\n别开玩笑了！"
    qian_speaking "别过来！喂，肯定是有什么误会的地方！怎么可能！等——"
    na "——！"
    show bfem_0l at char_left with dissolve
    qian "两个人靠近，我剧烈挣扎起来，却没有用，在用力的拉扯中从床上摔倒在地。\n好痛……我几乎瞬间就冒出了眼泪，在挺直的身板前显得狼狈又讽刺。"
    qian "没有人理会这点，我被拖住，床边的东西因为磕绊而掉在地上，我却没办法把它们拿起来，只能踉跄着往外走。"
    hide qian_worry1
    show qian_shocked0 at char_mid
    qian_speaking "喂，等等……等等啊！"

    scene bg_office_0 with fade
    show qian_silent0 at char_left with dissolve
    qian "这里是管控所。\n巨大的顶灯不知疲倦地射出明亮的白色光线，刺眼到让人眼睛生疼。我穿着睡衣站在角落的一间房间中央，有一种无所适从的局促。"
    qian "……为什么……我无声地吸了一口气，压抑着翻涌的情绪，看向离我最近的人。"
    hide qian_silent0
    show qian_worry11 at char_left
    qian_speaking "到底发生了什么？没有说明吗？"
    qian "我的声音发紧，从嗓子里挤出来，听着有些尖锐。她却毫无所觉，只是瞥过来一眼，而后像习以为常地转过头，无视。"
    qian "我呆呆地站在原地，像个傻子。\n……感觉，糟透了。"

    scene bg_office_1 with fade
    show qian_silent0 at char_left
    show bfem_0r at char_right with dissolve
    bfem_speaking "我问你答，懂吗？"
    qian_speaking "……为什么？你们还没回答我的问题。"
    bfem_speaking "我问，你答。"
    qian "她加重语气，令我下意识缩了缩肩膀。威压……那种令人不舒服的感觉清晰地裹在我身上。\n于是我顿了顿，还是绷紧声音说，好的。"
    scene bg_office_1 with fade
    show qian_calm0 at char_left
    show bfem_0r at char_right
    bfem_speaking "你了解过你家人的工作吗？"
    hide qian_calm0
    show qian_calm1 at char_left
    qian_speaking "在研究所做研究，关于生物科学……其他的我也不知道，她们不能说。"
    bfem_speaking "家里有藏东西的地方吗？"
    qian_speaking "为什么这也要问——我没有，我的房间里没有……别的，不知道。"
    hide qian_calm1
    show qian_calm0 at char_left
    qian "问题越来越多，配合刺目的灯光，让我头晕脑胀，到最后已经变成下意识作答，无法思考。\n但即使是这样……我也没能问出任何东西。"
    bfem_speaking "拿着。"
    hide qian_calm0
    show qian_silent0 at char_left
    qian_speaking "好的……啊，什么？"
    qian "我依旧是下意识回应，说完才发现并不是在问问题，而是有东西被递过来。\n荆棘之城的统一终端机，正面屏幕，反面刻着城市印章。但……这并不是我原来的终端。"
    qian "为……不，我已经发现了，就算询问也不会有人回答。\n屏幕亮起，这个全新的终端上面正显示着我的名字，以及一条带有鲜红色标签的消息。"
    hide qian_silent0
    hide bfem_0r
    na "通知：\n因编号T19957及编号T20234涉及S级禁令，编号T25648作为直接血缘关系，将被剥夺一切原有城市权利。"
    show qian_shocked1 at char_mid
    qian "等等，什么意思……\n我机械性地点亮屏幕，打开消息，读完信息的时候才后知后觉，似乎有什么很重要的事情。"
    qian "怎么可能？宋女士和黄女士都是单纯的工作狂，谁犯错都不可能是她们犯错。\n况且，S级禁令，那基本上意味着能够动摇整个城市的危险。"
    qian "我不明白。\n我不明白……为什么？"
    hide qian_shocked1
    show bfem_0r at char_mid with dissolve
    bfem_speaking "看完了吗？走吧。"
    show qian_shocked1 at char_mid
    qian_speaking "什么？不，等等，我不懂……喂！\n你，你们不能这样……给我一个解释啊！为什么？！"
    hide qian_shocked1
    show qian_close1 at char_mid
    qian_speaking "……唔！好痛，痛……啊啊！"
    scene bg_office_1
    scene bg_office_2 with fade
    qian "和之前一样，四个高大女人围着我，手拿武器，仿佛我罪大恶极。\n可我明明只是在家里睡觉，一无所知。只是在睡觉而已，醒来却发生这些事情。\n还有宋女士和黄女士，不知道她们怎么样了……"
    scene bg_office_3 with Fade(0.1,0.2,0.1)
    qian "我全身上下只有一套居家睡衣和崭新的终端，身体被控制住，被拉着往外走。\n我死死咬住嘴唇，避免让眼泪流下来，显得更加狼狈不堪。"
    
    
    return





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