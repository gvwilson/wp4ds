"""Utilities."""

from pathlib import Path


SUFFIXES = {".css", ".csv", ".html", ".js", ".json", ".md", ".py", ".sh", ".txt"}


def find_files(opt, root_skips=[]):
    """Collect all interesting files."""
    return {
        filepath: _read_file(filepath)
        for filepath in Path(opt.root).glob("**/*.*")
        if _is_interesting_file(filepath, root_skips)
    }


def find_symlinks(opt, root_skips=[]):
    """Collect all interesting files."""
    return [
        filepath
        for filepath in Path(opt.root).glob("**/*")
        if _is_interesting_symlink(filepath, root_skips)
    ]


def _is_interesting_file(filepath, root_skips):
    """Is this file worth checking?"""
    if not filepath.is_file():
        return False
    if str(filepath).startswith("."):
        return False
    if filepath.suffix not in SUFFIXES:
        return False
    if str(filepath.parent.name).startswith("."):
        return False
    if any(str(filepath).startswith(s) for s in root_skips):
        return False
    return True


def _is_interesting_symlink(filepath, root_skips):
    """Is this symlink worth checking?"""
    if not filepath.is_symlink():
        return False
    if str(filepath).startswith("."):
        return False
    if any(str(filepath).startswith(s) for s in root_skips):
        return False
    return True


def _read_file(filepath):
    """Read file as bytes or text."""
    if filepath.suffix in SUFFIXES:
        return filepath.read_text()
    else:
        return filepath.read_bytes()
