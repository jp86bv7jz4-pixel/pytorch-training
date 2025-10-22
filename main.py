from utils.count import count_word

if __name__ == "__main__":
    s = "hello world"
    print("e:", count_word(s, "es"))
    print("o:", count_word(s, "o"))
    print("l:", count_word(s, "l"))