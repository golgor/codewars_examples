# Given a string of characters S such as "AAAABBBBBXCCCCAAA" and an integer K such as 3.
# The string can be compressed as A4B5X4C3A i.e. if the number of characters > 2
# Encode for example AAAA as A4 to save data.
# Use a substring of size K to remove characters in S and find the best compression for S.
import random

def generate_test_case(min_length: int, variations: int, characters: list):
    list_chars = []
    while sum([len(c) for c in list_chars]) < min_length:
        choice = random.choice(characters)
        counts = random.randint(1,5)
        list_chars.append(choice*counts)

    return ("".join(list_chars), random.randint(2,4))

S, K = generate_test_case(20, 4, ['A', 'B', 'C', 'D', 'X'])

# Test case 1
Test_case1 = ("CCDDDDCCCCCDDBBBBBBBBB", 3)

# Test case 2
Test_case2 = ("DDXXXXXCCCCBBCCCCCCCCCC", 2)

def solution(S, K):
    result = []
    for i in range(len(S)-K):
        string = S[0:i] + S[i+K:]
        encoded_string = ""
        while len(string) > 0:
            char = string[0]
            count = len(string)-len(string := string.lstrip(char))
            if count >= 3:
                encoded_string += char + str(count)
            else:
                encoded_string += char*count

        result.append(dict(encoded=encoded_string, substring=S[i:K+i], length=len(encoded_string)))
    
    best_encoding = min(result, key=lambda x: x.get("length"))
    # print(
    #     f"Max encoding achieved:",
    #     f"\nEncoded string: {best_encoding.get('encoded')}",
    #     f"\nSubstring: {best_encoding.get('substring')}",
    #     f"\nLength: {best_encoding.get('length')}"
    # )
    return best_encoding.get("length")

if __name__ == "__main__":
    print(solution(S, K))