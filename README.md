#
<h1 align="center">Привет, меня зовут Сергей
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

# Yaml resume pdf
<p><font color="green">Этот репозиторий содержит yaml резюме, конвертирует его в json и создаёт html файл резюме. Затем nginx.</font></p>

## Настройка для локального использования (Можно использовать Tasks)
1. `npm install -g resume-cli`
2. `npm install jsonresume-theme-stackoverflow`
3. `resume export resume.pdf --theme=stackoverflow`
<p><font color="red">Это нужно для использования из под консоли. Также можно использовать</font> <font color="blue">Docker</font></p>

## Темы
[Можно выбрать другую тему на сайте](https://www.npmjs.com/searchranking=maintenanceq=jsonresume-theme)

Для установки нужно указать `npm install <Название темы>`

## Использование
-----

1. Написать резюме в Yaml файле как в файле Example_resume
2. Поместить его в папку "module2 - git"
3. Выполнить `py Resume_json.py`
4. Экспортировать файл в pdf формат `<имя_файла_в_формате_yaml> export <Имя_выходящего файла>.pdf --<Тема_резюме>`


На самом деле можно просто сразу писать резюме в json файле и экспортировать его в pdf

### Команды
[Также здесь есть Task](https://taskfile.dev/)

Посмотреть список команд:
```shell
task --list-all
```
Создать файл resume.json:
```shell
task json
```
Создать файл resume.html:
```shell
task html
```
Собрать Docker образ с названием "resume":
```shell
task docker-build
```
Запустить контейнер с названием "resume-nginx" (У контейнера опция --rm):
```shell
task docker-run
```
Остановить контейнер:
```shell
task task docker-stop
```
Также работа с docker-compose:
```shell
task compose-build
```
```shell
task compose-up
```
```shell
task compose-down
```
## Выполнение задания GitHub Actions
1. Создал Workflow 'CI'
2. Написал job 'build-builder'. В Dockerfile есть multi-stage build (многоэтапная сборка). В Action происходит сборка сборка стадии builder, а затем все остальные.
3. Добавил публикацию на Dockerhub (я её отключил 'push: false')
4. ![image](https://github.com/sergey69934/Docker-resume/assets/124598976/d68e5c57-a951-4827-9438-41f69a5cba69)
5. ![image](https://github.com/sergey69934/Docker-resume/assets/124598976/b4d71cdf-16ad-4442-94a1-51fefb940cc8)
6. ![image](https://github.com/sergey69934/Docker-resume/assets/124598976/25d2600a-8eab-468e-b0a0-a070ee2c0a3d)

## Дата последнего изменения
15-02-2024

