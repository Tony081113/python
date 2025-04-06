import paho.mqtt.client as mqtt
import requests
import time
import ssl
import logging
import textwrap
import os  # 新增导入 os 模块

# 设置日志
logging.basicConfig(filename='mqtt_news_publisher.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# MQTT 回调函数
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected successfully to Adafruit IO.")
    else:
        logging.error(f"Failed to connect, return code {rc}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        logging.warning("Unexpected disconnection.")
    else:
        logging.info("Disconnected successfully.")

def on_publish(client, userdata, mid):
    logging.info(f"Message with mid {mid} published successfully.")

# 获取和发布新闻
def get_news(api_key):
    logging.debug("Fetching news from API")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    news_content = [f"Title: {article['title']}\nDescription: {article['description']}\n" for article in articles]
    full_news = "\n".join(news_content)
    logging.debug(f"Fetched news content: {full_news[:500]}...")  # 显示部分内容
    return full_news

def publish_news(client, topic, news_content):
    parts = textwrap.wrap(news_content, 1024, replace_whitespace=False)
    for part in parts:
        client.publish(topic, part)
        logging.debug(f"Published news part: {len(part)} bytes")

# Adafruit IO MQTT 设置
broker_address = "io.adafruit.com"
port = 8883
username = "yayayayayaya"
aio_key = "aio_Qphk35heUaR9hKB5A8m0hfJ4l376"
topic = f"{username}/feeds/mqtt-news"

client = mqtt.Client("NewsPublisher")
client.username_pw_set(username, aio_key)
client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)
client.tls_insecure_set(False)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

try:
    client.connect(broker_address, port=port)
    client.loop_start()

    # 从环境变量中获取 API 金钥
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        logging.error("API key not found. Please set the NEWS_API_KEY environment variable.")
        raise ValueError("API key not found")

    while True:
        news_content = get_news(api_key)
        publish_news(client, topic, news_content)
        time.sleep(600)  # 休眠 600 秒 (10 分钟)

except KeyboardInterrupt:
    logging.info("Program stopped manually")

finally:
    client.loop_stop()
    client.disconnect()
