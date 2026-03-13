# TANGRAM Project Page

This repository contains the source code for the official project website:
**[TANGRAM: Making Unstructured KV Cache Practical for Long-Term Conversation LLM Serving](https://aiha-lab.github.io/TANGRAM/)**.

## 💡 Overview
**TANGRAM** is an efficient LLM serving system designed to make unstructured KV cache compression practical for Long-Term Conversations (LTC). It addresses memory fragmentation and system bottlenecks to achieve:
* **9x Memory Savings**
* **2~9x Throughput Improvement**
* **<1% Accuracy Drop**

## 🔗 Links
* **[Official Website](https://aiha-lab.github.io/TANGRAM/)**
* **[Research Paper](https://aiha-lab.github.io/TANGRAM/#)**
* **[Main Code Repository](https://aiha-lab.github.io/TANGRAM/#)**

## 🏛️ System Architecture
TANGRAM introduces three core techniques:
1. **Profile-Guided Fixed Allocation** – Eliminates scheduling stalls.
2. **Head-Grouped PagedAttention** – Resolves memory fragmentation.
3. **AOT Load Balancing** – Ensures uniform GPU utilization.

---