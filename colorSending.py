from PIL import ImageGrab
import serial
import time

# Định nghĩa cổng COM (thay COM4 bằng cổng COM thực tế)
ser = serial.Serial('COM25', 115200, timeout=1)

# Danh sách các tọa độ x và y
coordinates = [
    (150, 900), (150, 750), (150, 600), (150, 450), (150, 300),
    (150, 150), (310, 150), (470, 150), (630, 150), (790, 150),
    (950, 150), (1110, 150), (1270, 150), (1430, 150), (1590, 150),
    (1750, 150), (1750, 300), (1750, 450), (1750, 600), (1750, 750), (1750, 900)
]

try:
    while True:
        for x, y in coordinates:
            screenshot = ImageGrab.grab()
            pixel_color = screenshot.getpixel((x, y))
            r, g, b = pixel_color
            print(f"r: {r}")
            ser.write(bytes([r, g, b]))

            # Đợi để đảm bảo Arduino xử lý
            time.sleep(0.02)
except KeyboardInterrupt:
    print("Đã dừng chương trình.")

# Đóng cổng COM sau khi kết thúc
ser.close()
