{%- if cookiecutter.base_image == "Waggle AI / ML" -%}
FROM waggle/plugin-base:1.1.1-ml
{%- elif cookiecutter.base_image == "Waggle Minimal" -%}
FROM waggle/plugin-base:1.1.1-base
{%- elif cookiecutter.base_image == "Python 3.11" -%}
FROM python:3.11
{%- endif %}

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
