"""pycolorpicker - setup.py"""
import setuptools

LONG_DESC = open('README.md').read()

setuptools.setup(
    name="pycolorpicker",
    version="1.0",
    author="Lorenz Leitner",
    author_email="lrnz.ltnr@gmail.com",
    description="Python Color Picker",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    url="https://github.com/lolei/pycolorpicker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": [
        "pycolorpicker=pycolorpicker:main"]},
    python_requires=">=3.6",
    install_requires=[
        'pyautogui',
        'pyperclip',
        'pynput',
    ],
)
