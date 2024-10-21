#python script
import os
import socket
from collections import Counter
import contractions

# File paths
file1_path = '/home/data/IF.txt'
file2_path = '/home/data/AlwaysRememberUsThisWay.txt'
output_dir = '/home/data/output'
output_path = os.path.join(output_dir, 'result.txt')

# Read and count words in the first file
def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().lower().split()
    return words

# Handle contractions in the second file and count words
def count_words_with_contractions(file_path):
    with open(file_path, 'r') as file:
        text = contractions.fix(file.read().lower())
        words = text.split()
    return words

# Count total words and frequent words
def analyze_words():
    words_file1 = count_words(file1_path)
    words_file2 = count_words_with_contractions(file2_path)

    # Calculate total words
    total_words_file1 = len(words_file1)
    total_words_file2 = len(words_file2)
    grand_total = total_words_file1 + total_words_file2

    # Top 3 most frequent words in each file
    top3_file1 = Counter(words_file1).most_common(3)
    top3_file2 = Counter(words_file2).most_common(3)

    # Get the IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write the results to output file
    with open(output_path, 'w') as output_file:
        output_file.write(f"Total words in IF.txt: {total_words_file1}\n")
        output_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n")
        output_file.write(f"Grand total of words: {grand_total}\n")
        output_file.write(f"Top 3 most frequent words in IF.txt: {top3_file1}\n")
        output_file.write(f"Top 3 most frequent words in AlwaysRememberUsThisWay.txt: {top3_file2}\n")
        output_file.write(f"IP address of the container: {ip_address}\n")

# Execute the script
if __name__ == '__main__':
    analyze_words()
    
    # Print the result to the console
    with open(output_path, 'r') as result_file:
        print(result_file.read())
