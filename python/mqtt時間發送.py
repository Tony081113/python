import paho.mqtt.client as mqtt
import time
from datetime import datetime
import ssl
import logging

# 设置日志
logging.basicConfig(filename='mqtt_time_publisher.log', 
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Adafruit IO MQTT 伺服器设置
broker_address = "io.adafruit.com"
port = 8883
username = "yayayayayaya"
aio_key = "aio_Qphk35heUaR9hKB5A8m0hfJ4l376"
topic = "yayayayayaya/feeds/mqtt-kebbi"

# 创建一个 MQTT 客户端实例
client = mqtt.Client("TimePublisher")
client.username_pw_set(username, aio_key)

# 配置 SSL/TLS
client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLS, ciphers=None)
client.tls_insecure_set(False)

# 连接到 MQTT 服务器
client.connect(broker_address, port=port)
logging.info("Connected to Adafruit IO MQTT broker")

# 发送时间的函数
def publish_time():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")  # 获取当前时间并格式化为时:分
        client.publish(topic, current_time)  # 发布时间到指定主题
        logging.info(f"Published {current_time} to topic {topic}")
        time.sleep(60)  # 每60秒发送一次

try:
    publish_time()  # 开始发送时间
except KeyboardInterrupt:
    logging.info("Program stopped by user")
    client.disconnect()  # 断开 MQTT 连接
