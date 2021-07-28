# Reviewing the Trachoma model

#### Reviewers: Thibault Lestang and Ben Lambert (OxRSE members)

#### Date: 28th July 2021

## Introduction

The OxRSE team were tasked with reviewing the `Trachoma_Simulation()` function at https://github.com/ArtRabbitStudio/ntd-model-trachoma with an aim to improving the efficiency of it. The review that we conducted encompassed the following elements:

1. profiling the code to identify bottlenecks

2. suggesting improvements to individual units of code and benchmarking these pieces versus the existing versions

3. integrating these changes into the model and benchmarking the whole 

Note that, in 3., we have not extensively tested our modifications and suggest this be done before integrating our changes.



# Code profiling

We first profiled the `Trachoma_Simulation` function. On initial running of the function, it was clear that it was running in parallel. Since parallelisation can make it harder to understand code profiling results, we changed the line:

`num_cores = 1`

to:

`num_cores = 1`

in the `trachoma_simulations.py` file.



To do so, we analysed the following code snippet (`test_run.py`; extracted from the `trachoma_tests.ipynb` notebook):

```python
from trachoma.trachoma_simulations import Trachoma_Simulation


BetFilePath = 'files/InputBet_scen1.csv'
MDAFilePath = 'files/InputMDA_scen1.csv'
PrevFilePath = 'files/OutputPrev_scena1.csv'
InfectFilePath = 'files/Infect.csv'

Trachoma_Simulation(BetFilePath=BetFilePath,
                    MDAFilePath=MDAFilePath,
                    PrevFilePath=PrevFilePath,
                    SaveOutput=False,
                    OutSimFilePath=None,
                    InSimFilePath=None,
                    InfectFilePath=InfectFilePath)
```

To profile the code, we used `cProfile` and [snakeviz](https://jiffyclub.github.io/snakeviz/), running the following bash command:

`python3 -m cProfile -o temp.dat test_run.py`

The resultant code took ~475s to run.