from PIL import ImageGrab
import serial
import time

# Định nghĩa cổng COM (thay COM4 bằng cổng COM thực tế)
ser = serial.Serial('COM25', 57600, timeout=1)
'''
# Độ phân giải Full HD
full_hd_width = 1920
full_hd_height = 1080

# Tọa độ trung tâm của màn hình Full HD
x = full_hd_width // 2
y = full_hd_height // 2
'''
def get_pixel_color(x, y):
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x, y))
   # Chụp màn hình và lấy màu sắc tại tọa độ x, y
    #screenshot = ImageGrab.grab(bbox=(0, 0, full_hd_width, full_hd_height))
    #pixel_color = screenshot.getpixel((x, y))
    r, g, b = pixel_color
    return r, g, b
def average_color (x,y) :
    distance = 80
    r_top , g_top , b_top = get_pixel_color ( x + distance, y + distance)
    r , g , b = get_pixel_color(x,y)
    r_bot , g_bot , b_bot = get_pixel_color(x - distance , y - distance)
    r_ave = (r_top + r + r_bot)//3
    g_ave = (g_top + g + g_bot)//3
    b_ave = (b_top + b + b_bot)//3
    return r_ave , g_ave , b_ave
x0 = 150
y0 = 900
x1 = 150
y1 = 530
x2 = 150
y2 = 150
x3 = 800
y3 = 200
x4 = 950
y4 = 200
x5 = 1500
y5 = 200
x6 = 1800
y6 = 150
x7 = 1800
y7 = 530
x8 = 1800
y8 = 900
'''
x0 = 2650
y0 = 1100

x1 = 2650
y1 = 650

x2 = 2650
y2 = 300

x3 = 3000
y3 = 300

x4 = 3550
y4 = 300

x5 = 4000
y5 = 300

x6 = 4500
y6 = 300

x7 = 4500
y7 = 650

x8 = 4500
y8 = 1100
'''


while True:
    r0, g0, b0 = average_color(x0, x0)
    r1, g1, b1 = average_color(x1, y1)
    r2, g2, b2 = average_color(x2, y2)
    r3, g3, b3 = average_color(x3, y3)
    r4, g4, b4 = average_color(x4, y4)
    r5, g5, b5 = average_color(x5, y5)
    r6, g6, b6 = average_color(x6, y6)
    r7, g7, b7 = average_color(x7, y7)
    r8, g8, b8 = average_color(x8, y8)
    
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


    time.sleep(0.001)

# Đóng cổng COM sau khi kết thúc
ser.close()