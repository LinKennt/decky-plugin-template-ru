"""
Этот модуль предоставляет различные константы и вспомогательные функции, полезные для плагинов decky.

* Настройки и конфигурации плагина должны храниться в `DECKY_PLUGIN_SETTINGS_DIR`.
* Данные среды выполнения плагина должны храниться в `DECKY_PLUGIN_RUNTIME_DIR`.
* Постоянные файлы журналов плагина должны храниться в `DECKY_PLUGIN_LOG_DIR`

Избегайте записи за пределами `DECKY_HOME`, настоятельно рекомендуется хранить данные в указанных путях.

Доступны некоторые базовые вспомогательные функции для миграции: `migrate_any`, `migrate_settings`, `migrate_runtime`, `migrate_logs`.

Имеется средство логирования `logger`, которое записывает данные в рекомендуемое место.
"""

__version__ = '1.0.0'

import logging

from typing import Any

"""
Константы
"""

HOME: str
"""
Домашний каталог пользователя, от имени которого выполняется процесс. 
Переменная окружения: `HOME`. 
Если в флагах плагина указан `root`, то это будет `/root`, в противном случае — пользователя, в домашнем каталоге которого находится Decky. 
Например: `/home/deck`
"""

USER: str
"""
Имя пользователя, от имени которого выполняется процесс. 
Переменная окружения: `USER`. 
Это будет `root`, если в параметрах плагина указан `root`, в противном случае — пользователь, в домашнем каталоге которого находится Decky. 
Например: `deck`
"""

DECKY_VERSION: str
"""
Версия decky loader.
Переменная окружения: `DECKY_VERSION`. 
Например: `v2.5.0-pre1`
"""

DECKY_USER: str
"""
Пользователь, в домашнем каталоге которого находится decky. 
Переменная окружения: `DECKY_USER`. 
Например: `deck`
"""

DECKY_USER_HOME: str
"""
Домашний каталог пользователя, в котором находится decky. 
Переменная окружения: `DECKY_USER_HOME`. 
Например: `/home/deck`
"""

DECKY_HOME: str
"""
Корневой каталог decky.
Переменная окружения: `DECKY_HOME`.
Например: `/home/deck/homebrew`
"""

DECKY_PLUGIN_SETTINGS_DIR: str
"""
Рекомендуемый путь для хранения файлов конфигураций (создаётся автоматически). 
Переменная окружения: `DECKY_PLUGIN_SETTINGS_DIR`. 
Например: `/home/deck/homebrew/settings/decky-plugin-template`
"""

DECKY_PLUGIN_RUNTIME_DIR: str
"""
Рекомендуемый путь для хранения данных среды выполнения (создаётся автоматически).
Переменная окружения: `DECKY_PLUGIN_RUNTIME_DIR`.
Например: `/home/deck/homebrew/data/decky-plugin-template`
"""

DECKY_PLUGIN_LOG_DIR: str
"""
Рекомендуемый путь для хранения постоянных журналов (создаётся автоматически).
Переменная окружения: `DECKY_PLUGIN_LOG_DIR`.
Например: `/home/deck/homebrew/logs/decky-plugin-template`
"""

DECKY_PLUGIN_DIR: str
"""
Корневой каталог плагина.
Переменная окружения: `DECKY_PLUGIN_DIR`.
Например: `/home/deck/homebrew/plugins/decky-plugin-template`
"""

DECKY_PLUGIN_NAME: str
"""
Имя плагина, указанное в файле 'plugin.json'.
Переменная окружения: `DECKY_PLUGIN_NAME`.
Например: `Example Plugin`
"""

DECKY_PLUGIN_VERSION: str
"""
Версия плагина, указанная в файле 'package.json'.
Переменная окружения: `DECKY_PLUGIN_VERSION`.
Например: `0.0.1`
"""

DECKY_PLUGIN_AUTHOR: str
"""
Автор плагина, указанный в файле 'plugin.json'.
Переменная окружения: `DECKY_PLUGIN_AUTHOR`.
Например: `John Doe`
"""

DECKY_PLUGIN_LOG: str
"""
Путь к основному файлу журнала плагина.
Переменная окружения: `DECKY_PLUGIN_LOG`.
Например: `/home/deck/homebrew/logs/decky-plugin-template/plugin.log`
"""

"""
Вспомогательные функции для миграции
"""


def migrate_any(target_dir: str, *files_or_directories: str) -> dict[str, str]:
    """
    Перенос файлов и каталогов в новое место и удаление старых.
    Указанные файлы будут перенесены в `target_dir`.
    Указанные каталоги будут рекурсивно перенесены в `target_dir`.

    Возвращает соответствие старого -> нового местоположения.
    """


def migrate_settings(*files_or_directories: str) -> dict[str, str]:
    """
    Перенос файлов и каталогов, относящихся к настройкам плагина, в рекомендуемое место и удаление старых.
    Указанные файлы будут перенесены в `DECKY_PLUGIN_SETTINGS_DIR`.
    Указанные каталоги будут рекурсивно перенесены в `DECKY_PLUGIN_SETTINGS_DIR`.

    Возвращает соответствие старого -> нового местоположения.
    """


def migrate_runtime(*files_or_directories: str) -> dict[str, str]:
    """
    Перенос файлов и каталогов, относящихся к данным среды выполнения плагина, в рекомендуемое место и удаление старых.
    Указанные файлы будут перенесены в `DECKY_PLUGIN_RUNTIME_DIR`.
    Указанные каталоги будут рекурсивно перенесены в `DECKY_PLUGIN_RUNTIME_DIR`.

    Возвращает соответствие старого -> нового местоположения.
    """


def migrate_logs(*files_or_directories: str) -> dict[str, str]:
    """
    Перенос файлов и каталогов, относящихся к логам плагина, в рекомендуемое место и удаление старых.
    Указанные файлы будут перенесены в `DECKY_PLUGIN_LOG_DIR`.
    Указанные каталоги будут рекурсивно перенесены в `DECKY_PLUGIN_LOG_DIR`.

    Возвращает соответствие старого -> нового местоположения.
    """


"""
Логирование
"""

logger: logging.Logger
"""Основной логгер плагина, записывающий в `DECKY_PLUGIN_LOG`."""

"""
Обработка событий
"""
# TODO (сделать) более хорошую документацию, я ленивый (AAGaming00)
async def emit(event: str, *args: Any) -> None:
    """
    Отправляет событие на фронтенд.
    """