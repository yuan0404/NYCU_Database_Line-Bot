
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ImagemapSendMessage, QuickReply, QuickReplyButton, MessageAction, BaseSize, MessageImagemapAction, ImagemapArea, CarouselTemplate, CarouselColumn, MessageTemplateAction
)

import os
import json
import logging
import boto3
import sys
import pymysql
import numpy
import pandas

line_bot_api = LineBotApi(os.environ['Channel_access_token'])
handler = WebhookHandler(os.environ['Channel_secret'])

def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        mtext = event.message.text
        if mtext == '@找美食':
            try:
                image_url = 'https://i.imgur.com/oY4cf4t.jpg'
                imgwidth = 1040
                imgheight = 1040
                message = ImagemapSendMessage(
                    base_url=image_url,
                    alt_text="美食分類",
                    base_size=BaseSize(height=imgheight, width=imgwidth),
                    actions=[
                        MessageImagemapAction(
                            text='@伴手禮',
                            area=ImagemapArea(
                                x=0,
                                y=0,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@小吃',
                            area=ImagemapArea(
                                x=imgwidth*0.5,
                                y=0,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@飲料與甜點',
                            area=ImagemapArea(
                                x=0,
                                y=imgheight*0.5,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@餐廳',
                            area=ImagemapArea(
                                x=imgwidth*0.5,
                                y=imgheight*0.5,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                    ]
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        elif mtext == '@找住宿':
            try:
                image_url = 'https://i.imgur.com/Nn4rncm.jpg'
                imgwidth = 1040
                imgheight = 347
                message = ImagemapSendMessage(
                    base_url=image_url,
                    alt_text="飯店分類",
                    base_size=BaseSize(height=imgheight, width=imgwidth),
                    actions=[
                        MessageImagemapAction(
                            text='@飯店',
                            area=ImagemapArea(
                                x=0,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*1
                            )
                        ),
                        MessageImagemapAction(
                            text='@旅館',
                            area=ImagemapArea(
                                x=imgwidth*0.33,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*1
                            )
                        ),
                        MessageImagemapAction(
                            text='@民宿',
                            area=ImagemapArea(
                                x=imgwidth*0.66,
                                y=0,
                                width=imgwidth*0.34,
                                height=imgheight*1
                            )
                        ),
                    ]
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        elif mtext == '@找景點':
            try:
                image_url = 'https://i.imgur.com/BJnw4Do.jpg'
                imgwidth = 1040
                imgheight = 693
                message = ImagemapSendMessage(
                    base_url=image_url,
                    alt_text="景點分類",
                    base_size=BaseSize(height=imgheight, width=imgwidth),
                    actions=[
                        MessageImagemapAction(
                            text='@歷史建築',
                            area=ImagemapArea(
                                x=0,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@自然景觀',
                            area=ImagemapArea(
                                x=imgwidth*0.33,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@宗教文化',
                            area=ImagemapArea(
                                x=imgwidth*0.66,
                                y=0,
                                width=imgwidth*0.34,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@博物館',
                            area=ImagemapArea(
                                x=0,
                                y=imgheight*0.5,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@公園與休閒區',
                            area=ImagemapArea(
                                x=imgwidth*0.33,
                                y=imgheight*0.5,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@市區景點',
                            area=ImagemapArea(
                                x=imgwidth*0.66,
                                y=imgheight*0.5,
                                width=imgwidth*0.34,
                                height=imgheight*0.5
                            )
                        ),
                    ]
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@伴手禮/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@伴手禮/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@伴手禮/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@小吃':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@小吃/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@小吃/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@小吃/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@飲料與甜點':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@飲料與甜點/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@飲料與甜點/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@飲料與甜點/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@餐廳':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@餐廳/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@餐廳/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@餐廳/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@飯店':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@飯店/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@飯店/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@飯店/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@旅館':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@旅館/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@旅館/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@旅館/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@民宿':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@民宿/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@民宿/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@民宿/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@歷史建築':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@歷史建築/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@歷史建築/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@歷史建築/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@自然景觀':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@自然景觀/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@自然景觀/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@自然景觀/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@宗教文化':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@宗教文化/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@宗教文化/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@宗教文化/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@博物館':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@博物館/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@博物館/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@博物館/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@公園與休閒區':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@公園與休閒區/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@公園與休閒區/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@公園與休閒區/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@市區景點':
            try:
                message = TextSendMessage(
                    text='請選擇地區',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="東區", text="@市區景點/東區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="北區", text="@市區景點/北區")
                            ),
                            QuickReplyButton(
                                action=MessageAction(label="香山區", text="@市區景點/香山區")
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@伴手禮/東區': 
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹利利號',
                                text='(03)5227365\n新竹市東區中正路96巷6號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/東區/新竹利利號/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/東區/新竹利利號/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='福源花生醬',
                                text='(03)5328118\n新竹市東區東大路一段155號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/東區/福源花生醬/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/東區/福源花生醬/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )    
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@伴手禮/東區/新竹利利號/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '原味肉鬆、芝麻肉鬆、厚薄片肉乾'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/東區/新竹利利號/介紹':
            try:
                message = TextSendMessage(
                    text = '出了巷口就是中正路，周邊大型連鎖餐飲美食店林立，蝸居「巷仔內」的利利號，門面不大，卻能屹立一甲子，獨到的美味，是市長林智堅的口袋美食之一，不少新竹人也已經吃了三代。「我現在有空還會自己走路去買兒子喜歡吃的肉鬆」林智堅說，這家老字號的肉品，都好吃。窄窄的門面，毫不起眼，進入店裡才發現縱深長，屋子前方是門市，擺滿各式肉乾、肉鬆、香腸、臘肉與火腿，香氣撲鼻；利利號目前由葉日棟、葉日傳兄弟經營，日棟負責業務行銷，日傳專注產品開發與品管，「我們71年從學徒做起」葉日傳回憶說，每天清晨4、5點就得到市場選購溫體豬肉，回家開始備料、搥肉、炒製各式肉品、調味、烘乾，每道步驟都遵循傳統，一點不馬虎。門市後方就是工廠，一座30多年歷史的傳統大灶上，擺著三口大鍋，所有肉鬆製品都在大鍋裡炒製，利利號肉品口味數十年不變，兄弟倆接手姨丈的店，堅持傳統做工，像肉鬆、肉脯是用龍眼木搥製，依肉品軟硬度一槌、一槌把纖維敲鬆，保持肉質彈性與肉汁的鮮味；肉乾分厚、薄兩種口感，也是人工一片片擺上烤架烘烤；煙燻臘肉、香腸則選用台灣杉含量較高的木屑粉，炭火燻製，產品多了道獨特燻香味，傳統做工不若機器快速，成本也高，兄弟倆認為，能換來顧客數十年來的信賴，一切都值了。因應國人健康與養生風尚，利利號的肉製品逐步朝少鹽、少糖、口味清淡化的方向走。利利號的核心技術，也吸引多家知名品牌大廠委託代工，兄弟倆商議後，不願讓機器取代手作的細緻與口感，僅提供熟客及優質廠商服務，「讓客人吃得健康美味，是利利號永遠不變的信念。」他們這麼堅持著。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/東區/福源花生醬/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '花生醬（顆粒、滑順）、花生（角）塘、黑芝麻醬、白芝麻醬、花生醬夾心蔬菜餅'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/東區/福源花生醬/介紹':
            try:
                message = TextSendMessage(
                    text = '「福源花生醬」是台灣知名度最高的花生醬品牌，設立60年，純手工製造，不加一滴水，也無防腐劑，口感綿密、香氣濃郁，還吃得到顆粒，讓人百吃不厭。早年新竹的花生醬工廠多集中在東大路一帶，與此區位居交通樞鈕有關，形成獨特的花生醬製造聚落；福源花生醬堅持手作，也講究真材實料，逐漸打開知名度；不過，隨著時代進步，市場充斥各式機器量產的花生製品，純手工製造的花生醬工廠在利潤有限與人力不足情況下，紛紛轉行，唯福源挺立至今。「福源」原由一名山東漢子經營，因他的家人不願承接，當時經營花生批發的曾和昌，不捨這好味道消失，與妻子劉瑞英討論後，決定接手，他們全心投入，也專注品質的態度，讓福源品牌發光發亮，目前已由第二代曾俊強接棒。福源堅持選用彰化、雲林的九號花生，這品種的花生油脂多、香氣濃郁，專門用來榨油，也稱之為「油豆」；曾家人特別挑選其中顆粒粗大的花生米來作花生醬，此豆炒起來香氣四溢、口感溫潤。花生最怕不新鮮，為了防止儲存不當滋生黃麴毒素，只要一進貨，馬上放進冰庫保存，維持最佳品質。福源招牌花生醬，每天現做，絕不隔夜囤貨，每次得炒上150斤花生，製作時的溫度、火候是成敗關鍵，太焦會苦、太生又有豆青味，絲毫不得馬虎；由於百分之百使用花生原豆與白糖製成，不加一滴水或添加物，花生醬一開封，滿溢的花生香氣席捲五官，濃密馥郁，單吃或抹在吐司上都好吃，不僅口感綿密，還吃得到花生顆粒，是老饕與行家最愛。'                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹水潤餅',
                                text='(03)5243708\n新竹市北區成功路326號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/北區/新竹水潤餅/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/北區/新竹水潤餅/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='彭成珍餅舖',
                                text='(03)5224877\n新竹市北區西安街5巷21號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/北區/彭成珍餅舖/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/北區/彭成珍餅舖/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='淵明餅舖',
                                text='0952170115\n新竹市北區中山路112號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/北區/淵明餅舖/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/北區/淵明餅舖/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新復珍商行',
                                text='(03)5222205\n新竹市北區北門街6號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/北區/新復珍商行/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/北區/新復珍商行/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )    
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@伴手禮/北區/新竹水潤餅/推薦菜色':
            try:
                message = TextSendMessage(
                    text='水潤餅'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區/新竹水潤餅/介紹':
            try:
                message = TextSendMessage(
                    text='外地人乍聽「水潤餅」的名字時，會以為是潤餅的一種，其實水潤餅和潤餅完全是兩回事。它是許多新竹人從小吃到大的「古早零嘴」，早期新竹還有多家製作水潤餅的店，然而隨著時代變遷與利潤降低，這簡單樸實的老味道也漸漸凋零，如今新竹只剩下「德龍商行」仍持續販售。德龍商行的二代老闆楊水龍，從國中開始跟父親學做水潤餅，兩代經營至今已超過50年。水潤餅外型圓扁，形狀不太規則，餅皮有斑狀的火痕，原料一如其單純的外型，只有麵粉、水、糖、鹽和肉桂粉；因為不含人工添加物和防腐劑，只能保存3至4天，冷凍能保存半年。楊老闆說：「外地類似這樣的餅都做得像山東大餅一樣，又乾又硬，跟我們的水潤餅不同。」水潤餅的水份較多且軟軟的，類似台語的「水軟水軟」，因而得名。咬一口水潤餅就會發現它不僅軟Q易入口，還帶著一點鹹甜麵粉香的濕潤口感，與傳統大餅的酥脆完全不同，成了早期老人和小孩最愛的點心。撕開餅皮，大大小小的氣孔，淡淡的肉桂香從中散開，滋味雖不濃郁，卻引人入勝，適合作茶點。說起自家水潤餅之所以成為新竹特色美食之一，楊老闆笑說：「因為城隍爺有保佑」。原來大約40多年前，一群在城隍廟服務的志工阿嬤將水潤餅做為獻給城隍爺的供品，此後水潤餅便逐漸興起，更因此成為「平安餅」；每逢農曆七月中元節，新竹都城隍廟范謝將軍遶境出巡時，都會將水潤餅用紅線穿成串，綁在神將身上，供信眾求食保平安，「用水潤餅作為平安餅」的風俗也成為新竹獨一無二的文化傳統。隨著飲食習慣的改變，水潤餅逐漸被人遺忘，年輕一輩新竹人，對這種廟會食品恐怕也僅存朦朧印象。市府在推動「新竹好物」美食復興計畫時，市長林智堅想起了水潤餅，特別推薦，希望更多人認識新竹在地獨特的日常美味。現今年輕人也開發出許多創意吃法，例如把這款古早味零嘴夾上餡料，包上肉末、荷包蛋，或者塗上果醬、咖哩，起司，都有令人驚豔的口感。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區/彭成珍餅舖/推薦菜色':
            try:
                message = TextSendMessage(
                    text='花生糖派對(原味、綜合堅果)、竹塹餅、麻糬紅豆Q餅、新竹椪餅'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區/彭成珍餅舖/介紹':
            try:
                message = TextSendMessage(
                    text='若非熟門熟路，一般人可能不知道狹窄的西安街巷裡，有一家傳承三代的傳統糕餅老舖─彭成珍。80多年前，彭成珍阿公以製作傳統糕餅維生，當時賣竹塹餅、柴梳餅等漢餅，每到節慶，也做些應景糕點，像新年的寸棗、中秋月餅、初一十五拜拜的紅龜粿等，主要批發給柑仔店，建立一定口碑。第三代的彭垂明原服務銀行界，從小跟在父母身邊幫忙，每逢中秋大月製餅人手不足時，總得請假幫忙，每見父母常沒日沒夜忙碌，一天睡不到幾小時，加上年紀大了體力明顯變差，決定辭掉工作，返鄉扛起家業。接手後彭垂明發現，消費者飲食習慣改變，看著老顧客逐漸凋零，吃傳統漢餅的人越來越少，開始思索如何突破困境；他先從產品包裝設計著手，也加入品牌行銷的概念，逐漸讓「彭成珍餅舖」名號被更多人看見，拓展消費群，轉型成功後，連太太李虹瑤也辭職投入家族事業，兩代人全心守護這家老餅舖。除了傳統糕餅，彭垂明夫妻倆都愛吃花生糖，常自己製作，並分享給同事，因為不錯吃，口碑建立，同事們起鬨要團購，意外成為人氣商品；在大賣場看見一桶桶的綜合堅果，也讓彭突發異想，將堅果加入花生糖中，作出口感更豐富的堅果花生糖；看著堅果、花生在熱鍋裡相互擁抱跳舞的模樣，將產品取名「花生糖派對」，傳達熱鬧、歡愉的心情，這項產品香脆不黏牙，獲選2016新竹市竹好呷類商品。（「花生糖派對」屬季節限定商品，夏天天氣過熱，麥芽糖無法凝固，端午節至中秋節期間不販售）。兩代人做傳統竹塹餅、柴梳餅、新竹椪餅，第三代研發花生糖派對，讓彭成珍餅舖在傳統之外，也開發新品，為這巷弄裡的三代店，點燃邁向下一世紀新餅業的燈火。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區/淵明餅舖/推薦菜色':
            try:
                message = TextSendMessage(
                    text='肉燥水蒸鹹蛋糕、風味芋頭餅、冰立方吐司'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區/淵明餅舖/介紹':
            try:
                message = TextSendMessage(
                    text='滷肉燥搭鬆軟蛋糕，在口中會撞出怎樣的火花？那份飽含肉香的鹹味與麵粉香的微甜，咀嚼之後留在舌尖的感動，會讓你回味無窮；這款糕點正是新竹知名的淵明水蒸蛋糕，曾獲選新竹十大10。位於中山路城隍廟對面的淵明餅舖，已有70年歷史，創辦人楊深淵老先生早年利用美援物資，單純以麵粉加蛋和糖，做出口感綿密、口味清爽的水蒸蛋糕，為新竹美食補上一頁。水蒸蛋糕發跡於新竹大戲院、樂民戲院交叉路口，那是早年新竹北區最繁華的商圈之一，楊老先生在路口設攤，每到週末假日電影開演前，就是楊家人最忙的時候，熱騰騰冒著煙的蒸糕，飄散出迷人香氣，挑起觀眾的食慾，之後一傳十、十傳百，成了新竹人看電影時非買不可、最夯的點心。第二代老闆楊滉崇從小為了家務，幫忙劈柴、挑水、生火，在煙霧迷漫的廚房工作，他說，水蒸蛋糕於他，就像家人一般熟悉，不可或缺，也是他人生記憶的全部。水蒸蛋糕的製作過程看似簡單，卻需慢工細活，每塊蛋糕先鋪一層底，分別放入紅豆、芋頭和肉燥內餡，上面再鋪一層蛋糕，才能進爐蒸，「火候掌控很重要，表皮要維持一定的濕度。」他說，製作時間超過一個半小時；他遵循傳統古法，只用蛋、糖、麵粉三種原料，製程中不加一滴油或香料、色素、防腐材料，要讓消費者吃得健康又養生。楊老闆對食材相當堅持，甜味水蒸蛋糕裡的「紅豆餡」，選用顆粒大、皮薄、顏色鮮紅的國產紅豆，「芋頭泥」也用上好芋頭，切塊、熬煮後，撈起來呈現淡淡紫色；店裡招牌是肉燥水蒸鹹蛋糕，加了滷肉燥的餡入口難忘，淵明水蒸蛋糕質地綿密鬆軟、爽口不油膩，如搭配冰涼沙士，甜甜鹹鹹的台式風味，會讓你一口接一口！目前，第三代楊志安也加入營運，為傳統老店走出新風格，他愛吃麵包，開發新品牌「十方吐司坊」，以老麵長時發酵，只用鮮奶不加水，做出鮮奶吐司入口即化又Ｑ彈，手按壓後即恢復原形，也快速竄紅成為超人氣商品！'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區/新復珍商行/推薦菜色':
            try:
                message = TextSendMessage(
                    text='竹塹餅、柴梳餅、核桃酥餅、水蒸蛋糕、美祿柑、綠豆椪'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/北區/新復珍商行/介紹':
            try:
                message = TextSendMessage(
                    text='有一種餅，作家焦桐說它的滋味是「輕淡的甜蜜含蓄著輕淡的鹹，鬆，軟，香，那滋味在口舌之間，纏綿，深情，像戀人的吻。」文字間的雋永意蘊無法一一道出，但繾綣之感彷彿融入腸胃與心底，久久不散。這是竹塹餅，以新竹古城為其名的特色糕點。竹塹餅創辦人吳張換女士原本在城隍廟前賣肉粽，1898年，年僅20多歲的她在新復珍的現址開始經營糕餅舖，巧妙地將包肉粽的蔥香、料香、豬油香應用到糕餅上，成了顧客最愛的口味，廣受歡迎；本來稱為肉餅或糕皮餅，但因為外地人常說「要買竹塹城的那個肉餅」，「竹塹餅」之名因而流傳開來。「新復珍」第四代吳紘一接手後，堅守最初的手工做法，現今需求量大增的竹塹餅，仍是老員工們純手工捏製而成。竹塹餅最重要的食材是豬板油和油蔥；吳紘一說，採用的是新竹本地的黑毛豬製成的豬板油，加上自己剝製、切、炸的油蔥，不同於一般外面工廠的機器製作，不但味道更香，內餡軟加上外皮酥脆，成就新復珍的百年好品牌。竹塹餅也是新竹人的共同記憶，曾有嫁到外縣市的女顧客回來新復珍買餅，開心地跟店員分享︰「我從小吃你們的竹塹餅吃到大」，言談之間，對於竹塹餅的驕傲和喜悅表露無遺。因為餡料和口感特殊而享有盛名的竹塹餅，近年因應民眾口味的改變也做了調整；現今的竹塹餅保留了漢餅精神中甜中帶鹹的豐厚味道，內餡已見不到早時白白的豬油塊，只保留下濃郁的豬油香，符合現代人少油膩、輕口味的需求。此外又推出了「小竹塹」，讓竹塹餅更精緻、討喜。每年節慶前後也是竹塹餅購買的旺季，在地人以竹塹餅當作禮品，送禮自用兩相宜，至今這股風氣不僅持續盛行且不斷往外擴散，提供外縣市民眾選購餅食糕點的多元選擇，也讓這纏綿的幸福繼續傳承下去。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='邱記麻糬',
                                text='(03)5371805\n新竹市香山區中華路六段807號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/香山區/邱記麻糬/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/香山區/邱記麻糬/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )    
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@伴手禮/香山區/邱記麻糬/推薦菜色':
            try:
                message = TextSendMessage(
                    text='麻糬餅、客家紅豆手工麻糬、客家小肉餅'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@伴手禮/香山區/邱記麻糬/介紹':
            try:
                message = TextSendMessage(
                    text='傳統手做麻糬，融合客家意象與風味，邱記麻糬各式創新產品，總讓人回味。邱坤方、趙芳齡夫婦1986年創立邱記麻糬，憑藉創新動力，曾獲新竹市政府主辦的「網路票選十大美食」，深受各界好評。邱氏夫婦原從事玻璃製造，因產業外移，轉行喜餅代理商，「雖然業績很好，但代理商利潤非常低」，因手上有現成客戶，兩人決定創業。當時，餅皮包麻糬的產品，口感獨到，深受歡迎，是創業第一選項產，請了位中式糕餅老師傅來幫忙。不過，老師傅做的麻糬餅保存期限僅一、二天，不符成本，夫婦倆專程到花蓮請教麻糬業者，以不添加防腐劑為前提，經討論研究，找到保存七天的方法。建立基本技術後，兩人開始在麻糬餅裡添加各種餡料，包括：芋頭、抹茶、紅豆、芝麻、花生、黑糖，外皮使用天然糯米，餅皮酥脆，一口咬下，香甜滿溢；陸續開發出：粢粑蕃薯燒、蒟蒻養生鳳梨酥、客家小肉餅、芋頭餅、地瓜餅、桂花糕等餅品，同樣有特色。值得一嘗是「麻糬雪柿」，將麻糬和紅豆塞入柿子後冷凍，食用時取出稍候一會兒回溫，嘗起來冰涼Q彈，備受年輕人青睞，也獲選新竹市106年度十大美食。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區':
            try:
                message1 = TemplateSendMessage(
                    alt_text='小吃',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='艷麗PondokSunny',
                                text='0965356956\n新竹市東區南大路52號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/艷麗PondokSunny/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/艷麗PondokSunny/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='璽子牛肉麵',
                                text='(03)5715959\n新竹市東區博愛街31號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/璽子牛肉麵/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/璽子牛肉麵/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='草根廚房',
                                text='(03)5200351\n新竹市東區柴橋路350號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/草根廚房/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/草根廚房/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='小山東館',
                                text='(03)5330550\n新竹市東區民族路252號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/小山東館/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/小山東館/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='老王記小館',
                                text='(03)5348686\n新竹市東區中央路300號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/老王記小館/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/老王記小館/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='大眾小館',
                                text='(03)5622540\n新竹市東區南大路93-3號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/大眾小館/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/大眾小館/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='老港陳',
                                text='(03)5278186\n新竹市東區南門街55號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/老港陳/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/老港陳/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message2 = TemplateSendMessage(
                    alt_text='小吃',
                    template=CarouselTemplate(
                        columns=[   
                            CarouselColumn(
                                title='南門當歸鴨麵線',
                                text='(03)5253216\n新竹市東區南門街30號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/南門當歸鴨麵線/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/南門當歸鴨麵線/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='無名早餐店（饅頭肉排蛋）',
                                text='(03)5721869\n新竹市東區學府路112號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/無名早餐店（饅頭肉排蛋）/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/無名早餐店（饅頭肉排蛋）/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='石家魚丸',
                                text='(03)5242965\n新竹市東區東區興學街27號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/石家魚丸/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/石家魚丸/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='禾日香魯肉飯',
                                text='(03)5280276\n新竹市東區民族路163號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/禾日香魯肉飯/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/禾日香魯肉飯/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='榮記客家湯圓',
                                text='(03)5238238\n新竹市東區武昌街64號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/榮記客家湯圓/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/榮記客家湯圓/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='水哥養生早餐',
                                text='(03)5327479\n新竹市東區民主路64號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/水哥養生早餐/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/水哥養生早餐/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='燒餅屋',
                                text='(03)5712623\n新竹市東區東山街54號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/東區/燒餅屋/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/東區/燒餅屋/介紹',
                                   ),
                                ]
                            )
                        ]
                    )
                )
                message = [message1, message2]
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@小吃/東區/艷麗PondokSunny/推薦菜色':
            try:
                message = TextSendMessage(
                    text='千層糕、娘惹糕、南洋叻沙鍋'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/艷麗PondokSunny/介紹':
            try:
                message = TextSendMessage(
                    text='2015年9月開幕的「豔麗PondokSunny」，提供星馬、印尼的特色糕點與餐食，開店時間不長，已廣受在地食客好評。店名「Pondok」意指南洋島國常見的茅草小屋，熱情的南洋風格也表現在多彩的內部空間，牆面的手拓彩繪，到桌椅、燈罩的布樣，都是店主李依庭親手打造，各項擺飾是她多次與母親往返東南亞各地的收藏，營造了獨特而溫馨的用餐氛圍。「豔麗」的緣起來自店主的母親姚燕麗，她在印尼出生，父母是馬來西亞及新加坡華僑，這樣的家族背景，讓她對東南亞各地特色料理與文化相當熟悉，嫁來台灣近30年，懷念家鄉味，開始做起南洋點心，起初在新竹縣北埔擺攤，因女兒願意接手，才決定在香山開南洋風餐館。南洋糕點是「豔麗」的主打商品，口味多元的娘惹糕及千層糕，一蒸一烤，都是慢工出細活的好滋味，台灣人講究健康養生，老闆娘順意民情，捨棄傳統娘惹糕大量以人工色素增色的做法，改用竹炭、梔子等天然食材，與酒釀桂圓、地瓜融合，創新口味。店裡餐點道道都有好評，值得一提是「牛肉丸」，選用台南溫體黃牛肉，肉質鮮美，製作時加入牛筋，口感更Q彈；餐後可以來碗甜湯，大家熟知的南洋甜湯是摩摩喳喳，還可以嘗嘗「錢多錢多」的南洋香蘭米苔目，或是加入仙草、錢多、亞答子、西谷米的「南洋珍寶」，一碗就能嘗到多種配料。老闆娘自製的印尼蝦膏、辣椒、紅蔥頭等手工蝦醬，也具特色，少了市售蝦醬的濃重腥味，像糯米椒蝦拌醬、小魚蝦拌醬，用來佐餐、拌麵或爆炒時蔬，都很對味。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/璽子牛肉麵/推薦菜色':
            try:
                message = TextSendMessage(
                    text='斤餅、斤餅包牛肉、清燉牛肉麵、炸醬麵'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/璽子牛肉麵/介紹':
            try:
                message = TextSendMessage(
                    text='「璽子牛肉麵」位於十八尖山登山口旁，雖非開業數十年的老字號，卻以每日現點、現做的斤餅打響名號，用餐時間總見大排長龍。店內最吸引人的，莫過於師傅在工作台前製斤餅的畫面，這是顧客必點的鎮店招牌，人氣旺到在竹北開分店，人潮依舊絡繹不絕。「璽子」老闆是江蘇人，早年在台北牛肉麵館工作，10年前興起開店念頭，將工作經驗化為技術，開了這間店。店內事務由老闆與老闆娘家人一同打理，每天一早都到店內親自燉煮牛肉、調配醬料。如今，老闆娘的兄長、妹妹已分別擔負起本店與竹北店的店長，更親自傳授斤餅功夫給師傅，讓產品品質如一。既然號稱「斤餅專賣店」，招牌自然就是斤餅。「斤餅」一詞的由來，據說是因為在大陸販售時都稱斤論兩而得名，它的做法是將植物油與麵粉製作成的油酥，跟揉好的麵糰開層疊後捲成一團，下鍋前再成圓餅狀，煎烤至金黃熟透，就是外皮酥鬆又帶嚼勁的斤餅。單點斤餅時，師傅會在餅上塗抹甜麵醬，再夾入青蔥，甜麵醬的鹹甜滋味配上略為辛嗆的蔥段，簡單又美味；點食率最高的是京醬肉絲（附斤餅）及斤餅包牛肉，前者以甜麵醬等配料炒製肉絲，用斤餅包覆食用；後者則在餅內捲入切成薄片的滷牛腱及青蔥，風味絕佳，各有千秋。「璽子」的另一項招牌是清燉牛肉麵，最能嘗到牛肉原味。將整條澳洲牛腱肉切成三大塊後下鍋燉煮，腱肉內層夾雜的牛筋，經長時間燉煮後軟化，起鍋後再切大塊配麵食用，口感極為軟嫩，充滿膠質又帶有牛肉豐厚鮮味，頗受饕客好評。此外，店家也提供以薄切羊肉搭配清湯的清燉羊肉湯、炸醬麵、香辣肉醬乾麵等選擇。種類不多，但道道吃得出店家用心。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/草根廚房/推薦菜色':
            try:
                message = TextSendMessage(
                    text='極品烤鴨、草根鍋餅'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/草根廚房/介紹':
            try:
                message = TextSendMessage(
                    text='2004年開幕的草根廚房位於柴橋路山腰，沿山坡而建的紅磚黑瓦屋，高低起落著，高聳的樹木環繞，推開朱紅木門，彷彿走入鄉野林間訪友一般。老闆陳世淵本身就是新竹人，從小跟在經營客家、台菜餐廳的父母身邊幫忙，累積深厚餐飲底子，後來回到老家現址開起了草根廚房。取名「草根」，是希望客人在這裡不僅能吃得安心健康，還能無拘無束，就像在家裡和親友吃飯一般自在。到「草根廚房」得吃什麼？看看每桌都有烤鴨就懂了！店裡的極品烤鴨選用宜蘭櫻桃鴨，陳世淵說草根選用的鴨殺完需足4斤半重，且須具備約70天左右的鴨熟度，烤起來韻味與口感才會好。鴨先醃上八角、月桂葉等七、八種香料略為提味，採用明火掛爐烤法，將木炭香氣燒入鴨肉，在高溫中鴨皮更為酥脆。「草根廚房」的烤鴨，採皮肉分離片法，一隻鴨約能片上二十幾片鴨皮。咬下酥脆鴨皮，伴隨清脆聲而出的是濃厚鴨脂香，竄得滿口盡是油香，原味品嘗就讓人難忘，蘸上特製甜麵醬，以純手工荷葉餅包裹宜蘭三星蔥、小黃瓜一起入口，帶出鹹香、鴨皮的脆、蔥的辛香及黃瓜的清脆爽口，豐富的層次，帶來味覺驚喜。極品烤鴨除了烤鴨切盤外，還有酸菜鴨骨燉湯、醬爆鴨骨、生菜鴨鬆等不同吃法。除了烤鴨，「草根鍋餅」也千萬別錯過。鍋餅是淮揚菜的特色點心，豬肉、蝦仁內餡配上滿滿韭菜末，韭菜的特殊香氣與多汁口感，和鍋餅灑滿白芝麻的酥脆外皮，形成強烈對比，讓人一吃就上癮。冬季來到草根廚房，還有期間限定（10∼4月底）的酸白菜鍋，酸白菜、川丸子、鴨血等配料都是店家自製。主角酸白菜用的是山東大白菜，將米漿水、花椒、高粱酒、鹽等以傳統古法醃上一個月發酵而成。大量酸白菜配上每天一早熬的大骨高湯，再放入寬粉條、肉片、凍豆腐、川丸子、鴨血、白蝦、蛤蜊、新鮮菇類等豐盛配料，微酸的湯頭讓人胃口大開，一口接一口好不歡暢！'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/小山東館/推薦菜色':
            try:
                message = TextSendMessage(
                    text='鍋貼、水餃、酸辣湯、家常炒菜'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/小山東館/介紹':
            try:
                message = TextSendMessage(
                    text='尋常中午時分，客人或笑語宏亮或親切問候；踏入小山東館，老闆陳英訓和老闆娘劉碧玉對客人如數家珍：這對高齡近90的老夫妻已經吃了30多年、那一桌是科學園區上班的老主顧、這位住在附近⋯⋯，整間餐館彷彿大家庭。小山東館原本是間貨運行，這一帶當年是眷村，司機來自大江南北，常分享各自的拿手料理，老闆娘也擁有一手好廚藝。民國71年由陳英訓出資，眾人合力在貨運行一角開了小吃部，因主廚是山東人，取名「小山東館」。小吃部初試啼聲便大獲好評，吃水餃鍋貼的人比貨運行的貨還多，客人甚至得和貨物搶位置。後來，陳老闆決定將貨運行改成小吃部，成就了飄香30多年老味道的小山東館。小山東館的家常麵食中，舊雨新知必點的招牌料理是鍋貼。老闆夫妻堅持品質，餃子麵皮和內餡都是自己製，先將麵粉揉勻，放置十分鐘讓麵糰「醒過來」、放鬆後，將麵糰撥成小塊，壓扁、拉長，放入餡料；餡料選用上等黑豬後腿肉，除了蔥、高麗菜和一般常見調味料，還加入了自己熬榨出的黑毛豬油與特殊秘方。煎成金黃色的鍋貼，擺盤成太陽花的形狀，兩頭麵皮包起來的設計，巧妙地將湯汁鎖在裡頭，一口咬下，不僅嘗到爽脆的高麗菜和鮮甜肉餡，飽滿的湯汁更充盈其中，調味料除了豬油，胡椒粉、辣椒油都老闆夫妻手工製作，讓人欲罷不能，難怪假日一天能賣出2000多顆！老店往往面臨後繼無人的問題，所幸小山東館第二代子女決心拋棄科技新貴光環，毅然接手，並搬遷到新址開業，讓這迷人的懷舊老味道，在新竹繼續傳承下去。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/老王記小館/推薦菜色':
            try:
                message = TextSendMessage(
                    text='小籠包、水餃、綠豆稀飯'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/老王記小館/介紹':
            try:
                message = TextSendMessage(
                    text='老王記的水餃每天現包現賣，由黃家兩姊妹負責，兩人一個半小時得包完1000顆水餃。前一天先將韭菜或高麗菜洗好晾乾，早上現切、現包，肥瘦參半的豬肉加入水和薑攪拌，少了油膩，多了些濃郁薑味，菜與肉的比例各半，吃起來十分爽口。小籠包、蒸餃、水餃，三種看似相近的麵食製品，在「老王記」裡卻大不同，分別使用不同麵糰製皮、內餡比例及烹煮方法，口感與味覺不一樣；從基本的食材選用與製程設計，都反應店主對食物的要求與堅持。發跡於1948年的舊東門市場，最早是「天津老王記包子舖」，歷經搬遷、更名，2009年落腳中央路現址，由第三代接手，以「老王記」之名營業，店裡大小事都全家人一手打理，親力親為，光前置備料就花費數小時，「花同樣的錢，就該享受同樣的品質保證。」年輕的黃老闆說。老王記的麵食都現點現做，當天製作賣完就收，絕不讓客人吃到回籠的食物；就連客人C-預訂，也都盡量在客人取餐前兩、三分鐘，餐點做好並打包完成，讓客人享受到尚青的美味。以老麵製作麵皮的小籠包是招牌，麵糰的發酵程度依天候、濕度、溫度、環境、時間不一，憑經驗和手感來判斷。負責小籠包麵糰製作的黃老闆謙虛說，「花了10年才完全掌控麵糰的發酵技術。」麵糰必冷藏保存，讓它在低溫中慢慢發酵約8小時，由於擀麵、包餡都在高溫的廚房中進行，如此一來，移進室溫後，麵糰發酵的速度會變慢，品質也相對穩定。十年磨一劍，完全真功夫，為呈現一流口感的天津小籠包，黃先生不斷研發改良，內餡的肉每天要花上1個多小時細挑骨頭、肉筋，讓客人吃到細緻順口的餡，挑不出細骨或難以下嚥的食材，嚴格的品管與自我要求，讓來客心服口服，一吃成主顧。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/大眾小館/推薦菜色':
            try:
                message = TextSendMessage(
                    text='炒飯、花雕雞、麻油松阪豬、鹹蛋苦瓜'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/大眾小館/介紹':
            try:
                message = TextSendMessage(
                    text='原本是攀高搬重物的粗工，變身持鍋鏟的廚師！李俊德憑著吃苦耐勞的性格與積極學習的態度，讓自己的職涯轉身成功，也讓新竹市多了一處美食天地。在新竹市南大路的大眾小館，是新竹人耳熟能詳的快炒店，除了各色炒飯，花雕雞、麻油松阪豬、鹹蛋苦瓜這三道菜，是必點名菜。練就這麼一身炒功，李俊德可是從學徒做起！「當年薪水低，什麼都要做。」李俊德說，踏進廚房對他來說是全新體驗，從基礎學起，當時的師徒制是：師父領進門，修行看個人，老廚師並不主動叫學徒學習，得自動自發，他改變幹粗活的率性，仔細觀察師傅每道菜的步驟，逐漸領略到掌廚的要義，抓到每道料理的精髓。每天清晨6點半，李俊德送孩子上學後，便到經國路的果菜市場，親自挑選新鮮食材，「要確保每一道料理的品質」。9點半到11點是店內備料，之後便是一天最忙碌的時刻。大眾小館的經典菜是花雕雞、麻油松阪豬、鹹蛋苦瓜。花雕雞選用土雞腿，去骨後，以精選台灣菸酒公賣局的花雕酒醃漬，與杏鮑菇一併油炸，封住肉汁後起鍋備用，緊接著把切好的紅黃甜椒與青椒入鍋快炒，放入備料，再次爆嗆，燜燒約6分鐘起鍋。麻油松阪豬是將松阪豬與杏鮑菇先汆燙，另起一鍋以老薑片、麻油爆香，再將松阪豬等放入鍋中，加水、米酒、枸杞等一同拌炒；他說，松阪豬選用新竹本地的黑豬肉，非進口，油花分佈均勻，軟嫩可口、齒頰留香。另一道鹹蛋苦瓜與一般快炒店手法不同，不清炒，以油炸方式呈現。首先，將苦瓜切成薄片後油炸，鹹蛋黃弄碎後，放入鍋中，加少許鹽巴、蔥與辣椒拌炒，苦瓜宛如黃金般的色澤，視覺與口感都華麗。大眾小館的炒飯，在網路被稱譽為「新竹炒飯王」，不過，近年來已減少品項僅留下部分經典炒飯，不要錯過！'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/老港陳/推薦菜色':
            try:
                message = TextSendMessage(
                    text='鮮蝦腸粉、紅油抄手、皮蛋瘦肉粥、蛋意麵'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/老港陳/介紹':
            try:
                message = TextSendMessage(
                    text='老港陳老闆陳樹水本身是香港人，懷抱夢想來到台灣這塊土地，為新竹多元並茂的美食地圖增添一縷芳香。「起初，我是賣潤餅的」，直到2004年左右，才開始賣起現今在新竹膾炙人口的老港陳港式美食。一開始，是由老闆開著發財車在以前的中興百貨擺攤，最後在2012年落腳到南門街這家紅磚造的老店面。每日晚上7點過後，店內的人潮便逐漸聚集，到了深夜時刻更是一位難求，得要等待多時才能一飽口福。「我們最推薦鮮蝦腸粉、紅油抄手、皮蛋瘦肉粥以及蛋意麵。」鮮蝦腸粉是將再來米粉調製而成，淋上特調的醬汁，入口難忘。紅油抄手則是選用有豐富脂肪的豬腩，也就是俗稱的五花肉，滋味極好。在老港陳這碗看似簡單的皮蛋瘦肉粥，是用豬骨熬製的上湯去熬米成粥，比起坊間的粥，多了一份鮮甜可口的軟爛滋味。而蛋意麵則深受年輕女性喜愛，簡單美味。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/南門當歸鴨麵線/推薦菜色':
            try:
                message = TextSendMessage(
                    text='當歸鴨麵線、當歸豬腳麵線、當歸滷味拼盤'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/南門當歸鴨麵線/介紹':
            try:
                message = TextSendMessage(
                    text='明亮燈光與潔淨店面，南門當歸鴨和你想像的傳統「老店」不一樣；走進店裡，老闆熱情的噓寒問暖，及當歸湯暖暖甜甜的滋味，卻又如此傳統。民國55年創立的老店，緣自一場暖心意外，老闆陳慶源的父親早年熬製當歸鴨湯，單純給家人補冬，幾年下來，好味道傳遍鄰里，紛紛央求分享，最後只能開店，滿足大家需求。招牌當歸鴨湯正是他父親白手起家研究出來的配方，選用當歸、桂皮、枸杞、紅棗、熟地，搭配豬腳和六支全鴨一起燉煮，湯頭喝起來多了點「圓潤」口感。「這是很抽象的感覺，就像白開水沒味道，熬煮過的湯頭就很不一樣」陳慶源說。陳慶源退伍後從父親手中接下店面，才發現這個從小吃到大的味道原來很特別，也在經營過程中，更貼近父親。「我爸個性很固執，接手後第五、六年才能體會他的固執是對的，堅持也是對的」他說，前幾年曾建議父親修改配方、更換中藥商，統統被打回票，也讓他漸漸感受到，美味和父親的堅持是綁在一起的。美食也需順應潮流，在保存父親傳統手藝之外，他也嘗試創新，新舊拔河中，從傳統玩出新味。舉例說，他看準市場需求，推出當歸豬腳麵線，客人可以帶給長輩們過生日；近期也研發當歸餛飩、當歸羊肉，並加入太太親手做的小菜豐富菜色，拓展客源。「創新是必要的」，不過菜色新，料理流程卻都遵循傳統，絲毫不馬虎，所幸，這樣的創新，也得到老主顧的普遍讚賞。鍋爐底下的火持續燃燒，那份為家人冬天進補的心意從未熄滅。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/無名早餐店（饅頭肉排蛋）/推薦菜色':
            try:
                message = TextSendMessage(
                    text='饅頭肉排蛋、豬肉餡餅、韭菜餡餅、蛋餅加肉排'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/無名早餐店（饅頭肉排蛋）/介紹':
            try:
                message = TextSendMessage(
                    text='開業30多年的無名早餐店，老闆娘蔡媽媽20多歲開賣迄今，累積穩定的顧客群，不少主顧客都成為好朋友。早餐店原本是蔡媽媽為補貼家用的副業，沒想到做出興趣與名聲，生意越做越好，因人手不夠，丈夫、兒女索性全部投入，成為家人的共同事業。本身對吃極有興趣的蔡媽媽，最喜歡在廚房裡摸索，每天研究新菜色，做出好料理跟大家分享。「端上桌的，一定要好吃，不美味的，不上桌。」這是她的原則。店裡招牌「饅頭肉排蛋」是最有媽媽味道的活力早餐，也是人氣最夯的商品。她說，兒子挑食，不想讓他每天吃相同的早餐，於是靈機一動：自己醃排骨、煎排骨，再加入荷包蛋，夾進當天現做的饅頭裡，如此一顆飽滿紮實的饅頭，吃起來既方便又飽肚，裡頭更有滿滿媽媽的愛心，沒想到此舉讓客人瞧見，也嚷著來一顆，意外成為店裡明星商品。無名早餐店生意好，門口經常大排長龍，蔡媽媽一家人並不因為生意好而鬆懈，每天戰戰兢兢用心備好每項產品，為客人準備熱騰騰的早餐。當然，老客人也總是心甘情願地等待，用這樸實又認真的一味，來開啟一天的活力。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/石家魚丸/推薦菜色':
            try:
                message = TextSendMessage(
                    text='骨仔肉魚丸湯、香菇摃丸、滷肉飯，石家魚丸'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/石家魚丸/介紹':
            try:
                message = TextSendMessage(
                    text='風城馳名老店之一，創辦人沿街敲缽、愛妻疼女的真實故事，足以寫成厚厚的一本家傳奮鬥史。石家的招牌美食—骨仔肉魚丸湯，料鮮味美，用魚漿打成的丸子Q彈富咬勁，軟嫩的骨仔肉幾乎入口即化，再搭配香滑濃郁的清澈鮮高湯，是新竹離鄉遊子深深懷念的家鄉味。1944年，創辦人石朝俊13歲，跟師傅學了手藝出師後，沿街挑擔賣魚丸。日子雖清苦，但天公疼憨人，讓他娶到姚綢這位精通廚藝的好妻子，她突發奇想將餡料包在丸子內，沒想到大受客人歡迎。「做出好吃的魚丸讓顧客滿意，是我們堅持的理念。」石家魚丸採用最上等的食材，魚漿選用深海魚，加赤肉、蔥和荸薺三種內餡，傳統工法現包現做。鍋裡的丸子隨沸水不停滾動，工作區內員工雙手幾乎沒停過，「來喲~來喲~燒ㄟ魚丸湯！」石老闆用大湯勺熟練地撈起一鍋丸子，大聲吆喝注意別被燙傷。石老闆秉持傳統製程繁複費時，「先把魚肉刮下來剁碎攪拌，每一鍋餡料攪和10分鐘以上，直到拌出肉的黏性為止。」經過大火熬煮的豬骨仔肉，口感軟嫩，細肉入口即化，坐在一旁的石老太太端了一碗魚丸湯，笑臉盈盈地和客人聊天，和善親切的態度不改當年。坐在店裡的一位老闆級顧客也攜家帶眷固定到石家魚丸報到，「我從年輕小夥子讀書打工時就開始喝他們的魚丸湯，吃了30年，口味好、價格公道、服務又好！」客人絡繹不絕，從店門口排到巷口，形成巷弄美食的另類街景。傳統道地的家鄉美味，令人想起廚房裡媽媽的身影，僅僅是一碗小小的魚丸湯，連異鄉遊子也抵擋不了它的美味，吃了還想再吃，一甲子老店果真魅力無窮！'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/禾日香魯肉飯/推薦菜色':
            try:
                message = TextSendMessage(
                    text='招牌魯肉飯、太陽飯、泡菜、小魚辣椒、手工魚羹'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/禾日香魯肉飯/介紹':
            try:
                message = TextSendMessage(
                    text='「好東西得經得起挑戰！」老闆鄭明枝開朗的說；經營魯肉飯小吃，源自喜歡做菜給家人吃，從法院書記官退休後，一頭栽入「魯肉飯」製作，無師自通，抓到要訣，後來決定開店，主打魯肉飯，因肉香濃郁，吃完唇齒留芳，備受歡迎，便以「香」字拆解出來的「禾日」當店名。禾日香創店至今5年，女兒也加入營運行列，稱得上二代合力；鄭明枝負責出菜，除滷肉燥，還供應古早味白菜滷、雞絲飯、滷大腸、炒菜心、泡菜、手工魚羹湯等，都是些常民小菜，簡單卻有好味道；招牌魯肉飯加值變成「太陽飯」，更是紅翻天，暖暖的菜名，入口就有滿滿的幸福。鄭明枝做滷肉燥都選用整塊松阪肉，肥瘦比例適當，手工切大丁塊，不假手機器；肉燥越滷越香，肥肉逐漸熟透化開，只剩瘦肉，松阪肉的口感佳，不會柴化澀口。他說，因為全家四代都在店裡吃三餐，把客人當家人看待，自己吃什麼，客人就吃什麼，所以不惜成本，店內所有配菜也秉持這樣想法，這份真心，已得到顧客認同。加入魯肉飯一級戰區，要異軍突起不容易，鄭明枝全家總動員，每年農曆春節假期，百業皆休時，他們開店，還辦熱鬧的吃魯肉飯抽紅包活動，一方面服務顧客，也招徠新客群。禾日香也開發冷凍滷肉燥包、泡菜罐、瓶裝小魚辣椒及手工魚羹包，提供外帶與宅配，還參加十大10甄選，希望透過多元管道曝光，打響「禾日香」的知名度。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/榮記客家湯圓/推薦菜色':
            try:
                message = TextSendMessage(
                    text='客家湯圓、白斬肉飯、梅菜爌肉飯、粉㲖'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/榮記客家湯圓/介紹':
            try:
                message = TextSendMessage(
                    text='年輕潮流服飾店家林立的文昌街區，隱身一間近30年的老店─榮記客家湯圓，憑藉客家家常味，緊緊扣住年輕人的味蕾，在許多新竹人的味覺記憶裡，添上難以忘懷的好滋味。民國78年，老闆娘吳周秋子因須扛家計，身為客家人又愛吃湯圓，索性在騎樓下擺攤，賣起自己最熟悉的客家湯圓；當年，攤子上僅寫著「客家湯圓」四個字，之後為方便客人尋找，以三個孩子名字中的「榮」字命名，將路邊攤搬到老家一樓開設店面，成就今日的規模。米食向來是客家人的拿手絕活，傳統客家湯圓的特色是不包餡的紅、白小湯圓，可甜、可鹹，尤以能當主食的鹹湯圓最受歡迎。她說，鹹湯圓作法各家不同，各具風味，基本上都會加入茼蒿、肉絲、香菇、蝦米、韭菜等配料。對客家人而言，油蔥、蝦米爆香後的味道，決定了湯頭的好壞；食物才送上桌，油蔥、蝦米揉合的香氣已撲鼻，「這種強烈的存在感是屬於客家人的味道」。「榮記」的客家湯圓以較富黏性的純糯米手工揉製，每顆湯圓都得搓揉到表面完全沒有毛細孔，水煮時較不容易吸收水分，吃起來更Q彈；「榮記」鹹湯圓有獨特的美味，除了香菇、蝦米、蒜頭、肉絲、胡椒，還加入三種中藥材，大火炒出香氣，之後淋上醬油、加少許以大骨、雞骨熬煮的高湯，湯頭濃郁又鮮甜。抱著不讓客人餓著的心，榮記湯圓用大碗公裝盛，不僅青菜配料多，湯圓也毫不客氣地佔去大半碗，份量多，常讓客人忍不住驚呼，一般成年人也一碗就飽，加上價格親民，是庶民小吃中最物美價廉的選擇。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/水哥養生早餐/推薦菜色':
            try:
                message = TextSendMessage(
                    text='牛肉五穀飯糰、豬里肌飯糰、烤雞腿飯糰'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/水哥養生早餐/介紹':
            try:
                message = TextSendMessage(
                    text='這家早餐店週六一天就能賣出1000個飯糰，平日營業時間，門口也總大排長龍。搭計程車時只要說：「我要到水哥飯糰」，司機大哥就會載你到目的地；「水哥養生早餐」在新竹市人心中，儼然已成地標。暱稱「水哥」的老闆呂呂水，常因姓名中有雙呂，引發顧客好奇。他是中餐廚師，曾任職台北五星飯店多年，921大地震後，想找一個能跟家人在一起、方便照顧小孩的工作，決定到新竹市賣飯糰。1999年從擺攤賣25元飯糰加送豆漿起家，至今已有自家店面。水哥創意飯糰的口味由水哥的太太發想，再由餐飲底蘊深厚的水哥付諸實現。店裡的主力飯糰口味，從傳統肉鬆、紅燒鰻、仔魚、燻雞、豬里肌、烤雞腿，到電視《食尚玩家》主持人浩子、阿翔大力推崇的牛肉五穀飯糰、西式口味的培根蔥蛋飯糰與香腸蔥蛋飯糰等，口味多變，加上不斷推陳出新，讓忠實客戶保有新鮮感。不只口味求新求變，店裡賣的餐飲，也以自己的孩子能每天吃、吃不膩來考量，因此，食材講究安全衛生，能安心食用為原則。水哥說，飯糰最惱人的問題是容易脹氣，他將飯糰中的白米與糯米比例稍做調整，解決這個問題。不過，問題來了，白米比糯米多，口感變得較軟爛，不如糯米來得帶有嚼勁，水哥開始研究，怎樣把白米煮得跟糯米一樣好吃，選用香氣足的新米，不過，新米香氣足但水分含量多，煮來容易爛，尤其不適合捏飯糰；他再摸索出一套獨特的煮飯系統，用高壓蒸煮，最短時間內讓米心熟透，使新米煮好仍保有Q彈口感，他將煮飯流程、比例數據化，詳細記錄每一次煮飯的數據與口感變化，花了十年時間，終於找到最接近心中完美的飯糰口感。水哥飯糰的份量也十分驚人，最輕235公克，最重的340公克，比一瓶飲料還來得重上許多，這樣的大份量飯糰最低消只要28元，最貴一款不過65元，經濟又實惠，不管男女老少，都愛上這一味。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/燒餅屋/推薦菜色':
            try:
                message = TextSendMessage(
                    text='蔥酥餅、甜酥餅、燒餅夾九層塔蛋'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/東區/燒餅屋/介紹':
            try:
                message = TextSendMessage(
                    text='「從小住眷村，每天經過眷村伯伯開的燒餅早餐店，總是被那股撲鼻的燒餅香吸引，那時候家裡窮，無緣品嘗，吃一口傳統手工燒餅，一直是我心中最大的夢想⋯⋯。」沒想到這個夢想，成為陳照淨創業的原動力。陳照淨的燒餅手藝是跟永和一名江蘇籍的高姓師傅學習，高師傅強調做傳統燒餅不能怕辛苦，得按部就班，不許馬虎，才做得出真正的傳統味；陳照淨秉持同樣精神，創業開店，「堅持傳統味是我的初衷」她說。「燒餅屋」做的餅項很多，有香蔥大餅、長形薄燒餅、蔥酥餅、甜酥餅（紅糖、白糖、芋香口味），其中，點食率最高的是長形薄燒餅，不管夾九層塔煎蛋或青蔥煎蛋，受歡迎程度都破表。「燒餅都是現點現做，在大烤箱內輪流烤。」她說，工作人員必須非常專心控制時間，不停翻面，可以想見夏天沒冷氣的時候是多麼辛苦，也因為這份用心，當酥脆的燒餅送進客人口中的剎那，瞬間讓人感動！除了強調現做與口感，燒餅屋重視食材，讓客人吃得健康無負擔，店內燒餅都用高級沙拉油揉製，素食者也能嘗。像紅糖酥餅內餡，便採用新竹縣寶山鄉的紅糖，蛋餅皮也堅持自己揉麵製，不買現成品，每日限量供應，假日很快就完售。燒餅屋的用心不只展現在食物上，盛裝食物的杯盤，也都用瓷器與紙袋，絕不用塑膠袋；因為是排隊的店，為了不讓顧客向隅，燒餅屋還提供簡訊訂餐服務，只要前一天晚上九點以前訂餐，隔天就能到店裡取得熱騰騰燒餅餐。如此的用心與貼心，都被顧客放入心裡，不僅口口相傳，呷好逗相報，很多是一吃成主顧。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區':
            try:
                message1 = TemplateSendMessage(
                    alt_text='小吃',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='樹林頭麵店',
                                text='(03)5314945\n新竹市北區東大路二段423號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/樹林頭麵店/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/樹林頭麵店/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='揭家牛肉麵',
                                text='(03)5364668\n新竹市北區東大路三段373號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/揭家牛肉麵/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/揭家牛肉麵/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='漁香甜不辣',
                                text='(03)5238843\n新竹市北區大同路86號2010號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/漁香甜不辣/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/漁香甜不辣/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='蔡記燒酒雞',
                                text='(03)5233885\n新竹市北區中正路190號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/蔡記燒酒雞/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/蔡記燒酒雞/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='阿富魯肉飯',
                                text='(03)5254305\n新竹市北區中山路75號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/阿富魯肉飯/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/阿富魯肉飯/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='三福麵線',
                                text='0987875333\n新竹市北區竹光路214號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/三福麵線/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/三福麵線/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message2 = TemplateSendMessage(
                    alt_text='小吃',
                    template=CarouselTemplate(
                        columns=[   
                            CarouselColumn(
                                title='老店薑母雞',
                                text='(03)5284895\n新竹市北區少年街51號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/老店薑母雞/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/老店薑母雞/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='鴨肉許',
                                text='(03)5253290\n新竹市北區中正路212號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/鴨肉許/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/鴨肉許/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='西市汕頭館',
                                text='(03)5244430\n新竹市北區西安街70號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/西市汕頭館/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/西市汕頭館/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='余家金城廣東粥',
                                text='(03)5277412\n新竹市北區水田街2號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/余家金城廣東粥/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/余家金城廣東粥/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='北門炸粿',
                                text='(03)5220471\n新竹市北區城北街15號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/北門炸粿/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/北門炸粿/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='廟口鴨香飯',
                                text='(03)5231190\n新竹市北區中山路142號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@小吃/北區/廟口鴨香飯/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@小吃/北區/廟口鴨香飯/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message = [message1, message2]
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
        elif mtext == '@小吃/北區/樹林頭麵店/推薦菜色':
            try:
                message = TextSendMessage(
                    text='陽春麵、榨菜肉絲麵、滷味拼盤'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/樹林頭麵店/介紹':
            try:
                message = TextSendMessage(
                    text='樹林頭麵店是時代的座標，讓過去的記憶降落，讓現在的人們見證歷史。「我老公以前隸屬空軍第八大隊，是支轟炸大隊。」我們進店時，91歲的常客姚奶奶正和老闆聊得起勁。原來，麵店老闆李增水以前是空軍第三十四大隊的士官長，跟老奶奶有說不完的話題；其實，東大路這一帶以前有許多空軍眷村，一旁的鐵道路顧名思義是以前火車軌道，專門載送貨物直達機場。樹林頭麵店始於民國63年，由老闆娘周雲玉的媽媽創立，因應外省人飲食習慣，經營麵食早餐，菜色說起來稀鬆平凡，盡是處處可見的陽春麵、榨菜肉絲麵、炸醬麵、滷味，但光憑這幾樣菜就能收服許多人的胃，可見店家功力。店裡的招牌是「辣椒醬」和「山東醋」，正是老眷村人念念不忘的味道，「這些外面買不到，很多人搬到台北後特別回來吃。」周雲玉說；辣椒醬用的是花椒，香而不嗆，略帶辛辣；山東醋清淡爽口，不似市面上賣的醋那麼酸，兩種醬料搭在一起是絕配，淋在各類麵食、滷味上，都讓麵點加分，「這是老外省人的口味，年輕人不知道，但我這麼一教，大家都說好吃！」周雲玉笑說。滷味拼盤是店裡的另一項人氣產品，經常早上10點前就銷售一空，其中，最受歡迎的莫過於豬頭肉和豆腐干；豬頭肉經小火熬煮1∼2個小時，油脂消失，軟硬適中，老闆娘每天都要吃上一份，豆腐干裡頭有孔洞，能讓湯汁入味，滷得到味，咬下去滷汁溢出，口感鬆軟又香氣飽滿。樹林頭麵店走過四十多個年頭，老闆夫婦見證了老主顧的成長與凋零，與客人也成了無話不說的朋友，「我喜歡看老客人，跟他們一起聊聊老故事或八卦，相當有趣。」老闆娘笑著說，她也希望這家店成為社區交誼廳，繼續經營下去，將棒子交給兒子。仗打完了，眷村拆了，當時的記憶結晶成一碗碗湯麵，道道滋味都是大時代矇住的心跳。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/揭家牛肉麵/推薦菜色':
            try:
                message = TextSendMessage(
                    text='牛肉麵、牛肉乾麵、豬骨湯腸麵、各式滷味'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/揭家牛肉麵/介紹':
            try:
                message = TextSendMessage(
                    text='「揭家牛肉麵」開業已六十餘年，是新竹知名老字號，許多常客從小吃到大。店面鄰近南寮漁港，人潮絡繹不絕，是在地人難以忘懷的家鄉美味。揭家牛肉麵主要供應乾麵、湯麵及無肉牛肉湯麵，另有陽春麵及搭配滷大腸的牛骨、豬骨湯腸麵等，麵食品項單純，但櫃台上擺著的一大盆滷味，卻令人垂涎欲滴，每樣都想來上一口。早期的東大路與武陵路、鐵道路周邊，是空軍眷村，鄰近空軍聯隊基地，來自大陸各省的眷戶，常會烹煮家鄉味與鄰居分享。揭家第一代老闆揭奶奶1950年代，在眷村開牛肉麵館及滷味店，村裡人待客，習慣到「揭家」切點滷味；第二代揭強中國海專畢業後，原打算跟商船出海，但因身為家中獨子，姊妹們又旅居國外，選擇留在家中照顧父母，也跟著母親學習煮麵、滷牛肉技藝，接手後，天沒亮就得起床，一做也四十多年。「揭家」經典牛肉麵是紅燒口味，基底是以牛骨長時間熬煮成的濃白高湯，加上糖、鹽、醬油、薑、八角等調味料，再將澳洲牛腩滷至軟嫩入味，湯頭看似濃稠，其實爽口，入口滿是牛肉鮮香。店內使用的麵條也十分講究，早年都用眷村鄰居手工揉製、攤車叫賣的麵條，現在改用原供應店家、品質一致的產品，讓開業的好味道至今不變；不吃牛肉的客人也有好選擇：豬骨湯腸麵，這是應當時空軍基地常客的要求而做的，湯頭以豬大骨熬製，配上煮好的麵條及口感Q軟的滷肥腸，愛吃肥腸的人肯定欲罷不能。使用老滷汁烹製的滷味堪稱佐餐良伴，包括：豬頭皮、豬腳、豬腸、豬肚、牛腱、牛肚、牛筋、鴨翅、鴨胗、鴨蛋等，種類豐富，顧客選好喜歡的品項後，老闆娘會幫忙秤重、切盤，滷味直接吃就很美味，也可搭配山東醋、店家自製辣油、蔥白，調配沾醬，後勁十足的辣味，搭純釀山東醋的溫和酸味，嘗起來更加爽口。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/漁香甜不辣/推薦菜色':
            try:
                message = TextSendMessage(
                    text='原味甜不辣、鹽酥甜不辣、綜合飯、牛蒡甜不辣'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/漁香甜不辣/介紹':
            try:
                message = TextSendMessage(
                    text='深受在地人喜愛的「漁香甜不辣」，以新鮮、純正的魚漿原料製作，不加人工添加物，備受消費者肯定。「漁香」已傳承三代，第一代經營者是東門市場內的小魚舖，因每天採購的新鮮魚貨總會剩下一些，不想浪費，開始製作魚漿，沒想到大受好評，後來轉型專賣魚漿，新竹不少小吃店都向他們買魚漿，再自行加工製成其他產品出售。「漁香甜不辣」專賣店原在中央路上，只賣原味甜不辣、鹽酥甜不辣和幾樣冷凍魚漿製品，兩年前遷到大同路現址，室內面積擴大，用餐環境也變寬敞，菜單內容較多元，除了基本魚漿製品，增加飯、麵主食和多款小菜。身為長男的第三代老闆陳昱府，年輕時便知道自己須扛起家業，為了讓家傳的魚漿生意能永續經營，接手後，從甜不辣專賣店起步，講究新鮮與衛生的態度，做出口碑後，轉大同路擴大營業，從店面規劃、裝潢到擬菜單，大小事都親力親為，力求打造出明亮衛生、顧客舒適用餐的空間。招牌甜不辣原料簡單，每日現做，基底魚漿在東門市場一樓的老舖每天現絞，再送到二樓工廠成型，現炸成各式甜不辣；甜不辣有魚棗、魚條、魚餅三種，魚漿中分別加入雞蛋、豬肉、洋蔥，吃得到魚漿的鮮味與彈性，新口味牛蒡甜不辣可以酥炸後當小菜，鹹香滋味加上碎牛蒡的清脆口感，值得一試。佐餐的包餡魚丸湯，魚丸裡加了豬肉、青蔥、荸薺、鹽、糖拌成的餡料，由師傅們以熟練的技術手捏成型後下水烹煮，與高湯一同享用，口味特佳。「漁香」所有產品都不使用多餘人工添加物，因此不耐久煮，為了讓顧客享用最佳口感，每一份都得下單後現煮，如果覺得不過癮，順手帶幾包冷凍魚棗、魚條、魚餅或包餡魚丸，回家DIY，也是不錯的。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/竹樂食堂/推薦菜色':
            try:
                message = TextSendMessage(
                    text='古早味蚵仔煎、烤排骨、紅燒魚皮、黑米糕'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/竹樂食堂/介紹':
            try:
                message = TextSendMessage(
                    text='位於民富國小對面的竹樂食堂，是老牌熱炒店，開店30年來，從不用菜單，如同一般海產店，客人先在門口冰櫃前選擇想吃的生鮮食材，老闆依季節時令來配菜，因此，即便是一樣的生鮮，配的青菜都不一樣。說到竹樂食堂，新竹市老一輩人一定豎起大拇指，創店老闆陳國龍已76歲，他年輕時學廣式、福州料理和酒家菜，曾和友人在大同路開大春餐廳22年，民國76年到西大路開店，以家常熱炒為主，菜色都自行研發，目前已由第二代陳順溢、李靜居接手，不過，陳國龍還親自採買，「食材新鮮，才做得出好料理」。「歷任市長都來過，住附近的柯文哲家人也常來」老闆娘說，來店的熟客多，雖沒菜單，熟客也都信任，像白斬雞、古早味蚵仔煎、烤排骨、紅燒魚皮、黑米糕、土魠魚羹湯等，都是店裡招牌；尤其蚵仔煎、烤排骨點食率最高，這兩道菜食材單純、做法簡單，卻有讓人一吃再吃的魅力。古早味蚵仔煎是將鮮蚵汆燙後，加入青蔥和地瓜粉，入鍋煎至兩面金黃酥脆才上桌，滿滿的蚵仔，咬下去外酥內軟，百吃不厭；烤排骨也只用簡單的調味料醃過，放入200度烤箱中烤20分鐘就完成，肉排軟嫩多汁、還有嚼勁。「我們的料理方式都很簡單，重點在掌握食材的新鮮度」陳順溢說，對食材有信心，才敢放在透明冰櫃讓客人選。竹樂食堂沒有豪氣的裝潢，空間也不大，但消費者仍願意造訪的另一原因是竹樂食堂童叟無欺，價格親民。30年來，從廚房料理到外場服務，全由竹樂食堂家族親力親為，很多食材也是親戚朋友自己栽植的，「清楚食材來源，才吃得安心」老闆娘說，這也是竹樂食堂開店的初衷。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/蔡記燒酒雞/推薦菜色':
            try:
                message = TextSendMessage(
                    text='藥膳燒酒烏骨雞、金錢蝦、里肌糖醋肉、墨魚香腸'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/蔡記燒酒雞/介紹':
            try:
                message = TextSendMessage(
                    text='台灣到處都有燒酒雞，但新竹市「蔡記雞酒燒」這家25年老店，讓人印象特別深刻！店名「雞酒燒」發想自台語「燒酒雞」，老闆蔡思涵故意將店名反著取，看得出他反骨的個性與趣味，反映在菜色設計與創新上，也大不相同。蔡記雞酒燒的店面不大，沒事先訂位，向隅機率很高，雖然價格不便宜，卻經常高朋滿座，原因是蔡思涵比客人嘴刁，自己不吃的也不會給客人吃！他認為，開店不是有得賣、賺錢就好，要有自己的標準，「餐飲業是良心事業，貴也要貴得有道理」。以店裡招牌藥膳燒酒烏骨雞來說，半隻雞要價近千元，硬是比一般燒酒雞貴上許多，原因在於他使用的滷包，除了特別調製的中藥配方，最重要一味是加了一斤上萬元、精磨成粉的冬蟲夏草，光這味成本就不低，但為了讓燒酒雞食補功能發揮到極致，「再貴也省不得」。這道招牌雞湯選用營養價值、口感都屬上乘的烏骨雞，重量也錙銖必較，太小沒份量、口感差，太大肉質過柴、纖維太粗，唯有精選的4斤重，才能完美呈現蔡記招牌。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/阿富魯肉飯/推薦菜色':
            try:
                message = TextSendMessage(
                    text='魯肉飯、摃丸湯、肉羹湯'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/阿富魯肉飯/介紹':
            try:
                message = TextSendMessage(
                    text='深夜時分，城隍廟口前，一家亮著橘黃小燈的攤位上，食客來來往往，燈下混合了蒸氣與香氣的光影，讓夜歸人感受到溫暖，不自覺停坐下來，嘗嘗魯肉飯與肉羹湯。這店是阿富魯肉飯，民國79年，創辦人陳金連女士為了餵飽自己的五個孩子，在當時北部還不盛行魯肉飯時，跟左鄰右舍請教魯肉飯做法，找到廟口一隅，便做起生意，如今成為竹塹城的深夜食堂。「一開始連個招牌都沒有」，不過因為營業到半夜，加上魯肉飯選用的肉塊跟其他魯肉飯店不同，做出特色，也成功打響知名度，幾年後才以孩子名字中的「富」字，取名「阿富魯肉飯」。「阿富魯肉飯」好記又庶民，如今已傳到第二代，由老么邱彥貴和姊姊一起經營；邱彥貴如實傳承了母親堅持的古早味及創業理念：「用最經濟實惠的價格把大家餵飽」，除了口味不變，魯肉飯、筍絲、油豆腐或湯品價格，也都十分親民。他說，廣受青睞的魯肉飯維持母親古法，肉塊肥瘦比約7比3，肥肉選豬的肩頸肉，瘦肉是前腿肉，採兩段式滷製法製成，滷第一次時，先將豬肉、砂糖、鹽、醬油及特製滷包，放入大鍋，加水烹煮約一小時，過程中須不斷攪拌，讓受熱和調味料均勻分布，待肉熟後，蓋上鍋蓋悶半小時；第二次滷時，先把滷汁上油脂瀝掉，再加水攪拌約四十分鐘，滷出來的肉塊，不僅有豬肉的膠質和彈性，且入口即化、粒粒分明，滷肉塊與湯汁淋上白飯，再灑一點中藥房磨製的黑胡椒粉，造就了阿富魯肉飯的美味，每天可賣出6、7百碗。「我和小孩也愛吃魯肉飯，賣給客人的一定是我們自己喜歡吃的。」邱老闆每天一早送小孩上學後，開始備料工作，因為有三家店，一整天要準備8到10鍋的滷肉和小菜食材，再分送到各店面，相當辛苦，不過，當飯菜送上桌，看到客人露出滿足的笑容、讚不絕口時，生活中幸福的醍醐味，也自然散發出來。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
       
        elif mtext == '@小吃/北區/三福麵線/推薦菜色':
            try:
                message = TextSendMessage(
                    text='蚵仔大腸麵線、三福麵線、牛肉麵線'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/三福麵線/介紹':
            try:
                message = TextSendMessage(
                    text='乾淨衛生的環境、舒適自在的氛圍與道地台灣家鄉味，顛覆一般人對傳統小吃的刻板印象，「三福麵線」讓旅人留下深刻印記。在白色為基調的溫馨木質空間，聆聽輕鬆音樂，享受古早味小吃蚵仔大腸麵線，相當療癒，連鴨血、牛肉等食材，也都能加進麵線裡，這份驚豔，讓人發現庶民小吃：麵線的百搭特質。老闆娘在新北市三重長大，這座與繁華台北市僅一橋之隔，許多北上打拚外地人落腳的城市，匯聚眾多中南部引進的南方味小吃攤，麵線攤尤其多，「當時的三重，三兩步就一家麵線攤」，她從三輪車麵線攤吃起，記憶中那是早晚必嘗食物，嫁作新竹媳婦，卻遍尋不著家鄉的麵線味。2008年，老闆娘與友人合資創業，兩個餐飲業門外漢，選擇以成本較低的麵線入手，在城隍廟邊的小店開業，憑藉家庭主婦挑嘴的特質，找到家鄉麵線烹調最佳手法，2013年4月遷店竹光路，因為媒體報導，名氣大增，生意大好，即便下午才營業，主廚卻得清晨開始備料。三福麵線的湯頭色澤特別深，常有客人問為什麼？老闆娘笑笑說，因為「忠於記憶中的家鄉味」。原來，製作湯頭大有學問，老闆娘利用汆燙蚵仔的大鍋湯，加入獨門秘方熬煮而成，保留蚵仔麵線最甜美的原汁原味，絕不加味精，讓人吃得美味又安心。麵線的兩大配角是：蚵仔與大腸，食材的選擇、處理與烹調是大學問。鮮甜飽滿的海蚵，專程到南台灣尋找老字號的養蚵人家，保持海水浸泡宅配，烹煮前才開箱，保留大海天然的鹹甜香，大腸僅以白醬油加少許八角滷製，呈現食材原味。豬大腸的處理更講究，她選用品質保證、當日新鮮的豬大腸，先用大鍋沸水汆燙去血水，再徒手將每條大腸仔細翻面、剪除內層油脂再翻回來，之後用白醬油滷製去味、吹涼、分裝，這麼「厚工」費時，只為讓客人吃到沒有腥味、有著不油不膩嚼勁的豬大腸。麵線雖是庶民小吃，要煮得好吃需要功力。老闆娘說，三福曾被科學園區的工程師封為「麵線界的LV」，能得到這樣的評價，正是店家對自我品質的堅持。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/老店薑母雞/推薦菜色':
            try:
                message = TextSendMessage(
                    text='招牌薑母雞、狀元雞'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/老店薑母雞/介紹':
            try:
                message = TextSendMessage(
                    text='「婆婆做薑母烏骨雞幫我做月子、補身體，因緣際會成就了這家店。」女主人李小珍感性地說出婆媳間感人的互動。老店薑母雞民國92年創店，當初主打「烏骨雞」同業都不看好，認為悖離傳統，沒想到卻異軍突起，創造佳績。「其實，烏骨雞比鴨肉更適合女性，很多顧客都用我們的薑母雞做月子。」李小珍說。薑母雞主要材料是老薑和烏骨雞，老薑搗碎加入中藥材炒香，與炒過的烏骨雞肉做成主湯底，搭配客人點食的各式配料，湯頭愈煮愈甜，而薑的辛辣溶入湯底，增添口感，連老薑本身都變得好吃。店裡用的老薑來自南投縣，烏骨雞則是經檢驗認證的農場長期供應，店裡還張貼了所有材料產地證明，讓顧客吃得安心。目前店裡供應五種湯底：薑母雞、薑母鴨、首烏雞、淮蔘雞、狀元雞，前四種湯底都屬溫補鍋，新開發的狀元雞是養生鍋，以烏骨雞、鮑魚片、茶樹菇、羊肝菌菇等溫補食材為主，因菌菇類有豐富多醣體，適合四季吃或不想吃過燥補鍋、注重養生的顧客選用，所有湯底中，薑母雞點食率最高。李小珍也重視主鍋配料的選材，每天早上6、7點就到市場備料，「新鮮是第一原則」，絕不濫竽充數，也不以多元取勝，不適合補鍋湯底的配料如：茼蒿菜、麻糬燒等火鍋料，因口感不對，都不採用。至於搭配的麵線，則選用有四十餘年歷史的宏廣製麵廠生產的麵線，口感Q滑不軟爛，淋上自製蔥香油和少許豆腐乳沾醬，有獨特的香氣和口感，也是老店薑母雞必嘗的一味。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/鴨肉許/推薦菜色':
            try:
                message = TextSendMessage(
                    text='鴨肉湯麵、炒鴨血、燻鴨肉'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/鴨肉許/介紹':
            try:
                message = TextSendMessage(
                    text='厚實的木砧板上不斷傳來剁鴨肉的低沉咚咚聲，暱稱「二姊」的許美惠剁鴨肉的手沒停過；從小到大，她跟在父親許文河身旁，看著父親剁鴨肉的身影長大。兩代人在鴨肉、砧板刀起刀落間忙碌著，一晃眼就是50年。靠著賣煙燻鴨肉，許文河養大一家人；出身彰化鹿港的他，在新竹最初賣的並非鴨肉，而是家鄉味麵線糊，十幾歲到台北餐廳當學徒，看著師傅烹煮鴨肉的歷程，累積鴨肉料理竅門，再調整口味，最後琢磨出一套煙燻鴨的方法，將煙燻過的鴨肉加到切仔麵裡，當他端出第一碗風味獨特的鴨肉麵時，讓客人驚豔，一炮打響名號，這麵也成了「鴨肉許」獨家招牌菜。熱情好客的許文河以自家姓取店名「鴨肉許」，從最初的推車擺攤，累積出一批死忠顧客，逐漸在新竹闖出名號，中正路開店後更成熱門商店，朋友送了他一塊匾，題名「日理萬鴨」，名副其實；如今「鴨肉許」擁有中正路、北門街與西大路3間店面，分由三個女兒打理，每天平均要賣上百隻鴨子，新竹在地人最愛光顧的，是二姊許美惠掌舵的中正路總店。煙燻鴨肉是「鴨肉許」的主角，衍生出鴨肉湯麵、炒鴨肉麵、鴨肉飯、炒鴨血等料理，煙燻鴨肉的好壞，決定了所有料理的口感；「鴨肉許」選用4∼4.5斤重的土番鴨，這樣大小的鴨肥瘦合宜，有足夠的油脂，皮厚質細，肉纖維不會太粗、太老；鴨隻洗淨、蒸熟後，放入加了甘草等20多種中藥材的滷湯裡浸泡入味，再以白糖煙燻上色增香，可口的煙燻鴨肉於焉完成。可別小看煙燻的每個步驟，正因為以炊蒸取代水煮、用浸泡方式入味，鴨肉肉汁不致流失，口感更顯溫潤，鮮度與甘甜度也大大提升，上菜前再淋灑一匙蒸鴨時收集的原汁，鮮美的味道如畫龍點睛，讓整盤煙燻鴨肉更增餘韻、悠長而濃郁。這樣有滋有味的煙燻鴨，讓人吃起來嘴巴、手指頭滿是煙燻香，鴨肉汁不經意地從嘴裡往指尖流淌，叫人忍不住貪戀地吸吮起來，此刻，「吮指回味」已不只是形容詞，活脫脫成了饕客們賞鴨的美味動詞呀！'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/西市汕頭館/推薦菜色':
            try:
                message = TextSendMessage(
                    text='火鍋、炒沙茶牛肉麵、祖傳特製沙茶醬、牛雜湯'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/西市汕頭館/介紹':
            try:
                message = TextSendMessage(
                    text='從城隍廟口轉到廟旁的西門市場，沿著小巷弄往前走，不仔細找，或許就錯過這家屹立新竹近70年的老字號店家─「西市汕頭館」。從民國38年創立，至今已傳到第四代，店也擴展到3家。走進老店內，馬上聽到熱情招呼聲；雖然過了午餐時間，店內仍有客人，黃家四兄弟家族分工，人人在自己崗位上各司其職，確保品牌的誠信與價值。「西市汕頭館」黃家大哥黃沛峰說，因為父親是校長，從小教導兄弟們一定要和睦互助，不打架、不爭吵、不說髒話，偶而起爭執，也是就事論事，針對食材或營運策略做討論，因此能合作創業迄今，如今他的兒子也開始參與家族事業了。「遵古法」是汕頭館的經營原則，無論食材選擇、料理火候或湯頭，都有一定的堅持，也非全照食譜制式製作，而是以客為尊，依據不同客戶需求、順應潮流，調整口味，目標是永續經營。潮汕料理偏甜，汕頭館配合台灣人的口味做微調，減油、少辣、不加糖，其中，選用新鮮的非冷凍肉，搭配祖傳沙茶醬佐料，不論用在牛肉火鍋、炒沙茶牛肉麵或牛雜湯，都相當可口也是人氣聖品。黃家大哥說，牛肉火鍋的賞味口訣是「肉不離筷、鍋底三秒」，依此口訣，以雙刀法切出來的薄薄蝴蝶狀肉片，在熱湯中，會從鮮紅色轉為淡粉白，入口後，瞬間滿腔軟嫩感與鮮甜香氣。牛雜湯的牛肉選用黏附骨頭上的半筋半肉，加上自製檸檬和獨門香料，熬煮七小時，湯頭看似深濃，嘗來卻清爽，白蘿蔔和牛肉的甘甜融為一體，由於一天僅熬一鍋，是有緣人才嘗得到的私房料理。黃沛峰最享受烹煮菜餚的過程，因為全神貫注，心無旁騖，煩惱盡除；當料理端上桌、得到客人稱讚時，那份成就感，更是不凡！如果你是火鍋或牛肉料理愛好者，路過新竹城隍廟，不妨來西市汕頭館坐坐，嘗一口傳承超過一甲子的鮮滋味吧。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/余家金城廣東粥/推薦菜色':
            try:
                message = TextSendMessage(
                    text='廣東粥、皮蛋瘦肉粥'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/余家金城廣東粥/介紹':
            try:
                message = TextSendMessage(
                    text='在中正路與水田街轉角處，毫不起眼的「余家金城廣東粥」，外觀雖老舊，許多新竹人談到吃粥，多數會想到這家店，好味道讓嘗過的人，不自覺豎起大拇指說：讚！「余家金城廣東粥」開業20多年，老闆余健俊早年學習金門廣東粥的煮食秘訣，飲水思源，以金門縣金城鎮為名創業。金門廣東粥屬廣東「生滾粥」，將米粒煮到不見形體，跟台灣的清粥、鹹粥，粥體粒粒分明不一樣。余家廣東粥煮法是先煮一大鍋粥，顧客訂餐後，從大鍋搯出少量粥到小鍋猛火烹煮，依品項加入新鮮肉類、海鮮或動物內臟等主料，稍微煮開後即關火，「這動作是要保持粥內食材的新鮮度」他說，也確保饕客嘗到鮮嫩香滑粥品，這是生滾粥的特色，也成了余家廣東粥的特色。說到自家廣東粥好吃的秘訣，余健俊謙虛地說：沒甚麼啦！除了料好實在，不偷工減料，最重要是確保高湯鮮美！金城廣東粥的湯底有學問，以甘草、當歸、紅棗等多種中藥材，跟雞骨頭一起燉煮超過三小時，聞起來有淡淡中藥香卻不濃烈，雅而不淡，恰分地增添雞骨高湯的厚度與豐富性。湯底有了靈魂，還得用老米來煮，因為老米澱粉含量多，煮起來能產生更多黏性，此外，老米容易吸附高湯，吃起來自然更入味。獨門的中藥湯底，配上濃稠綿細的米粥與食材的鮮甜，口腔裡填滿了豐美的味道，熱呼呼的，身體都暖了起來。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/北門炸粿/推薦菜色':
            try:
                message = TextSendMessage(
                    text='肉粿、蚵仔嗲、米糕、蒜頭'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/北門炸粿/介紹':
            try:
                message = TextSendMessage(
                    text='城北街的午後是熱鬧的，午茶時間，總開始有人聚湧在一家不起眼的老舊小攤前，短短百來公尺，長長的人龍不時消長，攤前難有清閒，這家店正是高人氣的「北門炸粿」。「北門炸粿」日治時期起家，第一代老闆翁老先生拜師學藝後，推著台車沿街叫賣，至今傳到第四代的翁文芬、陳美麗夫妻，已有百年歷史。說到這味超親民的庶民小吃，早年可是有錢人家才吃得起的高級食物！「北門炸粿」最初只賣肉粿、蚵仔嗲，106年前，豬肉、蚵仔是相當昂貴的食材，也只有上流貴族人家才消費得起；第一代老闆看準北門街上住的多是商賈、望族，選定北門街附近設攤開業。可貴的是，延續一世紀的老滋味，價格卻意外地維持半世紀前的親民，過去是10元，近幾年來物價高漲，老闆才不得已將原本一個銅板價，調漲到每樣12元，真是佛心來著！「北門炸粿」屹立不搖，沒被時代淘汰，憑藉的是紮實的用料與口耳相傳的好口味，店裡的各式炸物，吃起來口感酥脆如餅乾，明明是油炸物卻無油膩感，除了油炸時的火候、時間的精準控制外，外層裹粉上也費了心，選用在來米與黃豆一起磨成漿，才保有酥脆、不易濕軟的咀嚼口感。對於「炸粿」食材的選用，店家處處用心，保留古早味，米糕、芋頭糕全自家製作，不用現成或半成品，招牌炸米糕採用口感Q彈、清新米香的長糯米（秈糯）製作，將長糯米燜煮熟透後，加入二號砂糖調味拌攪均勻，置鐵盤放冰箱降溫定型，隔天拿出來切塊，冰過的米糕口感更Q彈；另一道獨門炸蒜頭，得手工挑選又粗又肥滿的顆粒，將粗的一端切段，再一刀刀切成花，下油炸時，自然開成一朵花！攤位小小的，價錢小小的，口味卻大大的好，走過時代的試煉，這小物成了新竹人從小到大的味覺記憶，也成了遠遊的新竹人，難以忘懷的鄉愁。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/廟口鴨香飯/推薦菜色':
            try:
                message = TextSendMessage(
                    text='鴨香飯、燻鴨切盤、炒鴨血'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/北區/廟口鴨香飯/介紹':
            try:
                message = TextSendMessage(
                    text='2016年以一道鴨香飯入選「竹好呷」，深獲媒體推薦的「廟口鴨香飯」，以鮮明的媽媽Logo與獨門的全鴨料理，擄獲在地人及遠道而來的遊客的心，用餐時段經常一位難求。「小吃店的好味道、餐廳的服務品質」是廟口鴨香飯的經營目標。年輕的第二代李嘉偉談起鴨香飯緣起說，20多年前，媽媽從中山店現址起家，當時經營快炒攤，因緣際會認識一位老師傅，學會鴨肉料理。後來，媽媽在北門街擺攤賣鴨肉麵，因與市場區隔不大，生意不好；李嘉偉從小在店裡長大，每天正餐不外麵或米粉，媽媽偶而會用豬油拌飯給他吃，味道讓他懷念，建議媽媽改賣鴨肉飯，經多次調試口味，賣出口碑，也成就了今天的鴨香飯。店家每天約需處理100∼150隻生鴨，精選皮薄油脂少的新鮮鴨隻，清理乾淨後，全鴨蒸半個小時，稍微放涼，再技術性剖切，塗上一層秘傳醬汁，再加冰糖煙燻3分鐘，「短短3分鐘做兩次煙燻，考驗技術」，必須適時打開鍋蓋讓濃煙散去，去除多餘苦味，第二次燜燻是逼出鴨的香氣，鴨隻金黃色的表皮乍聞是煙燻香，一口咬下卻香嫩多汁，相當迷人。鴨肉的脂肪不同其他動物油，成分很像橄欖油，蒸鴨滴下的鴨油、肉汁湯液等，都是店裡製作醬汁、炒菜的聖品，煙燻過的鴨骨頭更是熬煮湯頭的重要提味精華。一隻鴨從頭到腳、從內到外，無一不能利用，除招牌鴨香飯外，店裡還有炒鴨血、炒鴨腸、炒下水（鴨心、鴨胗、鴨肝）、鴨肉切盤，濃郁香稠的高湯則來自煙燻鴨骨、鴨油等精華，讓顧客回味再三。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='蚵舉壯元',
                                text='0983000960\n新竹市香山區中華路五段322號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@伴手禮/香山區/蚵舉壯元/推薦菜色',
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@伴手禮/香山區/蚵舉壯元/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )    
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/香山區/蚵舉壯元/推薦菜色':
            try:
                message = TextSendMessage(
                    text='招牌烤蚵、私房牛肋條、豆豉鮮蚵飯'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@小吃/香山區/蚵舉壯元/介紹':
            try:
                message = TextSendMessage(
                    text='看似荒涼的台一線省道上，隱藏一處新竹人即使花上大半小時車程也要一嘗的燒烤店：蚵舉壯元，簡單無華的店舖，卻有令人食後發出讚嘆聲的厚實力！店裡招牌烤鮮蚵，來自鄰近自家養蚵場，產地直達餐桌，鮮味全不流失。在新竹香山區美山里的外海，濕地形成了養蚵最佳的天然屏障，香山蚵業全盛時期，台灣北部的蚵仔八成以上來自此地。老闆張小華家族經營鮮蚵批發業已50年，張小華是第三代，夫婦承接事業，長久以來，總有客戶詢問是否能代烤蚵仔？2012年，第四代張皓恩大學畢業了，決定協助家業，在自家蚵田旁設攤，賣起烤鮮蚵，還逐步增加海鮮、肉類與湯品、麵點等燒烤料理，成為省道台一線上最馳名的公路美食。香山蚵仔多「懸掛式」養殖，在蚵殼打洞，用釣魚線串起，懸吊在兩根竹竿之間，放養海中，潮汐影響蚵仔進食時間與數量，約兩年才能採收，比南台灣要多兩倍時間，不過，因蚵場在潮間帶，蚵仔能享受充分日照，還可吃到漲退潮水帶來的新鮮微生物，「天天吃美食」，肉質也較南台灣的紮實彈牙、口感細密，被譽為蚵界的楊貴妃與健美先生。4∼11月是香山蚵產期，採鮮蚵得配合潮汐，蚵農趁退潮採收，經常一下海就是5、6個小時，且蚵場多是軟爛泥，採蚵時大腿深陷泥沼中，得花好幾倍吃奶力氣才能前進。長衫、長褲、手套，都是採蚵基本配備，防曬之外，也避免手腳被鮮蚵銳利邊殼割傷。蚵農看天吃飯，工時長又辛苦，願意投入的年輕人越來越少；所幸，年輕的張皓恩不畏苦，願意在家幫忙，父子聯手，希望帶進年輕人新的創意。目前，他的父母和弟弟負責鮮蚵採收、批發，皓恩負責廚房燒烤，也引入國內外鮮蚵與生蠔供大眾品味，不僅傳承家族養蚵事業，也期望為香山蚵業發展，留下燦爛的一頁。'
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='星巴克新竹州圖門市',
                                text='(03)5228587\n新竹市東區文化街8號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/東區/星巴克新竹州圖門市/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/東區/星巴克新竹州圖門市/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='影咖啡',
                                text='line id: @fru8127g\n新竹市東區金城一路67號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/東區/影咖啡/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/東區/影咖啡/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='河堤上的貓',
                                text='(03)5244189\n新竹市東區民族路33巷68號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/東區/河堤上的貓/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/東區/河堤上的貓/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='墨咖啡',
                                text='(03)5220608\n新竹市東區林森路180號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/東區/墨咖啡/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/東區/墨咖啡/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='安琪拉的魔法屋',
                                text='(03)5637150\n新竹市東區長春街40巷10號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/東區/安琪拉的魔法屋/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/東區/安琪拉的魔法屋/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='本味木瓜牛奶專賣店',
                                text='(03)5235280\n新竹市東區林森路104號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/東區/本味木瓜牛奶專賣店/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/東區/本味木瓜牛奶專賣店/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='直達咖啡',
                                text='(03)6669582\n新竹市東區光復路一段544巷9弄14號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/東區/直達咖啡/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/東區/直達咖啡/介紹',
                                    ),
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/星巴克新竹州圖門市/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '請上星巴克官網查詢'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/星巴克新竹州圖門市/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹州圖書館前身是「新竹街圖書館」，為了紀念1923年日本大正天皇東宮太子裕仁訪問新竹而籌款興建，1925年完成，改為「新竹州圖書館」，台灣光復後由新竹市政府接收，定名為新竹市立圖書館，後又改為「新竹縣立圖書館」作為圖書館使用，民國73年由新光集團取得產權。經過公、私協力保存文化資產的努力之下，109年9月修復完成後的新竹州圖重新開放，配合台灣設計展和110年台灣燈會，展開為期半年的策展活動，展覽結束後已交還新光集團做後續利用規劃。圖書館是一棟洋式建築物，外觀簡潔俐落，立面上的柱子以刻意加強裝飾的磚形條紋，讓建築物顯的穩重，上層則採退縮方式留出陽台，陽台上設計短的梭柱支撐屋樑，使得屋頂變得輕盈，更增添下層立面穩固的對比感。入口處突出的門廊空間，加寬的門柱與上層的中央雙柱，塑造強烈的入口意象。立面上強化的立體柱，配合開窗的虛實變化給人強烈的厚實感。星巴克「新竹州圖書館」門市112年3月30日正式營運，為桃竹苗區首間市定古蹟門市，亦是讓古蹟活化再利用的良好範例。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        
        elif mtext == '@飲料與甜點/東區/影咖啡/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '金磚布丁、可麗露、手沖精品咖啡'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/影咖啡/介紹':
            try:
                message = TextSendMessage(
                    text = '「影咖啡」主打攝影主題與手作甜點，店內每個角落都精心設計，處處可見攝影作品與相機及鏡頭造型的擺飾，極富人文氣息。店主彭枝微從小在新竹南寮長大，喜歡旅行與攝影，求學、就業都未曾離開過這片土地。在科學園區工作7、8年後，倦於一成不變的生活，毅然放下穩定的高薪，到澳洲打工度假兩年，再利用一個月時間走訪紐西蘭，以相機紀錄當地美麗風光，一方面思維未來發展方向。回台後，她做了決定，開設這家結合自己攝影興趣與理想的咖啡館，「所有裝潢、菜單，自己規劃設計。」加上分別是專業攝影師及飯店主廚的兩個弟弟協助，整家店的風格概念完整，餐點也具一定品質。為了創業，彭枝微從頭學習相關專業課程，並考取咖啡師國際證照；店裡除了提供義式濃縮咖啡為基底沖泡出來的各種花式咖啡，還有手沖精品咖啡，選用的咖啡豆，是向世界盃咖啡大師台灣區冠軍的達人簡嘉程採購，由她自己研磨、手沖，表現不同產地咖啡豆的個別風味。影咖啡的所有甜點，都搭配自製香草糖製作，每種甜點都帶有淡淡甜香的香草味，招牌甜品像：金磚布丁、可麗露、檸檬塔、季節水果塔、檸檬生乳酪蛋糕、起司條等，經常中午剛過就售罄。其中，獲選2016年竹好呷網路票選第一名伴手禮的金磚布丁，以類似鳳梨酥的酥皮，搭配雞蛋、牛奶、香草糖製作的內餡一起烘烤，人氣超旺；「我花費一年多時間試做、調整火侯才成功。」她說，用心做出來的成品，外皮金黃酥脆、布丁內餡又不過熟，出爐後還需冷凍定型一晚才能脫模，因為純手工製作，數量有限，訂單已排到兩、三個月之後。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/河堤上的貓/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '咪‧咕嚕嚕、黑森林奶茶'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/河堤上的貓/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹限定的手搖飲店，是舊城區護城河畔的「河堤上的貓」，這家兩名年輕女子創業的店，從老闆到店面設計與飲品，充滿文青風，是新竹排隊名店，不僅是年輕學子成長的共同記憶，票房破億的《我的少女時代》，也特來取景。2006年，兩名當時26歲的年輕女孩，攜手創立這家小店，說起開店的歷程，仍漾著青春朝氣的陳穎瑩與郭乃菁說，最初懷抱著幫朋友圓夢的想法，天真創業，可兩人毫無餐飲經驗，又沒家人奧援，一路跌跌撞撞，相當辛苦，「曾多次想放棄」，後來遇到了一隻流浪貓「啵布」，牠離奇的求生過程，激勵了兩人，重新思考再出發，成就了「河堤上的貓」。手搖飲料已成國民飲品，新店一家家開，為了區隔，兩人對飲品命名特別花心思，「啵布」提供不少靈感，店裡招牌飲品是以特調奶茶為基底，加入大、小珍珠與綠豆的「咪‧咕嚕嚕」就挺富巧思，陳穎瑩說，貓咪在接受主人安撫時會抬頭發出「咕嚕嚕」的聲音，就像喝完了奶茶，也發出「咕嚕嚕」般幸福滿足的聲音一樣；曾經有客人問：為什麼取這麼抽象的名字呢？旁人逗趣回應，這是咒語喔！喝之前要先唸「咪‧咕嚕嚕」，飲料才好喝。店裡的招牌還有「小方塊綠奶茶」、「玉荷冰茶」等，都巧妙利用珍珠口感的QQ小方塊及特調綠茶，一新茶飲控的味覺經驗，口味清爽。11年了，客人來來去去，河堤上的貓已不單純是間茶飲小店，反而容納了所有曾經路過品嘗茶飲的人們的情感；「店雖小，卻滿是客人生活日常的印記，這是河堤上的貓最有價值的地方。」曾經，有熟客在店前拍婚紗，且預約店家飲品當做婚宴飲料；曾經，有人為她們送上麵包，表達謝意；曾經，有研究生在畢業論文首頁，標示感謝文.........，儘管細微，卻都是支持她們繼續前進的動力；「我們會繼續在一起，和消費者、員工，創造更多美好的回憶。」'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/墨咖啡/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '義式咖啡、單品咖啡、手作甜點（檸檬系列、核桃布朗尼）'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/墨咖啡/介紹':
            try:
                message = TextSendMessage(
                    text = '簡約文青風的墨咖啡，是許多新竹人嘗手作點心與品咖啡的最愛名店，2樓小酒館，更是熱愛世界手工精釀啤酒者朝聖之地。10年咖啡館資歷的老闆周義翔，早在學生時代就到咖啡館吧台打工，對咖啡深深著迷，也立志成為專業的咖啡人；因為長期在咖啡館工作，了解咖啡館經營的辛酸與苦樂，熟悉咖啡館經營管理的Know-how，圓熟了創設「墨咖啡」的實力。墨咖啡明亮寬敞的空間，洋溢著濃濃的書卷香，1樓是北歐簡約風的咖啡天地，2樓淡雅和風的精緻小酒館，周義翔說，因為弟弟喜歡品酒，利用2樓空間規劃一處供應世界各國手工精釀啤酒的專門店，讓咖啡館意外多了份微醺的選擇。來這裡，除了品飲義式或頂級單品咖啡，不妨嘗嘗手工製作的糕點，滿足苦與甜之間，味蕾交織對應的滋味；店家推薦檸檬系列手作甜點：檸檬生乳酪蛋糕、檸檬塔，主廚重視原物料的新鮮與品質，選用法國奶油與CreamCheese，製作耗時，出爐的檸檬起司香，令人陶醉；另一款招牌是核桃布朗尼，選用法國與厄瓜多的巧克力製作，滿滿的核桃香氣搭巧克力的苦甜滋味，是巧克力嗜食者首選。「墨咖啡也是新竹文創者交流平台！」周義翔說，咖啡館向來是文人雅士聚會場所，台北不少咖啡館也常變成文創工作者匯聚的地方，墨咖啡有相同的期許，店裡不定期舉辦藝文交流與座談，間或展售文創商品，讓咖啡館增添了文藝風。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/安琪拉的魔法屋/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '反轉焦糖蘋果蛋糕、巧克力雪山頂、栗南瓜起司蛋糕'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/安琪拉的魔法屋/介紹':
            try:
                message = TextSendMessage(
                    text = '美味的甜點一如戀人，散發獨到的魅力，引誘著蠢蠢欲動的味蕾，撫慰人心。「安琪拉的魔法屋」在長春街的僻靜巷弄間，前院是一處多肉植栽構成的小小綠色森林花園，造訪時，斑駁木門裡，已飄出陣陣烘烤餅乾和蛋糕的暖香。熱愛藝術、大膽追求人生價值的魔法屋主人安琪拉，捨棄竹科新貴的工作，花了1年時間拜師學藝，從學徒到主廚，歷經篳路藍縷的艱辛與繁盛枝葉的美好，如今已在糕餅界擁有一席之地，充滿創意的糕點更獨樹一格。安琪拉重視生態保育，食材選用堅持土地與人互相依存的生態關係，除了起司從國外進口外，多數採用台灣在地食材，尤其青睞對環境友善、不施農藥小農栽植的有機作物，烘焙過程中，也流露她對料理的堅持與用心，焦糖蘋果蛋糕剛好使用一顆至少300公克重的蘋果，奶油炒香的焦糖和微酸的蘋果結合，加了杏仁粉和蘭姆酒的蛋糕主體，值得一嘗。安琪拉獨創各式曼妙滋味的手工蛋糕，還有備受喜愛的手工餅乾，詢問度超高，一款外國人稱之為ChocolateCrinkleCookies，國人稱巧克力雪球的餅乾，安琪拉稱之為冬季限定版「巧克力雪山頂」，第一口咬嚼時覺得不像餅乾，僅手掌大，裡面深藏蛋糕般酥軟的口感，每顆都像下過雪的山頂造型，還有美美的山峰裂紋，配上一壺好茶或咖啡，幸福滿滿！安琪拉還有許多經典餅乾，希臘雪球、寶石果醬、蔓越莓核桃燕麥等，都是熱門品項，經常出爐沒多久就賣光，自嘲喜歡撿拾、收藏老東西的安琪拉，店裡盡是她多年的珍藏與藝術品；她也喜愛各國雜貨，從鄉村風廚具到負盛名的手繪盤具組，都能讓旅人像尋寶般處處驚豔。卸下繁複的應對及招呼，沉浸在無菜單料理的美味中，大飽朵頤後再來一片招牌起司蛋糕和濃郁香醇的熱咖啡，在忙碌中細品人生。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/本味木瓜牛奶專賣店/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '木瓜牛奶、現榨蔬果汁、綠豆沙'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/本味木瓜牛奶專賣店/介紹':
            try:
                message = TextSendMessage(
                    text = '簡樸的門面，非觀光人潮熱點，能屹立40多年，憑藉的是紮實的工序與用心，逐步建立起消費者綿長的味蕾記憶。「我們服務正港新竹在地人，外地客也多是新竹人G-來的。」牆上巨幅的老照片，顯現「本味」的老字號，從現址對面的路邊攤賣甘蔗汁起家，隨著60年代台灣經濟起飛，漸漸更換產品品項，改賣新鮮現打果汁，並以鮮奶取代煉乳，成為明星招牌的木瓜牛奶專賣店。不以花俏擺飾製造視覺效果，全靠真材實料，不加太多的水或其他添加物，單純以滿滿份量的水果，端出本味十足用心的誠意。第二代的柯老闆自信地說，自家產品與別人不同之處，就是呈現單一水果「本味」的果汁，而非果汁水，不靠其他水果提味，口感就夠濃醇香。他以「兩個小孩喝一杯500C.C.的草莓牛奶，不用1分鐘」來形容自家果汁厲害之處，好喝到完全停不住，一口喝完，來不及外帶回家！要呈現水果最單純原始的味道，對於主角—水果的挑選自然不得馬虎，使用新鮮、熟度剛剛好的水果，才能呈現出果香鮮甜的滋味。因此，本味的食材都是從產地直批，嚴選自屏東的木瓜，大小重量完全憑經驗精確判斷，果肉甜度高，香氣濃，也因此招牌「木瓜牛奶」自然是濃稠香醇。除了人氣商品木瓜牛奶，還有依季節輪替的新鮮飲品：冬天的草莓牛奶、柳丁汁，夏天就是芒果汁、酪梨牛奶、西瓜汁以及綜合蔬果汁。客製化私房果汁，隨顧客需求搭配，製作專屬的黃金比例，完全不加一滴水，貼心的服務每一位老顧客。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/直達咖啡/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '咖啡豆、手沖咖啡、流淚鬆餅'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/東區/直達咖啡/介紹':
            try:
                message = TextSendMessage(
                    text = '「接軌國際，新鮮直達」是直達咖啡最初命名的初衷。直達，有著直接、公平與正義的意涵，也正是直達咖啡經營的核心價值。老闆劉得煒神采奕奕地說：「我們不想做複雜的事，讓主角來說話。」這裡的主角，指的就是「咖啡豆」，「煒哥」是多數咖友的暱稱，他經營咖啡館的理念、方向，與坊間咖啡館大不同，把咖啡當成新鮮食材，自然樸質的概念，將高品質的豆子分享給好友，是直達創業的最高目標。早年，台灣咖啡館流行進口深烘焙的咖啡豆，一般人對咖啡的認知也停留在深焙豆的焦苦味，直達開業後強調淺焙豆，營運初期，多數人對淺焙新鮮咖啡豆沖泡出來略帶酸度的咖啡，還無法接受，煒哥不厭其煩解說，花了好一番時日，加上近幾年全球咖啡飲品潮流翻轉，透過網路資訊推播，咖友才逐漸瞭解新鮮咖啡豆的原始好滋味，「能喝酸咖啡才能喝到好咖啡」，這是他常說的一句話。「好咖啡需要緩緩品味」，煒哥希望客人到直達咖啡，能放慢速度，慢慢喝一杯好咖啡，也透過「慢」來找到合於自己品味的專屬咖啡，體會咖啡的美好。對於首次來店客，工作人員會不厭其煩地詢問客人對於香、甘、酸、醇、苦等滋味的喜好，為客人挑選一支專屬的豆子，如此嚴謹的態度，對應了老闆的堅持：「咖啡豆與人，是我們的兩大資產。」煒哥認為，台灣咖啡市場已逐漸走向精品咖啡豆的趨勢，過去，一般人對咖啡豆的要求，並不在意「新鮮」與否，如今，嗜咖啡者卻百般挑惕，追求新鮮、莊園、精品豆；不過，精品咖啡種類繁多，初入門者往往目不暇給，他特別推薦帶有洋甘菊香與薄荷清涼的衣索比亞耶加雪夫水洗豆，是最佳入門豆。直達咖啡經營目標不侷限在咖啡豆的販售，煒哥期望拉高國人對咖啡的正確認知；兩年前開始造訪荷蘭、日本等優質豆商，相互交流，也親自到法屬留尼旺島拜訪世界最稀有、頂級「尖波旁豆」的農家，「希望把世界各地的好豆引進台灣」。不斷汲引新知是煒哥團隊的特質，他們以「聽懂、明白、簡單、熱情、相信」10個字，定義2017年的直達，同時啟動校園巡迴演講，將從新竹起步，擴及全國，把國際咖啡界最新、最正確的知識與技術，用簡單聽得懂的話，傳遞給咖啡愛好者與年輕人。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='薪石窯柴燒窯烤',
                                text='(03)5720073\n新竹市東區水利路46巷67-3號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@餐廳/東區/薪石窯柴燒窯烤/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@餐廳/東區/薪石窯柴燒窯烤/介紹',
                                    ),
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/東區/薪石窯柴燒窯烤/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '手工窯烤麵包、蜜橘吐司、窯烤南瓜燉飯、鳳梨酥'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/東區/薪石窯柴燒窯烤/介紹':
            try:
                message = TextSendMessage(
                    text = '中午時分，陣陣烘烤麵糰與pizza的香氣，隨著木材炙燒的熱度與聲響，從門前一座紅磚砌成的柴窯口，溢傳出來；這時的店裡早已賓客盈門。以窯烤麵包馳名的「薪石窯」，座落在稻田包圍的尋常農村巷弄裡，距離市中心區有些距離，卻阻擋不了千里尋香的饕客。老闆娘戴慧欣喜愛烘焙，也樂於將自己手作麵包點心，分送給鄰里鄉親品嘗；在一次法國旅行中，看到一家特別的店，使用石窯烘焙麵包，那份特殊的香氣與口感，縈繞迄今，念念不忘。回國後，萌生了開店的念頭；正好，一位麵包師傅從越南帶回法國殖民時期遺留下來的石窯模型，跟原本經營建築業的先生許禮瑩一起研究，依著模型，打造一口「新老窯」，也開啟了「薪石窯」的美食天地。「這口窯是台灣目前唯一雙層窯」，許禮瑩驕傲地說，也是這家店的主角，坊間的柴窯，烤室與燒材的地方多半在同一層，薪石窯特殊之處，是烤室與燒柴處各作一層，這樣的設計可以使窯內溫度保持均勻，讓食材完整受熱，烘烤出更美味的料理。薪石窯主夫妻都重視自然養生，店裡選用的食材，也多是台灣友善土地或有機無毒的在地農作，像拉拉山的水蜜桃、梨山蜜蘋果、萬丹紅豆、新竹茂谷柑等，巧妙的運用在麵包、糕點或窯燒料理中，透過這些在地小農的食材，以最實惠的價格，讓每位顧客都能享受到「大地的食物，自然的味道。」薪石窯除了現烤的招牌麵包與pizza外，還創新設計了窯烤美食，德國豬腳、客家鹹豬肉分享餐，粗獷豬肋排、魚肚肉條、栗子雞肉飯、南瓜燉飯等，都教賓客吮指叫好，現場還提供親子DIY烘焙體驗課程，目前開放Pizza、鳳梨酥、紅豆麵包等課程，「期待透過DIY，一方面增進賓客親子間情誼，也跟薪石窯有更深刻的情意連結。」夫妻倆真心的說。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='光華冰果店',
                                text='(03)5322318\n新竹市北區光華東街35號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@飲料與甜點/北區/光華冰果店/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@飲料與甜點/北區/光華冰果店/介紹',
                                    ),
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/北區/光華冰果店/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '綜合冰、四果湯、銀耳蓮子湯'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/北區/光華冰果店/介紹':
            try:
                message = TextSendMessage(
                    text = '在許多新竹人心中，「光華」是記憶中陪伴成長的一家老冰菓室，老闆張琮和說：「很多客人學生時期開始光顧，結婚、生子、甚至到外地打拚多年後，還會攜家帶眷回來，回味年輕時代的滋味！」店家始終如一的執著與堅持，讓純粹的「老」味道，牽動外地遊子的心。藥劑師轉行的老闆張琮和，以頂真的態度和不斷研發創新的精神，認真處理每一道冰品的工序，例如：用熱「悶」法讓每樣食材達到恰如其分的口感，像紅豆以快鍋煮熟，悶30分鐘後立即加糖，讓粒粒紅豆入味，綠豆煮半熟即關火靜悶，讓綠豆保留完整外貌，口感綿密；看似簡單的糖水，竟結合兩種糖，加上繁複工序，首先將二號砂糖炒出蔗糖香氣，加入較甜的白糖拌炒，交融出香、味兼具的糖水.....，種種好吃的食材，全憑高度實驗精神累積出經驗值，讓光華的甜品味道了得。除了對食材用料的執著，冰果店品飲空間也絲毫不馬虎，雖是40年老店，裝潢設計依然新意盎然；「做一行得像一行」，張琮和認真地說，為了給客人舒適的飲品環境，幾乎每兩年店內裝潢都重新整修，讓客人保有新鮮感。凡事都愛嘗試的張老闆，空間設計也不假他人，巧妙利用鏡子返照與透視，營造出寬敞的空間感，連牆上馬賽克的拼貼也獨到，呈現他理想中的質感。張琮和慎選食材，且不限定產地或品種，全依季節時令挑選出最優質、最合宜的食材來製作，發揮當令食材的特性，也因為堅持所有配料當天熬煮製作，每一款冰品甜湯，都具絕佳口感與風味，讓客人感受老冰菓室的心意。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/北區':
            try:
                message = TextSendMessage(
                    text = '這個區域沒有您想要查詢的資料'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@飲料與甜點/香山區':
            try:
                message = TextSendMessage(
                    text = '這個區域沒有您想要查詢的資料'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='食物',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='Luau•pizza柴寮披薩',
                                text='0908502903\n新竹市香山區元培街323巷5號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@餐廳/香山區/Luau•pizza柴寮披薩/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@餐廳/香山區/Luau•pizza柴寮披薩/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='古今車用中蔬食餐廳',
                                text='(03)5182615\n新竹市香山區南湖路215巷255弄115號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@餐廳/香山區/古今車用中蔬食餐廳/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@餐廳/香山區/古今車用中蔬食餐廳/介紹',
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='天香海鮮店',
                                text='(03)5387537\n新竹市香山區延平路二段1584號',
                                actions=[
                                    MessageTemplateAction(
                                        label='推薦菜色',
                                        text='@餐廳/香山區/天香海鮮店/推薦菜色'
                                    ),
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@餐廳/香山區/天香海鮮店/介紹',
                                    ),
                                ]
                            )
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/香山區/Luau•pizza柴寮披薩/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '驕傲的咖哩(PIZZA)、季節限定PIZZA'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/香山區/Luau•pizza柴寮披薩/介紹':
            try:
                message = TextSendMessage(
                    text = 'Luau，是夏威夷原住民語，意指在花叢草坪上的微醺PARTY，「我希望來到Luau的朋友，都能像在花園裡開派對般的悠然、隨性。」老闆波哥對Luau柴寮披薩店有這樣的期許；從環境到餐點，Luau的確是一處能夠放鬆、發呆與自在、悠遊的休閒空間。波哥是土生土長的新竹人，原從事服裝設計，長年海內外打拚，10多年前退休返鄉，在香山這塊坡地實踐理想，波哥對自己的退休生活設定，越簡單越好、自在享受手作的細節；他把數十年的人生閱歷與藝術修為，落實在這座自然樸質又生氣盎然的世外桃源。園區廣達1700多坪，餐廳所在地原是頹圮的老合院建築，後院小山坡居高臨下，保留自然原始生態，閒逛間還能找到農家鑿取的10多口古井，開發這片園區時，波哥秉持不增加環境負擔，盡量就地取材、廢物利用的原則，處處可見巧思。園區散置許多深具歷史價值的老東西，例如城隍廟附近撿拾的上百年磚瓦、刻有昭和3年字樣的火車站木條座椅、廟宇龍柱的石珠等，他還會木工，店裡有他製作的龍眼木貴妃座椅、相思木材質的三張「客雅溪」概念方桌、洗衣板餐盤……等，柴窯造型與屋牆顏彩也都跳脫一般人的想像，玩出洋溢著摩洛哥、印度等異國風情的隨興空間。他也愛園藝，整年都可見花開─2月滿牆鮮橘炮仗花、3月底4月初爬滿藤架的紫藤、夏日是盛開的千曲花⋯⋯，與顏彩強烈的建築物輝映得繽紛多彩。除了空間引人入勝，Luau的餐點也好。波哥愛吃，探訪各地特色小農，友善土地供應的食材，也尊重時令蔬果，巧妙融入菜單中；純手工窯烤PIZZA，從基本款的瑪格麗特、夏威夷、咖哩牛肉，到季節限定的紫環貝（3∼10月）、鎖管（5∼6月），還有新竹老總舖師製作燒賣時會用到的霜蝦（12∼翌年2月）等，都是絕美鮮味，水果披薩也是一絕，鳳梨、釋迦、榴槤、芒果皆可入味。在繁花盛開季節，還可能巧遇紫藤入味的甜品呢。Luau招牌菜是「發呆的雞」、「衝浪的紫環貝」，原生老品種小絲瓜、老欉芒果派，都教人驚豔。「發呆的雞」加了檸檬葉、月桂葉、洋蔥、義大利綜合香料，先蒸熟，再入烤箱微烤，保有雞肉的甜汁，口味絕佳；「衝浪的紫環貝」披薩，每只貝都張開口，像衝浪般，饒富趣味，特製的美牛頂級「厚切勒眼」，鮮嫩可口都教人回味。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/香山區/古今車用中蔬食餐廳/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '三杯猴菇豆腐煲、雲南米線、藥膳養生火鍋'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/香山區/古今車用中蔬食餐廳/介紹':
            try:
                message = TextSendMessage(
                    text = '「古今車用中蔬食餐廳」坐落於與新竹縣寶山鄉接壤處，佔地22甲，晴天時，藍天白雲襯托四周青翠山丘，景色宜人。「古今車用中」店名取自《道德經》「執古之道，以御今之有。」與《中庸》「執其兩端，用其中於民。」的兩段話，加上店裡展示的五台經典古董車，將傳統經典名句與工業發展的極致產品混搭，具濃厚的後現代精神。餐廳建築外觀採東方灰瓦白牆風，內部空間則洋溢著地中海度假氛圍，刷白牆面、洗石子地板配上靛藍天花板、座椅與歐風窗櫺，中央吧台則以天然石塊妝點，營造出自然優美的用餐環境。餐廳2015年開業，由一群志同道合的朋友共同經營，推廣健康蔬食，店內一角掛著古今各國吃素名人的相片，還自栽無毒、有機的各種時令蔬菜，用在餐飲上，實踐「產地到餐桌」的理想。用餐採半自助式，有焗烤、火鍋、義大利麵、砂鍋煲、石鍋拌飯、烏龍麵、披薩等選擇，不少特殊食材、調味料都從海外帶回台灣，交廚房師傅或義工烹煮。招牌三杯猴菇豆腐煲選用產自中國的乾燥猴頭菇，以清水浸泡數天後，加入杏鮑菇、香菇、油豆腐、薑片、九層塔、辣椒等熱炒，口感厚實的猴頭菇吸入鹹甜濃香的醬汁，非常下飯，另外，搭配蕃茄、味噌、起司、肉骨茶等特色湯底的各式火鍋也值得一試，附上白飯、自製沙茶醬及時蔬、菇類、豆腐、蒟蒻、南瓜等食材組成的豐富配料盤，也是絕佳選擇。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/香山區/天香海鮮店/推薦菜色':
            try:
                message = TextSendMessage(
                    text = '墨魚香腸、烤二層肉、炸軟絲'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif mtext == '@餐廳/香山區/天香海鮮店/介紹':
            try:
                message = TextSendMessage(
                    text = '這間店簡單得只剩下美味。天香海鮮店老闆陳清文有如鄉間隱士，在市郊開店，不汲於富貴，開店做菜信手拈來寫意自如；客人進門後沒多餘招呼，轉身走進廚房，一晃眼，桌上就是六菜一湯。一般海鮮店有的這裡都有，海鮮店沒有的這裡也有：墨魚香腸、田雞肚、二層肉，許多人是初次遇見。天香海鮮店民國67年由陳清文的母親創立，一開始只是小小麵攤，生意越做越好，規模逐漸擴大。讀電子科的陳清文壓根兒沒想過自己會走這一行，「小時候看到客人就躲」。正所謂無心插柳柳成蔭，退伍後接下棒子，一做20多年，「比媽媽經營得還久」，餐桌也從12桌增加到24桌。墨魚香腸可謂「海鮮版」香腸，由墨魚、花枝漿、花枝肉組成，鮮而不膩；田雞肚則是田雞呼吸的氣囊，外型小巧，嚼勁脆口；最特別莫過於二層肉，取豬小排最上面部位，也就是俗稱三層肉中間那一層，每隻豬身上僅能取出幾百公克，數量極少，外觀像松阪豬，口感卻大不同，松阪豬肉軟，二層肉較脆，烤二層肉是人氣招牌菜，口感特殊，當有人稱讚這道菜特別，陳清文一臉淡定說，「我小時候媽媽就做過了」。說到料理海鮮的秘訣，陳清文直言全無技巧，只有「新鮮」二字訣。每天早上6、7點到新竹魚市場採購，那裡魚貨多元，有新竹當地，也有基隆、甚至空運來的。新鮮二字訣也貫徹到餐廳經營，「我們沒有菜單，今天什麼新鮮就出那幾樣，我不喜歡被菜單綁住。」秉持原味，不亂加多餘調味，陳清文的料理如人，簡單直率。咬一口海鮮，大自然的原味綻開齒間，在情感通膨的現代更顯美味。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif  mtext == '@歷史建築/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹驛—新竹火車站',
                                text='新竹市東區中華路二段445號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/新竹驛—新竹火車站/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='迎曦門',
                                text='新竹市東區東門街中正路交叉口',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/迎曦門/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='護城河',
                                text='新竹市東區林森路至世界街口',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/護城河/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='辛志平校長故居',
                                text='新竹市東區東門街32號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/辛志平校長故居/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='國立新竹高中劍道館',
                                text='新竹市東區學府路36號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/國立新竹高中劍道館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='台灣菸酒公司新竹營業所',
                                text='新竹市東區東門街59號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/台灣菸酒公司新竹營業所/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='孔廟',
                                text='新竹市東區新竹公園',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/孔廟/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='李克承博士故居',
                                text='新竹市東區勝利路199號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/東區/李克承博士故居/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@歷史建築/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹州廳—新竹市政府',
                                text='新竹市北區中正路120號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/北區/新竹州廳—新竹市政府/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@歷史建築/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='香山火車站',
                                text='新竹市香山區中華路5段349巷2弄7號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@歷史建築/香山區/香山火車站/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@自然景觀/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='青草湖',
                                text='新竹市東區明湖路775巷',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/東區/青草湖/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@自然景觀/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='十七公里海岸線',
                                text='東西向快速道路西端終點附近，頭前溪橋出海口',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/北區/十七公里海岸線/介紹'
                                    )
                                ]
                            ),
                             CarouselColumn(
                                title='魚鱗天梯',
                                text='新竹市北區南寮漁港臨海處',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/北區/魚鱗天梯/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif  mtext == '@自然景觀/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='青青草原',
                                text='新竹市香山區元培街往香山中學方向（沿路有標示）',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/青青草原/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='青青草原溜滑梯',
                                text='新竹市香山區草原路青青草原入口處',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/青青草原溜滑梯/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='香山濕地',
                                text='新竹市香山區西濱快速道路風情海岸',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/香山濕地/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='金城湖賞鳥區',
                                text='新竹市香山區海埔路右轉直行可抵金城橋',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/金城湖賞鳥區/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='朝山陸橋',
                                text='新竹市香山區朝山里西濱公路（台61線）80公里處',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/朝山陸橋/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='海山漁港',
                                text='新竹市香山區海山里西濱公路旁',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/海山漁港/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='賞蟹步道',
                                text='新竹市香山區中華路五段320巷55-1號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/賞蟹步道/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='南港賞鳥區',
                                text='從西濱快速道路84.1公里處轉往海邊方向',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/南港賞鳥區/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='十七公里南港站',
                                text='從西濱快速道路84.1公里處轉往海邊方向',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@自然景觀/香山區/十七公里南港站/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@宗教文化/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='關帝廟',
                                text='新竹市東區關帝里南門街109-1號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/東區/關帝廟/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='竹蓮寺',
                                text='新竹市東區竹蓮街100號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/東區/竹蓮寺/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='普天宮',
                                text='新竹市東區高峰路306巷66號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/東區/普天宮/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='開台金山寺',
                                text='新竹市東區仙水里金山201號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/東區/開台金山寺/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@宗教文化/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='都城隍廟',
                                text='新竹市北區中山路75號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/北區/都城隍廟/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='外媽祖長和宮',
                                text='新竹市北區北門街135號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/北區/外媽祖長和宮/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='水仙宮',
                                text='新竹市北區中山路75號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/北區/水仙宮/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='天公壇',
                                text='新竹市北區中山路431巷36號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/北區/天公壇/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='北大教堂',
                                text='新竹市北區中正路156號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/北區/北大教堂/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@宗教文化/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='香山天后宮',
                                text='新竹市香山區中華路五段420巷191號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@宗教文化/香山區/香山天后宮/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@博物館/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹市美術館',
                                text='新竹市東區中央路116號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/東區/新竹市美術館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='影像博物館',
                                text='新竹市東區中正路65號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/東區/影像博物館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='玻璃工藝博物館',
                                text='新竹市東區東大路一段2號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/東區/玻璃工藝博物館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='科學園區探索館',
                                text='新竹市東區科技五路1號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/東區/科學園區探索館/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@博物館/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='消防博物館',
                                text='新竹市北區中山路4號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/北區/消防博物館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='新竹生活美學館',
                                text='新竹市北區武昌街110號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/北區/新竹生活美學館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='新竹眷村博物館',
                                text='新竹市北區東大路二段105號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/北區/新竹眷村博物館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='黑蝙蝠中隊文物陳列館',
                                text='新竹市北區東大路二段16號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/北區/黑蝙蝠中隊文物陳列館/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='康樂農村文物陳列館與輕便車道',
                                text='新竹市北區東大路三段335巷31號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/北區/康樂農村文物陳列館與輕便車道/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@博物館/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='春池觀光玻璃工廠',
                                text='新竹市香山區牛埔南路372號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@博物館/香山區/春池觀光玻璃工廠/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@公園與休閒區/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='高峰植物園',
                                text='新竹市東區寶山路仙宮里9鄰',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/東區/高峰植物園/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='新竹公園',
                                text='新竹市東區東大路一段2號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/東區/新竹公園/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='新竹市立動物園',
                                text='新竹市東區博愛街111號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/東區/新竹市立動物園/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='中央公園',
                                text='新竹市東區東大路與中央路口',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/東區/中央公園/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='新竹鐵道藝術村',
                                text='新竹市東區花園街64號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/東區/新竹鐵道藝術村/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='隆恩圳',
                                text='新竹市東區沿三民路自民主路至東大路段',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/東區/隆恩圳/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@公園與休閒區/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹漁港',
                                text='新竹市北區頭前溪出海口南側',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/北區/新竹漁港/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='槺榔驛',
                                text='新竹市北區東大路三段430巷23號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/北區/槺榔驛/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='新竹綠園道',
                                text='新竹市北區沿經國路自民主路至東大路段',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/北區/新竹綠園道/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='東大飛行公園',
                                text='新竹市北區東大路二段16號旁',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/北區/東大飛行公園/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='樹林頭公園',
                                text='新竹市北區東大路二段544-594號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/北區/樹林頭公園/介紹'
                                    )
                                ]
                            ),
                            CarouselColumn(
                                title='南寮旅服中心',
                                text='新竹市北區南寮街261號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/北區/南寮旅服中心/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@公園與休閒區/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='港南運河公園',
                                text='新竹市香山區海埔路600號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@公園與休閒區/香山區/港南運河公園/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@市區景點/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='東門市場',
                                text='新竹市東區大同路86號',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@市區景點/東區/東門市場/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif  mtext == '@市區景點/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='景點',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='北門大街',
                                text='新竹市北區北大路與中山路之間',
                                actions=[
                                    MessageTemplateAction(
                                        label='介紹',
                                        text='@市區景點/北區/北門大街/介紹'
                                    )
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@市區景點/香山區':
            try:
                message = TextSendMessage(
                    text = '這個區域沒有您想要查詢的資料'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/新竹驛—新竹火車站/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹百年老車站建於1913年，由留學德國的日本人松ケ崎萬長設計，是一座混合式的西洋建築，新竹驛呈現德國近代建築風采，主要採德式歌德建築元素，但也具有部分巴洛克建築風格，迥異於同時期其他官廳建築，是鐵道建築中的經典。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/迎曦門/介紹':
            try:
                message = TextSendMessage(
                    text = '迎曦門（東門城）是竹塹城僅存的城樓，為國定古蹟。迎曦門城樓下段稱為城座，以條形花崗石石塊疊砌而成，城門洞為圓拱形，是城市的出入口；上層城樓原為木構造建築，現已改為混泥土造，城樓結構共二十四根立柱，屋頂部分為歇山重簷式構造，屋脊的起翹短而有力，以顯示威武的氣氛，城門前豎有石碑一座，為竹塹築成歷史的紀錄，城門前的廣場又稱「新竹之心」，為一個結合傳統與現代科技的市民廣場，是新竹文化的象徵地標。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/護城河/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹市護城河從火車站經東門城到世界街，全長約800公尺，寬約56公尺的護城河是台灣僅存城門與護城河原址保留的珍貴歷史風貌，河畔周邊充滿人文氣息，與舒適的綠意步道，沿著河畔可漫遊市區欣賞日據時期古建築群。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/辛志平校長故居/介紹':
            try:
                message = TextSendMessage(
                    text = '辛志平為新竹中學校長，校長故居是日式建築，建築四周圍繞著庭園，有著日本大正中期官舍和洋折衷風格，室內空間自玄關、走廊與室內起居室、書房等井然有序。校長故居原已頹圮，整修後開放供民眾參觀，是文青新據點。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/國立新竹高中劍道館/介紹':
            try:
                message = TextSendMessage(
                    text = '劍道館建於1926年，是台灣現存武道場中唯一採洋式風格，為磚造木構雙折瓦頂的建築，山牆面呈現高聳的尖形山峰，牆面是清水磚，仿造西式建築的扶壁作法，透過外凸的磚柱，將屋頂的重量引導到地面，雖經修建但仍可見當年典雅風格。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/台灣菸酒公司新竹營業所/介紹':
            try:
                message = TextSendMessage(
                    text = '台灣菸酒公司新竹營業所日治時期稱為「臺灣總督府專賣局新竹支局」，前身是「台北專賣支局新竹出張所」，1935年完工，建築本體受到現代主義影響，強調水平線條，裝飾優雅，迥異於繁複的巴洛克式，在當時是非常前衛的設計風格。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/孔廟/介紹':
            try:
                message = TextSendMessage(
                    text = '原為淡水廳儒學學宮，清嘉慶23年起文廟開考入學，新竹學子終於擁有自己的學堂。新竹孔廟在清代時為官廟，大門不繪製門神，而是以門釘為防禦。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/東區/李克承博士故居/介紹':
            try:
                message = TextSendMessage(
                    text = '李克承先生是新竹第一位醫學博士，懸壺濟世五十年，備受各方讚譽。李克承博士故居約興建於1943年間，是日本傳統和式建築，但採用現代主義建築流行風格，多由線條構成簡潔的圖樣系統，且具備歷史人物空間特色，是具代表性及地方特色之文化資產價值。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/北區/新竹州廳—新竹市政府/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹州廳建於1925年，建築形式為和洋混合風格，是當時常用建築風格。正門玄關採用雙柱式門廊搭配兩側小塔樓，頗有氣勢。大廳內的洋式拱廊與羅馬柱十分氣派，翼樓突出的量體增加了穩重感，整體形式視野開闊，氣勢磅礡。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@歷史建築/香山區/香山火車站/介紹':
            try:
                message = TextSendMessage(
                    text = '香山驛建於1928年，是西部鐵道幹線碩果僅存的木造火車站之一，以阿里山運來的檜木，建造純日式風格建築，至今依然保存完好。雖然候車空間狹小，但與當地人生活息息相關，成為香山人記憶中不可或缺的建築。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/東區/青草湖/介紹':
            try:
                message = TextSendMessage(
                    text = '青草湖曾為重要水庫，新竹市政府於民國96年以杭州西湖為藍圖，徹底改造青草湖，形成小西湖的景致。環湖步道串聯了周邊風景，靈隱寺、鳳凰橋、映月橋、于飛島等景點，很適合慢步或單車環湖。新竹市政府近年著手推動青草湖環境改善，積極進行清淤工作，並針對景觀平台、木棧道、照明設施規劃整建，更推出新型水域遊憩，106年9月青草湖水域遊憩中心開始營運，帶入運動、休閒元素，結合青草湖環境優勢，舉辦各項水上活動，營造城市運動風氣。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/北區/十七公里海岸線/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹沿海蔚藍海岸線十七公里處，上千公頃的潮間帶，是北台灣最大的海濱溼地，孕育了大量的蝦蟹螺貝類，漁產豐富的新竹漁港，除了嘗海鮮、放風箏、欣賞港口各式漁船美景之外，也能騎鐵馬欣賞沿途怡人的風光。而紅樹林公園、金城湖賞鳥區、賞鳥棧道，則富含各種生態風貌，客雅溪口潮間帶留鳥與候鳥時時流連，騎著自行車在海邊逐風而行，或是晨起賞鳥暮映落日，是假日舒適的好去處。香山濕地自然生態區、美山蔚藍海岸區、海山漁港等地，遍地的招潮蟹與和尚蟹，是極富樂趣與教育意義的親子戲水弄潮天堂。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/北區/魚鱗天梯/介紹':
            try:
                message = TextSendMessage(
                    text = '站在被網友們封為「魚鱗天梯」的護岸上，可以比過去更加靠近海灘，以魚鱗式的階梯取代傳統消波塊，打造出一片臨海特色觀海階梯，為近期非常受到民眾歡迎的拍照打卡區。漁港的堤防周邊必須做護坡工程，過去是使用俗稱「肉粽」的消坡塊堆疊，而市政府在新竹漁人碼頭的改造工程中採用自然原生大石塊做拋石護堤，並在拋石節點設置階梯型人工消坡塊，讓海堤身兼消波阻隔的功能外，也更加親近與休憩功能。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/青青草原/介紹':
            try:
                message = TextSendMessage(
                    text = '青青草原位於香山丘陵內，保有牧草區與林像，是新竹市難得的自然山林。這一片一望無際翠綠的大草原有油桐植栽，黑板樹植栽、休憩涼亭，是踏青及放風箏的好所在。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/青青草原溜滑梯/介紹':
            try:
                message = TextSendMessage(
                    text = '青青草原草原路入口區配合山丘地形，打造戶外兒童遊樂場設置探索區與賞鳥教育區，設置有四座大型磨石子彩色溜滑梯，溜滑梯最長滑道總長約54公尺，為北台灣最長磨石子溜滑梯。探索區除溜滑梯外並有兒童爬網，賞鳥樹屋，兒童傳聲筒等遊樂設施，小朋友奔跑在木平台階梯，由戶外溜滑梯高處滑下可觀賞五色鳥，紅嘴黑鵯，喜鵲等，為最大也最有趣的自然生態兒童遊樂場，可為大朋友及小朋友帶來高探索性的豐富遊樂體驗。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/香山濕地/介紹':
            try:
                message = TextSendMessage(
                    text = '香山濕地生態豐富，是台灣沿海招潮蟹族群最繁盛的泥灘濕地，孕育大量蝦、蟹、螺、貝而吸引大批水鳥覓食棲息，也是西伯利亞鳥類遷徙的必經之處之一。香山潮間帶1996年在國際拉姆薩公約組織會議中被正式列為「東亞水鳥保護網棲息地」一環，更是國際鳥盟指名重要的野鳥保育棲地，並於2001年公告為新竹市濱海野生動物保護區，2013年公告為國家級重要濕地。香山也是北台灣最大的蚵場，更是台灣牡蠣養殖的北限，一望無際的濕地遠處可見成列的風力發電風車，傍晚落日霞光映照，是絕美景色。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/金城湖賞鳥區/介紹':
            try:
                message = TextSendMessage(
                    text = '金城湖是客雅溪出海口北岸的半天然湖，潮間帶有著豐富的海濱生物，吸引鳥類到此覓食，周圍茂密森林，提供鳥類隱蔽的空間，湖中央的兩塊沙洲就成了鳥類棲息的場所。遇到漲、退潮時，鳥類雲集停歇覓食，是港南最重要的賞鳥據點。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/朝山陸橋/介紹':
            try:
                message = TextSendMessage(
                    text = '朝山陸橋也是個美麗的景點，這個陸橋橫跨西濱公路，連結朝山社區與香山濕地，陸橋的外觀很特別，是一個類似船型的陸橋，陸橋又有個綽號叫鹹魚翻身，看起來像魚又像船。在陸橋上面，社區的風光一覽無疑，在面向大海的方向，沿岸有巨大的風力發電機與廣大的溼地，風景真的很漂亮，新竹最有名的香山夕照，就是在這個景點上。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/海山漁港/介紹':
            try:
                message = TextSendMessage(
                    text = '海山漁港是新竹市唯二漁港，具備漁業與遊憩多功能，是漁民出海作業據點，沿岸蚵田分布，潮間帶生態、無敵海景和美麗夕陽，是家庭出遊的休閒勝地，'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/賞蟹步道/介紹':
            try:
                message = TextSendMessage(
                    text = '賞蟹步道長250公尺，沿著步道可欣賞弧邊招潮蟹、德氏仿厚蟹等十多種螃蟹，退潮時「萬蟹奔騰」景象更是壯觀。透過賞蟹步道，讓市民與溼地更親近。賞蟹步道設計的弧度和彎道是根據螃蟹出沒地點與時間，讓民眾站在步道上就能欣賞豐富多樣的螃蟹物種，還能觀察可愛的彈塗魚與美麗夕陽。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/南港賞鳥區/介紹':
            try:
                message = TextSendMessage(
                    text = '南港賞鳥區是一處小而美的生態區，一年四季都有不同候鳥進駐，寧靜的湖面經常可見小水鴨悠游其中。堤防內側的數個水塘，是由廢棄漁塭自然形成，已成為野鳥覓食後休憩的場所，因此也成為賞鳥的好去處。在新竹鳥會的調查紀錄資料中，這裡除了有大量的鷺科、燕科、文鳥科等鳥種出沒之外，秋冬交接時，還有數量可觀的雁鴨科鳥種，包括小水鴨、尖尾鴨、綠頭鴨等，而魚鷹、澤鵟、遊隼、紅隼等猛禽也偶而可見。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@自然景觀/香山區/十七公里南港站/介紹':
            try:
                message = TextSendMessage(
                    text = '「17公里南港站」新設無障礙空中步道和廁所，並保留原有的瞭望塔，讓民眾可以欣賞被網友封為「台版撒哈拉沙漠」且具有國家級生態濕地美名的香山沙丘。站上瞭望台可一次飽覽沙丘、夕陽、風車、海景四大景致，是17公里自行車道絕美隱藏版祕境！17公里南港站在不破壞棲地、不驚擾鳥類的前提下，打造親近自然的服務設施，將原有瞭望台重新粉刷成為自然色系的灰黑色、內部則為黃色，形成美麗的反差，也新設自行車停放廣場、無障礙觀景步道以及男女廁所。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/東區/關帝廟/介紹':
            try:
                message = TextSendMessage(
                    text = '清乾隆42年所建，主祀關聖帝君，配祀文昌帝君，廟宇建築裝飾簡樸，不僅沒有龍柱，大門口也以一對石鼓代替石獅子，更特別的是關帝廟具官廟性質，所以廟門不繪門神而是用門釘，每逢考季學子前來祈求考運亨通，絡繹不絕。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/東區/竹蓮寺/介紹':
            try:
                message = TextSendMessage(
                    text = '創建於清乾隆46年，當地人稱為觀音亭，寺中主要奉祀三尊觀世音菩薩，其中最小尊的三媽已有300多年歷史。竹蓮寺建築風格以閩式建築為主，廟頂及廟樑採用玻璃剪黏拼貼各種麒麟與龍身，全寺莊嚴細膩，深具藝術及保存價值。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/東區/普天宮/介紹':
            try:
                message = TextSendMessage(
                    text = '位於寺廟林立的新竹古奇峰，「古奇遠眺」是新竹八景之一，高120公尺的關公神像是名聞遐邇的地標。主要奉祀玉皇大帝與關聖帝君，寺內同時也是宗教歷史文物館，包含武聖關公歷史館、中日古董樓、古董木眠床等。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/東區/開台金山寺/介紹':
            try:
                message = TextSendMessage(
                    text = '金山寺是三級古蹟，建於清咸豐3年，建築風格古樸，主建物是清朝中期的建築，單進三開間帶左右護龍，正殿和左廂房至今仍保持舊有建物，濃厚的常民歷史感有別於其他廟宇的風格。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/北區/都城隍廟/介紹':
            try:
                message = TextSendMessage(
                    text = '為三級古蹟，與竹蓮寺、外天后宮並稱為新竹三大廟宇，建築規模宏大，本體採三殿式，龍柱、石獅大門上方八卦藻井都是一代名匠所造，大殿上懸掛的「金門保障」匾額，為清光緒帝所賜，是全台位階最高的城隍爺。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/北區/外媽祖長和宮/介紹':
            try:
                message = TextSendMessage(
                    text = '建於清乾隆7年，位在竹塹城北門外，所以稱為外媽祖廟或外天后宮。長和宮各部裝飾十分用心，其中三川殿的牆堵石雕仍為清朝原件，所供奉的媽祖為關節四肢可以活動的「軟身神像」，頭上所鑲頭髮，相傳即為媽祖真髮。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/北區/水仙宮/介紹':
            try:
                message = TextSendMessage(
                    text = '水仙是海洋之神，夏禹就是水仙尊王，原來奉祀在長和宮的後殿，清同治5年時在長和宮左側修建水仙宮，水仙宮韻致高雅，三川殿步口簷柱為方形石柱，步口員光是書卷形式，步口通樑上是獅座，雕刻線條流暢，手藝精良。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/北區/天公壇/介紹':
            try:
                message = TextSendMessage(
                    text = '最早興建於清乾隆年間，1913年由本地士紳等眾募集銀錢重建，原稱金闕殿。新竹天公壇擁有二百多年歷史，是台灣少數主祀玉皇大帝的道教廟宇。正殿主祀玉皇大帝，配祀有：三官大帝、五榖先帝、托塔李天王、文昌帝君等神明。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/北區/北大教堂/介紹':
            try:
                message = TextSendMessage(
                    text = '北大教堂，1957年落成是天主教的信仰中心。建築近似哥德式，以凸顯接近天堂上升的形式為概念隨處可見向上概念的尖形線條。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@宗教文化/香山區/香山天后宮/介紹':
            try:
                message = TextSendMessage(
                    text = '香山天后宮奉祀天上聖母，是本地漁民信仰中心，整建於1825年(清道光5年)，1876年（清光緒2年）重建竣工，地方人士敬獻的「靈昭海國」的匾額，至今仍懸掛正殿。1924年(大正13年)再度重修落成，三川殿前的石雕構件古樸，雕刻手法反映大正年間時代特色，殿內古匾額和壁飾也傳承人文風華，為見證香山地區信仰之文化資產，已登錄為歷史建築。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/東區/新竹市美術館/介紹':
            try:
                message = TextSendMessage(
                    text = '1920年，日本政府改正地方制度，於新竹州新竹郡管轄的新竹街(現新竹市)設置新竹街役場；原街役場設於郡役所內，直至1925年才建成，今日的新竹市美術館於焉誕生。本館歷經多次轉型：1930年，新竹街升格為新竹市，新竹街役場也更名為「新竹市役所」(類似今日的市政府)；1991年成為新竹市戶政事務所，並於2001年公告為市定古蹟。為活化古蹟再利用，2004年起，經新竹市政府3年整修後，於2007年定名為「新竹市美術館暨開拓館」；2016年再經轉型成為當代藝術展覽空間，即現今的「新竹市美術館」，期許為新竹市帶來更多藝術氣息。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/東區/影像博物館/介紹':
            try:
                message = TextSendMessage(
                    text = '1933年啟用的國民戲院，昔稱「新竹市營有樂館」，建築形式融合羅馬與阿拉伯風格，牆面裝飾幾何圖形和花草圖紋，為早期鋼構建物，整建後蛻變為台灣第一座以電影為主題的影像博物館。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/東區/玻璃工藝博物館/介紹':
            try:
                message = TextSendMessage(
                    text = '座落於新竹公園，原是建於1936年的日本自治會館，建築物採用仿歐式庭院風格，結合日式的典雅樸實，呈現東西融合的古典浪漫意象。1999年改建為新竹玻璃工藝博物館，展示新竹玻璃工藝製品。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/東區/科學園區探索館/介紹':
            try:
                message = TextSendMessage(
                    text = '科學園區探索館主要展示台灣高科技產業、科學園區發展歷程相關文物，讓民眾了解竹科從早期的王安電腦，到現今區內產業軌跡。探索館常態展示以園區發展史、台灣產業、科技相關文物等為主，而特展區則規劃近期產業趨勢，如雲端設計、新式平板等設計產品。想要了解竹科從過去的蔗田、茶園，到如今點矽成金的歷程，探索館歡迎以預約方式由館內安排解說員。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/北區/消防博物館/介紹':
            try:
                message = TextSendMessage(
                    text = '建於1937年，六層樓高的瞭望台是當時全新竹市最高的建築，消防員從瞭望台判定失火地點，再利用傳聲筒通知消防員，頂樓還有用來通知的古消防警鐘。消防博物館展示消防文物與歷史，也是防火救災的教育功能展示體驗區。(因進行古蹟修復級展設更新，休館至114年12月31日)'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/北區/新竹生活美學館/介紹':
            try:
                message = TextSendMessage(
                    text = '建於1921年之後，主體建物是日治時期公會堂建築，兩側柱列相當精緻，東側外廊道保存迴廊拱圈，融合臺灣傳統建築與西方設計手法。自新竹公會堂至今日的美學館，均常態舉辦藝文，長期提供美學教育，深具歷史意義。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/北區/新竹眷村博物館/介紹':
            try:
                message = TextSendMessage(
                    text = '常態性展示並保存眷村生活用品與文物，重現眷村生活的小角落。入口大門以眷村紅門白線的傳統造形設計，廣場展示著空軍軍用飛機副油箱水塔，館內展示眷村歷史、生活情境，與文化特展，走一趟博物館等於重新認識了眷村生活文化。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/北區/黑蝙蝠中隊文物陳列館/介紹':
            try:
                message = TextSendMessage(
                    text = '黑蝙蝠中隊是1952年美國中央情報局在台工作站「西方公司」與空軍的合作，1953年部隊遷至新竹基地，1958年開始稱為「黑蝙蝠中隊」。文物館內重現了大時代的故事，述說當時的任務與歷史、殉難的英雄，以及黑蝙蝠實體文物。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/北區/康樂農村文物陳列館與輕便車道/介紹':
            try:
                message = TextSendMessage(
                    text = '康樂社區昔時為康榔庄，是日據時期州道及輕便軌道途中要道，里民提供舊時家傳文物與生活器物，成立了文物陳列館，重現當年生活光景。康樂里至今仍保留有「輕便車」，如今軌跡多數已湮沒，但康樂里還重新架設一小段重現舊回憶。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@博物館/北區/消防博物館/介紹':
            try:
                message = TextSendMessage(
                    text = '北大教堂，1957年落成是天主教的信仰中心。建築近似哥德式，以凸顯接近天堂上升的形式為概念隨處可見向上概念的尖形線條。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/東區/高峰植物園/介紹':
            try:
                message = TextSendMessage(
                    text = '高峰植物園設於1932年日治時代，原名「新竹州立赤土崎林業試驗場」，佔地二、三十公頃，培育多種本土植物及外來樹種，計有342種植物，目前並已發現40種鳥類及20種蟲類，四季還有候鳥行經或留鳥棲息，擁有豐美生態體系。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/東區/新竹公園/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹公園佔地18公頃，舊稱中山公園，又名公二公園，創建於西元1916年。新竹公園距離火車站只有十分鐘的路程，是新竹市民休閒運動的最佳去處，公園內綠樹成蔭，蒼松翠柏，還有玻璃工藝博物館、玻璃工坊、麗池、湖畔料亭、大沙坑、體育館、田徑場等，兼具休閒、運動、人文、歷史機能。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/東區/新竹市立動物園/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹市立動物園創園於1936年，為全台現址最老也最迷你的動物園，也是新竹市充滿著歷史記憶重要的休憩地點。108年底改建後的動物園擁有兩大核心目標，首先是以動物生活福祉為優先，除了打造類棲地環境，讓動物生活場域更寬廣，動線設計也以「不打擾動物」為原則；第二，則是讓園區成為最適合親子的「生命教育場域」，讓新竹市不只有一群快樂的動物，更有一群友善動物的可愛市民。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/東區/中央公園/介紹':
            try:
                message = TextSendMessage(
                    text = '中央公園獨特親子遊樂空間，非罐頭化遊樂設施，包括「地景式溜滑梯」及「碗狀型可躺式盪鞦韆」等，保留許多市民難忘的共同回憶─磨石子溜滑梯，新舊融合，期盼爸媽帶著孩子們來玩時，也能回味自己的童年時光。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/東區/新竹鐵道藝術村/介紹':
            try:
                message = TextSendMessage(
                    text = '原來是台鐵建於民國30年新竹站的3-5號倉庫，濃濃的日式風格，從閒置空間廢棄角落結合舊倉庫的記憶，走出當代藝文空間的時代意義。藝術村內擁有展演廳，開放藝術家駐村、展覽或活動策辦，是欣賞藝術的交流平台。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/東區/隆恩圳/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹市隆恩圳是台灣三大古圳之一，過去的隆恩圳將三民路「一分為二」，河道左右的聯通度相當低、居民的生活空間分割、往來受限，107年5月「隆恩圳景觀空間」正式完工，在兼顧生態環境考量下，架高平台、橋梁橫跨河面，除了滿足親子休閒的功能，也創造都市中供人步行、停留的環境，也讓水圳兩旁的巷道連結性更強，創造「大街串小巷」的親近生活感。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/北區/新竹漁港/介紹':
            try:
                message = TextSendMessage(
                    text = '新竹南寮漁港最早位於現在舊漁港的十七公里海岸所在地，因流砂淤塞遷移而另建新港，舊漁港至今仍保留製冰廠及漁船出海時的加冰設備。漁港內聚集海味珍饌的地方是新竹漁港直銷中心，隨著季節捕獲的當令海鮮天天上岸，吸引人潮品嚐海鮮、購買漁獲。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/北區/槺榔驛/介紹':
            try:
                message = TextSendMessage(
                    text = '這木造的小車站與古輕便車道為日治時期所建，昔日運送貨物的任務已被時代所汰換，如今遊客搭上古輕便車慢慢繞著槺榔庄前行，沿途會經過民宅，欣賞大自然風光與田園樂活氣息。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/北區/新竹綠園道/介紹':
            try:
                message = TextSendMessage(
                    text = '1公里長的新竹綠園道，分為三期改造而成，保留大量綠地草皮供市民親近綠環境，另打造適合各年齡層同遊的休閒環境，於第二期東大、民權路段設置碗公型磨石子溜滑梯與攀爬區，碗公型溜滑梯遠看如同一個大大的微笑，也可稱為「微笑溜滑梯」。新竹綠園道從原本僅2公尺寬的人行道拓寬為6公尺，並重新整理動線、梳理樹林，自然光線散落在林蔭步道間，讓整體視覺更加明亮、通透，更運用巧思，運用街角空間設置活動廣場，以各式遊具點綴在綠廊間，讓市民朋友與大自然的關係更加緊密。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/北區/東大飛行公園/介紹':
            try:
                message = TextSendMessage(
                    text = '東大飛行公園以黑蝙蝠中隊執行任務的特點為設計主題，規劃入口意象、飛行記事、星空航道、夢想之翼、飛行廣場、聽見夢想與新月椅等7大裝置藝術，如：以弧形鋼板鏤空的「星空航道」，營造出日夜光線撒落的光影、以長條鋼板打造「夢想之翼」雷射切割出飛機線條，營造飛機翱翔於蒼穹意象，讓東大飛行公園成為歷史與遊憩兼具的城市綠地。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/北區/樹林頭公園/介紹':
            try:
                message = TextSendMessage(
                    text = '樹林頭公園位於東大路二段，面積有二點八公頃，民國九十五年前為國防部5、6、7空軍眷村，眷村拆除後閒置約十年，民國一〇四年十二月，市政府完成綠美化工程，讓原本的荒地成為市民休憩散步的好去處。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/北區/南寮旅服中心/介紹':
            try:
                message = TextSendMessage(
                    text = '設置了更衣室與親子廁所，室內提供遊客舒適友善的諮詢與休息空間。並新規劃4座溜滑梯，其中室內一座13.5公尺長、2樓高，還有可俯瞰南寮無敵海景的觀景平台。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@公園與休閒區/香山區/港南運河公園/介紹':
            try:
                message = TextSendMessage(
                    text = '港南運河風景區於民國76年設立，為了重新吸引市民來到優質水岸空間，市府於107年以生態第一優先、景觀再造、親水環境等三大目標，推動「港南運河親水再造計畫」。園區北側景觀區營造為兒童天堂，導入攀爬網、平衡木等特色共融遊具；南側則打造休閒臨水散步道並設置親水木平台，更有無邊際觀夕平台，讓民眾眺望美麗夕陽及海景。區內並設自行車驛站，及兒童滑步車區，更貼心設置家長休息區及洗腳區，讓大小朋友都能盡情遊玩放鬆。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@市區景點/東區/東門市場/介紹':
            try:
                message = TextSendMessage(
                    text = '東門市場是新竹市第一座有手扶梯的建築物，在民國60年代，是新竹是最繁榮的賣場，但隨時代變遷及民眾消費習慣改變，東門市場逐漸沒落，近年來市府整合各項資源鼓勵青年進駐創業，目前已成立東門市場青年基地，民眾更能在市場裡覓得特色餐點、下午茶、咖啡以及異國料理，傳統產業互相激盪，為老市場注入新活力。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@市區景點/北區/北門大街/介紹':
            try:
                message = TextSendMessage(
                    text = '竹塹舊城最繁榮的北門大街，包括華麗的巴洛克建築周益記，多家百年老店如繡妝行，佛具店，中藥店等，近年來也新興一些文青店家，為老街增添新創意。'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區':
            try:
                message1 = TemplateSendMessage(
                    alt_text='飯店',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹國賓大飯店',
                                text='(03)5151111\n新竹市東區中華路2段188號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/新竹國賓大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新竹老爺大酒店',
                                text='(03)5631122\n新竹市東區光復路1段227號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/新竹老爺大酒店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新苑庭園大飯店',
                                text='(03)5226868\n新竹市東區大同路11號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/新苑庭園大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='煙波大飯店-麗池館',
                                text='(03)5203181\n新竹市東區明湖路773號1-6樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/煙波大飯店-麗池館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='煙波大飯店-溫莎館',
                                text='(03)5203181\n新竹市東區明湖路775巷51號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/煙波大飯店-溫莎館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='煙波大飯店-都會一館',
                                text='(03)6120000\n新竹市東區民生路177號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/煙波大飯店-都會一館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='金頓大飯店',
                                text='(03)5646655\n新竹市東區光復路一段238號4-12樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/金頓大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='金燕大飯店',
                                text='(03)5227151\n新竹市東區民族路13號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/金燕大飯店/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message2 = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='迎曦大飯店(文化店)',
                                text='(03)5347266\n新竹市東區文化街10號2-10樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/迎曦大飯店(文化店)/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='元首大飯店',
                                text='(03)5711111\n新竹市東區建功一路29號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/元首大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='悅豪大飯店',
                                text='(03)5267890\n新竹市東區復興路22號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/悅豪大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新苑名流都會館',
                                text='(03)5211888\n新竹市東區大同路20號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/新苑名流都會館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='日月光國際大飯店',
                                text='(03)5456363\n新竹市東區中央路355巷16號1，3-6樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/日月光國際大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新竹伊普索酒店',
                                text='(03)5169308\n新竹市東區公道五路2段111號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/新竹伊普索酒店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='芙洛麗大飯店',
                                text='(03)6238899\n新竹市東區民族路69號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/芙洛麗大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='吉發明月大飯店',
                                text='(03)5281818\n新竹市東區東門街128號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/東區/吉發明月大飯店/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message = [message1, message2]
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))

        elif mtext == '@旅館/東區':
            try:
                message1 = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='心園商務旅館',
                                text='(03)5313525\n新竹市東區民權路223號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/心園商務旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='微旅商務旅館',
                                text='(03)5323183\n新竹市東區民生路268號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/微旅商務旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='豪美旅店',
                                text='(03)5218441\n新竹市東區勝利路86號1-2F',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/豪美旅店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='紫晶汽車旅館',
                                text='(03)5620789\n新竹市東區頂竹里東南街53巷18號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/紫晶汽車旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='普邑斯商務旅館',
                                text='(03)5428681\n新竹市東區東區民權路193號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/普邑斯商務旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='老爺旅社',
                                text='(03)5711585\n新竹市東區光復路二段167號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/老爺旅社/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='左岸假期旅店',
                                text='(03)5284800\n新竹市東區中華路二段502號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/左岸假期旅店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='華泰經典旅店',
                                text='(03)5243145\n新竹市東區勝利路15號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/華泰經典旅店/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message2 = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='東賓大旅社',
                                text='(03)5223161\n新竹市東區林森路14號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/東賓大旅社/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='柿子紅快捷旅店',
                                text='(03)5223232\n新竹市東區大同路23巷5號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/柿子紅快捷旅店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='賓城大旅社',
                                text='(03)5269255\n新竹市東區中正路13號5-10樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/賓城大旅社/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='芝蘭賓館',
                                text='(03)5254166\n新竹市東區中華路二段480號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/芝蘭賓館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='金座渡假汽車旅館',
                                text='(03)5201833\n新竹市東區明湖路928-2，930號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/金座渡假汽車旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新都旅館',
                                text='(03)5261131\n新竹市東區中南街12號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/新都旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='國賓旅館',
                                text='(03)5243164\n新竹市東區大同路21號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/國賓旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='東城精品旅館',
                                text='(03)5222648\n新竹市東區府後街5巷1號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/東城精品旅館/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message3 = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='湖山渡假汽車旅館',
                                text='(03)5203000\n新竹市東區明湖路1001號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/湖山渡假汽車旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='承攜行旅新竹中央館',
                                text='(03)5212323\n新竹市東區中央路106號B2，1樓，8-15樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/承攜行旅新竹中央館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='晶悅精品旅館',
                                text='(03)6667567\n新竹市東區關新二街49號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/晶悅精品旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='歐遊國際精品旅館',
                                text='(03)5790088\n新竹市東區埔頂路500號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/歐遊國際精品旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='暐順和選旅',
                                text='(03)5715888\n新竹市東區光明里1鄰大學路16號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/暐順和選旅/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='達龍商旅',
                                text='(03)5166666\n新竹市東區東園里4鄰光復路二段808號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/達龍商旅/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='水蜜桃時尚旅店',
                                text='(03)5234138\n新竹市東區民族路29號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/水蜜桃時尚旅店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='琺何旅館有限公司',
                                text='(03)5610011\n新竹市東區振興里振興路109號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/東區/琺何旅館有限公司/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message = [message1, message2, message3]
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@民宿/東區':
            try:
                message = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='瘋人苑',
                                text='0955396833\n新竹市東區新竹市世界街128號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@民宿/東區/瘋人苑/查看更多'
                                    ),
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@飯店/北區':
            try:
                message = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='荷米斯飯店',
                                text='(03)5269999\n新竹市北區西大路606號1-9樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/北區/荷米斯飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='宏碁大道城飯店',
                                text='(03)5282255\n新竹市北區北大路358號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/北區/宏碁大道城飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='卡爾登飯店',
                                text='(03)5259999\n新竹市北區北大路225號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/北區/卡爾登飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='柏克萊大飯店',
                                text='(03)5251155\n新竹市北區中正路151號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/北區/柏克萊大飯店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新竹福華大飯店',
                                text='(03)5282323\n新竹市北區中正路178號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/北區/新竹福華大飯店/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@旅館/北區':
            try:
                message1 = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='風之海岸旅館',
                                text='(03)5366095\n新竹市北區尚濱路36號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/風之海岸旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='棒球精緻旅店',
                                text='(03)5261172\n新竹市北區西大路549號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/棒球精緻旅店/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='啊囉哈一六八汽車旅館',
                                text='(03)5362277\n新竹市北區西濱路1段217號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/啊囉哈一六八汽車旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='約客旅舘',
                                text='(03)5361122\n新竹市北區東大路四段121號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/約客旅舘/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='合悅都會商旅',
                                text='(03)5234499\n新竹市北區西大路417號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/合悅都會商旅/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='月圓汽車旅館',
                                text='(03)5231728\n新竹市北區少年街88號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/月圓汽車旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='豪美商旅有限公司',
                                text='(03)5213333\n新竹市北區中正路107號11樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/豪美商旅有限公司/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message2 = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='向日葵汽車旅館',
                                text='(03)5359797\n新竹市北區經國路二段150號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/向日葵汽車旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='水晶旅館有限公司',
                                text='(03)5366789\n新竹市北區聖軍路75號\n總房間數：35\n最低房間價格：5200\n最高房間價格：6400\n對外營業之餐飲：無',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/水晶旅館有限公司/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='城市花園汽車旅館',
                                text='(03)5422989\n新竹市北區東大路二段377號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/城市花園汽車旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='薇閣精品旅館',
                                text='(03)5238080\n新竹市北區中正路137號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/薇閣精品旅館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='金沙商務旅舘',
                                text='(03)5368221\n新竹市北區東濱街18號4樓',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/金沙商務旅舘/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='新舍商旅新竹館',
                                text='(03)5221082\n新竹市北區西大路658號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/新舍商旅新竹館/查看更多'
                                    ),
                                ]
                            ),
                            CarouselColumn(
                                title='或者風旅',
                                text='(03)5220505\n新竹市北區大同路175號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/北區/或者風旅/查看更多'
                                    ),
                                ]
                            )
                        ]
                    )
                )
                message = [message1, message2]
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@民宿/北區':
            try:
                message = TextSendMessage(
                    text = '這個區域沒有您想要查詢的資料'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
                
        elif mtext == '@飯店/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='新竹德威大飯店',
                                text='(03)5297300\n新竹市香山區富群街3號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@飯店/香山區/新竹德威大飯店/查看更多'
                                    ),
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@旅館/香山區':
            try:
                message = TemplateSendMessage(
                    alt_text='轉盤樣板',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                title='馬德里經典旅館',
                                text='(03)5305533\n新竹市香山區中華路四段729號',
                                actions=[
                                    MessageTemplateAction(
                                        label='查看更多',
                                        text='@旅館/香山區/馬德里經典旅館/查看更多'
                                    ),
                                ]
                            ),
                        ]
                    )
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@民宿/香山區':
            try:
                message = TextSendMessage(
                    text = '這個區域沒有您想要查詢的資料'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        
        elif mtext == '@飯店/東區/新竹國賓大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：257\n最低房間價格：10000\n最高房間價格：105000\n對外營業之餐飲：有'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@飯店/東區/新竹老爺大酒店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：208\n最低房間價格：8000\n最高房間價格：16000\n對外營業之餐飲：有'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@飯店/東區/新苑庭園大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：65\n最低房間價格：6600\n最高房間價格：12600\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@飯店/東區/煙波大飯店-麗池館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：66\n最低房間價格：9900\n最高房間價格：24200\n對外營業之餐飲：有'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@飯店/東區/煙波大飯店-溫莎館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：23\n最低房間價格：4800\n最高房間價格：10000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@飯店/東區/煙波大飯店-都會一館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：238\n最低房間價格：8800\n最高房間價格：17600\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/金頓大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：88\n最低房間價格：3000\n最高房間價格：5000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        
        elif mtext == '@飯店/東區/金燕大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：39\n最低房間價格：1180\n最高房間價格：1500\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/迎曦大飯店(文化店)/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：174\n最低房間價格：8800\n最高房間價格：15000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/元首大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：32\n最低房間價格：1800\n最高房間價格：1800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/悅豪大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：35\n最低房間價格：2240\n最高房間價格：8980\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/新苑名流都會館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：35\n最低房間價格：6600\n最高房間價格：11600\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/日月光國際大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：60\n最低房間價格：4800\n最高房間價格：6600\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/新竹伊普索酒店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：140\n最低房間價格：12000\n最高房間價格：25000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/芙洛麗大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：140\n最低房間價格：12000\n最高房間價格：25000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/東區/吉發明月大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：64\n最低房間價格：3200\n最高房間價格：6000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/心園商務旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：32\n最低房間價格：2200\n最高房間價格：4000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/微旅商務旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：52\n最低房間價格：1380\n最高房間價格：9600\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/豪美旅店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：3\n最低房間價格：3000\n最高房間價格：3000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/紫晶汽車旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：43\n最低房間價格：1700\n最高房間價格：4500\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/普邑斯商務旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：57\n最低房間價格：2730\n最高房間價格：2880\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/老爺旅社/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：18\n最低房間價格：1380\n最高房間價格：4800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/左岸假期旅店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：39\n最低房間價格：2880\n最高房間價格：3980\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/華泰經典旅店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：41\n最低房間價格：1400\n最高房間價格：2000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/東賓大旅社/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：47\n最低房間價格：800\n最高房間價格：3950\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/柿子紅快捷旅店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：39\n最低房間價格：2800\n最高房間價格：5880\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/賓城大旅社/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：36\n最低房間價格：750\n最高房間價格：2300\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/芝蘭賓館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：48\n最低房間價格：680\n最高房間價格：3500\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/金座渡假汽車旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：25\n最低房間價格：1200\n最高房間價格：5500\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/新都旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：16\n最低房間價格：400\n最高房間價格：400\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/國賓旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：26\n最低房間價格：700\n最高房間價格：1100\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/東城精品旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：28\n最低房間價格：600\n最高房間價格：800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/湖山渡假汽車旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：50\n最低房間價格：1580\n最高房間價格：1760\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/承攜行旅新竹中央館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：138\n最低房間價格：8000\n最高房間價格：10000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/晶悅精品旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：57\n最低房間價格：2000\n最高房間價格：8000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/歐遊國際精品旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：20\n最低房間價格：3380\n最高房間價格：22800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/暐順和選旅/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：173\n最低房間價格：9500\n最高房間價格：60000\n對外營業之餐飲：有'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/達龍商旅/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：46\n最低房間價格：3200\n最高房間價格：8800\n對外營業之餐飲：有'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/水蜜桃時尚旅店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：39\n最低房間價格：2200\n最高房間價格：8000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/東區/琺何旅館有限公司/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：42\n最低房間價格：13000\n最高房間價格：13000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@民宿/東區/瘋人苑/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：5\n最低房間價格：7200\n最高房間價格：8800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/北區/荷米斯飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：72\n最低房間價格：1200\n最高房間價格：4800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/北區/宏碁大道城飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：118\n最低房間價格：1800\n最高房間價格：16800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/北區/卡爾登飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：117\n最低房間價格：7800\n最高房間價格：10000\n對外營業之餐飲：有'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/北區/柏克萊大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：39\n最低房間價格：5450\n最高房間價格：12800\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/北區/新竹福華大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：165\n最低房間價格：4600\n最高房間價格：15000\n對外營業之餐飲：有'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/風之海岸旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：45\n最低房間價格：1680\n最高房間價格：2000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/棒球精緻旅店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：31\n最低房間價格：1200\n最高房間價格：2000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/啊囉哈一六八汽車旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：32\n最低房間價格：5580\n最高房間價格：7180\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/約客旅舘/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：38\n最低房間價格：6000\n最高房間價格：6000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/合悅都會商旅/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：18\n最低房間價格：3200\n最高房間價格：5500\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/月圓汽車旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：34\n最低房間價格：1680\n最高房間價格：1680\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/豪美商旅有限公司/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：21\n最低房間價格：3600\n最高房間價格：4400\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/向日葵汽車旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：31\n最低房間價格：2580\n最高房間價格：3780\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/城市花園汽車旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：24\n最低房間價格：1960\n最高房間價格：4250\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/薇閣精品旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：72\n最低房間價格：6000\n最高房間價格：6000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/金沙商務旅舘/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：15\n最低房間價格：4000\n最高房間價格：6000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/新舍商旅新竹館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：64\n最低房間價格：4200\n最高房間價格：5180\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/北區/或者風旅/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：5\n最低房間價格：3600\n最高房間價格：5400\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@飯店/香山區/新竹德威大飯店/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：230\n最低房間價格：5500\n最高房間價格：8500\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif mtext == '@旅館/香山區/馬德里經典旅館/查看更多':
            try:
                message = TextSendMessage(
                    text = '總房間數：23\n最低房間價格：12000\n最高房間價格：12000\n對外營業之餐飲：無'
                )
                line_bot_api.reply_message(event.reply_token,message)
            except:
                line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))


    # get X-Line-Signature header value
    signature = event['headers']['x-line-signature']

    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
            }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
        }
    
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImagemapSendMessage, QuickReply, QuickReplyButton, MessageAction, BaseSize, MessageImagemapAction, ImagemapArea
)

import os
import json
import logging
import boto3
import sys
import pymysql
import numpy
import pandas

line_bot_api = LineBotApi(os.environ['Channel_access_token'])
handler = WebhookHandler(os.environ['Channel_secret'])

db_host = os.environ['host']
db_user = os.environ['user']
db_password = os.environ['password']
db_name = os.environ['name']

def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        mtext = event.message.text
        tab=None
        ar=None
        tp=None
        if mtext=='@找住宿':
            tab=1
        elif mtext=='@找景點':
            tab=2
        elif mtext=='@找美食':
            tab=3

        if mtext == '@找美食':
            try:
                image_url = 'https://i.imgur.com/oY4cf4t.jpg'
                imgwidth = 1040
                imgheight = 1040
                message = ImagemapSendMessage(
                    base_url=image_url,
                    alt_text="美食分類",
                    base_size=BaseSize(height=imgheight, width=imgwidth),
                    actions=[
                        MessageImagemapAction(
                            text='@伴手禮',
                            area=ImagemapArea(
                                x=0,
                                y=0,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@小吃',
                            area=ImagemapArea(
                                x=imgwidth*0.5,
                                y=0,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@飲料與甜點',
                            area=ImagemapArea(
                                x=0,
                                y=imgheight*0.5,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@餐廳',
                            area=ImagemapArea(
                                x=imgwidth*0.5,
                                y=imgheight*0.5,
                                width=imgwidth*0.5,
                                height=imgheight*0.5
                            )
                        ),
                    ]
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        elif mtext == '@找住宿':
            try:
                image_url = 'https://i.imgur.com/Nn4rncm.jpg'
                imgwidth = 1040
                imgheight = 347
                message = ImagemapSendMessage(
                    base_url=image_url,
                    alt_text="飯店分類",
                    base_size=BaseSize(height=imgheight, width=imgwidth),
                    actions=[
                        MessageImagemapAction(
                            text='@飯店',
                            area=ImagemapArea(
                                x=0,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*1
                            )
                        ),
                        MessageImagemapAction(
                            text='@旅館',
                            area=ImagemapArea(
                                x=imgwidth*0.33,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*1
                            )
                        ),
                        MessageImagemapAction(
                            text='@民宿',
                            area=ImagemapArea(
                                x=imgwidth*0.66,
                                y=0,
                                width=imgwidth*0.34,
                                height=imgheight*1
                            )
                        ),
                    ]
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
        elif mtext == '@找景點':
            try:
                image_url = 'https://i.imgur.com/BJnw4Do.jpg'
                imgwidth = 1040
                imgheight = 693
                message = ImagemapSendMessage(
                    base_url=image_url,
                    alt_text="景點分類",
                    base_size=BaseSize(height=imgheight, width=imgwidth),
                    actions=[
                        MessageImagemapAction(
                            text='@歷史建築',
                            area=ImagemapArea(
                                x=0,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@自然景觀',
                            area=ImagemapArea(
                                x=imgwidth*0.33,
                                y=0,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@宗教文化',
                            area=ImagemapArea(
                                x=imgwidth*0.66,
                                y=0,
                                width=imgwidth*0.34,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@博物館',
                            area=ImagemapArea(
                                x=0,
                                y=imgheight*0.5,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@公園與休閒區',
                            area=ImagemapArea(
                                x=imgwidth*0.33,
                                y=imgheight*0.5,
                                width=imgwidth*0.33,
                                height=imgheight*0.5
                            )
                        ),
                        MessageImagemapAction(
                            text='@市區景點',
                            area=ImagemapArea(
                                x=imgwidth*0.66,
                                y=imgheight*0.5,
                                width=imgwidth*0.34,
                                height=imgheight*0.5
                            )
                        ),
                    ]
                )
                line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))

        if mtext=='@飯店':
            tp=1
        elif mtext=='@旅館':
            tp=2
        elif mtext=='@民宿':
            tp=3
        elif mtext=='@歷史建築':
            tp=4
        elif mtext=='@自然景觀':
            tp=5
        elif mtext=='@宗教文化':
            tp=6
        elif mtext=='@博物館':
            tp=7
        elif mtext=='@公園與休閒區':
            tp=8
        elif mtext=='@市區景點':
            tp=9
        elif mtext=='@伴手禮':
            tp=10
        elif mtext=='@小吃':
            tp=11
        elif mtext=='@飲料與甜點':
            tp=12
        elif mtext=='@餐廳':
            tp=13

        message = TextSendMessage(
            text='請選擇地區',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="東區", text="@東區")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="北區", text="@北區")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="香山區", text="@香山區")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

        if mtext=='@東區':
            ar=10018010
        elif mtext=='@北區':
            ar=10018020
        elif mtext=='@香山區':
            ar=10018030
        
        connection = pymysql.connect(host=db_host,
                             user=db_user,
                             password=db_password,
                             database=db_name,
                             cursorclass=pymysql.cursors.DictCursor)
          
        if tab == 3:
            with connect_db.cursor() as cursor:

                sql = """
                SELECT Name, Info, Address
                FROM Food
                WHERE Areacode = ? AND Type = ?
                """
                cursor.execute(sql,(ar,tp))
                data1 = cursor.fetchall()
                df1 = pd.DataFrame(data1, columns=['Name', 'Info','Address'])

                sql = """
                SELECT Name, Recommand
                FROM Food
                WHERE Areacode = ? AND Type = ?
                """
                cursor.execute(sql,(ar,tp))
                data2 = cursor.fetchall()
                df2 = pd.DataFrame(data2, columns=['Name', 'Recommand'])

                sql = """
                SELECT Name, Introduce
                FROM Food
                WHERE Areacode = ? AND Type = ?
                """
                cursor.execute(sql,(ar,tp))
                data3 = cursor.fetchall()
                df3 = pd.DataFrame(data3, columns=['Name', 'Introduce'])

            num=df1.shape[0]
            pin=None

            if num == 0:
                try:
                    message = TextSendMessage(
                        text = '這個區域沒有您想要查詢的資料'
                    )
                    line_bot_api.reply_message(event.reply_token,message)
                except:
                    line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
            else:
                try:
                    message = TemplateSendMessage(
                        alt_text='食物',
                        template=CarouselTemplate(
                            columns=[
                                CarouselColumn(
                                    title=f"{col}\n{df1.iloc[i][col]}",
                                    actions=[
                                        MessageTemplateAction(
                                            label='推薦菜色',
                                            text='@{i}/推薦菜色'
                                        ),
                                        MessageTemplateAction(
                                            label='簡介',
                                            text='@{i}/簡介',
                                        ),
                                    ]
                                )for i in range(num) for col in ['Name', 'Info','Address']
                            ]
                        )
                    )
                    line_bot_api.reply_message(event.reply_token,message)
                    if mtext.startswith('@') and mtext.split('/')[1] == '推薦菜色':
                        try:
                            pin = int(mtext.split('/')[0].replace('@', ''))
                            message = TextSendMessage(
                                text = df2.iloc[pin]['Recommand']
                            )
                            line_bot_api.reply_message(event.reply_token,message)
                        except:
                            line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
                    if mtext.startswith('@') and mtext.split('/')[1] == '簡介':
                        try:
                            pin = int(mtext.split('/')[0].replace('@', ''))
                            message = TextSendMessage(
                                text = df3.iloc[pin]['Introduce']
                            )
                            line_bot_api.reply_message(event.reply_token,message)
                        except:
                            line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
                except:
                    line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤! '))
        elif tab == 2:
            with connect_db.cursor() as cursor:

                sql = """
                SELECT Name, Address
                FROM Sightseeing
                WHERE Areacode = ? AND Type = ?
                """
                cursor.execute(sql,(ar,tp))
                data1 = cursor.fetchall()
                df1 = pd.DataFrame(data1, columns=['Name','Address'])

                sql = """
                SELECT Name, Introduce
                FROM Sightseeing
                WHERE Areacode = ? AND Type = ?
                """
                cursor.execute(sql,(ar,tp))
                data2 = cursor.fetchall()
                df2 = pd.DataFrame(data2, columns=['Name', 'Introduce'])

            num=df1.shape[0]
            pin=None

            if num == 0:
                try:
                    message = TextSendMessage(
                        text = '這個區域沒有您想要查詢的資料'
                    )
                    line_bot_api.reply_message(event.reply_token,message)
                except:
                    line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
            else:
                try:
                    message = TemplateSendMessage(
                        alt_text='景點',
                        template=CarouselTemplate(
                            columns=[
                                CarouselColumn(
                                    title=f"{col}\n{df1.iloc[i][col]}",
                                    actions=[
                                        MessageTemplateAction(
                                            label='簡介',
                                            text='@{i}/簡介',
                                        ),
                                    ]
                                )for i in range(num) for col in ['Name','Address']
                            ]
                        )
                    )
                    line_bot_api.reply_message(event.reply_token,message)
                    if mtext.startswith('@') and mtext.split('/')[1] == '簡介':
                        try:
                            pin = int(mtext.split('/')[0].replace('@', ''))
                            message = TextSendMessage(
                                text = df3.iloc[pin]['Introduce']
                            )
                            line_bot_api.reply_message(event.reply_token,message)
                        except:
                            line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
                except:
                    line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
        elif tab == 1:
            with connect_db.cursor() as cursor:

                sql = """
                SELECT Name, Info, Address, Room, Lowest_p, Highest_p, Restaurant
                FROM Living
                WHERE Areacode = ? AND Type = ?
                """
                cursor.execute(sql,(ar,tp))
                data1 = cursor.fetchall()
                df1 = pd.DataFrame(data1, columns=['Name', 'Info','Address','Room','Lowest_p', 'Highest_p', 'Restaurant'])

            num=df1.shape[0]
            pin=None

            if num == 0:
                try:
                    message = TextSendMessage(
                        text = '這個區域沒有您想要查詢的資料'
                    )
                    line_bot_api.reply_message(event.reply_token,message)
                except:
                    line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))
            else:
                try:
                    message = TemplateSendMessage(
                        alt_text='轉盤樣板',
                        template=CarouselTemplate(
                            columns=[
                                CarouselColumn(
                                    title=f"{col}\n{df1.iloc[i][col]}"
                                ) for i in range(num) for col in ['Name', 'Info', 'Address', 'Room', 'Lowest_p', 'Highest_p', 'Restaurant']
                            ]
                        )
                    )
                    line_bot_api.reply_message(event.reply_token,message)
                except:
                    line_bot_api.reply_message(event.reply_token,TextMessage(text='發生錯誤!'))

    # get X-Line-Signature header value
    signature = event['headers']['x-line-signature']

    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
            }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
        }
    
