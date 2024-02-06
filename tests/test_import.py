"""Test workflowtest."""
from src import workflowtest


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(workflowtest.__name__, str)
