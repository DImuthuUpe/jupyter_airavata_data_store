import os
from pathlib import Path


class AiravataFileOperations:

    basePath = "/tmp"

    def is_file(self, path):
        return Path(self.basePath + path).is_file()

    def file_exists(self, path):
        return Path(self.basePath + path).exists() and Path(self.basePath + path).is_file()

    def dir_exists(self, path):
        return Path(self.basePath + path).exists() and Path(self.basePath + path).is_dir()

    def ls_dir(self, path):
        return os.listdir(self.basePath + path)

    def read_file(self, path):
        with open(self.basePath + path, 'r') as readFile:
            data = readFile.read()
        return data

    def write_file(self, path, content):
        with open(self.basePath + path, "w") as text_file:
            text_file.write(content)

    def create_dir(self, path):
        Path(self.basePath + path).mkdir()

    def rename_file(self, oldPath, newPath):
        os.renames(self.basePath + oldPath, self.basePath + newPath)

    def delete_file(self, path):
        os.remove(self.basePath + path)