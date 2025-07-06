import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from QASystem.output import generate_response

def test_rag_chain_response():
    response = generate_response("What causes fatigue?")
    assert isinstance(response, str)
    assert len(response) > 0
