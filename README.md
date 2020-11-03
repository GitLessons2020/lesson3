Базовый репозиторий для четвертой лекции

Проверить, что python работает

```bash
python --version
```
Должны увидеть версию 3+

Создать виртуальное окружение
```bash
python -m venv ./venv
```

Настроить политику PowerShell 
Решение проблемы:

1. Открываем терминал от админа.

2. Пишем и запускаем: `Set-ExecutionPolicy RemoteSigned`

3. На вопрос отвечаем: A (Да для всех)

Активировать виртуальное окружение
```bash
.\venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

Выполнить в powershell 
```bash
$env:FLASK_APP="program.py"
```

Запустить приложение

```bash
flask run
```


> Выйти из виртуального окружения - `deactivate`