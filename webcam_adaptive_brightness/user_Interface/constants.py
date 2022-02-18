import ctypes

COLOR = {
    'black'         :'#000000',
    'dark_gray_1'   :'#141414',
    'dark_gray_2'   :'#262626',
    'dark_gray_3'   :'#383838',
    'dark_gray_4'   :'#4A4A4A',
    'dark_gray_5'   :'#5C5C5C',
    'light_gray_1'  :'#9A9A9A',
    'white'         :'#FFFFFF',

    'highlight':'#c7e2f2',
    'fg'    :'#5B9BD5',
    'hover' :'#364A5B',
    'error' :'#FF5050',
}

SCALE_FACTOR = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
TEXT_FACTOR = 1 / SCALE_FACTOR
