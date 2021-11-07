import nltk
import random


def main():
    filename = input()
    with open(filename, "r", encoding="utf-8") as file:
        corpus = file.read().split()

    trigrams = list(nltk.trigrams(corpus))

    trigram_dict = {}
    for head1, head2, tail in trigrams:
        head = f"{head1} {head2}"
        trigram_dict.setdefault(head, {})
        trigram_dict[head].setdefault(tail, 0)
        trigram_dict[head][tail] += 1

    for _ in range(10):
        print(build_sentence(trigram_dict))


def build_sentence(trigram_dict):
    token = first_word(trigram_dict)
    sentence = token.split()
    while True:
        next_possible_tokens = list(trigram_dict[token].keys())
        weights = list(trigram_dict[token].values())
        token = token.split()[1] + " " + random.choices(next_possible_tokens, weights)[0]
        sentence.append(token.split()[1])
        if len(sentence) >= 5 and token.split()[1][-1] in ".!?":
            break
    return " ".join(sentence)


def first_word(trigram_dict):
    while True:
        phrase = random.choice(list(trigram_dict.keys()))
        word = phrase.split()[0]
        if word[0].isupper() and word[-1] not in ".!?":
            return phrase


if __name__ == "__main__":
    main()
