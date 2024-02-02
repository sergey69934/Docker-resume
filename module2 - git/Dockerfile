# Этап 1: Сборка JSON из YAML
FROM python:3.8.18-alpine3.18 as builder

ARG TASK_BINARY=task_linux_amd64.tar.gz

# Установка Tasks
COPY ${TASK_BINARY} /tmp/
RUN tar -xzf /tmp/${TASK_BINARY} -C /usr/local/bin/ \
    && rm /tmp/${TASK_BINARY}

RUN apk update && apk add --no-cache \
    build-base \
    npm \
    && rm -rf /var/cache/apk/*

RUN npm set progress=false
RUN pip install pyyaml

RUN npm install -g resume-cli

WORKDIR /app

COPY Resume.yml .
COPY Resume_json.py .
COPY Taskfile.yml .

FROM builder as build
WORKDIR /app
RUN task html
ENTRYPOINT ["task"]
CMD ["html"]

FROM busybox as release

WORKDIR /app/result
COPY --from=build /app/resume.html .
