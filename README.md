# TANGRAM Project Page

This repository contains the source code for the official project website:
**[Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving](https://aiha-lab.github.io/tangram-page/)**.

## 💡 Overview
**TANGRAM** is an efficient LLM serving system designed to make non-uniform KV cache compression practical for Multi-turn Conversations. It addresses memory fragmentation and system bottlenecks to achieve:
* **4× Memory Savings**
* **Up to 2.6× Throughput Improvement**
* **Minimal Accuracy Loss**

## 🔗 Links
* **[Official Website](https://aiha-lab.github.io/tangram-page/)**
* **[Research Paper](https://aiha-lab.github.io/tangram-page/#)**
* **[Main Code Repository](https://github.com/aiha-lab/tangram)**

## 🏛️ System Architecture
TANGRAM introduces three core techniques:
1. **Deterministic Budget Allocation** – Eliminates scheduling stalls.
2. **Head Group PagedAttention** – Resolves memory fragmentation.
3. **AOT Load Balancing** – Ensures uniform GPU utilization.

---