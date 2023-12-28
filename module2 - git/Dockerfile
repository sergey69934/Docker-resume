# Используем базовый образ с поддержкой Python
FROM python:3.8 as builder

# Задаем рабочую директорию
WORKDIR /

# Устанавливаем необходимые утилиты для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы в рабочую директорию
COPY Resume.yml /
COPY Resume_json.py /
COPY HTML.py /

# Устанавливаем зависимости
RUN pip install pyyaml json2html

RUN python Resume_json.py
RUN python HTML.py

# Определение основной команды
CMD ["sh", "-c", "python Resume_json.py && python HTML.py"]


# Используем базовый образ с поддержкой Python
FROM python:3.8 as result

# Задаем рабочую директорию
WORKDIR /

# Копируем файлы в рабочую директорию
COPY --from=builder /Resume.html /

# Образ 2: Использует результаты сборки Образа 1
FROM nginx:1.23.2-alpine as Out

# Копируем конфиг Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Копируем файл Resume.html из Образа 1 в директорию, где Nginx ожидает файлы
COPY --from=result /Resume.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/

# Определение основной команды
CMD ["nginx", "-g", "daemon off;"]
