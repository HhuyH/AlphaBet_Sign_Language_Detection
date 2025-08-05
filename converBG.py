from PIL import Image
import os

# Chuyển ảnh từ jpeg thanh jpg
INPUT_FOLDER = "./images"  # Thư mục chứa ảnh JPEG
OUTPUT_FOLDER = "./Convert_images"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    if file.lower().endswith((".jpeg", ".jpg")):
        img_path = os.path.join(INPUT_FOLDER, file)
        img = Image.open(img_path)
        img = img.convert("RGB")  # Đảm bảo không bị lỗi định dạng
        
        output_path = os.path.join(OUTPUT_FOLDER, file.replace(".jpeg", ".jpg"))
        img = img.resize((1024, 768))  # Giảm size ảnh
        
        # Nén ảnh: giảm chất lượng nhưng không mất nhiều chi tiết
        img.save(output_path, "JPEG", quality=70, optimize=True)  # Có thể thử quality=70-85

print(f"✅ Đã chuyển và nén ảnh, lưu tại: {OUTPUT_FOLDER}")
