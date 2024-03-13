## Getting Started

There might be either `python` or `C++` based solutions in this folders.
Thus, a `python` based script can be launched simply by running

```shell
python3 app.py
```

If there is no `makefile` present a simple `C++` application i.e. for example `app.cpp` file can be compiled with `make` command by running

```make
make app
```

If you prefer to compile by hand, than the following like can be used

```shell
g++ app.cpp -o app -std=c++17 -Wall -Wextra -pedantic -g
```

Additionally, there might be some input file which can be used for testing purposes, named `ipunt-1`, `input-2` and etc.

```shell
cat input-1 | ./app
```

Run all tests

```bash
for input in ./input-*; echo "${input}"; do cat "${input}" | ./app; done
```

If you are using a `fish` shell than this lines tuns into

```fish
for input in ./input-*;  echo $input; cat $input | ./app; end
```

## Locate binary files

```shell
 find . -type f ! -size 0 -exec grep -IL . "{}" \;
```
