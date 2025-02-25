# Create an animation that fits a line to data

## Installation

### Download the code 

Clone the repository to your machine using `git`, or [Download ZIP](https://github.com/andycasey/manim-line-example/archive/refs/heads/main.zip). With `git`:
```
git clone git@github.com:andycasey/manim-line-example.git
cd manim-line-example/
```

### Create a Python environment

I recommend using [`uv`](https://docs.astral.sh/uv/) for Python environments.

If you have an existing Python environment that you want to use, that's fine.
You will need to install the `manim` library. If you don't have an environment already, you can create one with `uv`:

```
uv venv
source .venv/bin/activate
uv pip install manim
```

## Make the animation

You will need to make sure you have activated your Python environment that has `manim` installed using `source .venv/bin/activate` from the folder where your environment was created.

For a high quality version:

```
manim -qk line.py FitLine
```

For a low-quality version:

```
manim -ql line.py FitLine
```

Both of these commands will create a video in the `media/videos/line/` folders.


## Contact

Andy Casey (andrew.casey@monash.edu)
