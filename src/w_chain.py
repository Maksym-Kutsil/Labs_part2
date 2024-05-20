def read_file(filename_in):
    list_of_words = []
    with open(f"../resources/{filename_in}", "r", encoding="utf-8") as wchain_in:
        # Reading the first line to get the number of words
        first_line = wchain_in.readline().strip()

        if not first_line:
            # If the first line is empty, return empty results
            return list_of_words

        num_of_word = int(first_line)

        for _ in range(num_of_word):
            word = wchain_in.readline().strip()
            list_of_words.append(word)


    # Sorting the list of words by length
    list_of_words.sort(key=len)
    return list_of_words


# Cheaking of can make a shorter word by deleting 1 letter
def shorter_word(shorter_word: str, longer_word: str):
    if len(longer_word) != len(shorter_word) + 1:
        return False

    longer_word_idx = 0
    for i in range(len(shorter_word)):
        if longer_word_idx == i - 1 and i != 0:
            longer_word_idx = i
        if shorter_word[i] != longer_word[longer_word_idx]:
            longer_word_idx += 1
            if shorter_word[i] != longer_word[longer_word_idx]:
                return False
    return True


# Finding max chain of words
def max_chain(word_list: list[str]):
    if len(word_list) == 0:
        return 0
    else:
        # Initializing chain_list with all chains with value 1
        chain_list = [1] * len(word_list)
        # Sorting the word list by length

        for i in range(len(word_list)):
            for j in range(i):
                # If the shorter word can be made from the longer word
                if len(word_list[i]) == len(word_list[j]) + 1 and shorter_word(word_list[j], word_list[i]):
                    chain_list[i] = max(chain_list[i], chain_list[j] + 1)

        return max(chain_list)


def write_output_file(filename_in, filename_out):
    list_of_words = read_file(filename_in)
    with open(f"../resources/{filename_out}", "w", encoding="utf-8") as wchain_out:
        wchain_out.write(str(max_chain(list_of_words)))