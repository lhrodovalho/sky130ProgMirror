A <b>programmable cascode current mirror</b> made using the Skywater 130 nm opensource PDK. </br>


Table of contents
==============================
<!--ts-->
  * [Summary](#Summary)
  * [Description](#Description)
    * [Schematics and Layouts](#Schematics-and-Layouts)
    * [Simulation Results](#Simulation-Results)
  * [Team Members](#Team-Members)
  * [References](#References)
<!--te-->

---
Summary
=======

This is a programmable cascode current mirror with selectable gains from 1/4 to 4. There are multiple configurations for the same gain and less current offset.

### Target Performance Summary

| Specifications        | -                            |
| :---                  | :---                         |
| VDD                   | 1.0-5.0 V                    |
| Area                  | m x n &mu;m²                 |

---
Description
===========

### Schematics and Layouts
---
![image](./lib/pgmirror/figures/progmirror_circuit.png)
![image](./lib/pgmirror/figures/progmirror_layout.png)

Programmable cascode current mirror circuit diagram and layout.

### Simulation Results

#### TT corner
![image](./docs/plots/tt_dc_vdd_io.png)

Status and Issues
============

* There are no Xschem files. All simulations are from extracted netlists.
* Documentation is extremely incomplete.

Team members
============

**Ph.D. Luís Henrique Rodovalho (Rodovalho)**
| [luishenriquerodovalho@gmail.com](mailto:luishenriquerodovalho@gmail.com?subject=Hi% "Hi!") <img width="15" src="https://cdn-icons-png.flaticon.com/128/2089/2089181.png" alt="email"> | 

References
==========

TO DO.

