# -*- coding: utf-8 -*-
"""Checker for the `.pylintrc <https://pylint.readthedocs.io/>`_ file.

See also `How do I find the option name (for pylintrc) corresponding to a specific command line option? <http://pylint.pycqa.org/en/stable/faq.html?highlight=.pylintrc#how-do-i-find-the-option-name-for-pylintrc-corresponding-to-a-specific-command-line-option>`_.

You can also run ``pylint --long-help | less`` and ``pylint --full-documentation | less`` to see all the options.
"""
from flake8_nitpick.files.base import BaseFile
from flake8_nitpick.types import YieldFlake8Error


class PylintRcFile(BaseFile):
    """Checker for the `.pylintrc <https://pylint.readthedocs.io/>`_ file.

    See also `How do I find the option name (for pylintrc) corresponding to a specific command line option? <http://pylint.pycqa.org/en/stable/faq.html?highlight=.pylintrc#how-do-i-find-the-option-name-for-pylintrc-corresponding-to-a-specific-command-line-option>`_.

    You can also run ``pylint --long-help | less`` and ``pylint --full-documentation | less`` to see all the options.
    """

    file_name = ".pylintrc"
    error_base_number = 340

    def suggest_initial_contents(self) -> str:
        """Suggest the initial content for this missing file."""
        return ""

    def check_rules(self) -> YieldFlake8Error:
        """Check rules for ``.pylintrc``."""
        return []
