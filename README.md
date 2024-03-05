# shape-classifier
Graph neural network for identifying shapes.
It's a very stupid idea to use AI for this, but its in the similar vein of teaching AI to predict the next few points given x points.

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

## TODO
- Shape synthesiser
    - Point (DONE)
    - Line (DONE)
    - Triangle (WIP)
    - Square (KIV)
    - Rectangle (KIV)
    - Trapezium (KIV)
    - Rhombus (KIV)
    - Parallelogram (KIV)
    - Trapezoid (KIV)

- Model Design Experiments

- Training Loop

