# Python

My Python scripts from courses and small personal experiments. It is an archive, kept as written at the time.

## Contents

| Path | Content |
|------|---------|
| root `*.py` | Small algorithm exercises: Fibonacci (naive, dynamic programming, fast), factorial, power, sums, binary search, largest element, quicksort, quadratic formula (`baskara.py`), matrices |
| `file_write/` | Times iterative, memoized recursive and fast-doubling Fibonacci, writes the timings to a file, and plots them with a MATLAB script |
| `file_share_python/` | File transfer over TCP sockets with `tqdm` progress bars (sender/receiver, folder variants, a zip-based `file_share.py` and a PyInstaller spec). It later became the [file_transfer_python](https://github.com/Gedankenn/file_transfer_python) repo |
| `ipv6/` | IPv6 echo client/server based on *Python Network Programming Cookbook* |
| `legendar/` | Subtitle (`.srt`) translator using Google Translate through [mtranslate](https://github.com/mouuff/mtranslate). It later became [Tradutor-legenda-online-python](https://github.com/Gedankenn/Tradutor-legenda-online-python) |
| `stocks/` | Stock quotes with `yfinance`, shown in a table and plotted with matplotlib. It later became the [stocks](https://github.com/Gedankenn/stocks) repo |
| `PyUserInput-master/` | Vendored copy of the third-party [PyUserInput](https://github.com/PyUserInput/PyUserInput) library (keyboard/mouse control) with its own license |

Many files have duplicates with `(1)`/`(2)` suffixes, left over from downloads/uploads.

## Running

Each script runs on its own with Python 3, for example:

```bash
python3 fibonacci.py
```
