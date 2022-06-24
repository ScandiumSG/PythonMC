# [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) approximation of the value of PI.\*

## How to use

Two options; a CLI and a plot generator

### CLI

Navigate to ./src and run

```
python CLIApproximator.py
```

Terminal will the prompt you for number of iterations desired, and if you want reports underway of the PI value. If you don't want status reports just press enter instead of entering any value.

### Plot generator

Navigate to ./src and run

```
python generatePlot.py
```

The terminal will prompt you for the number of datapoints/iterations to use. The plot should then be shown when all datapoints are generated and sorted.

## Modules required

See `./src requirements.txt` for modules required to run the application.

To install all using pip use the command

```
pip install -r requirements.txt
```

from within the `./src` folder

### Used modules:

-   [tqdm](https://github.com/tqdm/tqdm) - Status bar on CLI operations
-   [numpy](https://github.com/numpy/numpy) - Arrays
-   [matplotlib](https://github.com/matplotlib/matplotlib) - Plotting tool used for generatePlot.py

---

\* Potentially other approximations in the future.
