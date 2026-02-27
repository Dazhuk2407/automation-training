"""Tests for Lesson 12 exercises"""
import pytest
def test_exercises_exist():
    from pathlib import Path
    assert Path(__file__).parent.joinpath('EXERCISES.md').exists()
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
