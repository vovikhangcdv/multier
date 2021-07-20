# Multier

The skeleton script used to customize to run multi-threaded scripts.

## Usage

Open file `multier.py` and: 
- Step 1: Write your function

- Step 2: Define input list of function

- Step 3: Call multier function


```python
... # omit multier code
def funName(data1, data2):
    # TODO

if __name__ == '__main__':
    # TODO: dataList = ...
    _input = [tuple([data[0], data[1]]) for data in dataList]
    NUM_THREAD = 10
    multithreading(_input, funName, NUM_THREAD)
```