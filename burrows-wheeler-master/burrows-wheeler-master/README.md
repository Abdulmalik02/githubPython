# Burrows-Wheeler
Python implementation of the Burrows-Wheeler transform

https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

## Installation

`pip install burrowswheeler`

## Usage

```
from burrowswheeler import transform, inverse

string = 'banana'

transformed_string = transform(string)
print(transformed_string)

original_string = inverse(transformed_string)
print(original_string)

print(string == original_string)
```
