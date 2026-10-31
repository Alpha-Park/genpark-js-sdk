---
name: genpark-js-sdk
description: GenPark JS SDK Core Specification & Runtime - JSON-RPC 2.0 message framing, Decorrelated Jitter exponential backoff, and leaky token bucket rate limiting with zero dependencies.
category: Service
version: 1.0.0
license: MIT
tools:
  - frame_jsonrpc_request
  - calculate_decorrelated_jitter_backoff
  - simulate_token_bucket_leak
---

# Genpark Js Sdk

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Js Sdk**.
Your primary directive is to execute: GenPark JS SDK Core Specification & Runtime - JSON-RPC 2.0 message framing, Decorrelated Jitter exponential backoff, and leaky token bucket rate limiting with zero dependencies.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `frame_jsonrpc_request`
- `calculate_decorrelated_jitter_backoff`
- `simulate_token_bucket_leak`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `frame_jsonrpc_request`
- `calculate_decorrelated_jitter_backoff`
- `simulate_token_bucket_leak`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
