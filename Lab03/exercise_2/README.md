# LAB 3: Exercise 2

## Requirements

You must need to create a python virtual environment to create the plot from the `iostat` output

```bash
python3 -m venv venv
source venv/bin/activate
```

Then, install the iostat (included in the sysstat package). 

```console
 sudo apt-get install sysstat -y
```

And finally install `iostat-tool`.

```console
pip install iostat-tool
```

## Execution

After the steps below, you just need to change the test to run inside the line 98 in `exercise_2.py` file as follows:

```python
test_random_write()

```

Then, execute the python file and, at the same time, execute the bash script `iostat.sh`.

Wait until "Done!" is prompted in the console.

Finally, execute the `plot.sh` file to plot the iostat output with matplotlib. The result plot will be inside the `plots` folder.

