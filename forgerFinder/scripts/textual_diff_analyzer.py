from difflib import unified_diff

def compare_text_files(file1, file2):
    """Compare two text files and return the diff as a list of lines."""
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = f1.readlines()
        text2 = f2.readlines()

    diff = list(unified_diff(text1, text2, fromfile='Original Text', tofile='Suspect Text', lineterm=''))
    return diff

def print_diff_report(diff_lines):
    """Print differences in a readable format."""
    if not diff_lines:
        print("[INFO] No differences found in text files.")
    else:
        print("[INFO] Differences found:")
        for line in diff_lines:
            print(line)

if __name__ == "__main__":
    original_txt = '../data/originals/legit_text.txt'
    suspect_txt = '../data/suspicious/fake_text.txt'

    differences = compare_text_files(original_txt, suspect_txt)
    print_diff_report(differences)
