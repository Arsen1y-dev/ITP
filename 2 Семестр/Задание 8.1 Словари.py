with open('input.txt', 'r', encoding='utf-8') as file:
            data = ' '.join([line.strip('\n') for line in file.readlines()]).split()

def index_words():
        d_index = defaultdict(set)
        for i, elem in enumerate(data):
            if elem.isalpha():
                d_index[elem].add(i)
        return [(key, sorted(value)) for key, value in d_index.items()]