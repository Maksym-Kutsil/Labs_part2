def read_file(filename: str) -> list[str]:
    with open(f"../resourses/{filename}", "r", encoding="utf-8") as file:
        words_amount = int(file.readline())
        words = [file.readline().strip() for _ in range(words_amount)]
    return sorted(words, key=len)


def find_max_sequence_words(words: list[str]) -> int:
    dp = {word: 1 for word in words}
    for word in words:
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in dp:
                dp[word] = max(dp[word], dp[new_word] + 1)
    return max(dp.values())


def write_output(filename: str, result: int) -> None:
    with open(f"../resourses/{filename}", "w", encoding="utf-8") as file:
        file.write(str(result))


def find_w_chain_length(input_file: str, output_file: str) -> None:
    try:
        words = read_file(input_file)
    except ValueError:
        write_output(output_file, -1)
        return
    result = find_max_sequence_words(words)
    write_output(output_file, result)