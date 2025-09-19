# OnePSE
## Переводы ReadMe
[Русская версия](README-ru.md) [English version](README.md)
## Об проекте
*OnePSE* - Бесплатный, с открытым исходным кодом, Игровой движок на Python с использованием графического движка SDL
Данный проект создается одним человеком, а именно CodCatDev (12 лет), потому каждая звезда на Github - огромная мотивация для создателя!

Проект изначально был задуман как игра на Sdl2, но вскоре из за сложности sdl2 зародился этот движок, для упрощения работы с этим графическим движком.

## Примеры
Создание окна
```python
import onepse
app = onepse.CreateWindow() # Рендер окна
app.Show() # Показ окна
```

Вывод текста на экран
```python
import onepse
app = onepse.CreateWindow(title="Text render", size=(400,200)) # Рендер окна
app.Show() # Показ окна
app.Work() # Ожидание ивентов.
run = True
text = onepse.Text("Hello, Wolrd!", size=16) #  Создание текста
app.Render(text, pos=(200,100)) # Рендер текста на центре экрана
while run: # Главный цикл
    if app.QuitEvent(): # Проверка на выход и завершение программы
        run = False
```