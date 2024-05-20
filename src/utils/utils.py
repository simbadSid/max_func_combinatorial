import os
import fileinput


def project_root() -> str:
    return os.path.abspath(os.path.join(__file__, '../../../'))


class FileParser:
    """
    Class wrapper to access a file content (including stdin)
    Parameters
    ----------
    Path to the file to access, or None if accessing stdin. The path is relative to the root of the project

    Returns
    -------
    """
    def __init__(self, file_relative_path: str = None):
        self.generator = None
        if file_relative_path:
            def read_line_from_file():
                file_path = os.path.join(project_root(), file_relative_path)
                with open(file_path, 'r') as file:
                    for line in file:
                        yield line
            self.generator = read_line_from_file()
        else:
            def read_line_from_stdin():
                for line in fileinput.input():
                    yield line
            self.generator = read_line_from_stdin()

    def next_line(self) -> str:
        return next(self.generator)
