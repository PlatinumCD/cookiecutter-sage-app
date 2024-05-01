{% if cookiecutter.kind == "vision" -%}
FROM waggle/plugin-base:1.1.1-ml
{%- elif cookiecutter.kind == "usbserial_sensor" -%}
FROM python:3.11
{%- elif cookiecutter.kind == "minimal" -%}
FROM python:3.11
{%- elif cookiecutter.kind == "tutorial" -%}
FROM waggle/plugin-base:1.1.1-ml
{%- elif cookiecutter.kind == "performance" -%}
FROM waggle/plugin-base:1.1.1-ml

RUN git clone https://github.com/UO-OACISS/tau2.git /tau2

RUN cd /tau2 && \
    ./configure \
        -exec-prefix=waggle \
        -prefix=/tau  -python3 \
        -pythoninc=/usr/include/$(gcc -print-multiarch)/python3.6m \
        -pythoninc=/usr/include/python3.6 \
        -pythonlib=/usr/lib/$(gcc -print-multiarch) && \
    make install

ENV PYTHONPATH=/tau/waggle/lib
{%- endif %}

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
