# LRU Cache Service

A from-scratch implementation of an LRU (Least Recently Used) cache in Python,
exposed as a REST API using FastAPI.

## What is LRU?

LRU is a cache eviction policy: when the cache is full, it removes the item
that was used least recently. This implementation achieves O(1) time complexity
for both `get` and `put` by combining a hash map (dict) with a doubly linked list.

## Why this project?

- Demonstrates understanding of a classic data structures like doubly linked list and hashmap.
- Shows how to expose a data structure as a service via a REST API.
- Benchmarks hit/miss rate to measure cache effectiveness.


## Tech Stack

- Python 3
- FastAPI (REST API layer)
- Pytest (unit tests)

## Project Structure

```
lru-cache/
├── app/
│ ├── init.py
│ ├── cache.py # LRU Cache implementation (hash map + doubly linked list)
│ ├── models.py # Pydantic request/response models
│ ├── routes.py # FastAPI endpoints
│ └── main.py # FastAPI app entry point
├── tests/
│ ├── init.py
│ ├── test_cache.py # Unit tests for the cache class
│ └── test_routes.py # Tests for the API endpoints
├── benchmark/
│ └── benchmark.py # Benchmark script for measuring hit rate
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```


### 2. Run tests
```bash
pytest tests/ -v
```


### 3. Start the API server
```bash
uvicorn app.main:app --reload
```


Then open http://127.0.0.1:8000/docs to try the endpoints interactively.

### 4. Running BenchMarks Yourself

```bash
python benchmark/benchmark.py
```

## Benchmark Results

The benchmark sends 500 requests per run (70% reads, 30% writes) with a cache capacity of 6. The `Key Range` is the number of unique keys the workload uses. A smaller key range means the working set fits in the cache; a larger key range means the working set exceeds capacity and forces eviction.

| Key Range | Hit Rate |
|-----------|----------|
| 3         | 99.71%   |
| 4         | 97.27%   |
| 5         | 97.73%   |
| 20        | 26.18%   |

**Interpretation:** When the working set is smaller than the cache capacity, almost every read hits because all keys stay in the cache. As the working set grows past capacity, LRU eviction kicks in and the hit rate drops sharply. This confirms the cache is behaving as designed.


## API Endpoints

- `GET /cache/{key}` — Retrieve a value
- `POST /cache` — Insert or update a key-value pair
- `DELETE /cache/{key}` — Remove a key
- `GET /cache-stats` — View hit/miss statistics
- `GET /cache-items` — View current cache contents

## What I Learned

- How to implement a doubly linked list with dummy head and tail nodes.
- Why a hash map + doubly linked list gives O(1) time for LRU operations.
- How to expose a Python class as an HTTP service using FastAPI.
- How to write unit tests with pytest and integration tests with FastAPI's TestClient.
- How to benchmark a service and interpret the results.