def clean(text):
    if not isinstance(text, str):
        raise TypeError('Текст не должен содерать символы')
    return ''.join(x for x in text if x.isalpha() or x ==' ')

print(clean('Что за !@#$%^* ?!'))