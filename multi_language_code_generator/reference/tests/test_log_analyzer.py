import pytest
from reference.log_analyzer import LogAnalyzer

def test_analyze():
    analyzer = LogAnalyzer()
    logs = [
        '127.0.0.1 - - [10/Oct/2000:13:55:36 -0700] "GET /index.html HTTP/1.0" 200 2326',
        '127.0.0.1 - - [10/Oct/2000:13:55:37 -0700] "GET /bad.html HTTP/1.0" 404 123',
        '127.0.0.1 - - [10/Oct/2000:13:55:38 -0700] "GET /error.html HTTP/1.0" 500 456'
    ]
    result = analyzer.analyze(logs)
    assert result["total_requests"] == 3
    assert result["error_rate"] == (2/3) * 100

def test_empty_log():
    analyzer = LogAnalyzer()
    assert analyzer.analyze([]) == {"total_requests": 0, "error_rate": 0.0}
