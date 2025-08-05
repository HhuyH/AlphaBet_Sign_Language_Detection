import cv2
import os
import mediapipe as mp

dataset_dir = "test"
os.makedirs(dataset_dir, exist_ok=True)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cap.set(cv2.CAP_PROP_AUTO_WB, 1)  # Bật auto white balance
cap.set(cv2.CAP_PROP_WB_TEMPERATURE, 4500)  # Reset nhiệt độ màu về mức trung bình
cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.6)  
cap.set(cv2.CAP_PROP_CONTRAST, 0.6)  
cap.set(cv2.CAP_PROP_SATURATION, 0.6)  
cap.set(cv2.CAP_PROP_EXPOSURE, -4)  # Giảm phơi sáng nếu quá sáng  


counter = len(os.listdir(dataset_dir))  # Đếm số ảnh đã có

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    cv2.putText(frame, "Press SPACE to capture, 'q' to exit", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Camera', frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # Nhấn SPACE để chụp ảnh
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x_min, y_min, x_max, y_max = 640, 480, 0, 0
                for lm in hand_landmarks.landmark:
                    x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                    x_min, y_min = min(x_min, x), min(y_min, y)
                    x_max, y_max = max(x_max, x), max(y_max, y)
                
                # Tính toán vùng chứa bàn tay với khoảng lề nhỏ
                padding = 20
                x_min, y_min = max(x_min - padding, 0), max(y_min - padding, 0)
                x_max, y_max = min(x_max + padding, frame.shape[1]), min(y_max + padding, frame.shape[0])
                
                hand_img = frame[y_min:y_max, x_min:x_max]
                if hand_img.size > 0:
                    img_path = os.path.join(dataset_dir, f"{counter}.jpg")
                    cv2.imwrite(img_path, hand_img)
                    print(f"Saved: {img_path}")
                    counter += 1
    elif key == ord('q'):  # Nhấn 'q' để thoát
        break

cap.release()
cv2.destroyAllWindows()