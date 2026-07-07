# Tangram Project Page

Source code for the official project website of
**[Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving](https://aiha-lab.github.io/tangram-page/)**.

## Overview

**Tangram** brings KV cache compression to vLLM with ragged paging:

* **Non-uniform and uniform KV cache compression**, natively integrated into vLLM
* **Seamless vLLM integration** — compatible with paged attention, continuous batching, chunked prefill, and CUDA graph mode
* **Real memory reclamation** — compressed KV cache is actually freed, turning memory savings into higher serving throughput
* **Zero runtime scheduling overhead** — budget reservation and ahead-of-time (AOT) load balancing keep compression off the critical path

## Links

* [Official Website](https://aiha-lab.github.io/tangram-page/)
* [Paper (arXiv)](https://arxiv.org/abs/2606.06302)
* [Main Code Repository](https://github.com/aiha-lab/tangram)
