# подставляет data.json в шаблон и собирает один index.html
t = open('src/template.html', encoding='utf-8').read()
d = open('data.json', encoding='utf-8').read()
# '<' экранируем, чтобы строка </script> в ячейке не закрыла тег
d = d.replace('<', '\\u003c')
open('index.html', 'w', encoding='utf-8').write(t.replace('__DATA__', d))
