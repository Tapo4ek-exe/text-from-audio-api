import os

from settings import TEMP_DIR


class TempFileManager:
    def __init__(self) -> None:
        # Создание папки для временных файлов
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)

        self.temp_files = []

    def __del__(self) -> None:
        # Удаление всех временных файлов
        for filename in self.temp_files:
            self.delete_temp_file(filename)

        # Удаление папки для временных файлов
        if os.path.exists(TEMP_DIR):
            os.removedirs(TEMP_DIR)

    # Получение пути к временному файлу
    def __get_file_path(self, filename: str) -> str:
        return os.path.join(TEMP_DIR, filename)

    # Создание временного файла
    def save_temp_file(self, filename: str, content: bytes | str) -> str:
        filepath = self.__get_file_path(filename)
        with open(filepath, "wb") as file:
            file.write(content)

        self.temp_files.append(filename)

        return filepath

    # Удаление временного файла
    def delete_temp_file(self, filename: str) -> None:
        filepath = self.__get_file_path(filename)
        self.temp_files.remove(filename)
        if os.path.exists(filepath):
            os.remove(filepath)
