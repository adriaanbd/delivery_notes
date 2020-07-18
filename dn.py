from pathlib import Path


def get_pdfs(path: str) -> list:
    """Returns a list of paths of all pdf files under a target directory."""
    assert isinstance(path, str), 'Path must be a string'

    path_obj = Path(path)
    assert path_obj.is_dir(), 'Path must be an existing directory'

    path_iter = path_obj.rglob('*.pdf')
    file_list = [str(f) for f in path_iter if f.is_file()]

    return file_list


if __name__ == '__main__':
    pdf_paths: list = get_pdfs('')
    print(pdf_paths)