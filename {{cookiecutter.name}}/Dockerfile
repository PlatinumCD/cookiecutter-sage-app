{% if cookiecutter.kind == "vision" -%}
FROM waggle/plugin-base:1.1.1-ml
{%- elif cookiecutter.kind == "usbserial_sensor" -%}
FROM python:3.11
{%- elif cookiecutter.kind == "minimal" -%}
FROM python:3.11
{%- elif cookiecutter.kind == "tutorial" -%}
FROM waggle/plugin-base:1.1.1-ml
{%- elif cookiecutter.kind == "performance" -%}
# Performance Container w/ binaries instead of python:3.11
FROM python:3.11 
{%- endif %}

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

{% if cookiecutter.kind == "performance" -%}
ENTRYPOINT ["time", "python3", "main.py"]
{%- else -%}
ENTRYPOINT ["python3", "main.py"]
{%- endif %}
