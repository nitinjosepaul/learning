from line_reader import readFromFile
from unittest.mock import MagicMock
from pytest import raises

def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value = 'test line')
    mock_open = MagicMock(return_value = mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    mock_exists = MagicMock(return_value = True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = readFromFile('blah')
    mock_open.assert_called_once_with('blah', 'r')
    assert result == 'test line'

def test_throwsExceptionIfFileNotExists(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value = 'test line')
    mock_open = MagicMock(return_value = mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    mock_exists = MagicMock(return_value = False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = readFromFile('blah')