import pytest
from unittest.mock import MagicMock
from QASystem.voice import VoiceHandler


@pytest.fixture
def mock_sr_modules(mocker):
    mock_mic = MagicMock()
    mock_recognizer = MagicMock()
    mocker.patch("speech_recognition.Microphone", return_value=mock_mic)
    mocker.patch("speech_recognition.Recognizer", return_value=mock_recognizer)
    return mock_recognizer, mock_mic


@pytest.fixture
def mock_pyttsx3(mocker):
    mock_engine = MagicMock()
    mocker.patch("pyttsx3.init", return_value=mock_engine)
    return mock_engine


def test_listen_success(mock_sr_modules, mock_pyttsx3):
    mock_recognizer, mock_mic = mock_sr_modules
    mock_audio = MagicMock()
    mock_recognizer.listen.return_value = mock_audio
    mock_recognizer.recognize_google.return_value = "hello world"

    handler = VoiceHandler()
    result = handler.listen()
    assert result == "hello world"


def test_listen_failure(mock_sr_modules, mock_pyttsx3):
    mock_recognizer, mock_mic = mock_sr_modules
    mock_audio = MagicMock()
    mock_recognizer.listen.return_value = mock_audio
    mock_recognizer.recognize_google.side_effect = Exception("Recognition failed")

    handler = VoiceHandler()
    result = handler.listen()
    assert result == ""


def test_speak(mock_sr_modules, mock_pyttsx3):
    handler = VoiceHandler()
    handler.engine = mock_pyttsx3
    handler.speak("testing")
    mock_pyttsx3.say.assert_called_once_with("testing")
    mock_pyttsx3.runAndWait.assert_called_once()
