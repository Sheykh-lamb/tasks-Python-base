def words_index_map(strings: list) -> dict:

    dict1 = {}
    for text in " ".join(strings).split():
        dict1[text] = None

    for i in range(len(strings)):
        for word in strings[i].split():
            if dict1[word] is None:
                dict1[word] = {i}
            else:
                dict1[word].add(i)     
    return dict1    

    

     
strings = [
    "hello world",
    "world of python",
    "hello again"
]
print(words_index_map(strings))
# {'hello': {0, 2}, 'world': {0, 1}, 'of': {1}, 'python': {1}, 'again': {2}}