import os
import re
import argparse

def update_image_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 处理GitHub URL格式：提取UUID并转换
    content = re.sub(
        r'https://github\.com/wy876/POC/assets/\d+/([a-f0-9-]+)(?:\.png)?',
        r'../../images/\1.png',
        content
    )

    # 处理本地assets格式：直接转换路径
    content = re.sub(
        r'\./assets/([^)]+\.png)',
        r'../../assets/\1',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def process_md_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                update_image_links(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean image links in Markdown files')
    parser.add_argument('--dir', default='.', help='Directory to process (default: current directory)')
    args = parser.parse_args()

    process_md_files(args.dir)
    print("Image links updated successfully!")