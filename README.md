# TANGRAM Project Page

This repository contains the source code for the official project website:
**[Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving](https://aiha-lab.github.io/TANGRAM/)**.

## 💡 Overview
**TANGRAM** is an efficient LLM serving system designed to make non-uniform KV cache compression practical for Multi-turn Conversations. It addresses memory fragmentation and system bottlenecks to achieve:
* **4× Memory Savings**
* **Up to 2.6× Throughput Improvement**
* **<1% Accuracy Drop**

## 🔗 Links
* **[Official Website](https://aiha-lab.github.io/TANGRAM/)**
* **[Research Paper](https://aiha-lab.github.io/TANGRAM/#)**
* **[Main Code Repository](https://aiha-lab.github.io/TANGRAM/#)**

## 🏛️ System Architecture
TANGRAM introduces three core techniques:
1. **Deterministic Budget Allocation** – Eliminates scheduling stalls.
2. **Head Group PagedAttention** – Resolves memory fragmentation.
3. **AOT Load Balancing** – Ensures uniform GPU utilization.

---