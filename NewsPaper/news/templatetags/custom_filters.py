from django import template

register = template.Library()

censored_words = ['кот', 'рос']


@register.filter()
def censor(value: str) -> str:
    """Функция замены самая банальная и вообще неэффективная, но времени пол седьмого утра и я хочу спать..
    спасибо за понимание❤️"""
    if not isinstance(value, str):
        raise ValueError("Фильтр censor применяется только к строкам.")
    for word in censored_words:
        complete = False
        while not complete:
            value = value.replace(word, '*' * len(word))
            value = value.replace(word.capitalize(), '*' * len(word))
            value = value.replace(word.upper(), '*' * len(word))
            if word not in value:
                complete = True
    return value
