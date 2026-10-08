# Catapult Experiment

## Overview

This project investigates how different catapult settings affect projectile performance using a designed experiment and statistical analysis.

A \(2^k\) factorial experiment was used to study three experimental factors:

* **Arm Position**
* **Vertical Position**
* **Stop Angle**

The experiment was designed to evaluate the effects of these factors and their combinations on the measured response.

## Experimental Design

A \(2^k\) factorial design was used with three factors, each tested at two levels:

| Factor            | Levels     |
| ----------------- | ---------- |
| Arm Position      | 2 / 1 |
| Vertical Position | 4 / 1 |
| Stop Angle        | 90 / 120 |

This produced a total of \(2^3 = 8\) treatment combinations.

The factorial design allowed the effects of the individual factors and their interactions to be investigated.

## Data Analysis

The experimental data were analyzed using Python.

### Box-Cox Transformation

A Box-Cox transformation was applied to the response data to transform the distribution and improve the suitability of the data for statistical analysis.

The transformation was used to identify an appropriate form of the response variable before modeling the experimental results.

### Statistical Analysis

The transformed experimental data were analyzed to investigate the effects of:

* Arm Position
* Vertical Position
* Stop Angle
* Interactions between experimental factors

## Technologies

* Python
* NumPy
* pandas
* Statistical Analysis
* Design of Experiments
* \(2^k\) Factorial Design
* Box-Cox Transformation
* LaTeX

## Files

* **`finalproj.py`** — Python code used for the experimental data analysis.
* **`report/Wren_Nicol_Final_Report.pdf`** — Full report describing the experiment, analysis, results, and conclusions.
* **`report/catapult_report.tex`** — LaTeX source for the report.

## Report

The complete experimental methodology, statistical analysis, results, and conclusions are available in the report.
