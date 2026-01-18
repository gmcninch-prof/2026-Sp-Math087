---
author: George McNinch
title: |
  Resources: python & jupyter
date: 2026-01-01
---

# Overview

Our course will use the `python` programming language to perform
some machine computations needed to carry out mathematical modeling
tasks.

And parts of the notes of the course lectures will be made available
as `jupyter notebooks`.

There are a few ways that you should learn to interact with `python`
and `jupyter` for our class:

#. via [Google's colab]
#. by executing ``python`` code in a ``python`` interpreter on your computer
#. (optionally) using [jupyter notebooks](http://www.jupyter.org)  on your computer.

Here is a bit of what you need to know to enable these interactions:

- [Overview of `jupyter` notebooks](#notebooks)
- [Interacting with `jupyter` notebooks via colab](#colab)
- [installing the tools on your computer](#venv)
- [using the `jupyter notebook` viewer on your computer](#jupyter)


Before diving into the details, let me try to answer a few question
that you may have:

**Q** - do I need to install `juptyer` on my computer, or I just use `colab`?

: **A** - It is probably possible to just use `colab`. `colab`
  provides a reasonable environment for reading the course material,
  though for code execution it may (?) be a tad slow.
  
  **But**: using `python` exclusively through `colab` is a somewhat
  imperfect environment for producing code, and at least in the long
  run you'll be better served by learning to work with these tools on
  your own computer.

# An overview of `jupyter` notebooks {#notebooks}

[`Jupyter` notebooks] provide a way to package written material -- with
possible mathematical markup -- together with an interactive
environment for executing computer code.

The material for this course will mostly be presented in the form of
these `notebooks`. You can recognize `notebook` files by their
filename extension -- their file name has the form `*.ipynb`.
 
On the course site, notebooks will be posted with *two links* -- one
to `colab`, and one to an `*.ipynb` file.

- The simplest way to interact with `jupyter notebooks` is to use
  [Google's colab]. Clicking one of the links will open the notebook
  *in the cloud* via the site
  [colab.research.google.com](https://colab.research.google.com/).

- The other one link permits you to download the `notebook` file to
  your computer. In order to use this file, you will need to have a
  working installation of `python` and `jupyter`. See below for some
  discussion of how to [set up the required tools](#venv) and how to
  [use `jupyter`](#jupyter).

[`Jupyter` notebooks]: https://jupyter.org/
[Google's colab]: https://colab.research.google.com/

# Interacting with `jupyter` notebooks via Google's CoLab {#colab}

As [mentioned above](#notebooks), the course material will be
presented in the form of `jupyter` notebooks, and for each notebook
there will be a link to a copy of this notebook available via
`colab`.

`Colab` is a web-based free-to-use Jupyter notebook environment that
runs in *the cloud* and stores its notebooks on Google Drive.  When
you view a notebook in `colab` containing code, that code can be
executed. The code execution occurs *in the cloud*, which basically
means *on some google computer*. Thus, google's computer has `python`
and the relevant libraries installed and available.

You can choose to interact with the course notebooks on `colab`, abd
create your own notebooks there.

A good starting point to learn how to use colab (and jupyter notebooks
in general) is the document [Overview of Colaboratory
Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb).

# Installing the tools on your computer {#venv}

Here I hope to answer the questions: "What do I need to do to be able
to view and execute `jupyter` notebooks on my computer?"

(The instructions I'm about to give differ somewhat from instructions
I gave e.g. in Spring 2025).

We are going to use a tool called [`uv`](https://docs.astral.sh/uv/)
for managing `python` and it's libraries and packages.

To begin with, install `uv` following [the instructions
here](https://docs.astral.sh/uv/getting-started/installation/).

Open a `terminal` on your computer. We are going to use `uv` to create a directory
on your file system, so if you'd like that directory to be placed somewhere in particular,
you might changed directories in your terminal:

> ```
> george@valhalla:~$ cd math87
> george@valhalla:~/math87$ 
> ```

(You should only type the `cd jupyter` bit. And you may need to type a
more complicated string if the directory you created is nested below
your home directory. In these instructions going forward I'm going to
suppress writing the full `prompt` displayed by the terminal).

We now use `uv` to create a directory for `jupyter` and `python`
related packages by executing the following command in the terminal:

> ```
> $ uv init jupyter
> ```

You should see some output saying  something like

> ```
> Initialized project `jupyter` at `/home/george/math87/jupyter`.
> ```

Now change to the directory just created:

> ```
> $ cd jupyter
> ```

And install relevant packages:

> ```
> $ uv add jupyter matplotlib nbconvert numpy pandas scipy sympy
> ```

Now, we can use `uv` to start a `jupyter` server on your computer:

> ```
> $ uv run jupyter-lab
> ```

After running this command, you should see a bunch of output in the
terminal (which you can largely ignore). And a tab should open in your
browser with a URL like

> ```
> http://localhost:8888/lab
> ```

And in that tab you can interact with the `jupyter` server running on
your computer. You can stop that server from running by stopping the
`uv run juypter-lab` job (say be typing `ctrl-c` in the terminal, or
by closing the terminal completely...)

# Interacting with `jupyter` on your computer {#jupyter}


You can always view and interact with `jupyter notebooks` on
`colab`. But if you carried out the above installation instructions,
you can now use `jupyter` notebooks on your own computer.

As explained in the installation notes (above), you can start
`jupyter` from the command-line/terminal via `uv run jupyter-lab` in a
terminal, after first making sure you are in the correct directory).

In fact, there are various versions of the `jupyter` interface - you
could instead use the command `uv run jupyter notebook`. Honestly, I'm
not completely sure I understand why there are two different
interfaces; you should experiment for yourself.

The page that opens will have a `URL` that looks something like:

> ```
> http://localhost:8888/lab
> ```

This `URL` tells you that there is now a `server` running on your
local machine, and that your web browser is communicating with that
server.

In the web page at this location, you should see in particular an
interface where you can interact with `jupyter notebooks`. You can
create a new notebook from the `File` menu: `New -> Notebook`. If you
are asked to `Select Kernel`, you should select `Python 3`.

You are now editing a file name `Untitled.ipynb`. 

If you save a `jupyter notebook` (i.e. a `ipynb` file) in your directory tree, you can open it using
the `File` menu: `Open from path`

You can end the `jupyter` notebook session by typing `C-c` (twice)
in the terminal where you started the command, or by menu-driven
commands in the web-interface.


# Some learning resources for python and scientific computing


(Honestly, I just borrowed this list from a previous instructor, but
the links look useful).

* [DataCamp's interactive Intro to Python tutorial](https://www.learnpython.org/)
* [Python for Everybody (University of Michigan MOOC)](https://www.py4e.com/lessons)
* [A short Python and NumPy tutorial (Stanford CS231)](http://cs231n.github.io/python-numpy-tutorial/)
* [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)
* Numpy
  * [Introduction to
    NumPy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html)
  * [NumPy reference
    guide](https://docs.scipy.org/doc/numpy/reference/) (chapter 2 of
    VanderPlas' *Python Data Science Handbook*)
* Matplotlib
  * [Official Pyplot tutorial
    (short)](https://matplotlib.org/tutorials/introductory/pyplot.html)
  * [Visualization with Matplotlib (chapter 4 of VanderPlas' *Python
    Data Science
    Handbook*)](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html)
  * [Gallery of Matplotlib
    examples](https://matplotlib.org/gallery/index.html)
