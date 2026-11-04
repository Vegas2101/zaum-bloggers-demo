# подставляет data.json в шаблон и собирает один index.html
import sys

# дата выгрузки таблицы; от неё считаются «дата прошла» и «выход через N дн.»
SNAPSHOT = sys.argv[1] if len(sys.argv) > 1 else '2026-11-04'

t = open('src/template.html', encoding='utf-8').read()
d = open('data.json', encoding='utf-8').read()
# '<' экранируем, чтобы строка </script> в ячейке не закрыла тег
d = d.replace('<', '\\u003c')
t = t.replace('__DATA__', d).replace('__SNAPSHOT__', SNAPSHOT)
open('index.html', 'w', encoding='utf-8').write(t)
