# Data Locality Optimization in Python — HPC Performance Prototype

This repository contains a Python prototype developed to demonstrate the impact of data locality optimization on performance in high-performance computing (HPC) applications. The work is based on findings from the empirical study “An Empirical Study of High Performance Computing (HPC) Performance Bugs”, which highlights data locality issues as one of the most common and impactful sources of performance degradation in HPC systems.

This prototype compares two data-structure approaches:

  - A naïve Python list (non-contiguous memory, poor locality)
  - A NumPy contiguous array (optimized for spatial locality and vectorization)

The goal is to show how rethinking data structure layout—not the algorithm—can dramatically improve performance.


## Features

- Implements a simple numerical kernel: sum of squares

- Benchmarks:

  Python list loop
  
  NumPy vectorized array operation

- Generates a bar chart comparing execution times

- Demonstrates the performance impact of:

  contiguous memory
  
  vectorized operations
  
  cache-friendly access patterns

- Clear, reproducible results suitable for academic reporting

## Requirements

To run the prototype, install the required dependencies:

    pip install -r requirements.txt

Dependencies include:
  NumPy — for contiguous arrays and vectorized computation
  Matplotlib — for generating the performance chart
