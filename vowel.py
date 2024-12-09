def main():
    word = input("Input: ").lower()
    print(shorten(word))
def shorten(word):
    vowels = set("aeiou")
    return "".join(char for char in word if char not in vowels)

if __name__ == "__main__":
    main()
