{% if cookiecutter.kind == "vision" -%}
from waggle.plugin import Plugin
from waggle.data.vision import Camera
import numpy as np


def compute_mean_color(image):
    return np.mean(image, (0, 1)).astype(float)


def main():
    with Plugin() as plugin, Camera() as camera:
        for snapshot in camera.stream():
            # compute mean color
            mean_color = compute_mean_color(snapshot.data)

            # print mean color
            print(mean_color)

            # publish color
            plugin.publish("color.mean.r", mean_color[0], timestamp=snapshot.timestamp)
            plugin.publish("color.mean.g", mean_color[1], timestamp=snapshot.timestamp)
            plugin.publish("color.mean.b", mean_color[2], timestamp=snapshot.timestamp)
{% elif cookiecutter.kind == "usbserial_sensor" -%}
from waggle.plugin import Plugin
from serial import Serial


def main():
    with Plugin() as plugin, Serial("/dev/ttyUSB0", baudrate=9600) as dev:
        while True:
            print("recv", dev.readline())
{% elif cookiecutter.kind == "minimal" -%}
from waggle.plugin import Plugin


def main():
    with Plugin() as plugin:
        print("This is the start of an amazing app!")
{% elif cookiecutter.kind == "tutorial" -%}
import numpy as np
import cv2


def compute_mean_color(image):
    return np.mean(image, (0, 1)).astype(float)


def main():
    # read example image from file
    image = cv2.imread("example.jpg")

    # compute mean color
    mean_color = compute_mean_color(image)

    # print mean color
    print(mean_color)
{% elif cookiecutter.kind == "performance" -%}
import tau
import numpy as np
import cv2


def compute_mean_color(image):
    return np.mean(image, (0, 1)).astype(float)


def main():
    # read example image from file
    image = cv2.imread("example.jpg")

    # compute mean color
    mean_color = compute_mean_color(image)

    # print mean color
    print(mean_color)
{%- endif %}


{% if cookiecutter.kind == "performance" -%}
if __name__ == "__main__":
    tau.run('main()')
{% else -%}
if __name__ == "__main__":
    main()
{%- endif %}
