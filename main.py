# coding: utf-8
import pygame
import random
import cProfile

# 初始化游戏
pygame.init()
# 设置窗口，游戏名，默认背景颜色，字体对象
window = pygame.display.set_mode((900, 600), pygame.SRCALPHA)
surface = pygame.display.set_mode((900, 600), pygame.SRCALPHA)
w_window, h_window = 900, 600
pygame.display.set_caption('猪尾巴')
window.fill((255, 255, 255))
font_cat_20 = pygame.font.Font('py_pig/cat.ttf', 20)
font_cat_24 = pygame.font.Font('py_pig/cat.ttf', 24)
font_cat_30 = pygame.font.Font('py_pig/cat.ttf', 30)
font_cat_50 = pygame.font.Font('py_pig/cat.ttf', 50)
font_cat_80 = pygame.font.Font('py_pig/cat.ttf', 100)
font_north_120 = pygame.font.Font('py_pig/north.ttf', 120)
pygame.display.flip()


# 游戏首页
def enter_home():
    # 编辑首页
    image1 = pygame.transform.scale(pygame.image.load('py_pig/原木.jpeg'), (900, 600))
    window.blit(image1, (0, 0))
    pygame.draw.rect(surface, (245, 154, 35, 177), (325, 280, 250, 100), 0, border_radius=40)
    pygame.draw.rect(surface, (245, 154, 35, 177), (325, 420, 250, 100), 0, border_radius=40)
    window.blit(surface, (0, 0))
    font_start = font_cat_50.render('开始游戏', True, (0, 0, 255))
    font_rule = font_cat_50.render('游戏规则', True, (0, 0, 255))
    font_pig = font_north_120.render('猪尾巴', True, (255, 0, 0))
    w_start, h_start = font_start.get_size()
    window.blit(font_start, (450-w_start/2, 330-h_start/2))
    window.blit(font_rule, (450-w_start/2, 470-h_start/2))
    window.blit(font_pig, (270, 85))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                exit()
            # 按下鼠标
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # 按下开始游戏
                if 325 <= x <= 575 and 280 <= y <= 380:
                    pygame.draw.rect(surface, (250, 205, 145, 177), (325, 280, 250, 100), 0, border_radius=40)
                    font_start = font_cat_50.render('开始游戏', True, (128, 128, 255))
                    window.blit(font_start, (450 - w_start / 2, 330 - h_start / 2))
                    pygame.display.update()
                # 按下游戏规则
                elif 325 <= x <= 575 and 420 <= y <= 520:
                    pygame.draw.rect(surface, (250, 205, 145, 177), (325, 420, 250, 100), 0, border_radius=40)
                    font_rule = font_cat_50.render('游戏规则', True, (128, 128, 255))
                    window.blit(font_rule, (450 - w_start / 2, 470 - h_start / 2))
                    pygame.display.update()
            # 弹起鼠标
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                pygame.draw.rect(surface, (245, 154, 35, 177), (325, 280, 250, 100), 0, border_radius=40)
                pygame.draw.rect(surface, (245, 154, 35, 177), (325, 420, 250, 100), 0, border_radius=40)
                font_start = font_cat_50.render('开始游戏', True, (0, 0, 255))
                font_rule = font_cat_50.render('游戏规则', True, (0, 0, 255))
                window.blit(font_start, (450 - w_start / 2, 330 - h_start / 2))
                window.blit(font_rule, (450-w_start/2, 470-h_start/2))
                pygame.display.update()
                # 弹起开始游戏
                if 325 <= x <= 575 and 280 <= y <= 380:
                    print('开始游戏')
                    start_game()
                # 弹起游戏规则
                elif 325 <= x <= 575 and 420 <= y <= 520:
                    print('游戏规则')
                    rule_game()


# 开始游戏页面
def start_game():
    # 初始化
    window.fill((255, 255, 255))
    window.blit(pygame.transform.scale(pygame.image.load('py_pig/原木.jpeg'), (900, 600)), (0, 0))
    pygame.draw.rect(surface, (245, 154, 35, 177), (325, 115, 250, 100), 0, border_radius=40)
    pygame.draw.rect(surface, (245, 154, 35, 177), (325, 250, 250, 100), 0, border_radius=40)
    pygame.draw.rect(surface, (245, 154, 35, 177), (325, 385, 250, 100), 0, border_radius=40)
    pygame.draw.circle(surface, (0, 191, 191), (125, 125), 50, 0)
    font_pve = font_cat_50.render('人机对战', True, (0, 0, 255))
    font_2p = font_cat_50.render('双人对战', True, (0, 0, 255))
    font_pvp = font_cat_50.render('联机对战', True, (0, 0, 255))
    font_back = font_cat_30.render('返回', True, (0, 0, 255))
    w_start, h_start = font_2p.get_size()
    window.blit(font_pve, (450-w_start/2, 165-h_start/2))
    window.blit(font_2p, (450-w_start/2, 300-h_start/2))
    window.blit(font_pvp, (450-w_start/2, 435-h_start/2))
    window.blit(font_back, (95, 110))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                exit()
            # 按下鼠标
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # 按下人机对战
                if 325 <= x <= 575 and 115 <= y <= 215:
                    pygame.draw.rect(surface, (250, 205, 145, 177), (325, 115, 250, 100), 0, border_radius=40)
                    font_pve = font_cat_50.render('人机对战', True, (128, 128, 255))
                    window.blit(font_pve, (450 - w_start / 2, 165 - h_start / 2))
                    pygame.display.update()
                # 按下双人对战
                elif 325 <= x <= 575 and 250 <= y <= 350:
                    pygame.draw.rect(surface, (250, 205, 145, 177), (325, 250, 250, 100), 0, border_radius=40)
                    font_2p = font_cat_50.render('双人对战', True, (128, 128, 255))
                    window.blit(font_2p, (450 - w_start / 2, 300 - h_start / 2))
                    pygame.display.update()
                # 按下联机对战
                elif 325 <= x <= 575 and 420 <= y <= 520:
                    pygame.draw.rect(surface, (250, 205, 145, 177), (325, 385, 250, 100), 0, border_radius=40)
                    font_pvp = font_cat_50.render('联机对战', True, (128, 128, 255))
                    window.blit(font_pvp, (450 - w_start / 2, 435 - h_start / 2))
                    pygame.display.update()
                # 按下返回
                elif 90 <= x <= 160 and 90 <= y <= 160:
                    pygame.draw.circle(surface, (0, 255, 255, 177), (125, 125), 50, 0)
                    font_back = font_cat_30.render('返回', True, (128, 128, 255))
                    window.blit(font_back, (95, 110))
                    pygame.display.update()
            # 弹起鼠标
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                pygame.draw.rect(surface, (245, 154, 35, 177), (325, 115, 250, 100), 0, border_radius=40)
                pygame.draw.rect(surface, (245, 154, 35, 177), (325, 250, 250, 100), 0, border_radius=40)
                pygame.draw.rect(surface, (245, 154, 35, 177), (325, 385, 250, 100), 0, border_radius=40)
                pygame.draw.circle(surface, (0, 191, 191), (125, 125), 50, 0)
                font_pve = font_cat_50.render('人机对战', True, (0, 0, 255))
                font_2p = font_cat_50.render('双人对战', True, (0, 0, 255))
                font_pvp = font_cat_50.render('联机对战', True, (0, 0, 255))
                font_back = font_cat_30.render('返回', True, (0, 0, 255))
                window.blit(font_pve, (450 - w_start / 2, 165 - h_start / 2))
                window.blit(font_2p, (450 - w_start / 2, 300 - h_start / 2))
                window.blit(font_pvp, (450 - w_start / 2, 435 - h_start / 2))
                window.blit(font_back, (95, 110))
                pygame.display.update()
                # 弹起人机对战
                if 325 <= x <= 575 and 115 <= y <= 215:
                    print('人机对战')
                    battle_pve()
                # 弹起双人对战
                elif 325 <= x <= 575 and 250 <= y <= 350:
                    print('双人对战')
                    battle_2p()
                # 弹起联机对战
                elif 325 <= x <= 575 and 385 <= y <= 485:
                    print('联机对战')
                    battle_2p()
                # 弹起返回
                elif 90 <= x <= 160 and 90 <= y <= 160:
                    print('返回')
                    enter_home()


# 游戏规则页面
def rule_game():
    # 初始化
    window.fill((255, 255, 255))
    window.blit(pygame.transform.scale(pygame.image.load('py_pig/原木.jpeg'), (900, 600)), (0, 0))
    window.blit(font_cat_30.render('【规则】：', True, (0, 0, 0)), (50, 50))
    window.blit(font_cat_24.render('1.由一名玩家开始，从<卡组>随机抽取翻开一张扑克牌，置于<放置区>上。', True, (0, 0, 0)), (50, 100))
    window.blit(font_cat_24.render('2.切换到另外一名玩家操作，执行1操作，此时插入判定:', True, (0, 0, 0)), (50, 150))
    window.blit(font_cat_24.render('若翻开的花色与<放置区>原顶部扑克牌花色相同，', True, (0, 0, 0)), (75, 190))
    window.blit(font_cat_24.render('需将放置区的所有牌收到自己<手牌>内（即”吃“牌）。', True, (0, 0, 0)), (75, 220))
    window.blit(font_cat_24.render('3.在执行1操作前，若玩家<手牌>非空，则:', True, (0, 0, 0)), (50, 270))
    window.blit(font_cat_24.render('玩家可选择放弃翻牌，', True, (0, 0, 0)), (75, 310))
    window.blit(font_cat_24.render('同时需要从<手牌>中选择一张牌置于<放置区>顶部作为替代，判定同2操作。', True, (0, 0, 0)), (75, 340))
    window.blit(font_cat_24.render('4.若<卡组>非空，则重复2操作；', True, (0, 0, 0)), (50, 390))
    window.blit(font_cat_24.render('5.当<卡组>为空，且插入判定结算完成，游戏终止，进行结算判定:', True, (0, 0, 0)), (50, 440))
    window.blit(font_cat_24.render('比较两玩家<手牌>卡牌数量:', True, (0, 0, 0)), (75, 480))
    window.blit(font_cat_24.render('  ~剩余卡片数量小者获胜;', True, (0, 0, 0)), (75, 510))
    window.blit(font_cat_24.render('  ~数量相同则判断为平局。', True, (0, 0, 0)), (75, 540))
    pygame.draw.circle(surface, (0, 191, 191), (800, 500), 50, 0)
    font_back = font_cat_30.render('返回', True, (0, 0, 255))
    window.blit(font_back, (770, 485))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                exit()
            # 按下返回
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 765 <= x <= 835 and 465 <= y <= 535:
                    pygame.draw.circle(surface, (0, 255, 255, 177), (800, 500), 50, 0)
                    font_back = font_cat_30.render('返回', True, (128, 128, 255))
                    window.blit(font_back, (770, 485))
                    pygame.display.update()
            # 弹起返回
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                pygame.draw.circle(surface, (0, 191, 191), (800, 500), 50, 0)
                font_back = font_cat_30.render('返回', True, (0, 0, 255))
                window.blit(font_back, (770, 485))
                pygame.display.update()
                if 765 <= x <= 835 and 465 <= y <= 535:
                    print('返回')
                    enter_home()


# 双人对战
def battle_2p():
    # 初始数据定义
    # 两位玩家
    player = ('A', 'B')
    # 牌库
    num_library = {'黑桃': 13, '梅花': 13, '红心': 13, '方块': 13}
    library = []
    for i in range(0, 52):
        library.append(i+1)
    top = 0
    # 放置区
    num_placement = {'黑桃': 0, '梅花': 0, '红心': 0, '方块': 0}
    placement = []
    # 手牌
    hand_player = [{'黑桃': 0, '梅花': 0, '红心': 0, '方块': 0}, {'黑桃': 0, '梅花': 0, '红心': 0, '方块': 0}]
    hand_poker = [[], []]
    # 扑克牌统计
    poker = []
    flag = 0
    for i in range(1, 52):
        poker.append(pygame.image.load('py_pig/poker/' + str(i) + '.jpg'))
    poker_back = pygame.image.load('py_pig/poker/back.jpeg')
    i, j = 1, 0

    # 基本界面
    def basic_interface():
        window.blit(pygame.transform.scale(pygame.image.load('py_pig/原木.jpeg'), (900, 600)), (0, 0))
        pygame.draw.rect(window, (170, 170, 170), (100, 60, 330, 230), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (100, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (285, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (470, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (655, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (470, 100, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (655, 100, 145, 190), 0, border_radius=12)
        window.blit(font_cat_24.render('记牌器：', True, (0, 0, 0)), (125, 80))
        window.blit(font_cat_24.render('牌库:' + str(sum(num_library.values())), True, (0, 0, 0)), (110, 120))
        window.blit(font_cat_24.render('黑桃:' + str(num_library['黑桃']), True, (0, 0, 0)), (110, 150))
        window.blit(font_cat_24.render('梅花:' + str(num_library['梅花']), True, (0, 0, 0)), (110, 180))
        window.blit(font_cat_24.render('红心:' + str(num_library['红心']), True, (0, 0, 0)), (110, 210))
        window.blit(font_cat_24.render('方块:' + str(num_library['方块']), True, (0, 0, 0)), (110, 240))
        window.blit(font_cat_24.render('对手:' + str(sum(hand_player[i].values())), True, (0, 0, 0)), (210, 120))
        window.blit(font_cat_24.render('黑桃:' + str(hand_player[i]['黑桃']), True, (0, 0, 0)), (210, 150))
        window.blit(font_cat_24.render('梅花:' + str(hand_player[i]['梅花']), True, (0, 0, 0)), (210, 180))
        window.blit(font_cat_24.render('红心:' + str(hand_player[i]['红心']), True, (0, 0, 0)), (210, 210))
        window.blit(font_cat_24.render('方块:' + str(hand_player[i]['方块']), True, (0, 0, 0)), (210, 240))
        window.blit(font_cat_24.render('放置区:' + str(sum(num_placement.values())), True, (0, 0, 0)), (315, 120))
        window.blit(font_cat_24.render('黑桃:' + str(num_placement['黑桃']), True, (0, 0, 0)), (315, 150))
        window.blit(font_cat_24.render('梅花:' + str(num_placement['梅花']), True, (0, 0, 0)), (315, 180))
        window.blit(font_cat_24.render('红心:' + str(num_placement['红心']), True, (0, 0, 0)), (315, 210))
        window.blit(font_cat_24.render('方块:' + str(num_placement['方块']), True, (0, 0, 0)), (315, 240))
        window.blit(font_cat_24.render('玩家：' + player[j], True, (0, 0, 0)), (100, 310))
        window.blit(font_cat_24.render('牌数:' + str(sum(hand_player[j].values())), True, (0, 0, 0)), (300, 310))
        window.blit(font_cat_24.render('黑桃 ' + str(hand_player[j]['黑桃']), True, (0, 0, 0)), (135, 340))
        window.blit(font_cat_24.render('梅花 ' + str(hand_player[j]['梅花']), True, (0, 0, 0)), (320, 340))
        window.blit(font_cat_24.render('红心 ' + str(hand_player[j]['红心']), True, (0, 0, 0)), (505, 340))
        window.blit(font_cat_24.render('方块 ' + str(hand_player[j]['方块']), True, (0, 0, 0)), (690, 340))
        window.blit(font_cat_24.render('牌库 ', True, (0, 0, 0)), (520, 60))
        window.blit(font_cat_24.render('放置区', True, (0, 0, 0)), (690, 60))
        window.blit(pygame.transform.scale(poker_back, (105, 150)), (490, 120))

    # 进行收牌
    def drawing():
        hand_player[i]['黑桃'] += num_placement['黑桃']
        hand_player[i]['梅花'] += num_placement['梅花']
        hand_player[i]['红心'] += num_placement['红心']
        hand_player[i]['方块'] += num_placement['方块']
        num_placement['黑桃'] = num_placement['梅花'] = num_placement['红心'] = num_placement['方块'] = 0

    while True:
        basic_interface()
        # 是否显示放置区牌与手牌
        if top != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(top) + '.jpg'), (675, 120))
        if hand_player[j]['黑桃'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(1) + '.jpg'), (120, 395))
        if hand_player[j]['梅花'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(14) + '.jpg'), (305, 395))
        if hand_player[j]['红心'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(27) + '.jpg'), (490, 395))
        if hand_player[j]['方块'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(40) + '.jpg'), (675, 395))

        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                exit()
            # 玩家操作（鼠标弹起）
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                # 玩家交替操作
                if i == 1:
                    i, j = 0, 1
                else:
                    i, j = 1, 0
                # 出牌
                # 判断是否与牌顶同花色
                if 120 <= x <= 225 and 395 <= y <= 545 and hand_player[i]['黑桃'] > 0:
                    if 1 <= top <= 13:
                        drawing()
                        top = 0
                    else:
                        top = 1
                        hand_player[i]['黑桃'] -= 1
                        num_placement['黑桃'] += 1

                elif 305 <= x <= 410 and 395 <= y <= 545 and hand_player[i]['梅花'] > 0:
                    if 14 <= top <= 26:
                        drawing()
                        top = 0
                    else:
                        top = 14
                        hand_player[i]['梅花'] -= 1
                        num_placement['梅花'] += 1

                elif 490 <= x <= 595 and 395 <= y <= 545 and hand_player[i]['红心'] > 0:
                    if 27 <= top <= 39:
                        drawing()
                        top = 0
                    else:
                        top = 27
                        hand_player[i]['红心'] -= 1
                        num_placement['红心'] += 1

                elif 675 <= x <= 780 and 395 <= y <= 545 and hand_player[i]['方块'] > 0:
                    if 40 <= top:
                        drawing()
                        top = 0
                    else:
                        top = 40
                        hand_player[i]['方块'] -= 1
                        num_placement['方块'] += 1

                # 抽牌
                elif 490 <= x <= 595 and 120 <= y <= 270:
                    rand = random.randint(0, len(library)-1)
                    # 显示抽到的牌，鼠标移动或其他操作即取消显示
                    window.blit(pygame.image.load('py_pig/poker/' + str(library[rand]) + '.jpg'), (490, 120))
                    f = 0
                    # 判断是否与牌顶同花色
                    if 1 <= library[rand] <= 13:
                        print('抽到黑桃', library[rand])
                        num_library['黑桃'] -= 1
                        num_placement['黑桃'] += 1
                        if 1 <= top <= 13:
                            drawing()
                            f = 1
                    elif 14 <= library[rand] <= 26:
                        print('抽到梅花', library[rand]-13)
                        num_library['梅花'] -= 1
                        num_placement['梅花'] += 1
                        if 14 <= top <= 26:
                            drawing()
                            f = 1
                    elif 27 <= library[rand] <= 39:
                        print('抽到红心', library[rand]-26)
                        num_library['红心'] -= 1
                        num_placement['红心'] += 1
                        if 27 <= top <= 39:
                            drawing()
                            f = 1
                    else:
                        print('抽到方块', library[rand]-39)
                        num_library['方块'] -= 1
                        num_placement['方块'] += 1
                        if top >= 40:
                            drawing()
                            f = 1
                    if f == 0:
                        top = library[rand]
                    else:
                        top = 0
                    library.pop(rand)
                else:
                    if i == 1:
                        i, j = 0, 1
                    else:
                        i, j = 1, 0

                # 游戏结束
                if sum(num_library.values()) == 0:
                    if sum(hand_player[0].values()) < sum(hand_player[1].values()):
                        game_over(player[0])
                    elif sum(hand_player[0].values()) > sum(hand_player[1].values()):
                        game_over(player[1])
                    else:
                        game_over(0)

            # 刷新
            pygame.display.update()


# 人机对战
def battle_pve():
    player = ('电脑', 'A')
    num_library = {'黑桃': 13, '梅花': 13, '红心': 13, '方块': 13}
    library = []
    for i in range(0, 52):
        library.append(i+1)
    top = 0
    num_placement = {'黑桃': 0, '梅花': 0, '红心': 0, '方块': 0}
    placement = []
    hand_player = [{'黑桃': 0, '梅花': 0, '红心': 0, '方块': 0}, {'黑桃': 0, '梅花': 0, '红心': 0, '方块': 0}]
    hand_poker = [[], []]
    poker = []
    flag = 0
    for i in range(1, 52):
        poker.append(pygame.image.load('py_pig/poker/' + str(i) + '.jpg'))
    poker_back = pygame.image.load('py_pig/poker/back.jpeg')
    i, j = 0, 1

    # 基本界面
    def basic_interface():
        window.blit(pygame.transform.scale(pygame.image.load('py_pig/原木.jpeg'), (900, 600)), (0, 0))
        pygame.draw.rect(window, (170, 170, 170), (100, 60, 330, 230), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (100, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (285, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (470, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (655, 375, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (470, 100, 145, 190), 0, border_radius=12)
        pygame.draw.rect(window, (170, 170, 170), (655, 100, 145, 190), 0, border_radius=12)
        window.blit(font_cat_24.render('记牌器：', True, (0, 0, 0)), (125, 80))
        window.blit(font_cat_24.render('牌库:' + str(sum(num_library.values())), True, (0, 0, 0)), (110, 120))
        window.blit(font_cat_24.render('黑桃:' + str(num_library['黑桃']), True, (0, 0, 0)), (110, 150))
        window.blit(font_cat_24.render('梅花:' + str(num_library['梅花']), True, (0, 0, 0)), (110, 180))
        window.blit(font_cat_24.render('红心:' + str(num_library['红心']), True, (0, 0, 0)), (110, 210))
        window.blit(font_cat_24.render('方块:' + str(num_library['方块']), True, (0, 0, 0)), (110, 240))
        window.blit(font_cat_24.render('对手:' + str(sum(hand_player[i].values())), True, (0, 0, 0)), (210, 120))
        window.blit(font_cat_24.render('黑桃:' + str(hand_player[i]['黑桃']), True, (0, 0, 0)), (210, 150))
        window.blit(font_cat_24.render('梅花:' + str(hand_player[i]['梅花']), True, (0, 0, 0)), (210, 180))
        window.blit(font_cat_24.render('红心:' + str(hand_player[i]['红心']), True, (0, 0, 0)), (210, 210))
        window.blit(font_cat_24.render('方块:' + str(hand_player[i]['方块']), True, (0, 0, 0)), (210, 240))
        window.blit(font_cat_24.render('放置区:' + str(sum(num_placement.values())), True, (0, 0, 0)), (315, 120))
        window.blit(font_cat_24.render('黑桃:' + str(num_placement['黑桃']), True, (0, 0, 0)), (315, 150))
        window.blit(font_cat_24.render('梅花:' + str(num_placement['梅花']), True, (0, 0, 0)), (315, 180))
        window.blit(font_cat_24.render('红心:' + str(num_placement['红心']), True, (0, 0, 0)), (315, 210))
        window.blit(font_cat_24.render('方块:' + str(num_placement['方块']), True, (0, 0, 0)), (315, 240))
        window.blit(font_cat_24.render('玩家：' + player[j], True, (0, 0, 0)), (100, 310))
        window.blit(font_cat_24.render('牌数:' + str(sum(hand_player[j].values())), True, (0, 0, 0)), (300, 310))
        window.blit(font_cat_24.render('黑桃 ' + str(hand_player[j]['黑桃']), True, (0, 0, 0)), (135, 340))
        window.blit(font_cat_24.render('梅花 ' + str(hand_player[j]['梅花']), True, (0, 0, 0)), (320, 340))
        window.blit(font_cat_24.render('红心 ' + str(hand_player[j]['红心']), True, (0, 0, 0)), (505, 340))
        window.blit(font_cat_24.render('方块 ' + str(hand_player[j]['方块']), True, (0, 0, 0)), (690, 340))
        window.blit(font_cat_24.render('牌库 ', True, (0, 0, 0)), (520, 60))
        window.blit(font_cat_24.render('放置区', True, (0, 0, 0)), (690, 60))
        window.blit(pygame.transform.scale(poker_back, (105, 150)), (490, 120))

    # 进行收牌
    def drawing():
        hand_player[i]['黑桃'] += num_placement['黑桃']
        hand_player[i]['梅花'] += num_placement['梅花']
        hand_player[i]['红心'] += num_placement['红心']
        hand_player[i]['方块'] += num_placement['方块']
        num_placement['黑桃'] = num_placement['梅花'] = num_placement['红心'] = num_placement['方块'] = 0

    # 游戏循环
    while True:
        basic_interface()
        if top != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(top) + '.jpg'), (675, 120))
        if hand_player[j]['黑桃'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(1) + '.jpg'), (120, 395))
        if hand_player[j]['梅花'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(14) + '.jpg'), (305, 395))
        if hand_player[j]['红心'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(27) + '.jpg'), (490, 395))
        if hand_player[j]['方块'] != 0:
            window.blit(pygame.image.load('py_pig/poker/' + str(40) + '.jpg'), (675, 395))

        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                exit()
            if i == 0:
                # 玩家操作（鼠标弹起）
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    # 出牌
                    if 120 <= x <= 225 and 395 <= y <= 545 and hand_player[i]['黑桃'] > 0:
                        hand_player[i]['黑桃'] -= 1
                        if 1 <= top <= 13:
                            drawing()
                            hand_player[i]['黑桃'] += 1
                            top = 0
                        else:
                            top = 1

                    elif 305 <= x <= 410 and 395 <= y <= 545 and hand_player[i]['梅花'] > 0:
                        hand_player[i]['梅花'] -= 1
                        if 14 <= top <= 26:
                            drawing()
                            hand_player[i]['梅花'] += 1
                            top = 0
                        else:
                            top = 14

                    elif 490 <= x <= 595 and 395 <= y <= 545 and hand_player[i]['红心'] > 0:
                        hand_player[i]['红心'] -= 1
                        if 27 <= top <= 39:
                            drawing()
                            hand_player[i]['红心'] += 1
                            top = 0
                        else:
                            top = 27

                    elif 675 <= x <= 780 and 395 <= y <= 545 and hand_player[i]['方块'] > 0:
                        hand_player[i]['方块'] -= 1
                        if 40 <= top:
                            drawing()
                            hand_player[i]['方块'] += 1
                            top = 0
                        else:
                            top = 40

                    # 抽牌
                    elif 490 <= x <= 595 and 120 <= y <= 270:
                        rand = random.randint(0, len(library)-1)
                        window.blit(pygame.image.load('py_pig/poker/' + str(library[rand]) + '.jpg'), (490, 120))
                        f = 0
                        if 1 <= library[rand] <= 13:
                            print('抽到黑桃', library[rand])
                            num_library['黑桃'] -= 1
                            num_placement['黑桃'] += 1
                            if 1 <= top <= 13:
                                drawing()
                                f = 1
                        elif 14 <= library[rand] <= 26:
                            print('抽到梅花', library[rand]-13)
                            num_library['梅花'] -= 1
                            num_placement['梅花'] += 1
                            if 14 <= top <= 26:
                                drawing()
                                f = 1
                        elif 27 <= library[rand] <= 39:
                            print('抽到红心', library[rand]-26)
                            num_library['红心'] -= 1
                            num_placement['红心'] += 1
                            if 27 <= top <= 39:
                                drawing()
                                f = 1
                        else:
                            print('抽到方块', library[rand]-39)
                            num_library['方块'] -= 1
                            num_placement['方块'] += 1
                            if top >= 40:
                                drawing()
                                f = 1
                        if f == 0:
                            top = library[rand]
                        else:
                            top = 0
                        library.pop(rand)

                    # 游戏结束
                    if sum(num_library.values()) == 0:
                        if sum(hand_player[0].values()) < sum(hand_player[1].values()):
                            game_over(player[0])
                        elif sum(hand_player[0].values()) > sum(hand_player[1].values()):
                            game_over(player[1])
                        else:
                            game_over(0)
            else:
                if sum(num_library.values()) * 2 <= sum(hand_player[j].values()):
                    # 抽牌
                    rand = random.randint(0, len(library)-1)
                    window.blit(pygame.image.load('py_pig/poker/' + str(library[rand]) + '.jpg'), (490, 120))
                    f = 0
                    if 1 <= library[rand] <= 13:
                        print('抽到黑桃', library[rand])
                        num_library['黑桃'] -= 1
                        num_placement['黑桃'] += 1
                        if 1 <= top <= 13:
                            drawing()
                            f = 1
                    elif 14 <= library[rand] <= 26:
                        print('抽到梅花', library[rand]-13)
                        num_library['梅花'] -= 1
                        num_placement['梅花'] += 1
                        if 14 <= top <= 26:
                            drawing()
                            f = 1
                    elif 27 <= library[rand] <= 39:
                        print('抽到红心', library[rand]-26)
                        num_library['红心'] -= 1
                        num_placement['红心'] += 1
                        if 27 <= top <= 39:
                            drawing()
                            f = 1
                    else:
                        print('抽到方块', library[rand]-39)
                        num_library['方块'] -= 1
                        num_placement['方块'] += 1
                        if top >= 40:
                            drawing()
                            f = 1
                    if f == 0:
                        top = library[rand]
                    else:
                        top = 0
                    library.pop(rand)
                elif():
                    pass
                else:
                    # 抽牌
                    # 抽牌
                    rand = random.randint(0, len(library) - 1)
                    window.blit(pygame.image.load('py_pig/poker/' + str(library[rand]) + '.jpg'), (490, 120))
                    f = 0
                    if 1 <= library[rand] <= 13:
                        print('抽到黑桃', library[rand])
                        num_library['黑桃'] -= 1
                        num_placement['黑桃'] += 1
                        if 1 <= top <= 13:
                            drawing()
                            f = 1
                    elif 14 <= library[rand] <= 26:
                        print('抽到梅花', library[rand] - 13)
                        num_library['梅花'] -= 1
                        num_placement['梅花'] += 1
                        if 14 <= top <= 26:
                            drawing()
                            f = 1
                    elif 27 <= library[rand] <= 39:
                        print('抽到红心', library[rand] - 26)
                        num_library['红心'] -= 1
                        num_placement['红心'] += 1
                        if 27 <= top <= 39:
                            drawing()
                            f = 1
                    else:
                        print('抽到方块', library[rand] - 39)
                        num_library['方块'] -= 1
                        num_placement['方块'] += 1
                        if top >= 40:
                            drawing()
                            f = 1
                    if f == 0:
                        top = library[rand]
                    else:
                        top = 0
                    library.pop(rand)

            pygame.display.update()


# 游戏结束页面
def game_over(winner):
    window.blit(pygame.transform.scale(pygame.image.load('py_pig/原木.jpeg'), (900, 600)), (0, 0))
    if winner:
        win_font = font_cat_80.render('胜者是 ' + winner + ' !!!', True, (255, 50, 50))
        w, h = win_font.get_size()
        window.blit(win_font, (450 - w/2, 300 - h/2))
    else:
        win_font = font_cat_80.render('本局游戏结果为平局', True, (255, 50, 50))
        w, h = win_font.get_size()
        window.blit(win_font, (450 - w/2, 300 - h/2))
    pygame.draw.circle(surface, (0, 191, 191), (800, 500), 50, 0)
    window.blit(font_cat_30.render('返回', True, (0, 0, 255)), (770, 485))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                exit()
            # 按下返回
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 765 <= x <= 835 and 465 <= y <= 535:
                    pygame.draw.circle(surface, (0, 255, 255, 177), (800, 500), 50, 0)
                    font_back = font_cat_30.render('返回', True, (128, 128, 255))
                    window.blit(font_back, (770, 485))
                    pygame.display.update()
            # 弹起返回
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                pygame.draw.circle(surface, (0, 191, 191), (800, 500), 50, 0)
                font_back = font_cat_30.render('返回', True, (0, 0, 255))
                window.blit(font_back, (770, 485))
                pygame.display.update()
                if 765 <= x <= 835 and 465 <= y <= 535:
                    print('返回')
                    enter_home()


# 进入游戏首页
enter_home()