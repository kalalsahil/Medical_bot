import pytest
from unittest.mock import MagicMock, patch
from QASystem.tts import TextToSpeech


@pytest.fixture
def mock_pyttsx3(mocker):
    mock_engine = MagicMock()
    mocker.patch("pyttsx3.init", return_value=mock_engine)
    return mock_engine


def test_text_to_speech_initialization(mock_pyttsx3):
    tts = TextToSpeech(voice="female", rate=150, volume=0.8)
    assert tts.engine == mock_pyttsx3
    mock_pyttsx3.setProperty.assert_any_call("rate", 150)
    mock_pyttsx3.setProperty.assert_any_call("volume", 0.8)


def test_text_to_speech_voice_setting(mock_pyttsx3):
    mock_pyttsx3.getProperty.return_value = [MagicMock(id="male_id"), MagicMock(id="female_id")]
    tts = TextToSpeech(voice="female")
    mock_pyttsx3.setProperty.assert_any_call("voice", "female_id")

    tts.set_voice("male")
    mock_pyttsx3.setProperty.assert_any_call("voice", "male_id")


def test_text_to_speech_speak_sync(mock_pyttsx3):
    tts = TextToSpeech()
    tts._speak("hello world")
    mock_pyttsx3.say.assert_called_once_with("hello world")
    mock_pyttsx3.runAndWait.assert_called_once()


@patch("threading.Thread")
def test_text_to_speech_speak_async(mock_thread, mock_pyttsx3):
    tts = TextToSpeech()
    tts.speak("hello", async_mode=True)
    mock_thread.assert_called_once()