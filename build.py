# подставляет data.json в шаблон и собирает один index.html
t = open('src/template.html', encoding='utf-8').read()
d = open('data.json', encoding='utf-8').read()
open('index.html', 'w', encoding='utf-8').write(t.replace('__DATA__', d))
