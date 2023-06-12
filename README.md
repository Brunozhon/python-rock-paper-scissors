# Rock, Paper, Scissors in Python

This repo provides code for a simple game: Rock, Paper, Scissors.

## How to Run

First, download a Python IDE (if you don't have one). I suggest [PyCharm](https://www.jetbrains.com/pycharm/).

Next, download the Python files **AND** the license in this repo. (Just in case it wasn't obvious.)

Then, in PyCharm, create **TWO** new projects named `rock-paper-scissors` and `rock-paper-scissors-gui`.

Then, copy the `game.py` text in the `rock-paper-scissors` project and the `gui.py` text in the `rock-paper-scissors-gui` project.

> **Note:**
>
> You may have noticed that an error popped up saying that `PyQt6` is not a framework. In this case, for PyCharm, simply type the text below into PyCharm's terminal.
>
> ```
> pip install pyqt6
> ```

Finally, press the run button and see what happens.

## What if you want to/need to use a different GUI library?

### `PySide`

If you want to use PySide, simply replace `PyQt` with `PySide`.

You also have to use a different `pip` command, which will be shown below in case it wasn't obvious.

```
pip install pyside6
```

You can also try migrating to PyQt, alough the same code has also been tested using PySide.
