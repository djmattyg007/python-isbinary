============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/djmattyg007/python-isbinary/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Isbinary can always use more documentation, whether as part of the
official isbinary docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/djmattyg007/python-isbinary/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `isbinary` for local development.

1. Fork the `isbinary` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/python-isbinary.git

3. Run `poetry install` to install all dependencies in a virtualenv.

4. Create a branch for local development::

    $ git switch -c name-of-your-bugfix-or-feature

Now you can make your changes locally.

5. When you're done making changes, check that the code quality checks
   still pass::

    $ poetry run invoke lint
    $ poetry run invoke type-check
    $ poetry run invoke test

You can automatically reformat the code with isort and black by invoking
another task::

    $ poetry run invoke reformat

6. Commit your changes and push your branch to GitHub::

    $ git add -p
    $ git commit
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. If it includes changes to the main code, it should also include updates to
   the tests.
2. If the changes add new functionality, the docs should be updated. Put your
   new functionality into a function with a docstring, and add the feature to
   the list in README.rst.
3. The changes should work for all currently supported versions of Python.
   Feedback from CI should be automatically added to the pull request.

Tips
----

To run a subset of tests::

    $ poetry run invoke test --onefile=tests/test_symlinks.py
