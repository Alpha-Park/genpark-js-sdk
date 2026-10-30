# -*- coding: utf-8 -*-
"""
GenPark JS SDK MCP Server
FastMCP standard interface for JSON-RPC 2.0 framing, decorrelated jitter backoff, and token bucket rate limits.
"""

import json
from typing import Dict, Any, Optional
from client import GenParkJsSdk

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("genpark-js-sdk")
except ImportError:
    class MockFastMCP:
        def __init__(self, name):
            self.name = name
        def tool(self):
            def decorator(f):
                return f
            return decorator
    mcp = MockFastMCP("genpark-js-sdk")

sdk = GenParkJsSdk()

@mcp.tool()
def frame_jsonrpc_request(
    method: str,
    params: Any,
    request_id: Optional[Any] = 1,
    is_notification: bool = False
) -> str:
    """
    Frames and validates a compliant JSON-RPC 2.0 protocol envelope.
    """
    res = sdk.frame_jsonrpc_request(method, params, request_id, is_notification)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_decorrelated_jitter_backoff(
    attempt: int,
    previous_sleep_ms: float = 100.0,
    base_sleep_ms: float = 100.0,
    max_sleep_ms: float = 5000.0
) -> str:
    """
    Calculates next retry delay using AWS Decorrelated Jitter formula.
    """
    res = sdk.calculate_decorrelated_jitter_backoff(attempt, previous_sleep_ms, base_sleep_ms, max_sleep_ms)
    return json.dumps(res, indent=2)

@mcp.tool()
def simulate_token_bucket_leak(
    current_tokens: float,
    capacity: float = 100.0,
    fill_rate_per_sec: float = 20.0,
    elapsed_seconds: float = 1.5,
    tokens_requested: float = 15.0
) -> str:
    """
    Simulates token bucket replenishment and consumption.
    """
    res = sdk.simulate_token_bucket_leak(current_tokens, capacity, fill_rate_per_sec, elapsed_seconds, tokens_requested)
    return json.dumps(res, indent=2)

def main():
    print("Testing GenPark JS SDK:")
    print(frame_jsonrpc_request("tools/call", {"name": "lookup"}, 42))

if __name__ == "__main__":
    main()
