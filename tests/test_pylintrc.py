# -*- coding: utf-8 -*-
"""pylintrc tests."""
import pytest

from flake8_nitpick.files.pylintrc import PylintRcFile
from tests.helpers import ProjectMock


def test_pylintrc_should_be_deleted(request):
    """File should be deleted."""
    ProjectMock(request).style("").pylintrc("").lint().assert_errors_contain(
        f"NIP342 File {PylintRcFile.file_name} should be deleted"
    )


def test_missing_pylintrc(request):
    """Suggest something when .pylintrc is missing."""
    ProjectMock(request).style(
        """
        [nitpick.files."pylintrc"]
        missing_message = "Do something"
        """
    ).lint().assert_errors_contain(f"NIP341 File {PylintRcFile.file_name} was not found. Do something")


@pytest.xfail(reason="WIP")
def test_pylint_different_missing_keys(request):
    """Test different and missing keys."""
    ProjectMock(request).pylintrc(
        """
        [REPORTS]
        output-format=text
        """
    ).style(
        """
        [pylintrc.REPORTS]
        output-format = "colorized"
        [pylintrc.bla]
        key = "value"
        """
    ).lint().assert_errors_contain(
        """
        NIP343 File .pylintrc: [REPORTS]output-format is 'text' but it should be like this:
        [REPORTS]
        output-format = colorized
        """
    ).assert_errors_contain(
        """
        NIP324 File .pylintrc: section [bla] has some missing key/value pairs. Use this:
        [bla]
        key = value
        """
    )
