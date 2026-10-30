# -*- coding: utf-8 -*-
from client import GenParkJsSdk

sdk = GenParkJsSdk()

# 1. JSON-RPC Framing
req = sdk.frame_jsonrpc_request("agent/executeTask", {"taskId": "task-8801", "mode": "autonomous"}, request_id="req-99")
print(f"JSON-RPC Frame: Valid={req['valid']}")
print(f"  Payload: {req['framed_payload']}")

# 2. Decorrelated Jitter Backoff
prev_sleep = 100.0
print()
print("Decorrelated Jitter Backoff Sequence:")
for att in range(1, 5):
    res = sdk.calculate_decorrelated_jitter_backoff(attempt=att, previous_sleep_ms=prev_sleep, seed=att * 10)
    print(f"  Attempt {att}: NextSleep={res['next_sleep_ms']}ms (Prev={res['previous_sleep_ms']}ms)")
    prev_sleep = res['next_sleep_ms']

# 3. Leaky Token Bucket Rate Limiter
tb = sdk.simulate_token_bucket_leak(current_tokens=10.0, capacity=50.0, fill_rate_per_sec=10.0, elapsed_seconds=2.0, tokens_requested=25.0)
print()
print(f"Token Bucket: Allowed={tb['request_allowed']} (Remaining={tb['tokens_remaining']}/{tb['capacity']}, Status={tb['rejection_status']})")
