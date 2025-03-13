import os
import shutil
import datetime
import pytest
from scripts.new_file import create_note  # Import your function

# Define a temporary test directory
TEST_DIR = 'test_docs'

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Setup before and cleanup after tests."""
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)  # Clean up before each test
    os.makedirs(TEST_DIR, exist_ok=True)
    yield
    shutil.rmtree(TEST_DIR)  # Clean up after test

@pytest.mark.parametrize('test_date', [
    datetime.date(2025, 1, 1),
    datetime.date(2024, 12, 25),
    datetime.date(2023, 7, 4),
    datetime.date(2022, 3, 15),
])
def test_create_note(test_date):
    """Test if the note is created correctly."""
    post_topic = 'Test Post'
    year = str(test_date.year)
    month = f'{test_date.month:02d}_{test_date.strftime('%B').title()}'
    filename = f'{test_date.strftime('%Y%m%d')}_test_post.md'

    # Call the function with a custom base directory
    os.environ['BASE_DIR'] = TEST_DIR  # Override the directory for testing
    create_note(post_topic, base_dir=TEST_DIR, custom_date=test_date)

    # Check if the correct directories exist
    year_path = os.path.join(TEST_DIR, year)
    month_path = os.path.join(year_path, month)
    file_path = os.path.join(month_path, filename)

    assert os.path.exists(year_path), f'Year folder {year_path} was not created'
    assert os.path.exists(month_path), f'Month folder {month_path} was not created'
    assert os.path.exists(file_path), f'Markdown file {file_path} was not created'

    # Check file content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert f'# {post_topic}' in content, 'File content is incorrect'
