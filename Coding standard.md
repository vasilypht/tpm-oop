# Правила оформления кода

### Отступы

Используйте 4 пробела на каждый уровень отступа.

Продолжительные строки должны выравнивать обернутые элементы либо вертикально одним блоком, либо с использованием висячего отступа. При использовании висячего отступа следует применять следующие соображения:

* На первой линии недолжно быть аргументов;

* Остальные строки должны четко восприниматься как продолжение линии.

```python
def foo(a: int, b: int) -> int:
    c = a + b
    return c
```

```python
test_value = some_func(
        value_1,
        value_2,
        value_3)

print(test_value)

# or

def bar(value_1, value_2
        value_3, value_4):
    print(value_1)
```

### Табуляция или пробелы

Пробелы - самый предпочтительный метод отступов.

Практически во всех современные редактора табуляция конвертируется в определенное число пробелов, количество которых также настраивается в настройках.

### Максимальная длина строки

Ограничьте длину строки максимум 120 символами.

Для более длинных блоков текста с меньшими структурными ограничениями (строки документации или комментарии), длину строки следует ограничить 90 символами.

Длинные строки могут быть разбиты на несколько строк, обернутые в скобки. Это предпочтительнее использования обратной косой черты для продолжения строки.

### Пустые строки

Отделяйте функции верхнего уровня и определения классов двумя пустыми строками.

Определения методов внутри класса разделяются одной пустой строкой. Используйте пустые строки в функциях, чтобы указать логические разделы.

### Кодировка

Кодировка Python должна быть UTF-8.

### Импорты

Каждый импорт должен быть на отдельной строке.

```python
import os
import sys
```

Но в тоже время, можно писать так:

```python
from math import gcd, ceil, floor

# or

from math import (
    gcd,
    ceil,
    floor
)
```

Импорты всегда помещаются в начале файла, сразу после комментариев к модулю и строк документации, и перед объявлением констант.

Импорты должны быть сгруппированы в следующем порядке:

* Импорты из стандартной библиотеки

* Импорты сторонних библиотек

* Импорты модулей текущего проекта

Рекомендуется абсолютное импортирование, так как оно обычно более читаемо и ведет себя лучше если импортируемая система настроена неправильно:

```python
import pack1.pack2
from lib1.lib2 import foo_bar
```

Тем не менее, явный относительный импорт является приемлемой альтернативой абсолютному импорту, особенно при работе со сложными пакетами, где использование абсолютного импорта было бы излишне подробным:

```python
# GOOD
from ..lib import func_2
from .lib import func_3

# NOT GOOD
from lib1.lib2.lib3.lib4.lib5.lib5 import func_2
```

Шаблоны импортов (from <package name> import *) следует избегать.

### Комментарии

Комментарии должны являться законченными предложениями. Если комментарий — фраза или предложение, первое слово должно быть написано с большой буквы, если только это не имя переменной, которая начинается с маленькой буквы. 

Если комментарий короткий, можно опустить точку в конце предложения. Блок комментариев обычно состоит из одного или более абзацев, составленных из полноценных предложений, поэтому каждое предложение должно оканчиваться точкой.

Писать комментарии нужно на английском языке.

Старайтесь реже использовать "встрочные" комментарии.

Такой комментарий находится в той же строке, что и инструкция. "Встрочные" комментарии должны отделяться по крайней мере двумя пробелами от инструкции. Они должны начинаться с символа # и одного пробела. Комментарии в строке с кодом не нужны и только отвлекают от чтения, если они объясняют очевидное.

Пишите документацию для всех публичных модулей, функций, классов, методов. Строки документации необязательны для приватных методов, но лучше написать, что делает метод. Комментарий нужно писать после строки с def.

### Соглашение по именования

Никогда не используйте символы l (маленькая латинская буква «эль»), O (заглавная латинская буква «о») или I (заглавная латинская буква «ай») как однобуквенные идентификаторы.

В некоторых шрифтах эти символы неотличимы от цифры один и нуля. Если очень нужно l, пишите вместо неё заглавную L.

#### Имена модулей

Модули должны иметь короткие имена, состоящие из маленьких букв. Можно использовать символы подчеркивания, если это улучшает читабельность. То же самое относится и к именам пакетов, однако в именах пакетов не рекомендуется использовать символ подчёркивания.

Когда модуль расширения, написанный на С или C++, имеет сопутствующий python-модуль (содержащий интерфейс высокого уровня), С/С++ модуль начинается с символа подчеркивания, например, _socket.

#### Имена классов

Имена классов должны обычно следовать соглашению CapWords.

Вместо этого могут использоваться соглашения для именования функций, если интерфейс документирован и используется в основном как функции.

#### Имена исключений

Так как исключения являются классами, к исключениям применяется стиль именования классов. Однако вы можете добавить Error в конце имени (если, конечно, исключение действительно является ошибкой).

#### Имена глобальных переменных

Допускается использовать глобальные переменные только внутри одного модуля. Руководствуйтесь теми же соглашениями, что и для имен функций.

Добавляйте в модули, которые написаны так, чтобы их использовали с помощью from M import *, механизм __all__, чтобы предотвратить экспортирование глобальных переменных.

#### Имена функций

Имена функций должны состоять из маленьких букв, а слова разделяться символами подчеркивания — это необходимо, чтобы увеличить читабельность.

#### Аргументы функций и методов

Всегда используйте self в качестве первого аргумента метода экземпляра объекта.

Если имя аргумента конфликтует с зарезервированным ключевым словом python, обычно лучше добавить в конец имени символ подчеркивания, чем исказить написание слова или использовать аббревиатуру. Таким образом, class_ лучше, чем clss. (Возможно, хорошим вариантом будет подобрать синоним).

#### Имена методов и переменных экземпляров классов

Используйте тот же стиль, что и для имен функций: имена должны состоять из маленьких букв, а слова разделяться символами подчеркивания.

Используйте один символ подчёркивания перед именем для непубличных методов и атрибутов.

Чтобы избежать конфликтов имен с подклассами, используйте два ведущих подчеркивания.



#### Константы

Константы обычно объявляются на уровне модуля и записываются только заглавными буквами, а слова разделяются символами подчеркивания. Например: MAX_OVERFLOW, TOTAL.

### Общие рекомендации

- Код должен быть написан так, чтобы не зависеть от разных реализаций языка (PyPy, Jython, IronPython, Pyrex, Psyco и пр.).
  
  Например, не полагайтесь на эффективную реализацию в CPython конкатенации строк в выражениях типа a+=b или a=a+b. Такие инструкции выполняются значительно медленнее в Jython. В критичных к времени выполнения частях программы используйте "".join() — таким образом склеивание строк будет выполнено за линейное время независимо от реализации python.

- Сравнения с None должны обязательно выполняться с использованием операторов is или is not, а не с помощью операторов сравнения. Кроме того, не пишите if x, если имеете в виду if x is not None — если, к примеру, при тестировании такая переменная может принять значение другого типа, отличного от None, но при приведении типов может получиться False!

- При реализации методов сравнения, лучше всего реализовать все 6 операций сравнения (__eq__, __ne__, __lt__, __le__, __gt__, __ge__), чем полагаться на то, что другие программисты будут использовать только конкретный вид сравнения.
  
  Для минимизации усилий можно воспользоваться декоратором functools.total_ordering() для реализации недостающих методов.
  
  PEP 207 указывает, что интерпретатор может поменять y > х на х < y, y >= х на х <= y, и может поменять местами аргументы х == y и х != y. Гарантируется, что операции sort() и min() используют оператор <, а max() использует оператор >. Однако, лучше всего осуществить все шесть операций, чтобы не возникало путаницы в других местах.

- Всегда используйте выражение def, а не присваивание лямбда-выражения к имени.
  
  Правильно:
  
  ```python
  def f(x):
      return 2*x
  ```
  
  Неправильно:
  
  ```python
  f = lambda x: 2*x
  ```

- Наследуйте свой класс исключения от Exception, а не от BaseException. Прямое наследование от BaseException зарезервировано для исключений, которые не следует перехватывать.

- Используйте цепочки исключений соответствующим образом. В Python 3, "raise X from Y" следует использовать для указания явной замены без потери отладочной информации.

- Когда вы генерируете исключение, пишите raise ValueError('message') вместо старого синтаксиса raise ValueError, message.
  
  Старая форма записи запрещена в python 3.
  
  Такое использование предпочтительнее, потому что из-за скобок не нужно использовать символы для продолжения перенесенных строк, если эти строки длинные или если используется форматирование.

- Когда код перехватывает исключения, перехватывайте конкретные ошибки вместо простого выражения except:.
  
  К примеру, пишите вот так:
  
  ```python
  try:
      import platform_specific_module
  except ImportError:
      platform_specific_module = None
  ```
  
  Простое написание "except:" также перехватит и SystemExit, и KeyboardInterrupt, что породит проблемы, например, сложнее будет завершить программу нажатием control+C. Если вы действительно собираетесь перехватить все исключения, пишите "except Exception:".
  
  Хорошим правилом является ограничение использования "except:", кроме двух случаев:
  
  1. Если обработчик выводит пользователю всё о случившейся ошибке; по крайней мере, пользователь будет знать, что произошла ошибка.
  2. Если нужно выполнить некоторый код после перехвата исключения, а потом вновь "бросить" его для обработки где-то в другом месте. Обычно же лучше пользоваться конструкцией "try...finally".

- При связывании перехваченных исключений с именем, предпочитайте явный синтаксис привязки, добавленный в Python 2.6:
  
  ```python
  try:
      process_data()
  except Exception as exc:
      raise DataProcessingFailedError(str(exc))
  ```
  
  Это единственный синтаксис, поддерживающийся в Python 3, который позволяет избежать проблем неоднозначности, связанных с более старым синтаксисом на основе запятой.

- При перехвате ошибок операционной системы, предпочитайте использовать явную иерархию исключений, введенную в Python 3.3, вместо анализа значений errno.

- Постарайтесь заключать в каждую конструкцию try...except минимум кода, чтобы легче отлавливать ошибки. Опять же, это позволяет избежать замаскированных ошибок.
  
  Правильно:
  
  ```python
  try:
      value = collection[key]
  except KeyError:
      return key_not_found(key)
  else:
      return handle_value(value)
  ```
  
  Неправильно:
  
  ```python
  try:
      # Здесь много действий!
      return handle_value(collection[key])
  except KeyError:
      # Здесь также перехватится KeyError, который может быть сгенерирован handle_value()
      return key_not_found(key)
  ```

- Когда ресурс является локальным на участке кода, используйте выражение **with** для того, чтобы после выполнения он был очищен оперативно и надёжно.

- Менеджеры контекста следует вызывать с помощью отдельной функции или метода, всякий раз, когда они делают что-то другое, чем получение и освобождение ресурсов. Например:
  
  Правильно:
  
  ```python
  with conn.begin_transaction():
      do_stuff_in_transaction(conn)
  ```
  
  Неправильно:
  
  ```python
  with conn:
      do_stuff_in_transaction(conn)
  ```
  
  Последний пример не дает никакой информации, указывающей на то, что __enter__ и __exit__ делают что-то кроме закрытия соединения после транзакции. Быть явным важно в данном случае.

- Используйте строковые методы вместо модуля string — они всегда быстрее и имеют тот же API для unicode-строк. Можно отказаться от этого правила, если необходима совместимость с версиями python младше 2.0.
  
  В Python 3 остались только строковые методы.

- Пользуйтесь ''.startswith() и ''.endswith() вместо обработки срезов строк для проверки суффиксов или префиксов.
  
  startswith() и endswith() выглядят чище и порождают меньше ошибок. Например:
  
  Правильно:
  
  ```python
  if foo.startswith('bar'):
  ```
  
  Неправильно:
  
  ```python
  if foo[:3] == 'bar':
  ```

- Сравнение типов объектов нужно делать с помощью isinstance(), а не прямым сравнением типов:
  
  Правильно:
  
  ```python
  if isinstance(obj, int):
  ```
  
  Неправильно:
  
  ```python
  if type(obj) is type(1):
  ```
  
  Когда вы проверяете, является ли объект строкой, обратите внимание на то, что строка может быть unicode-строкой. В python 2 у str и unicode есть общий базовый класс, поэтому вы можете написать:
  
  ```python
  if isinstance(obj, basestring):
  ```
  
  Отметим, что в Python 3, unicode и basestring больше не существуют (есть только str) и bytes больше не является своего рода строкой (это последовательность целых чисел).

- Для последовательностей (строк, списков, кортежей) используйте тот факт, что пустая последовательность есть false:
  
  Правильно:
  
  ```python
  if not seq:
  if seq:
  ```
  
  Неправильно:
  
  ```python
  if len(seq)
  if not len(seq)
  ```

- Не пользуйтесь строковыми константами, которые имеют важные пробелы в конце — они невидимы, а многие редакторы (а теперь и reindent.py) обрезают их.

- Не сравнивайте логические типы с True и False с помощью ==:
  
  Правильно:
  
  ```python
  if greeting:
  ```
  
  Неправильно:
  
  ```python
  if greeting == True:
  ```
  
  Совсем неправильно:
  
  ```python
  if greeting is True:
  ```