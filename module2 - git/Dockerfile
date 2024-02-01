# Этап 1: Сборка JSON из YAML
FROM python:3.8.18-alpine3.18 as tojson

ARG TASK_BINARY=task_linux_amd64.tar.gz

# Установка Tasks
COPY ${TASK_BINARY} /tmp/
RUN tar -xzf /tmp/${TASK_BINARY} -C /usr/local/bin/ \
    && rm /tmp/${TASK_BINARY}

RUN apk update && apk add --no-cache \
    build-base \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY Resume.yml .
COPY Resume_json.py .
COPY Taskfile.yml .

RUN pip install pyyaml

#TODO: ?
RUN task json
ENTRYPOINT ["task"]
CMD ["json"]


FROM node:alpine as html

WORKDIR /app

# Копируем .npmrc внутрь контейнера
COPY .npmrc ./

COPY --from=tojson /app/resume.json .
COPY --from=tojson /app/Taskfile.yml .

RUN npm set progress=false
RUN npm install -g resume-cli
RUN npm install -g @go-task/cli

# ДЛЯ ИЗМЕНЕНИЯ ТЕМЫ МОЖНО ПРОПИСАТЬ: npm install <theme> и --theme <theme>
RUN task html

ENTRYPOINT ["task"]
CMD ["html"]

FROM busybox as release

WORKDIR /app/result
COPY --from=html /app/resume.html .
