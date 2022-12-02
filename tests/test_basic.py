from __future__ import annotations

import aiohttp
import pytest
from pixiv_metadata.__main__ import (
    get_pid,
    get_metadata,
    get_extra_tags,
    extract_tags,
    gen_note,
)


@pytest.fixture
async def session():
    async with aiohttp.ClientSession() as ret:
        yield ret


@pytest.fixture(scope="module")
def metadata():
    return {
        "illustId": "103287719",
        "illustTitle": "2022年12月 シカテマ新刊(R18)サンプル",
        "illustComment": "2022年12月末に通販で頒布予定のシカテマ新刊(R18)サンプルです。<br /><br />「湯けむりと兵糧丸」でお互いに勘違いしたまま旅館に入ってしまったシカテマが雰囲気に流されちゃうR18本。<br /><br />「ゆけむりオーバーラン/B5/24P/400円/R18」<br /><br />どうぞよろしくお願いいたします！",
        "id": "103287719",
        "title": "2022年12月 シカテマ新刊(R18)サンプル",
        "description": "2022年12月末に通販で頒布予定のシカテマ新刊(R18)サンプルです。<br /><br />「湯けむりと兵糧丸」でお互いに勘違いしたまま旅館に入ってしまったシカテマが雰囲気に流されちゃうR18本。<br /><br />「ゆけむりオーバーラン/B5/24P/400円/R18」<br /><br />どうぞよろしくお願いいたします！",
        "illustType": 1,
        "createDate": "2022-12-02T15:48:29+00:00",
        "uploadDate": "2022-12-02T15:48:29+00:00",
        "restrict": 0,
        "xRestrict": 1,
        "sl": 6,
        "urls": {
            "mini": "https://i.pximg.net/c/48x48/img-master/img/2022/12/03/00/48/29/103287719_p0_square1200.jpg",
            "thumb": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/29/103287719_p0_square1200.jpg",
            "small": "https://i.pximg.net/c/540x540_70/img-master/img/2022/12/03/00/48/29/103287719_p0_master1200.jpg",
            "regular": "https://i.pximg.net/img-master/img/2022/12/03/00/48/29/103287719_p0_master1200.jpg",
            "original": "https://i.pximg.net/img-original/img/2022/12/03/00/48/29/103287719_p0.jpg",
        },
        "tags": {
            "authorId": "10002432",
            "isLocked": False,
            "tags": [
                {
                    "tag": "R-18",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "userName": "モリトー",
                },
                {
                    "tag": "漫画",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "translation": {"en": "manga"},
                    "userName": "モリトー",
                },
                {
                    "tag": "テマリ",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "translation": {"en": "temari"},
                    "userName": "モリトー",
                },
                {
                    "tag": "シカテマ",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "translation": {"en": "Shikamaru/Temari"},
                    "userName": "モリトー",
                },
                {
                    "tag": "シカマル",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "translation": {"en": "shikamaru"},
                    "userName": "モリトー",
                },
                {
                    "tag": "奈良シカマル",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "translation": {"en": "奈良鹿丸"},
                    "userName": "モリトー",
                },
                {
                    "tag": "NARUTO",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "userName": "モリトー",
                },
                {
                    "tag": "R18",
                    "locked": True,
                    "deletable": False,
                    "userId": "10002432",
                    "userName": "モリトー",
                },
            ],
            "writable": False,
        },
        "alt": "モリトー的漫画",
        "storableTags": [
            "0xsDLqCEW6",
            "_hSAdpN9rx",
            "EewdJ7G0yf",
            "SxXLk6BxWY",
            "hvlhgsqCKv",
            "bpJ4_WW86s",
            "4LfBhWYcxv",
            "6n5sWl9nNm",
        ],
        "userId": "10002432",
        "userName": "モリトー",
        "userAccount": "noahnoah8972",
        "userIllusts": {
            "103287719": {
                "id": "103287719",
                "title": "2022年12月 シカテマ新刊(R18)サンプル",
                "illustType": 1,
                "xRestrict": 1,
                "restrict": 0,
                "sl": 6,
                "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/29/103287719_p0_square1200.jpg",
                "description": "2022年12月末に通販で頒布予定のシカテマ新刊(R18)サンプルです。<br /><br />「湯けむりと兵糧丸」でお互いに勘違いしたまま旅館に入ってしまったシカテマが雰囲気に流されちゃうR18本。<br /><br />「ゆけむりオーバーラン/B5/24P/400円/R18」<br /><br />どうぞよろしくお願いいたします！",
                "tags": [
                    "R-18",
                    "漫画",
                    "テマリ",
                    "シカテマ",
                    "シカマル",
                    "奈良シカマル",
                    "NARUTO",
                    "R18",
                ],
                "userId": "10002432",
                "userName": "モリトー",
                "width": 2154,
                "height": 3259,
                "pageCount": 8,
                "isBookmarkable": True,
                "bookmarkData": "None",
                "alt": "モリトー的漫画",
                "titleCaptionTranslation": {"workTitle": "None", "workCaption": "None"},
                "createDate": "2022-12-03T00:48:29+09:00",
                "updateDate": "2022-12-03T00:48:29+09:00",
                "isUnlisted": False,
                "isMasked": False,
                "aiType": 1,
            }
        },
        "likeData": False,
        "width": 2154,
        "height": 3259,
        "pageCount": 8,
        "bookmarkCount": 9,
        "likeCount": 6,
        "commentCount": 0,
        "responseCount": 0,
        "viewCount": 157,
        "bookStyle": "0",
        "isHowto": False,
        "isOriginal": False,
        "imageResponseOutData": [],
        "imageResponseData": [],
        "imageResponseCount": 0,
        "pollData": "None",
        "seriesNavData": "None",
        "descriptionBoothId": "None",
        "descriptionYoutubeId": "None",
        "comicPromotion": "None",
        "fanboxPromotion": "None",
        "contestBanners": [],
        "isBookmarkable": True,
        "bookmarkData": "None",
        "contestData": "None",
        "zoneConfig": {
            "responsive": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=illust_responsive_side&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55dpf5svzr&num=638a21ed133"
            },
            "rectangle": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=illust_rectangle&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55hqdfw0f4&num=638a21ed374"
            },
            "500x500": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=bigbanner&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55kaem69sz&num=638a21ed229"
            },
            "header": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=header&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55moge86of&num=638a21ed668"
            },
            "footer": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=footer&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55pdde2cq6&num=638a21ed745"
            },
            "expandedFooter": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=multiple_illust_viewer&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55rwyl3exa&num=638a21ed387"
            },
            "logo": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=logo_side&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55ua7qrqpd&num=638a21ed872"
            },
            "relatedworks": {
                "url": "https://pixon.ads-pixiv.net/show?zone_id=relatedworks&format=js&s=0&up=0&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&ref=www.pixiv.net%2F&is_spa=1&ab_test_digits_first=49&uab=&yuid=NQhidIY&suid=Ph8pwvl55wlukrwb8&num=638a21ed977"
            },
        },
        "extraData": {
            "meta": {
                "title": "#テマリ 2022年12月 シカテマ新刊(R18)サンプル - モリトー的漫画 - pixiv",
                "description": "この作品 「2022年12月 シカテマ新刊(R18)サンプル」 は 「R-18」「漫画」 等のタグがつけられた「モリトー」さんの漫画です。 「2022年12月末に通販で頒布予定のシカテマ新刊(R18)サンプルです。「湯けむりと兵糧丸」でお互いに勘違いしたまま旅館に入ってしまった…",
                "canonical": "https://www.pixiv.net/artworks/103287719",
                "alternateLanguages": [],
                "descriptionHeader": "本作「2022年12月 シカテマ新刊(R18)サンプル」为附有「R-18」「漫画」等标签的漫画。",
                "ogp": {
                    "description": "2022年12月末に通販で頒布予定のシカテマ新刊(R18)サンプルです。「湯けむりと兵糧丸」でお互いに勘違いしたまま旅館に入ってしまったシカテマが雰囲気に流されちゃうR18本。「ゆけむりオーバーラン/",
                    "image": "https://s.pximg.net/www/images/pixiv_logo.png",
                    "title": "#テマリ 2022年12月 シカテマ新刊(R18)サンプル - モリトー的漫画 - pixiv",
                    "type": "article",
                },
                "twitter": {
                    "description": "2022年12月末に通販で頒布予定のシカテマ新刊(R18)サンプルです。\n\n「湯けむりと兵糧丸」でお互いに勘違いしたまま旅館に入ってしまったシカテマが雰囲気に流されちゃうR18本。\n\n「ゆけむりオーバーラン/B5/24P/400円/R18」\n\nどうぞよろしくお願いいたします！",
                    "image": "https://s.pximg.net/www/images/pixiv_logo.png",
                    "title": "[R-18]2022年12月 シカテマ新刊(R18)サンプル",
                    "card": "summary",
                },
            }
        },
        "titleCaptionTranslation": {"workTitle": "None", "workCaption": "None"},
        "isUnlisted": False,
        "request": "None",
        "commentOff": 0,
        "aiType": 1,
        "noLoginData": {
            "breadcrumbs": {
                "successor": [],
                "current": {"zh": "2022年12月 シカテマ新刊(R18)サンプル"},
            },
            "zengoIdWorks": [
                {
                    "id": "103287737",
                    "title": "久岐忍",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/49/06/103287737_p0_square1200.jpg",
                    "description": "",
                    "tags": [
                        "GenshinImpact",
                        "Genshin_Impact",
                        "原神",
                        "久岐忍",
                        "Kuki_Shinobu",
                    ],
                    "userId": "31183597",
                    "userName": "A_Leg_",
                    "width": 1352,
                    "height": 1968,
                    "pageCount": 2,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#GenshinImpact 久岐忍 - A_Leg_的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:49:06+09:00",
                    "updateDate": "2022-12-03T00:49:06+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/11/09/12/13/22/23578725_ec24f3cab4bf8c51aa34a2df76d01973_50.jpg",
                },
                {
                    "id": "103287736",
                    "title": "まだ食べてないのにイタタ",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/49/05/103287736_p0_square1200.jpg",
                    "description": "",
                    "tags": ["テイルス", "ソニック"],
                    "userId": "13324",
                    "userName": "ちゃな",
                    "width": 1150,
                    "height": 3150,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#テイルス まだ食べてないのにイタタ - ちゃな的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:49:05+09:00",
                    "updateDate": "2022-12-03T00:49:05+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2010/09/08/11/42/18/2175035_8cd68dcaa9621ce2bbcb2d7faf8b5744_50.jpg",
                },
                {
                    "id": "103287735",
                    "title": "ぎゆしの\u3000ツイログ",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/56/103287735_p0_square1200.jpg",
                    "description": "",
                    "tags": ["ぎゆしの", "イラスト"],
                    "userId": "77714445",
                    "userName": "竹ブ",
                    "width": 537,
                    "height": 537,
                    "pageCount": 56,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#ぎゆしの ぎゆしの\u3000ツイログ - 竹ブ的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:56+09:00",
                    "updateDate": "2022-12-03T00:48:56+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/09/14/21/57/07/23332783_b444a10b81a44a823375dd204f395b86_50.jpg",
                },
                {
                    "id": "103287728",
                    "title": "ルヒアンゆずアヒルパーカー",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/39/103287728_p0_square1200.jpg",
                    "description": "",
                    "tags": ["オリキャラ", "ショタ", "パーカー"],
                    "userId": "8860711",
                    "userName": "🍯❄",
                    "width": 600,
                    "height": 450,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#オリキャラ ルヒアンゆずアヒルパーカー - 🍯❄的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:39+09:00",
                    "updateDate": "2022-12-03T00:48:39+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/05/26/22/20/24/22782147_101be21f5d6bcf44b4bb9b51f2116b32_50.jpg",
                },
                {
                    "id": "103287727",
                    "title": "AI Art #15",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/39/103287727_p0_square1200.jpg",
                    "description": "",
                    "tags": ["StableDiffusion", "AIイラスト", "AI"],
                    "userId": "88619035",
                    "userName": "zer0",
                    "width": 512,
                    "height": 512,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#StableDiffusion AI Art #15 - zer0的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:39+09:00",
                    "updateDate": "2022-12-03T00:48:39+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 2,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/12/01/01/58/23/23681821_f2456b849fb2441d370a335707b2cbc3_50.jpg",
                },
                {
                    "id": "103287723",
                    "title": "ペルソナ5",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/35/103287723_p0_square1200.jpg",
                    "description": "",
                    "tags": ["ペルソナ5", "雨宮蓮", "fanart"],
                    "userId": "64693958",
                    "userName": "风筝笑",
                    "width": 826,
                    "height": 1023,
                    "pageCount": 2,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#ペルソナ5 ペルソナ5 - 风筝笑的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:35+09:00",
                    "updateDate": "2022-12-03T00:48:35+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 0,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/09/08/07/19/59/23303914_5fbc281701791352426077af72eff83a_50.jpg",
                },
                {
                    "id": "103287722",
                    "title": "Three sisters",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/34/103287722_p0_square1200.jpg",
                    "description": "",
                    "tags": ["NovelAI", "血", "流血注意"],
                    "userId": "28201510",
                    "userName": "Oracle",
                    "width": 512,
                    "height": 1024,
                    "pageCount": 3,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#NovelAI Three sisters - Oracle的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:34+09:00",
                    "updateDate": "2022-12-03T00:48:34+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 2,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/12/02/14/44/04/23687528_7441ff8a7ecac4f68ce7c97c22c03950_50.png",
                },
                {
                    "id": "103287721",
                    "title": "同棲してるレイエマ",
                    "illustType": 1,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/custom-thumb/img/2022/12/03/00/48/32/103287721_p0_custom1200.jpg",
                    "description": "",
                    "tags": ["漫画", "レイエマ"],
                    "userId": "88060587",
                    "userName": "はり",
                    "width": 874,
                    "height": 1240,
                    "pageCount": 4,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#レイエマ 同棲してるレイエマ - はり的漫画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:32+09:00",
                    "updateDate": "2022-12-03T00:48:32+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/11/14/14/08/22/23602666_6e57784641bcc503eace5840732367f0_50.png",
                },
                {
                    "id": "103287716",
                    "title": "雷大炮",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/25/103287716_p0_square1200.jpg",
                    "description": "",
                    "tags": ["原神", "二创", "散兵"],
                    "userId": "76382246",
                    "userName": "杏仁豆腐羹",
                    "width": 271,
                    "height": 359,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#原神 雷大炮 - 杏仁豆腐羹的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:25+09:00",
                    "updateDate": "2022-12-03T00:48:25+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 0,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/12/03/00/42/19/23689574_24affbcdcf34b5f1e5ed62453908f3be_50.jpg",
                },
                {
                    "id": "103287713",
                    "title": "Fruit Picking",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/07/103287713_p0_square1200.jpg",
                    "description": "",
                    "tags": [
                        "nosferatu16",
                        "ssbbw",
                        "naïa",
                        "Konan",
                        "ケモノ",
                        "デブケモ",
                        "肉塊",
                        "猫",
                        "部族",
                        "筋肉",
                    ],
                    "userId": "4889790",
                    "userName": "nosferatu16",
                    "width": 984,
                    "height": 812,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#nosferatu16 Fruit Picking - nosferatu16的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:07+09:00",
                    "updateDate": "2022-12-03T00:48:07+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2021/10/14/02/45/43/21576567_18eff0f1bd6bcfb36d7b03050ad8a58f_50.png",
                },
                {
                    "id": "103287710",
                    "title": "青髪",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/05/103287710_p0_square1200.jpg",
                    "description": "",
                    "tags": ["オリジナル男子", "アルコールマーカー", "アナログイラスト", "オリジナ"],
                    "userId": "66440133",
                    "userName": "あまぞら",
                    "width": 767,
                    "height": 1024,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#オリジナル男子 青髪 - あまぞら的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:05+09:00",
                    "updateDate": "2022-12-03T00:48:05+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://s.pximg.net/common/images/no_profile_s.png",
                },
                {
                    "id": "103287704",
                    "title": "無題",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/02/103287704_p0_square1200.jpg",
                    "description": "",
                    "tags": ["オリジナル"],
                    "userId": "28350084",
                    "userName": "WarmGray",
                    "width": 3000,
                    "height": 3600,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#オリジナル 無題 - WarmGray的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:02+09:00",
                    "updateDate": "2022-12-03T00:48:02+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/12/03/00/31/48/23689534_ff73fdec94466911e541e3ca3f49e3db_50.jpg",
                },
                {
                    "id": "103287702",
                    "title": "ゴジータブルー",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/48/01/103287702_p0_square1200.jpg",
                    "description": "",
                    "tags": ["超サイヤ人SS", "ゴジータ", "ドラゴンボール"],
                    "userId": "61445737",
                    "userName": "Taiga",
                    "width": 2894,
                    "height": 4093,
                    "pageCount": 2,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#超サイヤ人SS ゴジータブルー - Taiga的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:48:01+09:00",
                    "updateDate": "2022-12-03T00:48:01+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/04/03/05/36/31/22488859_fe589439e866d2559056797d4573b622_50.jpg",
                },
                {
                    "id": "103287699",
                    "title": "キャラデザ",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/47/54/103287699_p0_square1200.jpg",
                    "description": "",
                    "tags": ["オリジナル"],
                    "userId": "170506",
                    "userName": "チワワウドン",
                    "width": 2540,
                    "height": 3560,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#オリジナル キャラデザ - チワワウドン的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:47:54+09:00",
                    "updateDate": "2022-12-03T00:47:54+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 1,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2019/01/10/02/41/22/15239165_3ae507b4ade6aea204cbd0bf15ecb201_50.jpg",
                },
                {
                    "id": "103287698",
                    "title": "ふわふわきらきらのおんなのこ",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/47/54/103287698_p0_square1200.jpg",
                    "description": "",
                    "tags": ["オリジナル", "nijijourney", "女の子", "百合"],
                    "userId": "88269378",
                    "userName": "ねむ/NovelAI",
                    "width": 450,
                    "height": 676,
                    "pageCount": 63,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#オリジナル ふわふわきらきらのおんなのこ - ねむ/NovelAI的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:47:54+09:00",
                    "updateDate": "2022-12-03T00:47:54+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 2,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/11/25/16/18/12/23656063_2000491510033ad7a320078823f048db_50.png",
                },
                {
                    "id": "103287695",
                    "title": "AI Art #14",
                    "illustType": 0,
                    "xRestrict": 0,
                    "restrict": 0,
                    "sl": 2,
                    "url": "https://i.pximg.net/c/250x250_80_a2/img-master/img/2022/12/03/00/47/50/103287695_p0_square1200.jpg",
                    "description": "",
                    "tags": ["StableDiffusion", "AIイラスト", "AI"],
                    "userId": "88619035",
                    "userName": "zer0",
                    "width": 512,
                    "height": 512,
                    "pageCount": 1,
                    "isBookmarkable": True,
                    "bookmarkData": "None",
                    "alt": "#StableDiffusion AI Art #14 - zer0的插画",
                    "titleCaptionTranslation": {
                        "workTitle": "None",
                        "workCaption": "None",
                    },
                    "createDate": "2022-12-03T00:47:50+09:00",
                    "updateDate": "2022-12-03T00:47:50+09:00",
                    "isUnlisted": False,
                    "isMasked": False,
                    "aiType": 2,
                    "profileImageUrl": "https://i.pximg.net/user-profile/img/2022/12/01/01/58/23/23681821_f2456b849fb2441d370a335707b2cbc3_50.jpg",
                },
            ],
            "zengoWorkData": {
                "nextWork": {"id": "103287721", "title": "同棲してるレイエマ"},
                "prevWork": {"id": "103287718", "title": "round 6  Rachel vs liu"},
            },
        },
    }


async def test_get_metadata(session):
    res = await get_metadata(session, "103287719")
    assert res["id"] == "103287719"
    assert "tags" in res


async def test_get_metadata_error(session):
    with pytest.raises(Exception, match="Download Metadata Error"):
        await get_metadata(session, "123123213")


def test_extract_tags(metadata):
    tags = extract_tags(metadata)
    assert "manga" in tags
    assert "R-18" in tags


def test_extra_tags_artist(metadata):
    extra = get_extra_tags(metadata)
    assert "Artist:10002432" in extra


@pytest.mark.parametrize(
    "bookmark,expected",
    [
        (12000, "BookmarkCount:10000+"),
        (9000, "BookmarkCount:5000+"),
        (4000, "BookmarkCount:1000+"),
    ],
)
def test_extra_tags_bookmark(metadata, bookmark, expected):
    metadata["bookmarkCount"] = bookmark
    tags = get_extra_tags(metadata)
    assert expected in tags


@pytest.mark.parametrize(
    "name,expected",
    [
        ("AGirl93596051.png", "93596051"),
        ("AGirl93596051_p1.png", "93596051"),
        ("2020_78621230.jpg", "78621230"),
        ("2020_78621230_p0.jpg", "78621230"),
        ("A20123_1234.jpg", "1234"),
        ("A20123_1234_p1.jpg", "1234"),
        ("sad123_p3.jpg", "123"),
        ("2_1_p0.jpg", "1"),
    ],
)
def test_get_pid(name, expected):
    res = get_pid(name)
    assert res == expected