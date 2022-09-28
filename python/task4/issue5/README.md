# Задание 5

Запуск тестов и генерация отчёта о покрытии запуском следующей команды из текущей директории:

```shell
python -m pytest -v test.py --cov=what_is_year_now --cov-report html > result.log
```

Отчёт располагается в директории `./htmlcov`.