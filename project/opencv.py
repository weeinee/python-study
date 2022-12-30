import PySimpleGUI as sg
import cv2

# 背景色
sg.theme('LightGreen')

# 定义窗口布局
layout = [
    [sg.Image(filename='', key='image')],
    [sg.Radio('None', 'Radio', True, size=(10, 1))],
    [sg.Radio('threshold', 'Radio', size=(10, 1), key='thresh'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(40, 15), key='thresh_slider')],
    [sg.Radio('canny', 'Radio', size=(10, 1), key='canny'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='canny_slider_a'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='canny_slider_b')],
    [sg.Radio('contour', 'Radio', size=(10, 1), key='contour'),
     sg.Slider((0, 255), 128, 1, orientation='h', size=(20, 15), key='contour_slider'),
     sg.Slider((0, 255), 80, 1, orientation='h', size=(20, 15), key='base_slider')],
    [sg.Radio('blur', 'Radio', size=(10, 1), key='blur'),
     sg.Slider((1, 11), 1, 1, orientation='h', size=(40, 15), key='blur_slider')],
    [sg.Radio('hue', 'Radio', size=(10, 1), key='hue'),
     sg.Slider((0, 225), 0, 1, orientation='h', size=(40, 15), key='hue_slider')],
    [sg.Radio('enhance', 'Radio', size=(10, 1), key='enhance'),
     sg.Slider((1, 255), 128, 1, orientation='h', size=(40, 15), key='enhance_slider')],
    [sg.Button('Exit', size=(10, 1))]
]

# 窗口设计
window = sg.Window('OpenCV实时图像处理',
                   layout,
                   location=(800, 400),
                   finalize=True)

# 打开内置摄像头
cap = cv2.VideoCapture(0)
while True:
    event, values = window.read(timeout=0, timeout_key='timeout')

    # 实时读取图像
    ret, frame = cap.read()

    # GUI实时更新
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window['image'].update(data=imgbytes)

window.close()