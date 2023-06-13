# Rock, Paper, Scissors in Python

This repo provides code for a simple game: Rock, Paper, Scissors.

## How to Run

First, download a Python IDE (if you don't have one). I suggest [PyCharm](https://www.jetbrains.com/pycharm/).

Next, download `game.py` and `gui.py` in this repo. (Just in case it wasn't obvious.)

Then, in PyCharm, create **TWO** new projects named `rock-paper-scissors` and `rock-paper-scissors-gui`.

Then, copy the `game.py` text in the `rock-paper-scissors` project and the `gui.py` text in the `rock-paper-scissors-gui` project.

> **Note**
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

### `PySimpleGUI`

> **Note**
>
> If you see that everything is invisible on macOS, please upgrade to the latest version of Python. If you did that, this message will show up:
>
> ```
> Mac OS Version is xx.x.x and patch enabled so applying the patch
> ```
>
> If you don't upgrade, this message will show up in red instead and all the text will be invisible.
>
> ```
> /path/to/python/file.py:xxxxx: UserWarning: You are running a VERY old version of tkinter x.x.x. You cannot use PNG formatted images for example. Please upgrade to 8.6.x
> warnings.warn('You are running a VERY old version of tkinter {}. You cannot use PNG formatted images for example. Please upgrade to 8.6.x'.format(tclversion_detailed), UserWarning)
> ```
>
> Upgrading to the latest version will be covered below.

Assuming that you read the note and use PyCharm on macOS, it comes equipped with Python 3.9. **That makes all of the text invisible!** To upgrade, follow the steps below:

First, go to [the lastest Python version's site](https://www.python.org/downloads/release/python-3114/) and scroll down to "macOS 64-bit universal2 installer". Click it.

Next, open the file up and follow the instrunctions on the file.

Then, in the "Applications" folder, find the folder that says "Python 3.11" and open it up.

Then, click on the "Install Certificate.command" file to install the certificates required.

Then, in PyCharm, create a new project\* and then click the interpreter that you are using.

Then, click "Add New Interpreter" and then "Add Local Interpreter".

> **Note**
>
> By this step, I hope you know where the interpreter was stored.

Then, locate the place the interpreter was, click it, and then click "OK".

Finally, copy and paste the code in `pysimplegi.py` and run the code!\*

\*This part applies to all users, macOS and non-macOS.

## What if you want a pre-built app?

Unfourtunately, the Qt version had a `segementation error`, so there is only the PySimpleGUI version.

You do not need to upgrade your Python or `pip`; this comes pre-installed with all the stuff you need.

Choose a file to download! (Windows and Linux versions don't exist yet, since my installer says that you have to run ot with the same OS that you wish to use.)

OS | File | Framework | Notes
---|---|---|---
macOS | [pysimplegui.zip](https://github.com/Brunozhon/python-rock-paper-scissors/blob/main/pysimplegui.zip) | PySimpleGUI | Run the `main` file. This version of PySimpleGUI uses Python 3.11 `tkinter` 8.6, not Python 3.9 and `tkinter` 8.5\*.

\*The former is the fixed version; the latter is the buggy version.
