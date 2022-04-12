# Lineのメッセージで気温と湿度を取得する

LINEのMessagingAPIを使用してRaspberryPiにメッセージを送信し気温と湿度の取得をします。

環境: <br>
Hard:Raspberry PiZero <br>
Sensor:AM2320

# 使用方法
## 1.センサーの取付
取付を詳しく説明してくださっているサイトがありますのでそこをもとにラズパイにセンサーの取付を行います。([参照](https://note.com/khe00716/n/n34bb4c087fdc))

## 2.Messaging APIの作成
noteにてMessagingApiとラズパイのサーバーの設定が詳しくのっている記事があります。記事があるので
この記事にそってLINEのMessagingAPIとラズパイの設定をしていきます。([参照](https://note.com/khe00716/n/n34bb4c087fdc))

app.pyに作成したMessagingAPIのチャネルシークレットとチャネルアクセストークンを設定します。


 
## 3.実行
任意のディレクトリにapp.pyを配置しflask runを実行することでLineのBotとAPIの連携は完了です。
Lineから「気温教えて」と入力することで温度と湿度が返答されれば完成です。
