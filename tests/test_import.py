"""Test workflowtest."""
from src import workflowtest # noqa: F821


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(workflowtest.__name__, str) # noqa: F821
