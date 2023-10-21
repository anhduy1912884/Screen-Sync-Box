from PIL import ImageGrab
import serial
import time

# Định nghĩa cổng COM (thay COM4 bằng cổng COM thực tế)
ser = serial.Serial('COM22', 9600, timeout=1)

while True:
    # Tọa độ của điểm ảnh bạn muốn kiểm tra
    x1 = 300
    y1 = 300
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x1, y1))
    r1, g1, b1 = pixel_color
    # ser.write(bytes([r1, g1, b1]))
    # time.sleep(0.001)

    x2 = 1600
    y2 = 300
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x2, y2))
    r2, g2, b2 = pixel_color
    ser.write(bytes([r1, g1, b1, r2, g2, b2]))
    time.sleep(0.02)


# Đóng cổng COM sau khi kết thúc
ser.close()
