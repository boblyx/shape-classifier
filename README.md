# shape-classifier
Graph neural network for identifying 2D shapes represented as a vector shape (i.e. list of vertices).

Admittedly, it's a very stupid idea to use AI for this as shapes can probably be identified faster using mathematical principles, but this exercise in the similar vein of teaching AI to predict the next few points given x points generated using a quadratic formula etc.

## Synthetic Data
- Generate 200 shapes as graphs
- Accompany each shape tensor with a scalar value describing the name of the shape as enum:
    - Point
    - Line
    - Triangle
    - Square
    - Rectangle
    - Trapezium
    - Rhombus
    - Parallelogram
    - Trapezoid

## Tensor Definition

### Node Positions 
```python
[[0,1], [1,1], [1,0] ...]
```

### Edges
```python
[[0,1], [1,2] ...]
```

### Shape 
```python
[3]
```
# Development
1. Create a python venv
```bash
python -m venv venv
```
2. Activate the venv and install dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt
```
3. Start Jupyter Notebook and open `main.ipynb`.
```bash
jupyter notebook
```

## TODO
- Shape synthesiser
    - Point (DONE)
    - Line (DONE)
    - Triangle (DONE)
    - Square (DONE)
    - Rectangle (KIV)
    - Trapezium (KIV)
    - Rhombus (KIV)
    - Parallelogram (KIV)
    - Trapezoid (KIV)

- Model Design Experiments

- Training Loop

