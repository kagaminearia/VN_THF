label q3_1:
    qian "迟玉，蓝石……不知为何，这两人的那个场景再度在我脑海里闪回。\n别再给我想那个了……！不，等等……说不定……"
    qian "一种莫名的情绪突如其来，我的视线来回滚动，不由得深深吸了一口气，然后……"
    lan_speaking "……"
    qian_speaking "唔……"
    chi_speaking "？！"
    qian_speaking "对不起，迟玉……现在听得见我说话吗？"
    #TODO: 闪回
    chi_speaking "哈，啊……"
    lan_speaking "你怎么敢？"
    qian_speaking "听我说……她，蓝石有这样做过吗？"
    chi_speaking "……她，我……"
    lan_speaking "不过是个失败品。"
    qian_speaking "我做了。所以别听她的，振作起来……你不用听她的！"
    chi_speaking "我……！"
    lan_speaking "我都没有动过的东西。"
    qian_speaking "迟玉放开我！"
    lan_speaking "你凭什么动我的东西？"
    qian_speaking "现在快跑！"
    lan_speaking "别妄想了！"
    chi_speaking "啊……！"
    #TODO: 快速闪过cg
    "呲——\n砰——\n咚——"
    qian_speaking "呜……！哈啊……"
    qian "只不过是一瞬间的事。我成功推开迟玉，拽着台灯往前一扑。"
    #TODO: 转场晃动
    chi_speaking "她，她绊倒了……"
    lan_speaking "你们跑不了——"
    #TODO: 上下摇晃的立绘
    qian_speaking "别管了，走！"
    chi_speaking "啊……好！"
    qian_speaking "哈啊……现在怎么办……虽然把两边的门堵上了，应该等不了多久吧……"
    #TODO: 转场
    chi_speaking "是，是啊……而且这个办公室外面的地方都是有监控的……"
    qian_speaking "结果跑出来了还是不行吗……你能不能找到人帮忙？"
    chi_speaking "不行，那之后……我的终端就被关掉了。\n不过这个房间也有逃生通道，抓紧时间的话……"
    qian_speaking "只能这样了……你可以带路吗？"
    chi_speaking "当然。\n对了……那个……"
    qian_speaking "啊？"
    chi_speaking "谢谢你，对我说那些话……还有，那个，你对我……"
    qian_speaking "呃，那个……我们还是先出去吧。"
    qian "迟玉的脸颊肉眼可见地泛起红色，我大概知道她下一句要说什么，于是也有些不自然，只好生硬地跳转话题。"
    qian "说话几句的时间，我们已经走到另一扇暗门附近，迟玉操作几下，便浮出来一块屏幕。"
    qian_speaking "这房间真是够大的……这是什么？身份验证吗？"
    chi_speaking "是的……不验证的话，也可以输密码……不过，只有一次机会。"
    qian_speaking "太刁钻了吧……"
    chi_speaking "至少……还有输密码的机会。"
    qian_speaking "也是，现在只能赌一把了……但我什么都不清楚，你……你和蓝石熟悉，有什么猜测吗？"
    chi_speaking "我也不是很清楚……但要猜数字密码的话，常见的就是那些吧……生日，纪念日，之类的……啊——"
    "砰！"
    chi_speaking "门，外面门要开了……"
    qian_speaking "我知道——"
    qian "真的，只能赌一把了……要输入什么呢——"
    # qte here
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'q3_1_0'
    show screen countdown
    menu:
        "【蓝石的生日】":
            "哔——"
            qian "错误……"
            hide screen countdown
            jump q3_1_0
        "【迟玉的生日】":
            "哔——"
            qian "错误……"
            hide screen countdown
            jump q3_1_0
        "【“迟玉”的生日】":
            hide screen countdown
            jump q3_1_1
        "【其他数字】":
            "哔——"
            qian "错误……"
            hide screen countdown
            jump q3_1_0

label q3_1_1: # ending here
    "叮——"
    qian_speaking "对了……！"
    "砰！"
    chi_speaking "快，快跑！"
    qian_speaking "嗯……！"
    lan_speaking "喂——"
    qian_speaking "！！！"
    #TODO: 闪烁，转场
    qian "两只手掌硬生生卡住了门缝，阻止我将它合拢。"
    qian_speaking "你竟然，自己……"
    lan_speaking "呵呵，呵呵呵……别走啊，我们还没聊完吧？"
    qian_speaking "你，你这人……"
    "咯吱，咯吱咯吱……\n咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱"
    qian "哈，哈啊……剧烈的挤压声让我的手掌也剧烈颤抖起来，我们僵持在这个位置，达到一种恶心的高度平衡。"
    chi_speaking "时茜……这，这是……？！"
    qian_speaking "你别看了……你，你先走吧。"
    lan_speaking "别想多……"
    chi_speaking "那怎么行，啊，怎么办……"
    lan_speaking "你们都别跑。"
    qian_speaking "喂……你放开吧！很痛吧！"
    lan_speaking "谁允许你反抗的？"
    qian_speaking "为什么这么执着啊……为什么非得是她啊！"
    lan_speaking "你懂什么。"
    qian_speaking "放——开——！只是这种事……至于做到这种程度吗！！！"
    lan_speaking "我想要的东西，必须属于我。"
    qian_speaking "你这……疯子啊啊啊啊啊！"
    "咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯吱咯\n啪！"
    "砰！\n轰！"
    qian_speaking "啊啊……呜……呃啊……"
    chi_speaking "没，没事吧……时茜……对不起，都怪我……"
    qian_speaking "没，不是说这些的时候，快走吧……"
    "嗡——"
    chi_speaking "糟了，她要启动穿梭机……"
    qian_speaking "快走！"
    qian "哈啊……哈……\n来回……折腾，我真的……要……没力气了……\n得快点……出去……就……不会被……啊……！"
    qian_speaking "啊……"
    #TODO: 摇晃
    chi_speaking "抓住我！"
    chi_speaking "好……很快……就出去——"
    "轰！！！"
    "……"
    "……"
    "……"
    qian_speaking "迟玉……！！\n……啊？"
    doctor_speaking "不要大声喧哗。"
    qian_speaking "这，这里是……"
    doctor_speaking "感觉好点的话，晚上来做个检查。"
    qian_speaking "诶等等别走——\n啊……"
    chi_speaking "时茜……"
    qian_speaking "啊！\n你没事……太好了……不过，这是……"
    qian "我瞬间转过头，看到那熟悉的脸庞和蓝色眼眸才猛地松了口气，这才有精力观察四周。\n这里是医院……刚才的医生出去后只剩我和迟玉两个人。"
    chi_speaking "看起来……好像得救了呢，谢谢你。\n你感觉怎么样？有哪里不舒服吗？"
    qian_speaking "头有点晕，其他还好……话说这是怎么回事？之前……她，蓝石……"
    chi_speaking "……\n是啊，她启动了自毁装置。除了我们，其他人大概都……"
    #TODO: 闪烁
    qian_speaking "怎么会……为什么啊……那个人，真的……到底是怎么想的……"
    chi_speaking "我大概……能猜到。"
    qian_speaking "啊？"
    chi_speaking "她……想要的东西，必须拿到才行……反过来说，如果拿不到，她……"
    qian_speaking "……宁愿都毁掉吗……"
    chi_speaking "嗯……"
    qian_speaking "就为了，这个吗……她到底是怎么做到的……\n你还真是……了解她呢。"
    chi_speaking "毕竟……我被她养了十几年。连累你了……对不起。"
    qian_speaking "啊，我不是想说那个！对，对了……之后会怎么样？"
    chi_speaking "不知道，但是……如果有留下来的资料，大概会被查到吧，这么大的事故……"
    qian_speaking "我是说……你之后呢？"
    chi_speaking "……\n如果管制局不处罚的话，应该会去做医生吧……\n那个，我之前要说的，你家里……"
    qian_speaking "我知道的。"
    chi_speaking "啊，那个……"
    qian "其实我早就有猜测了，只是一直不愿意确信而已。\n像蓝石那样作风的人，如果和我家里人起了冲突，之后还那样对我的话，那她们肯定早就……"
    qian_speaking "反正，也这样了……我，早就知道……"
    chi_speaking "……对不起……"
    qian_speaking "……不是你的错啊。"
    chi_speaking "不，不能这么算的，我知道，蓝石是因为我才……\n但她已经……我不知道做什么才能补偿你，只要你想的话……我什么都可以……"
    qian_speaking "……"
    chi_speaking "真的……！我没有说大话，我，我不想，看到你难过……对不起……"
    qian_speaking "……\n好吧，我知道了。"
    chi_speaking "嗯……！你说什么，我都会尽力去做的！"
    qian_speaking "好……那，\n以后，都一直跟我在一起吧。"
    chi_speaking "……唉……？"
    qian_speaking "这就是我的想法。"
    chi_speaking "啊……"
    chi_speaking "我，那个……\n我知道了……！"
    chi_speaking "我，我会的！！"
    qian_speaking "好啊。"

    return 

label q3_1_0: # ending here
    "砰！"
    qian "没时间了……"
    chi_speaking "时茜……"
    qian_speaking "……"
    qian "我无言地看向迟玉，她和她眼里的我在这一刻的时间被无限拉长。意识到这一刻到来时，我的内心竟然惊人的平静。"
    qian_speaking "抱歉啊，迟玉……"

    return 
