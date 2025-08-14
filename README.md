# American Sign Language Recognition (33 Classes)

Dự án nhận diện ngôn ngữ ký hiệu ASL sử dụng Convolutional Neural Network (CNN).  
Dữ liệu được **tự thu thập và xử lý thủ công**, qua nhiều bước tối ưu, đạt độ chính xác cuối cùng **94.62%**.

---

## 📌 Giới thiệu

Dự án này tập trung vào **nhận diện ngôn ngữ ký hiệu ASL (33 ký hiệu)** bằng **Convolutional Neural Network (CNN)**, với mục tiêu hỗ trợ giao tiếp cho cộng đồng người khiếm thính.

Ban đầu, mô hình được thử nghiệm với **Random Forest Classifier (RFC)** trên dữ liệu khung hình đầy đủ, nhưng không tổng quát hoá tốt với nhiều người dùng. Để cải thiện, dự án đã:

1. **Thu thập dữ liệu mới** chỉ tập trung vào vùng bàn tay.
2. **Xử lý background và data augmentation** (xoay, lật, thay background) để tăng tính đa dạng của dữ liệu.
3. **Chuyển sang CNN**, khai thác đặc trưng ảnh tốt hơn, đạt **94.62% accuracy** trên 33 ký hiệu.

Hiện tại, dự án **tập trung vào thu thập dữ liệu, train mô hình và demo nhận diện ký tự**. Tầm nhìn dài hạn là phát triển thành **ứng dụng di động hoàn chỉnh**, cho phép tổng hợp câu, chuẩn hóa bằng LLM và hỗ trợ phát âm Text-to-Speech, hoặc ngược lại từ lời nói sang ký hiệu cho người khiếm thính.

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

### GIF demo
![Demo](results/Demo.gif)


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

Ban đầu, dự án hướng tới việc phát triển một **ứng dụng di động hoàn chỉnh**, có khả năng:

1. **Thu thập từng ký tự** từ người dùng thông qua camera, sử dụng Computer Vision để nhận diện.
2. **Tổng hợp và chuẩn hóa câu** từ các ký tự nhận diện, sử dụng mô hình LLM để hiển thị câu hoàn chỉnh trên màn hình điện thoại.
3. **Phát âm câu** thông qua giọng nói nhân tạo (Text-to-Speech) để hỗ trợ giao tiếp.
4. **Chiều ngược lại**: từ lời nói của người bình thường, dịch sang ngôn ngữ ký hiệu cho người khiếm thính.

Do **thời gian và nguồn lực hạn chế**, hiện tại dự án **chỉ dừng ở mức thu thập dữ liệu, train CNN và demo nhận diện ký tự riêng lẻ** (xem GIF demo).

Tuy nhiên, tầm nhìn dài hạn vẫn là:

* Mở rộng thành một **hệ thống giao tiếp toàn diện giữa người khiếm thính và người bình thường**.
* Tối ưu mô hình cho **real-time trên thiết bị di động**.
* Mở rộng bộ ký hiệu, kết hợp với **text-to-speech** và **LLM để chuẩn hóa câu**, tạo trải nghiệm trực quan và tương tác cao.

