from pathlib import Path

from isbinary import is_binary_file


def test_broken_symlink(tmp_path: Path) -> None:
    symlink_file = tmp_path / "symlink-file"
    symlink_file.symlink_to(tmp_path / "non-existent-file")

    assert is_binary_file(symlink_file) is True
