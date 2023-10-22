from PIL import ImageGrab
import serial
import time

# Định nghĩa cổng COM (thay COM4 bằng cổng COM thực tế)
ser = serial.Serial('COM25', 9600, timeout=1)

def get_pixel_color(x, y):
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x, y))
    r, g, b = pixel_color
    return r, g, b

x0 = 150
y0 = 900

x1 = 150
y1 = 750

x2 = 150
y2 = 600

x3 = 150
y3 = 450

x4 = 150
y4 = 300

x5 = 150
y5 = 150

x6 = 310
y6 = 150

x7 = 470
y7 = 150

x8 = 630
y8 = 150

x9 = 790
y9 = 150

x10 = 950
x10 = 150

while True:
    # Tọa độ của điểm ảnh bạn muốn kiểm tra
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x0, y0))
    r0, g0, b0 = pixel_color
    
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x1, y1))
    r1, g1, b1 = pixel_color
    # ser.write(bytes([r1, g1, b1]))
    # time.sleep(0.001)

    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x2, y2))
    r2, g2, b2 = pixel_color

    r3, g3, b3 = get_pixel_color(x3, y3)
    r4, g4, b4 = get_pixel_color(x4, y4)
    r5, g5, b5 = get_pixel_color(x5, y5)
    r6, g6, b6 = get_pixel_color(x6, y6)
    r7, g7, b7 = get_pixel_color(x7, y7)
    r8, g8, b8 = get_pixel_color(x8, y8)

    ser.write(bytes([
    r0, g0, b0,
    r1, g1, b1, 
    r2, g2, b2,
    r3, g3, b3,
    r4, g4, b4,
    r5, g5, b5,
    r6, g6, b6,
    r7, g7, b7,
    r8, g8, b8
    ]))
    time.sleep(0.005)


# Đóng cổng COM sau khi kết thúc
ser.close()