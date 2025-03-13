import calendar
import os
import sys
import datetime
import locale
from slugify import slugify

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

def create_note(post_topic_name, base_dir='docs', custom_date=None):
    today = custom_date or datetime.date.today()
    year = str(today.year)
    month = f'{today.month:02d}_{calendar.month_name[today.month].title()}'
    post_topic_slugify = slugify(post_topic_name, separator='_')
    file_name = f"{today.strftime('%Y%m%d')}_{post_topic_slugify}.md"

    # Define directory structure
    year_dir = os.path.join(base_dir, year)
    month_dir = os.path.join(year_dir, month)
    file_path = os.path.join(month_dir)
    file_path = os.path.join(month_dir, file_name)

    # Ensure directories exist
    os.makedirs(month_dir, exist_ok=True)

    # Create the markdown file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {post_topic_name}\n\n")
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python new_file.py \"Post topic name\"")
        sys.exit(1)

    post_topic_name = sys.argv[1]
    create_note(post_topic_name)
