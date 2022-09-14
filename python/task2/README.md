#### Задание

Реализуйте класс CountVectorizer, имеющий
- метод fit_transform 
    принимает текстовый корпус
    возвращает терм-документную матрицу
- метод get_feature_names
    ничего не принимает
    возвращает список фичей (уникальных слов из корпуса)

#### Условия:
- пользоваться внешними пакетами запрещено
- решение должно быть в *.py файлах
- не должно быть замечаний по PEP8
- если умеешь, то напиши проверки/тесты

#### Пример решения
```
corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
# Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
#       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

print(count_matrix)
# Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
```

#### Примечание
Реализация не учитывает знаки препинания, т.е. для корректной работы должен подаваться текст без них.
