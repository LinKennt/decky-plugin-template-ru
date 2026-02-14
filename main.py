import os

# Модуль плагина decky находится в decky-loader/plugin
# Для удобства использования intellisense проверьте код репозитория decky-loader
# и добавьте путь `decky-loader/plugin/imports` в `python.analysis.extraPaths` в `.vscode/settings.json`
# Перевод. Прим.: Комментарий выглядит как осколок легаси - ему 3 года, и редактировался почти 2 назад.
# В `.vscode/defsettings.json` же для `python.analysis.extraPaths` указан путь `./py_modules`.
import decky
import asyncio

class Plugin:
    # Обычный метод. Его можно вызвать со стороны TypeScript, используя @decky/api.
    async def add(self, left: int, right: int) -> int:
        return left + right

    async def long_running(self):
        await asyncio.sleep(15)
        # Прохождение через кучу случайных данных, просто в качестве примера
        await decky.emit("timer_event", "Hello from the backend!", True, 2)

    # Asyncio-совместимый долгоиграющий код, выполняется в задаче при загрузке плагина
    async def _main(self):
        self.loop = asyncio.get_event_loop()
        decky.logger.info("Hello World!")

    # Функция, вызываемая первой во время процесса выгрузки, используйте её для обработки остановки вашего плагина,
    # но не полного удаления
    async def _unload(self):
        decky.logger.info("Goodnight World!")
        pass

    # Функция, вызываемая после `_unload` во время удаления, используйте её для очистки процессов и других остатков вашего
    # плагина, что могли остаться в системе
    async def _uninstall(self):
        decky.logger.info("Goodbye World!")
        pass

    async def start_timer(self):
        self.loop.create_task(self.long_running())

    # Миграции, которые следует выполнить до входа в `_main()`.
    async def _migration(self):
        decky.logger.info("Миграция")
        # Вот пример миграции журналов:
        # - `~/.config/decky-template/template.log` будет перенесено в `decky.decky_LOG_DIR/template.log`
        decky.migrate_logs(os.path.join(decky.DECKY_USER_HOME,
                                               ".config", "decky-template", "template.log"))
        # Вот пример миграци настроек:
        # - `~/homebrew/settings/template.json` переносится в `decky.decky_SETTINGS_DIR/template.json`
        # - `~/.config/decky-template/` все файлы и каталоги под этим корнем переносятся в `decky.decky_SETTINGS_DIR/`
        decky.migrate_settings(
            os.path.join(decky.DECKY_HOME, "settings", "template.json"),
            os.path.join(decky.DECKY_USER_HOME, ".config", "decky-template"))
        # Вот пример миграци данных среды выполнения:
        # - `~/homebrew/template/` все файлы и каталоги под этим корнем переносятся в `decky.decky_RUNTIME_DIR/`
        # - `~/.local/share/decky-template/` все файлы и каталоги под этим корнем переносятся в `decky.decky_RUNTIME_DIR/`
        decky.migrate_runtime(
            os.path.join(decky.DECKY_HOME, "template"),
            os.path.join(decky.DECKY_USER_HOME, ".local", "share", "decky-template"))
