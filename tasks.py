import os
import shlex
import sys

from invoke import task, util


in_ci = os.environ.get("CI", "false") == "true"
if in_ci:
    pty = False
else:
    pty = util.isatty(sys.stdout) and util.isatty(sys.stderr)


CODE_PATHS = (
    "isbinary",
    "tests",
    "tasks.py",
)


def _quote(*args: str) -> str:
    return " ".join(map(shlex.quote, args))


@task
def reformat(c):
    c.run(_quote("isort", "--skip=/tests/fixtures/", *CODE_PATHS), pty=pty)
    c.run(_quote("black", "--exclude=/tests/fixtures/", *CODE_PATHS), pty=pty)


@task
def lint(c):
    flake8_args = ("flake8", "--show-source", "--statistics", "--exclude", "tests/fixtures")
    c.run(_quote(*flake8_args, *CODE_PATHS), pty=pty)


@task
def test(c, onefile="", verbose=False):
    pytest_args = [
        "pytest",
        "--strict-config",
        "--cov=isbinary",
        "--cov-report=term-missing",
        "--ignore=tests/fixtures",
    ]
    if in_ci:
        pytest_args.extend(("--cov-report=xml", "--strict-markers"))
    else:
        pytest_args.append("--cov-report=html")

    if onefile:
        pytest_args.append(onefile)

    if verbose:
        pytest_args.append("-vv")

    c.run(_quote(*pytest_args), pty=pty)


@task
def type_check(c):
    c.run(_quote("mypy", *CODE_PATHS), pty=pty)


@task
def docs(c):
    with c.cd("docs"):
        c.run("sphinx-build -M html source build -a -W", pty=pty)
