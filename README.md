# Neural Networks

![](graphics/lander.gif)


## About 
This repo contains resources and code for a computer vision module on neural networks. 


### Note on Launching the Jupyter Notebooks
To properly view the images and animations, please launch your jupyter notebook from the root directory of this repository. 

## Lectures
| Order |   Notebook/Slides  | Topics | Required Viewing Before | Additional Reading | Notes |
| ----- | ------------------ | ------ | ----------------------- | ------------------ | ----- |
| 1 | [A Brief History of Neural Networks](https://github.com/unccv/neural_networks/blob/master/notebooks/A%20Brief%20History%20of%20Neural%20Networks.ipynb) | Development of Perceptrons, MLPs, Backpropogation | - | - | - |
| 2 | [Neural Nets Demystified Part 1](https://github.com/unccv/neural_networks/blob/master/notebooks/Neural%20Networks%20Demystified%20%5BPart%201%5D.ipynb) | Building a Simple Neural Networok, Forwardpropogation, Backpropogation| [Neural Networks Demystified Parts 1-4](https://www.youtube.com/watch?v=bxe2T-V8XRs) | [Who is afraid of non-convex loss functions?](https://www.youtube.com/watch?v=8zdo6cnCW2w) | Print [Backpropogation Notes](https://github.com/unccv/neural_networks/blob/master/backprop_guided_notes.pdf) before lecture. |
| 3 | [Neural Nets Demystified Part 2](https://github.com/unccv/neural_networks/blob/master/notebooks/Neural%20Networks%20Demystified%20%5BPart%202%5D.ipynb) | Backpropogation, Training, Regularization, Overfitting| [Neural Networks Demystified Parts 4-7](https://www.youtube.com/watch?v=bxe2T-V8XRs) | [Regularization for Deep Learning](https://www.deeplearningbook.org/contents/regularization.html) | - |


## Setup 

The Python 3 [Anaconda Distribution](https://www.anaconda.com/download) is the easiest way to get going with the notebooks and code presented here. 

(Optional) You may want to create a virtual environment for this repository: 

~~~
conda create -n cv python=3 
source activate cv
~~~

You'll need to install the jupyter notebook to run the notebooks:

~~~
conda install jupyter

# You may also want to install nb_conda (Enables some nice things like change virtual environments within the notebook)
conda install nb_conda
~~~

This repository requires the installation of a few extra packages, you can install them all at once with:
~~~
pip install -r requirements.txt
~~~

(Optional) [jupyterthemes](https://github.com/dunovank/jupyter-themes) can be nice when presenting notebooks, as it offers some cleaner visual themes than the stock notebook, and makes it easy to adjust the default font size for code, markdown, etc. You can install with pip: 

~~~
pip install jupyterthemes
~~~

Recommend jupyter them for **presenting** these notebook (type into terminal before launching notebook):
~~~
jt -t grade3 -cellw=90% -fs=20 -tfs=20 -ofs=20 -dfs=20
~~~

Recommend jupyter them for **viewing** these notebook (type into terminal before launching notebook):
~~~
jt -t grade3 -cellw=90% -fs=14 -tfs=14 -ofs=14 -dfs=14
~~~