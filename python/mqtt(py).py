import paho.mqtt.client as mqtt
import sqlite3

# MQTT 設定
MQTT_SERVER = "192.168.0.15"
MQTT_PORT = 1883
MQTT_ID = "windows_11"  # 將 ID 改為 windows_11
MQTT_USERNAME = "lmr0811"
MQTT_PASSWORD = "Tonylmr0811"

# SQLite 數據庫
DATABASE = 'mqtt_messages.db'

# 設置 MQTT 客戶端
client = mqtt.Client()  # 只創建一個客戶端，不傳遞 MQTT_ID

client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# 訂閱回調函數
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
    save_message_to_db(msg.topic, msg.payload.decode())

# 保存消息到 SQLite 數據庫
def save_message_to_db(topic, message):
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS messages (topic TEXT, message TEXT)''')
        c.execute("INSERT INTO messages (topic, message) VALUES (?, ?)", (topic, message))
        conn.commit()
        print(f"Message saved to DB: {topic} - {message}")
    except sqlite3.Error as e:
        print(f"Error saving message to DB: {e}")
    finally:
        conn.close()

# MQTT 客戶端設置
client.on_message = on_message

# 連接到 MQTT 伺服器
client.connect(MQTT_SERVER, MQTT_PORT)

# 訂閱 MQTT 主題
client.subscribe("com/tony")

# 開始 MQTT 迴圈，持續監聽訊息
client.loop_forever()
