# 引入所需的庫
import cv2  # 用於影像處理
import pytesseract  # 用於文字辨識

# 設定 Tesseract 的安裝路徑（根據你的安裝位置調整）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 開啟 webcam，0 代表第一個攝影機
cap = cv2.VideoCapture(0)

# 檢查攝影機是否成功開啟
if not cap.isOpened():
    print("無法開啟攝影機")
    exit()

while True:
    # 讀取攝影機畫面
    ret, frame = cap.read()
    
    # 檢查是否成功讀取畫面
    if not ret:
        print("無法讀取畫面")
        break

    # 將畫面轉為灰階圖像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用 Tesseract 辨識車牌上的文字
    # 設定參數以提高辨識率
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray, config=custom_config)

    # 在畫面上顯示辨識結果
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 顯示畫面
    cv2.imshow('License Plate Recognition', frame)

    # 按下 'q' 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()
