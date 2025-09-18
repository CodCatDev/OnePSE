import os
import pathlib
class _PATH:
    _ENGINE = pathlib.Path(__file__).resolve().parent.__str__()
VER = "SDL-2.32.10"
os.environ["PYSDL2_DLL_PATH"] = f"{_PATH._ENGINE}\\lib\\{VER}"
import sdl2 as sdl
import sdl2.ext as sdlext

sdlext.init()
window = sdlext.Window("OnePSE Debug", size=(640, 480))  # Создаем окно
window.show()
running = True
icon = f"{_PATH._ENGINE}\\res\\debugIcon.png"
surface = sdlext.load_image(icon)
sdl.SDL_SetWindowIcon(window.window, surface)
sdl.SDL_FreeSurface(surface)
while running:
        # 4. Обработка событий
        events = sdlext.get_events()  # Получаем список событий
        for event in events:
            if event.type == sdl.SDL_QUIT:  # Проверяем, не было ли события закрытия окна
                running = False  # Завершаем цикл
                break  # Выходим из цикла обработки событий

        # 5. Пауза (чтобы не перегружать процессор)
        sdl.SDL_Delay(10)
