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
    
