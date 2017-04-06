def word_count(phrase):

    s = "!:,._@$%^&🖖"
    words = phrase.strip().replace("\n", " ").replace("\t", " ")
    for char in s:
        words = words.replace(char, " ")
    words = words.lower().split()

    words = filter(None, words)

    count = {}
    for word in words:
        count[word] = 1 if word not in count else count[word] + 1

    return count