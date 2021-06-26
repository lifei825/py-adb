

def action(desc, action_type, **kwargs):
    return {device: {'desc': desc, 'xy': xy, 'type': action_type} for device, xy in kwargs.items()}


class Config(object):
    devices = {
        'mix2s': {
            'cache_path': 'mix2s_data.pk',
            # 'id': '192.168.1.88:5555',
            'id': 'f423bade'
        },
        'redmi': {
            'cache_path': 'redmi_data.pk',
            # 'id': '192.168.1.5:5554',
            'id': 'MZSWYXCMMZVOE68X',
        },
        'huawei': {
            'cache_path': 'huawei_data.pk',
            'id': 'BTFDU17318000996',
        },
        'redmi2': {
            'device': 'redmi',
            'cache_path': 'redmi_data.pk',
            'id': '192.168.1.5:5554',
        },
    }
    app = {
        'clears': {
            'name': '清理缓存',
            'pkg': 'com.huawei.systemmanager',
            'action': {
                'tap_qljs': action('点击清理加速', 'tap', **{'mix2s': (), 'redmi': (), 'huawei': (221, 1325)}),
                'wait_sm': {'desc': '等待扫描', 'interval': 50, 'type': 'sleep'},
                'tap_yjql': action('点击一键清理', 'tap', **{'mix2s': (), 'redmi': (), 'huawei': (542, 695)}),
            }
        },
        'qqyd': {
            'name': 'qqy阅读',
            'pkg': 'com.qq.reader',
            'action': {
                'tap_mf': action('点击免费', 'tap', **{'mix2s': (526, 2078), 'redmi': (), 'huawei': ()}),
                'tap_qyd': action('点击去阅读', 'tap', **{'mix2s': (916, 1214), 'redmi': (), 'huawei': ()}),
                'tap_book': action('选择小说', 'tap', **{'mix2s': (528, 1093), 'redmi': (), 'huawei': ()}),
                'tap_fy': action('点击翻页', 'tap', **{'mix2s': (1037, 250), 'redmi': (), 'huawei': ()}),
                'tap_bx': action('点击宝箱', 'tap', **{'mix2s': (898, 1850), 'redmi': (), 'huawei': ()}),
            }
        },
        'tb': {
            'name': '淘宝直播',
            'pkg': 'com.taobao.live',
            'action': {
                'tap_sp': action('点击赚钱', 'tap', **{'mix2s': (705, 136), 'redmi': (475, 116), 'huawei': (717, 174)}),
                'swipe_sp': action('上划视频', 'swipe',
                                   **{'mix2s': (558, 1444, 616, 717),
                                      'redmi': (500, 1044, 500, 717),
                                      'huawei': (558, 1244, 616, 717)}),
            }
        },
        'kkd': {
            'name': '快看点',
            'pkg': 'com.yuncheapp.android.pearl',
            'action': {
                'tap_sp': action('点击小视频', 'tap', **{'mix2s': (554, 2076), 'redmi': (378, 1552), 'huawei': (559, 1703)}),
                'swipe_sp': action('上划视频', 'swipe',
                                   **{'mix2s': (558, 1444, 616, 717),
                                      'redmi': (500, 1044, 500, 717),
                                      'huawei': (558, 1444, 616, 717)}),
            }
        },
        'jd': {
            'name': '京东极速版',
            'pkg': 'com.jd.jdlite',
            'action': {
                'tap_zq': action('点击赚钱', 'tap', **{'mix2s': (546, 2095), 'redmi': (), 'huawei': ()}),
                'tap_goods': action('点击逛商品', 'tap', **{'mix2s': (924, 1047), 'redmi': (), 'huawei': ()}),
                'tap_goods2': action('点击逛活动', 'tap', **{'mix2s': (924, 1233), 'redmi': (), 'huawei': ()}),
                'tap_goods3': action('点击看视频', 'tap', **{'mix2s': (924, 1409), 'redmi': (), 'huawei': ()}),
                'tap_sp': action('点击第一个视频', 'tap', **{'mix2s': (264, 934), 'redmi': (), 'huawei': ()}),
                'swipe_sp': action('上划屏幕', 'swipe', **{'mix2s': (537, 1543, 538, 870), 'redmi': (), 'huawei': ()}),
                'swipe_up': action('下划屏幕', 'swipe', **{'mix2s': (537, 548, 538, 2016), 'redmi': (), 'huawei': ()}),
                'tap_back': action('点击返回', 'tap', **{'mix2s': (64, 134), 'redmi': (), 'huawei': ()}),
            }
        },
        'toutiao': {
            'name': '今日头条',
            'pkg': 'com.ss.android.article.lite/com.ss.android.article.lite.activity.SplashActivity',
            'action': {
                'tap_bx': action('点击宝箱', 'tap', **{'mix2s': (943, 1888), 'redmi': (605, 1425), 'huawei': (916, 1542)}),
                'tap_bx_sp': action('点击宝箱领取金币看视频', 'tap',
                                    **{'mix2s': (545, 1409), 'redmi': (356, 1018), 'huawei': (551, 1236)}),
                'tap_task': action('点击任务', 'tap',
                                   **{'mix2s': (570, 2094), 'redmi': (354, 1584), 'huawei': (535, 1780)}),
                'wait_sp': {'desc': '等待广告视频', 'interval': 30, 'type': 'sleep'},
                'close_sp': action('关闭广告视频', 'tap',
                                   **{'mix2s': (971, 85), 'redmi': (655, 66), 'huawei': (961, 97)}),
                'tap_sleep': action('点击睡觉赚钱', 'tap', **{'mix2s': (), 'redmi': (207, 767), 'huawei': (334, 1156)}),
                'tap_sleep_start': action('我要睡了', 'tap', **{'mix2s': (), 'redmi': (360, 1477), 'huawei': (572, 1633)}),
            }
        },
        'kuaishou': {
            'name': '快手',
            'pkg': 'com.kuaishou.nebula',
            'action': {
                'tap_hb': action('点击首页红包', 'tap',
                                 **{'mix2s': (91, 933), 'redmi': (66, 777), 'huawei': (126, 884)}),
                'tap_menu': action('点击首页菜单', 'tap',
                                   **{'mix2s': (40, 158), 'redmi': (62, 129), 'huawei': (56, 138)}),
                'tap_menu_money': action('点击菜单去赚钱', 'tap',
                                         **{'mix2s': (541, 1070), 'redmi': (314, 766), 'huawei': (581, 1130)}),
                'tap_fuli': action('点击福利', 'tap',
                                   **{'mix2s': (937, 1395), 'redmi': (622, 1070), 'huawei': (933, 1044)}),
                'wait_sp': {'desc': '等待广告视频', 'interval': 35, 'type': 'sleep'},
                'tap_close_sp': action('关闭广告视频', 'tap',
                                       **{'mix2s': (985, 92), 'redmi': (660, 119), 'huawei': (1008, 108)}),
                'swipe_sp': action('上划视频', 'swipe',
                                   **{'mix2s': (558, 1444, 616, 717),
                                      'redmi': (500, 1044, 500, 717),
                                      'huawei': (558, 1444, 616, 717)}),
                'tap_close_wait': action('关闭等待', 'tap',
                                         **{'mix2s': (), 'redmi': (), 'huawei': (533, 1654)}),
                'tap_zb': action('看直播领金币', 'tap',
                                 **{'mix2s': (912, 1305), 'redmi': (623, 1173), 'huawei': (944, 1452)}),
                'tap_bx': action('宝箱领金币', 'tap',
                                 **{'mix2s': (925, 1628), 'redmi': (623, 1249), 'huawei': (918, 1301)}),
            }
        },
        'douyin': {
            'name': '抖音',
            'pkg': 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
            'action': {
                'tap_gold': action('点击首页金币', 'tap',
                                   **{'mix2s': (561, 2084), 'redmi': (371, 1561), 'huawei': (550, 1700)}),
                'tap_bx': action('点击宝箱', 'tap',
                                 **{'mix2s': (915, 2000), 'redmi': (607, 1485), 'huawei': (919, 1640)}),
                'tap_bx_sp': action('点击宝箱领取金币看视频', 'tap',
                                    **{'mix2s': (550, 1278), 'redmi': (372, 923), 'huawei': (550, 1103)}),
                'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                'close_sp': action('关闭广告视频', 'tap',
                                   **{'mix2s': (1006, 98),
                                      'redmi': (620, 144),
                                      'huawei': (945, 107)}),
                'tap_xs_sp': action('点击限时任务视频', 'tap',
                                    **{'mix2s': (885, 645),
                                       'redmi': (625, 425),
                                       'huawei': (893, 968)}),
                'swipe_sp': action('上划视频', 'swipe',
                                   **{'mix2s': (500, 1444, 500, 717),
                                      'redmi': (300, 1033, 300, 717),
                                      'huawei': (558, 1444, 616, 717)}),
            }
        },
        'huoshan': {
            'name': '火山',
            'pkg': 'com.ss.android.ugc.livelite',
            'action': {
                'tap_gold': action('点击首页红包', 'tap',
                                   **{'mix2s': (702, 2097), 'redmi': (440, 1538), 'huawei': (692, 1734)}),
                'tap_bx': action('点击宝箱', 'tap',
                                 **{'mix2s': (945, 1848), 'redmi': (629, 1373), 'huawei': (946, 1462)}),
                'tap_bx_sp': action('点击看视频金币翻倍', 'tap',
                                    **{'mix2s': (573, 1394), 'redmi': (339, 1029), 'huawei': (543, 1239)}),
                'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                'close_sp': action('关闭广告视频', 'tap',
                                   **{'mix2s': (918, 186),
                                      'redmi': (602, 133),
                                      'huawei': (903, 192)}),
                'swipe_sp': action('上划视频', 'swipe',
                                   **{'mix2s': (500, 1444, 500, 717),
                                      'redmi': (300, 1033, 300, 717),
                                      'huawei': (558, 1444, 616, 717)}),
            }
        },
        'shuabao': {
            'name': '刷宝',
            'pkg': 'com.jm.video',
            'action': {
                'swipe_sp': {'desc': '上划视频', 'xy': (500, 933, 500, 517), 'type': 'swipe'},
                'tap_task': action('点击任务', 'tap',
                                   **{'mix2s': (768, 2094),
                                      'redmi': (505, 1566),
                                      'huawei': (762, 1740)}),
                'tap_close_pop': action('关闭任务页弹窗', 'tap',
                                        **{'mix2s': (833, 566),
                                           'redmi': (567, 430),
                                           'huawei': (869, 369)}),
                'tap_sign': action('立即签到', 'tap',
                                   **{'mix2s': (887, 524),
                                      'redmi': (600, 362),
                                      'huawei': (910, 559)}),
                'tap_sign_sp': action('看视频签到', 'tap',
                                      **{'mix2s': (728, 1474),
                                         'redmi': (507, 1058),
                                         'huawei': (777, 1276)}),
                'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                'tap_close_sp': action('关闭视频', 'tap',
                                       **{'mix2s': (945, 107),
                                          'redmi': (658, 123),
                                          'huawei': (985, 116)}),
            }
        },
        'fish': {
            'name': '咸鱼游戏',
            'pkg': '',
            'action': {
                'tap_news': {'desc': '点击新闻', 'xy': (523, 344), 'type': 'tap'},
                'tap_back': {'desc': '左上角回退', 'xy': (93, 133), 'type': 'tap'},
                'tap_jiangli': {'desc': '点击领取奖励/换个笑话', 'xy': (560, 1742), 'type': 'tap'},
                'tap_confirm_jiangli': {'desc': '点击确认奖励', 'xy': (550, 1048), 'type': 'tap'},
            }
        },
        'weishi': {
            'name': '微视',
            'pkg': 'com.tencent.weishi',
            'action': {
                'swipe_sp': {'desc': '上划视频', 'xy': (300, 1444, 500, 717), 'type': 'swipe'},
            }
        },
        'qutt': {
            'name': '趣头条',
            'pkg': 'com.jifen.qukan',
            'action': {
                'tap_tt': action('点击头条', 'tap',
                                 **{'mix2s': (102, 2083), 'redmi': (80, 1572), 'huawei': (128, 1745)}),
                'tap_bx': action('点击时段奖励', 'tap',
                                 **{'mix2s': (983, 138), 'redmi': (641, 103), 'huawei': (996, 1470)}),
                'tap_task': action('点击任务', 'tap',
                                   **{'mix2s': (751, 2085), 'redmi': (500, 1567), 'huawei': (771, 1725)}),
                'tap_sign': action('视频签到', 'tap',
                                   **{'mix2s': (524, 994), 'redmi': (0, 0), 'huawei': (0, 0)}),
                'tap_sign_close': action('关闭签到视频', 'tap',
                                         **{'mix2s': (104, 68), 'redmi': (0, 0), 'huawei': (0, 0)}),
                'tap_tree': action('打开摇钱树', 'tap',
                                   **{'mix2s': (902, 1347), 'redmi': (0, 0), 'huawei': (0, 0)}),
                'tap_tree_gold': action('摇钱树领金币', 'tap',
                                        **{'mix2s': (569, 1663), 'redmi': (0, 0), 'huawei': (0, 0)}),
                'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                'tap_xsp': action('点击小视频', 'tap',
                                  **{'mix2s': (544, 2098), 'redmi': (367, 1539), 'huawei': (555, 1728)}),
                'swipe_sp': {'desc': '上划视频', 'xy': (500, 933, 500, 517), 'type': 'swipe'},
                'tap_xsp_egg': action('点击金蛋', 'tap',
                                      **{'mix2s': (988, 999), 'redmi': (665, 375), 'huawei': (0, 0)}),
            }
        },
        'tomato': {
            'name': '番茄小说',
            'pkg': 'com.dragon.read',
            'action': {
                'tap_fuli': action('点击福利', 'tap',
                                   **{'mix2s': (538, 2077),
                                      'redmi': (362, 1578),
                                      'huawei': (556, 1723)}),
                'tap_bx': action('点击宝箱', 'tap',
                                 **{'mix2s': (935, 1805),
                                    'redmi': (620, 1355),
                                    'huawei': (945, 1430)}),
                'tap_bx_sp': action('点击宝箱领取金币看视频', 'tap',
                                    **{'mix2s': (540, 1320),
                                       'redmi': (371, 840),
                                       'huawei': (567, 1122)}),
                'wait_sp': {'desc': '等待广告视频', 'interval': 35, 'type': 'sleep'},
                'tap_close_sp': action('关闭广告视频', 'tap',
                                       **{'mix2s': (973, 108),
                                          'redmi': (650, 134),
                                          'huawei': (981, 114)}),
                'tap_sj': action('点击书架', 'tap',
                                 **{'mix2s': (759, 2093),
                                    'redmi': (510, 1551),
                                    'huawei': (761, 1721)}),
                'tap_book': action('点击书籍', 'tap',
                                   **{'mix2s': (233, 548),
                                      'redmi': (157, 441),
                                      'huawei': (218, 669)}),
                'tap_page': action('点击翻页', 'tap',
                                   **{'mix2s': (878, 196),
                                      'redmi': (669, 166),
                                      'huawei': (1065, 160)}),
                'tap_ten_sp': action('看视频海量金币', 'tap',
                                     **{'mix2s': (810, 1836), 'redmi': (), 'huawei': ()}),
            }
        },
    }


