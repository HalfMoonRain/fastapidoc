import sys

def test_pythonpath():
    print("Current sys.path:", sys.path)  # Print the sys.path for debugging
    # sys.path에 'src' 디렉토리를 포함하는 경로가 있는지 확인합니다.
    assert any('src' in path for path in sys.path)