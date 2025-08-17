import platform
import sys

from config import settings


def create_allure_environment_file():
    """
    Создаёт файл environment.properties для отчётов Allure.
    Файл содержит информацию о тестовом окружении:
    - настройки из config
    - операционная система
    - версия Python
    """
    os_info = f'{platform.system()}, {platform.release()}'
    python_version = sys.version

    items = [f'{key}={value}' for key, value in settings.model_dump().items()]

    items.extend([
        f'os_info={os_info}',
        f'python_version={python_version}'
    ])

    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)