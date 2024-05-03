import re

with open("/Users/arseniy/Documents/GitHub/ITP/2 Семестр/test.txt", "r") as file:
    text = file.read()

sentences = re.split(r'(?<=[.?!])\s*', text.lower())

words_in_questions = set()
words_in_exclamations = set()
words_in_narratives = set()

last_questions = [sentence for sentence in sentences if sentence.endswith('?')]
last_exclamations = [sentence for sentence in sentences if sentence.endswith('!')]
last_narratives = [sentence for sentence in sentences if sentence.endswith('.')]

last_question = last_questions[-1] if last_questions else None
last_exclamation = last_exclamations[-1] if last_exclamations else None
last_narrative = last_narratives[-1] if last_narratives else None

last_words_in_question = set(last_question.strip().split()) if last_question else set()
last_words_in_exclamation = set(last_exclamation.strip().split()) if last_exclamation else set()
last_words_in_narrative = set(last_narrative.strip().split()) if last_narrative else set()

for sentence in sentences:
    words = set(sentence[:-1].lower().strip().split())
    if sentence.endswith('?'):
        words_in_questions.update(words)
    elif sentence.endswith('!'):
        words_in_exclamations.update(words)
    else:
        words_in_narratives.update(words)

result = words_in_questions.intersection(words_in_narratives).difference(words_in_exclamations)
print(result)





#1. Открывается файл "test.txt" и считывается его содержимое.
#2. Текст разбивается на предложения с использованием регулярного выражения, которое ищет знаки препинания (".", "?", "!") и разделяет текст по ним.
#3. Создаются множества words_in_questions, words_in_exclamations и words_in_narratives для хранения слов из вопросительных предложений, восклицательных предложений и повествовательных предложений соответственно.
#4. Находятся последние вопросительное, восклицательное и повествовательное предложения в тексте.
#5. Для каждого предложения из текста определяется множество слов, которые составляют это предложение (без знаков препинания). Затем эти слова добавляются в соответствующее множество в зависимости от типа предложения.
#6. Наконец, находится пересечение множеств слов в вопросительных и повествовательных предложениях, и из этого результата исключаются слова из восклицательных предложений.