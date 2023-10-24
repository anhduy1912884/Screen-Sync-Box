from PIL import ImageGrab
import serial
import time

# Định nghĩa cổng COM (thay COM4 bằng cổng COM thực tế)
ser = serial.Serial('COM25', 57600, timeout=1)

def get_pixel_color(x, y):
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x, y))
    r, g, b = pixel_color
    return r, g, b
def average_color_y (x,y) :
    distance = 100
    r_top , g_top , b_top = get_pixel_color ( x , y + distance)
    r , g , b = get_pixel_color(x,y)
    r_bot , g_bot , b_bot = get_pixel_color(x , y - distance)
    r_ave = (r_top + r + r_bot)//3
    g_ave = (g_top + g + g_bot)//3
    b_ave = (b_top + b + b_bot)//3
    return r_ave , g_ave , b_ave
def average_color_x (x,y) :
    distance = 100
    r_top , g_top , b_top = get_pixel_color ( x + distance, y )
    r , g , b = get_pixel_color(x,y)
    r_bot , g_bot , b_bot = get_pixel_color(x - distance , y)
    r_ave = (r_top + r + r_bot)//3
    g_ave = (g_top + g + g_bot)//3
    b_ave = (b_top + b + b_bot)//3
    return r_ave , g_ave , b_ave
x0 = 200
y0 = 700

x1 = 400
y1 = 250

x2 = 1450
y2 = 250

x3 = 1700
y3 = 700

while True:
    r0, g0, b0 = average_color_y(x0, x0)
    r1, g1, b1 = average_color_x(x1, y1)
    r2, g2, b2 = average_color_x(x2, y2)
    r3, g3, b3 = average_color_y(x3, y3)
    
    ser.write(bytes([
    r0, g0, b0,
    r1, g1, b1, 
    r2, g2, b2,
    r3, g3, b3  
    ]))

    time.sleep(0.001)

# Đóng cổng COM sau khi kết thúc
ser.close()