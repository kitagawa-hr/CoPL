"""
```
#def hoge = 1
#def fuga = 2

hoge less than fuga is true by B-Lt{};
```

will be converted to

```
1 less than 2 is true by B-Lt{};
```
"""

import sys



def tokenize_definition(def_expr):
    """
    Example:
        >>> tokenize_definition("#def hoge = 1")
        ("hoge", "1")
    """
    definition, variable = def_expr.split("=", 1)
    return definition[5:].strip(), variable.strip()


def main(text):
    defs = []
    converted_lines = []
    for line in text.split("\n"):
        if line.strip().startswith("#def"):
            defs.append(tokenize_definition(line))
        else:
            for before, after in defs:
                line = line.replace(before, after)
            converted_lines.append(line)
    return "\n".join(converted_lines)


if __name__ == "__main__":
    in_path = sys.argv[-1]
    with open(in_path) as f:
        text = f.read()
    print(main(text))
