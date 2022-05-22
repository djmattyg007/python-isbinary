==========
Quickstart
==========

To use isbinary in a project, import it and use `is_binary_file()` to guess
whether a file is binary or text.

For example::

    >>> from isbinary import is_binary_file
    >>> is_binary("README.rst")
    false

*****************
CommandLine Help
*****************

You can make use of isbinary on the commandline::

    $ python3 -m isbinary README.rst
    false

The command accepts one positional argument, which is the filename.

You can also supply `--help` to view help information::

    $ python3 -m isbinary --help
