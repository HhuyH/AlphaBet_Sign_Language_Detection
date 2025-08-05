# American Sign Language Recognition (33 Classes)

Dự án nhận diện ngôn ngữ ký hiệu ASL sử dụng Convolutional Neural Network (CNN).  
Dữ liệu được **tự thu thập và xử lý thủ công**, qua nhiều bước tối ưu, đạt độ chính xác cuối cùng **94.62%**.

---

## 📌 Giới thiệu

Ban đầu, mô hình được thử nghiệm với **Random Forest Classifier (RFC)** trên dữ liệu khung hình đầy đủ nhưng không tổng quát hoá được trên nhiều người dùng. Sau đó nhóm chuyển hướng:

1. **Thu thập lại dữ liệu** chỉ vùng bàn tay.
2. **Xử lý background** và áp dụng **augmentation**.
3. Chuyển sang **CNN** để khai thác đặc trưng ảnh tốt hơn.

Kết quả cuối cùng đạt **94.62% accuracy** trên 33 ký hiệu.

---

## 🚀 Tính năng

- Nhận diện **33 ký hiệu** trong ngôn ngữ ký hiệu tiếng Việt.
- Pipeline xử lý:
  - Loại bỏ background.
  - Crop vùng bàn tay.
  - Data augmentation (xoay, lật, thay background).
- Huấn luyện CNN với Keras/TensorFlow.

---

## 📊 Kết quả

- **Accuracy cuối cùng:** 94.62%
- Dataset gồm **33 lớp (0–32)**, hàng nghìn mẫu mỗi lớp.
- Dưới đây là số liệu ví dụ một số lớp:

### Accuracy & Loss
![Training Curve](results/Test%20loss%20and%20accuracy%20(CNN).png)


### Metrics chi tiết
Xem số liệu đầy đủ tại [metrics.txt](results/metrics.txt)


> Xem toàn bộ chi tiết trong file `metrics.txt` (hoặc notebook).

### Gợi ý hình minh hoạ:
- **GIF demo**: real-time dự đoán ký hiệu bằng camera.
- **Ảnh confusion matrix**: trực quan độ chính xác từng lớp.
- **Ảnh accuracy/loss curve**: quá trình train.

---

## 🛠 Cài đặt

### Yêu cầu
- Python 3.11.9
- TensorFlow/Keras
- OpenCV
- NumPy, Matplotlib

Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

---

## ▶️ Cách chạy

Hiện dự án được triển khai trong **một notebook duy nhất**:  
`Convolutional Neural Network.ipynb`

### 1. Chuẩn bị môi trường
Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

### 2. Chuẩn bị dữ liệu
- Nếu muốn huấn luyện từ đầu:
  - Chuẩn bị dữ liệu theo cấu trúc:
  ```
  (dữ liệu từ 0-9 từ a-z)
  data_cnn/
    ├── 0/
    ├── 1/
    ├── ...
    └── z/
  ```
  - Chạy các cell **thu thập ảnh** và **xử lý background** trong notebook.

- Nếu đã có file `.npy` (ví dụ `X_train(full_data).npy` và `Y_train(full_data).npy`):
  - Bỏ qua bước thu thập và xử lý.
  - Chạy trực tiếp phần **tách train/test** và **train CNN**.

### 3. Huấn luyện và đánh giá
- Chạy toàn bộ notebook theo thứ tự các cell.
- Kết quả cuối:
  - Accuracy ~94.62%
  - Confusion matrix, báo cáo precision/recall từng lớp.

### 4. Demo
- Có thể chỉnh notebook để dự đoán **real-time** qua camera:
  - Sử dụng Mediapipe + OpenCV.
  - Thay cell `collect image` bằng capture webcam và dùng model đã train để predict.

---

## 📂 Dataset

Dataset.

- **Cấu trúc dataset**:
  ```
  (dữ liệu từ 0-9 từ a-z)
  data_cnn/
    ├── 0/
    ├── 1/
    ├── ...
    └── z/
  ```

- Mỗi thư mục là 1 ký hiệu, chứa ảnh đã crop bàn tay.  
- Có thể cung cấp link Google Drive sau nếu cần.

---

## 🔮 Hướng phát triển

- Tối ưu mô hình cho **real-time trên thiết bị di động**.
- Mở rộng bộ ký hiệu hoặc tích hợp thành ứng dụng học ngôn ngữ ký hiệu.

---
