from setuptools import setup, find_packages

setup(
    name='Webcam Adaptive Brightness App',
    version='1.0.0',
    description='A webcam-based adaptive-brightness application built using OpenCV2 and Python 3',
    author='Ehren Castillo & Lejand Coralde',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'comtypes>=1.1.11',
        'customtkinter>=2.3',
        'darkdetect>=0.5.1',
        'numpy>=1.22.2',
        'opencv-python>=4.5.5.62',
        'Pillow>=9.0.1',
        'pygrabber>=0.1',
        'pystray>=0.19.2',
        'pywin32>=303',
        'six>=1.16.0',
        'toml>=0.10.2',
        'WMI>=1.5.1',
    ]
)