from distutils.log import ERROR
import sys
import time
import smbus

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    lineRes = event.message.text
    i2c = smbus.SMBus(1)
    address = 0x5c
    

    if lineRes == '気温教えて':
            try:
                            #スリーブ解除
                            i2c.write_i2c_block_data(address,0x00,[])                                          
            except:
                        try:
                            pass
                            # 読み取り命令
                            time.sleep(0.003)
                            i2c.write_i2c_block_data(address,0x03,[0x00,0x04])
                            # データ受取
                            time.sleep(0.015)
                            block = i2c.read_i2c_block_data(address,0,6)
                            humidity = float(block[2] << 8 | block[3])/10
                            temperature = float(block[4] << 8 | block[5])/10
                            # 読み取り結果を設定
                            linePost ='温度={0:0.1f}℃ 湿度={1:0.1f}%'.format(temperature, humidity)   
                        except:
                            linePost ="エラーが発生しました.もう一度やり直してください"    
    else:
        linePost = "「気温教えて」と入力してください"    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=linePost))


if __name__ == "__main__":
    app.run()