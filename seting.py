
class Config(object):
    cache_path = 'data.pk'
    devices = {
        'mix2s': {
            'cache_path': 'mix2s_data.pk',
            'id': '192.168.1.17:5555',
            'app': {
                'toutiao': {
                    'name': '今日头条',
                    'pkg': 'com.ss.android.article.lite/com.ss.android.article.lite.activity.SplashActivity',
                    'action': {
                        'tap_bx': {'desc': '点击宝箱', 'xy': (943, 1888), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (545, 1409), 'type': 'tap'},
                        'tap_task': {'desc': '点击任务', 'xy': (774, 2094), 'type': 'tap'},
                        'tap_sign_in': {'desc': '点击签到', 'xy': (774, 2094), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 30, 'type': 'sleep'},
                        'close_sp': {'desc': '关闭广告视频', 'xy': (971, 85), 'type': 'tap'}
                    }
                },
                'kuaishou': {
                    'name': '快手',
                    'pkg': 'com.kuaishou.nebula/com.yxcorp.gifshow.webview.KwaiWebViewActivity',
                    'action': {
                        'tap_menu': {'desc': '点击首页菜单', 'xy': (40, 158), 'type': 'tap'},
                        'tap_menu_money': {'desc': '点击菜单去赚钱', 'xy': (495, 920), 'type': 'tap'},
                        'tap_fuli': {'desc': '点击福利', 'xy': (937, 1400), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 22, 'type': 'sleep'},
                        'tap_close_sp': {'desc': '关闭广告视频', 'xy': (909, 92), 'type': 'tap'},
                        'swipe_sp': {'desc': '上划视频', 'xy': (558, 1444, 616, 717), 'type': 'swipe'},
                    }
                },
                'douyin': {
                    'name': '抖音',
                    'pkg': 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
                    'action': {
                        'tap_gold': {'desc': '点击首页金币', 'xy': (561, 2084), 'type': 'tap'},
                        'tap_bx': {'desc': '点击宝箱', 'xy': (915, 2000), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (550, 1278), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                        'close_sp': {'desc': '关闭广告视频', 'xy': (945, 107), 'type': 'tap'},
                        'tap_xs_sp': {'desc': '点击限时任务视频', 'xy': (874, 1201), 'type': 'tap'},
                        'swipe_sp': {'desc': '上划视频', 'xy': (300, 1444, 500, 717), 'type': 'swipe'},
                    }
                },
                'shuabao': {
                    'name': '刷宝',
                    'pkg': 'com.jm.video/com.jm.video.ui.main.MainActivity',
                    'action': {
                        'swipe_sp': {'desc': '上划视频', 'xy': (300, 1444, 500, 717), 'type': 'swipe'},
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
                'tomato': {
                    'name': '番茄小说',
                    'pkg': 'com.dragon.read',
                    'action': {
                        'tap_fuli': {'desc': '点击福利', 'xy': (538, 2077), 'type': 'tap'},
                        'tap_bx': {'desc': '点击宝箱', 'xy': (935, 1805), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (551, 1135), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 35, 'type': 'sleep'},
                        'tap_close_sp': {'desc': '关闭广告视频', 'xy': (973, 108), 'type': 'tap'},
                        'tap_sj': {'desc': '点击书架', 'xy': (761, 2099), 'type': 'tap'},
                        'tap_book': {'desc': '点击书籍', 'xy': (233, 648), 'type': 'tap'},
                        'tap_page': {'desc': '点击翻页', 'xy': (878, 196), 'type': 'tap'},
                    }
                },
            }
        },
        'redmi': {
            'cache_path': 'redmi_data.pk',
            'id': '192.168.1.26:5554',
            'app': {
                'toutiao': {
                    'name': '今日头条',
                    'pkg': 'com.ss.android.article.lite/com.ss.android.article.lite.activity.SplashActivity',
                    'action': {
                        'tap_bx': {'desc': '点击宝箱', 'xy': (605, 1425), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (356, 1018), 'type': 'tap'},
                        'tap_task': {'desc': '点击任务', 'xy': (501, 1584), 'type': 'tap'},
                        'tap_sign_in': {'desc': '点击签到', 'xy': (774, 2094), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 30, 'type': 'sleep'},
                        'close_sp': {'desc': '关闭广告视频', 'xy': (655, 66), 'type': 'tap'}
                    }
                },
                'douyin': {
                    'name': '抖音',
                    'pkg': 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
                    'action': {
                        'tap_gold': {'desc': '点击首页金币', 'xy': (371, 1561), 'type': 'tap'},
                        'tap_bx': {'desc': '点击宝箱', 'xy': (607, 1485), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (372, 923), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                        'close_sp': {'desc': '关闭广告视频', 'xy': (620, 144), 'type': 'tap'},
                        # 'tap_xs_sp': {'desc': '点击限时任务视频', 'xy': (613, 888), 'type': 'tap'},
                        'tap_xs_sp': {'desc': '点击限时任务视频', 'xy': (613, 1084), 'type': 'tap'},
                        'swipe_sp': {'desc': '上划视频', 'xy': (300, 1444, 500, 717), 'type': 'swipe'},
                    }
                },
                'kuaishou': {
                    'name': '快手',
                    'pkg': 'com.kuaishou.nebula/com.yxcorp.gifshow.webview.KwaiWebViewActivity',
                    'action': {
                        'tap_menu': {'desc': '点击首页菜单', 'xy': (62, 129), 'type': 'tap'},
                        'tap_menu_money': {'desc': '点击菜单去赚钱', 'xy': (314, 668), 'type': 'tap'},
                        'tap_fuli': {'desc': '点击福利', 'xy': (622, 1092), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 17, 'type': 'sleep'},
                        'tap_close_sp': {'desc': '关闭广告视频', 'xy': (619, 119), 'type': 'tap'},
                        'swipe_sp': {'desc': '上划视频', 'xy': (300, 1444, 500, 717), 'type': 'swipe'},
                    }
                },
                'shuabao': {
                    'name': '刷宝',
                    'pkg': 'com.jm.video/com.jm.video.ui.main.MainActivity',
                    'action': {
                        'swipe_sp': {'desc': '上划视频', 'xy': (300, 1444, 500, 717), 'type': 'swipe'},
                    }
                },
                'tomato': {
                    'name': '番茄小说',
                    'pkg': 'com.dragon.read',
                    'action': {
                        'tap_fuli': {'desc': '点击福利', 'xy': (362, 1578), 'type': 'tap'},
                        'tap_bx': {'desc': '点击宝箱', 'xy': (620, 1355), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (371, 840), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                        'tap_close_sp': {'desc': '关闭广告视频', 'xy': (650, 134), 'type': 'tap'},
                        'tap_sj': {'desc': '点击书架', 'xy': (510, 1551), 'type': 'tap'},
                        'tap_book': {'desc': '点击书籍', 'xy': (157, 441), 'type': 'tap'},
                        'tap_page': {'desc': '点击翻页', 'xy': (669, 166), 'type': 'tap'},

                    }
                },
            }
        },
        'huawei': {
            'cache_path': 'huawei_data.pk',
            'id': 'BTFDU17318000996',
            'app': {
                'toutiao': {
                    'name': '今日头条',
                    'pkg': 'com.ss.android.article.lite/com.ss.android.article.lite.activity.SplashActivity',
                    'action': {
                        # 'tap_sign_in': {'desc': '点击签到', 'xy': (774, 2094), 'type': 'tap'},
                        'tap_task': {'desc': '点击任务', 'xy': (780, 1780), 'type': 'tap'},
                        'tap_bx': {'desc': '点击宝箱', 'xy': (916, 1542), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (551, 1236), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 30, 'type': 'sleep'},
                        'close_sp': {'desc': '关闭广告视频', 'xy': (961, 97), 'type': 'tap'}
                    }
                },
                'kuaishou': {
                    'name': '快手',
                    'pkg': 'com.kuaishou.nebula/com.yxcorp.gifshow.webview.KwaiWebViewActivity',
                    'action': {
                        'tap_menu': {'desc': '点击首页菜单', 'xy': (56, 138), 'type': 'tap'},
                        'tap_menu_money': {'desc': '点击菜单去赚钱', 'xy': (533, 999), 'type': 'tap'},
                        'tap_fuli': {'desc': '点击福利', 'xy': (991, 1417), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 17, 'type': 'sleep'},
                        'tap_close_sp': {'desc': '关闭广告视频', 'xy': (900, 96), 'type': 'tap'},
                        'swipe_sp': {'desc': '上划视频', 'xy': (558, 1444, 616, 717), 'type': 'swipe'},
                    }
                },
                'douyin': {
                    'name': '抖音',
                    'pkg': 'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity',
                    'action': {
                        'tap_gold': {'desc': '点击首页金币', 'xy': (550, 1700), 'type': 'tap'},
                        'tap_bx': {'desc': '点击宝箱', 'xy': (919, 1640), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (550, 1103), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 37, 'type': 'sleep'},
                        'close_sp': {'desc': '关闭广告视频', 'xy': (945, 107), 'type': 'tap'},
                        'tap_xs_sp': {'desc': '点击限时任务视频', 'xy': (884, 1187), 'type': 'tap'},
                        'swipe_sp': {'desc': '上划视频', 'xy': (558, 1444, 616, 717), 'type': 'swipe'},
                    }
                },
                'shuabao': {
                    'name': '刷宝',
                    'pkg': 'com.jm.video/com.jm.video.ui.main.MainActivity',
                    'action': {
                        'swipe_sp': {'desc': '上划视频', 'xy': (300, 1444, 500, 717), 'type': 'swipe'},
                    }
                },
                'fish': {
                    'name': '咸鱼游戏',
                    'pkg': '',
                    'action': {
                        # 'tap_news': {'desc': '点击新闻', 'xy': (523, 344), 'type': 'tap'},
                        # 'tap_back': {'desc': '左上角回退', 'xy': (93, 133), 'type': 'tap'},
                        # 'tap_jiangli': {'desc': '点击领取奖励/换个笑话', 'xy': (560, 1742), 'type': 'tap'},
                        # 'tap_confirm_jiangli': {'desc': '点击确认奖励', 'xy': (550, 1100), 'type': 'tap'}
                    }
                },
                'tomato': {
                    'name': '番茄小说',
                    'pkg': 'com.dragon.read',
                    'action': {
                        'tap_fuli': {'desc': '点击福利', 'xy': (556, 1723), 'type': 'tap'},
                        'tap_bx': {'desc': '点击宝箱', 'xy': (945, 1430), 'type': 'tap'},
                        'tap_bx_sp': {'desc': '点击宝箱领取金币看视频', 'xy': (548, 971), 'type': 'tap'},
                        'wait_sp': {'desc': '等待广告视频', 'interval': 38, 'type': 'sleep'},
                        'tap_close_sp': {'desc': '关闭广告视频', 'xy': (981, 114), 'type': 'tap'},
                        'tap_sj': {'desc': '点击书架', 'xy': (761, 1721), 'type': 'tap'},
                        'tap_book': {'desc': '点击书籍', 'xy': (218, 669), 'type': 'tap'},
                        'tap_page': {'desc': '点击翻页', 'xy': (878, 177), 'type': 'tap'},
                    }
                },
            }
        }
    }



