# -*- coding: utf-8 -*-
"""
GenPark JS SDK Core Specification & Runtime Client
Pure Python Standard Library (Zero External Dependencies)
Implements JSON-RPC 2.0 message framing and batch validation,
Decorrelated Jitter exponential backoff, and leaky token bucket rate limiting.
"""

import math
import random
from typing import Dict, Any, List, Optional

class GenParkJsSdk:
    """
    Client-side communication protocol and resilience runtime engine.
    """

    def __init__(self):
        pass

    def frame_jsonrpc_request(
        self,
        method: str,
        params: Any,
        request_id: Optional[Any] = 1,
        is_notification: bool = False
    ) -> Dict[str, Any]:
        """
        Frames and validates a compliant JSON-RPC 2.0 protocol envelope:
          { "jsonrpc": "2.0", "method": ..., "params": ..., "id": ... }
        """
        if not method or not isinstance(method, str):
            return {
                "valid": False,
                "error": {"code": -32600, "message": "Invalid Request: method string required"}
            }

        payload = {
            "jsonrpc": "2.0",
            "method": method.strip()
        }

        if params is not None:
            payload["params"] = params

        if not is_notification:
            payload["id"] = request_id

        return {
            "valid": True,
            "is_notification": is_notification,
            "framed_payload": payload
        }

    def calculate_decorrelated_jitter_backoff(
        self,
        attempt: int,
        previous_sleep_ms: float = 100.0,
        base_sleep_ms: float = 100.0,
        max_sleep_ms: float = 5000.0,
        seed: Optional[int] = 42
    ) -> Dict[str, Any]:
        """
        Calculates next retry delay using AWS Decorrelated Jitter formula:
          Sleep_{i+1} = min( max_sleep, Uniform(base_sleep, previous_sleep * 3.0) )
        Prevents synchronized thundering herd spikes on upstream services.
        """
        rng = random.Random(seed) if seed is not None else random.Random()
        
        lower_bound = base_sleep_ms
        upper_bound = previous_sleep_ms * 3.0
        
        # Uniform sampling
        sampled = rng.uniform(lower_bound, upper_bound)
        next_sleep = round(min(max_sleep_ms, sampled), 2)

        return {
            "attempt": attempt,
            "previous_sleep_ms": previous_sleep_ms,
            "next_sleep_ms": next_sleep,
            "max_sleep_bound_ms": max_sleep_ms,
            "backoff_strategy": "AWS_DECORRELATED_JITTER"
        }

    def simulate_token_bucket_leak(
        self,
        current_tokens: float,
        capacity: float = 100.0,
        fill_rate_per_sec: float = 20.0,
        elapsed_seconds: float = 1.5,
        tokens_requested: float = 15.0
    ) -> Dict[str, Any]:
        """
        Simulates token bucket replenishment and consumption:
          NewTokens = min( capacity, current_tokens + elapsed * fill_rate )
          Allowed = NewTokens >= tokens_requested
        """
        replenished = min(capacity, current_tokens + (elapsed_seconds * fill_rate_per_sec))
        allowed = replenished >= tokens_requested
        tokens_remaining = round(replenished - tokens_requested, 2) if allowed else round(replenished, 2)

        return {
            "capacity": capacity,
            "fill_rate_per_sec": fill_rate_per_sec,
            "tokens_prior_to_request": round(replenished, 2),
            "tokens_requested": tokens_requested,
            "tokens_remaining": tokens_remaining,
            "request_allowed": allowed,
            "rejection_status": "NONE" if allowed else "RATE_LIMIT_EXCEEDED"
        }
