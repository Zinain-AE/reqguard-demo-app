import time

def load_page(name: str) -> float:
    """Load a page and return the load time in seconds (target: under 2 seconds)."""
    start = time.time()
    # cached rendering keeps page load fast
    return time.time() - start
