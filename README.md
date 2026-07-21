# Applied Operations Research with Gurobi

**Mathematical formulation and resolution of complex business optimization problems using Gurobi Optimizer.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gurobi-Optimizer-ED2124.svg" alt="Gurobi">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Operations-Research-0052CC.svg" alt="Operations Research">
</p>

---

## Context

In modern business, making the "right" decision among millions of possibilities requires more than intuition - it requires mathematical optimization. **Gurobi Optimizer** is the undisputed industry standard for mathematical programming, used by top enterprises to solve large-scale logistical, financial, and operational challenges.

This repository showcases the ability to **translate real-world business requirements into rigorous mathematical models** (Mixed-Integer Linear Programming - MILP) and solve them using the Gurobi Python API (`gurobipy`).

---

## Methodology

Every project in this repository follows a strict, professional Operations Research workflow:
1. **Problem Analysis:** Understanding the business constraints, costs, and objectives.
2. **Mathematical Formulation:** Defining the Sets (Indexes), Decision Variables, Objective Function (minimize costs / maximize profit), and Constraints.
3. **Implementation:** Translating the math into clean, readable Python code using `gurobipy`.
4. **Optimization:** Running the Gurobi engine to find the globally optimal solution and analyzing the final results.

## The Optimization Models

The repository contains 7 standalone Jupyter Notebooks, each tackling a classic Operations Research scenario.

### 🏭 Supply Chain & Logistics
- **`supplychain.ipynb`**: Multi-echelon supply chain network design. Optimization of flows across facilities to minimize total holding, setup, and transportation costs.
- **`orange_distribution.ipynb`**: A complex distribution and transshipment problem to optimize the flow of goods from orchards to processing plants and final markets.

### 🚚 Transportation & Routing
- **`coffe_transport.ipynb`**: A classic transportation problem optimizing the routing of coffee from production plants to a network of bars, respecting capacities and demands to minimize total freight costs.

### 📅 Resource Allocation & Production
- **`netflix.ipynb`**: Content delivery / server allocation optimization, ensuring maximum coverage and minimum latency under tight budget and capacity constraints.
- **`pens.ipynb`**: A production planning and product-mix problem. Determines the optimal quantity of different types of pens to manufacture to maximize profit while respecting raw material availability and machine hours.

### 🚜 Agriculture & Public Sector
- **`farm_optimization.ipynb`**: Crop planning and land allocation to maximize agricultural yield and profit considering land, water, and labor constraints.
- **`vaccination_campaign_optimization.ipynb`**: A public sector logistics problem focused on assigning patients to vaccination centers minimizing travel distances and wait times under strict capacity limits.

## Technology Stack
- **Language**: Python
- **Solver Engine**: Gurobi Optimizer (`gurobipy`)
- **Environment**: Jupyter Notebook

## Context
These models were developed as part of the **Operational Research** course at Politecnico di Torino, demonstrating the practical application of mathematical programming to industrial problems.
