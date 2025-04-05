import cv2

# 開啟攝像頭
cap = cv2.VideoCapture(0)

# 載入人臉辨識模型
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 檢查攝像頭是否成功開啟
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # 讀取攝像頭的影格
    ret, frame = cap.read()

    # 檢查影格是否成功讀取
    if not ret:
        print("Cannot receive frame")
        break

    # 縮小影格尺寸，避免尺寸過大導致效能不佳
    frame = cv2.resize(frame, (480, 300))

    # 將影格轉換為灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測人臉
    faces = face_cascade.detectMultiScale(gray)

    # 對每個偵測到的人臉進行馬賽克處理
    for (x, y, w, h) in faces:
        # 取得人臉區域
        mosaic = frame[y:y+h, x:x+w]

        # 設定馬賽克程度
        level = 15

        # 計算馬賽克區塊的大小
        mh = int(h / level)
        mw = int(w / level)

        # 縮小馬賽克區塊
        mosaic = cv2.resize(mosaic, (mw, mh), interpolation=cv2.INTER_LINEAR)

        # 放大馬賽克區塊
        mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)

        # 將馬賽克區塊貼回原影格中
        frame[y:y+h, x:x+w] = mosaic

    # 顯示處理後的影格
    cv2.imshow('you can not see me', frame)

    # 按下 q 鍵停止程式
    if cv2.waitKey(1) == ord('q'):
        break

# 釋放攝像頭資源
cap.release()

# 關閉視窗
cv2.destroyAllWindows()
