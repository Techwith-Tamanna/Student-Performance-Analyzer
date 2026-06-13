# Student-Performance-Analyzer

Welcome to my first official GitHub repository! 

**Student-Performance-Analyzer** is a Python-based automation tool designed to help educators to instantly transform raw student scores into meaningful, structured performance reports. By utilizing the power of the **NumPy** library, this script processes datasets efficiently, calculates key statistical milestones, and categorizes students into actionable academic tiers.

## Why I Built This?
As someone diving deep into Python and Data Analytics, I wanted to solve a real-world problem: **grading administrative overhead**. Teachers often spend hours manually calculating averages and sorting students into performance buckets. 
This project was built to:
1. **Automate** repetitive grading workflows.
2. **Practice** handling numerical data structures efficiently using NumPy.
3. **Master** conditional logic and loops in Python to generate clean console dashboards.

## Key Features & Architecture
The application is broken down into three distinct stages:

### 1. Statistical Core (Powered by NumPy)
Instead of using slow Python loops to calculate class statistics, the script utilizes vectorized NumPy functions for optimal performance:
* `np.mean(marks)`: Computes the exact arithmetic mean of the classroom.
* `np.max(marks)`: Instantly isolates the top-performing score.
* `np.min(marks)`: Identifies the lowest score to help track students who need immediate intervention.

### 2. Automated Performance Tiering
The script dynamically loops through the dataset and assigns a qualitative grade based on standard educational brackets:
* 🏆 **>= 80**: Excellent
* 👍 **>= 65**: Good
* 😐 **>= 33**: Average
* ⚠️ **< 33**: Essential Repeat

### 3. Final Summary Matrix
At the end of the execution, a clean tabular summary prints out the total headcount for each tier, giving educators an immediate bird's-eye view of classroom health.

---
## Tech Stack
* **Language:** Python 3.10+
* **Libraries:** NumPy (`import numpy as np`)
---

## Getting Started
### Prerequisites
Make sure you have Python installed on your machine. You will also need `pip` to install the NumPy package.

### Installation
**Clone this repository** to your local machine:
   ```bash
  git clone [https://github.com/Techwith-Tamanna/Sutdent-Performance-Analyzer.git](https://github.com/Techwith-Tamanna/Sutdent-Performance-Analyzer.git)
  cd Sutdent-Performance-Analyzer
