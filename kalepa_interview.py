# (Scrabble task)
# You get a set of tiles with some strings on them and a word. Write a function that determines whether the word can be constructed using the tiles. Any tile can be reused multiple times.
# Examples:
# tiles = {"ca", "at"}
# word = "cat"
# output: False


# tiles = {"ca", "at"}
# word = "caat"    
# output: True


# tiles = {"ca", "at"}
# word = "atcaca"
# output: True


def is_scrabble(tiles: list[str], word: str, memo=None) -> bool:
    if memo is None:
        memo = {}
    
    if word in memo:
        return True
    
    if not word:
        return True
    
    for tile in tiles:
        if word.startswith(tile) and is_scrabble(tiles, word[len(tile):], memo):  # recursive call
            memo[word] = True
            return True

    memo[word] = False
    return False

# def iterative_is_scrabble

if __name__ == "__main__":
    tiles = {"ca", "at"}
    word = "cat"
    # output: False
    print(f"The 1: {is_scrabble(tiles, word)}")


    tiles = {"ca", "at"}
    word = "caat"    
    # output: True
    print(f"The 2: {is_scrabble(tiles, word)}")

    tiles = {"ca", "at"}
    word = "atcaca"
    # output: True
    print(f"The 3: {is_scrabble(tiles, word)}")