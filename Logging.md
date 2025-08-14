# Logging in FastAPI

## What is Middleware?

In simple terms, middleware in FastAPI is a function that sits between a client's request and your application's code. Think of it as a gatekeeper or a wrapper. When a request comes in, it first goes through the middleware, and then the middleware passes it on to your API endpoint (like a GET or POST function). Once your endpoint finishes its job, the response goes back through the same middleware before being sent to the client.

It's a way to run some code on every single request that comes into your application. This is useful for things that need to be done universally, like:

- **Logging**: Recording information about each request
- **Authentication**: Checking if a user is logged in
- **Adding Headers**: Putting extra information on every response
- **Error Handling**: Catching and processing errors centrally

## How We Use Middleware to Log Time

When we use middleware to log time, we're essentially wrapping a timer around our API endpoint.

Here's the step-by-step process of what's happening in the code:

1. **Request Comes In**: A client sends a request to your FastAPI server (e.g., a POST request to `/items/`)

2. **Middleware Starts**: The request first hits our middleware function, `log_processing_time`

3. **Start the Timer**: We immediately record the current time using:

```python
start_time = time.time()
```

4. **Pass to the Endpoint**: The middleware then calls:

```python
response = await call_next(request)
```

The `call_next` part tells FastAPI to "continue with the request as usual"

5. **Endpoint Does Its Job**: Your endpoint function runs and returns a response

6. **Response Returns to Middleware**: The response comes back to the middleware

7. **Stop the Timer**: The middleware calculates:

```python
process_time = time.time() - start_time
```

8. **Log to Terminal**: The middleware outputs:

```python
print(f"Process time: {process_time} seconds")
```

9. **Response Sent to Client**: The middleware returns the response to the client

Here's the complete middleware example:

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_processing_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Process time: {process_time} seconds")
    return response
```

By using middleware, we don't have to manually add timing code to every single API endpoint. The middleware handles it automatically for all requests - it's a clean and efficient way to add universal features to your application.

📝 Notes – Logging & Threading in FastAPI (Modules 3 & 5)
🔹 Logging (Middleware + File Logs)
✅ What I Implemented

Created a logging middleware using @app.middleware("http").

For every request, captured:

Request method (GET/POST).

URL path.

Start & end timestamps.

Processing time (execution duration).

Wrote logs to a file logs.txt with timestamped entries.

📂 Example Log Entry
2025-08-14 17:59:35.886834 Request : POST /ask |
start time : 1755174572.6395307 |
final time : 1755174575.8707268 |
Processing time : 3.231196165084839

🛠️ How It Works

time.time() → measure start/end.

datetime.now() → add human-readable timestamp.

write_in_logs() → append log entry to file.

Middleware wraps every request → no extra code in endpoints.

👉 This lays the foundation for Module 5 (Logging & Error Handling).

🔹 Threading (Parallel Execution with ThreadPoolExecutor)
✅ What I Implemented

Iteration 1 (Sequential) → /bulk_summarizer/ loops through texts one by one.

Iteration 2 (Threaded) → /bulk_summarizer2/ uses ThreadPoolExecutor to parallelize LLM calls.

📂 Observed Results (from logs)

Sequential /bulk_summarizer/ = ~8.5s.

Threaded /bulk_summarizer2/ = ~4.3s.

🚀 ~2× speed improvement with threads.

🛠️ How It Works

Used Python’s concurrent.futures.ThreadPoolExecutor.

executor.map() applied LLM_integration concurrently to all texts.

Each LLM call is I/O-bound (API call) → threads reduce waiting time.

📌 Key Notes

max_workers=6 → controls parallel threads.

Best for I/O-bound tasks (API calls, DB queries).

For CPU-bound tasks → use ProcessPoolExecutor.

Results are returned as an iterator → converted into list.

# 📝 Notes – Logging & Threading in FastAPI (Modules 3 & 5)

## 🔹 Logging (Middleware + File Logs)

### ✅ What I Implemented

- Created a logging middleware using `@app.middleware("http")`
- For every request, captured:
  - Request method (GET/POST)
  - URL path
  - Start & end timestamps
  - Processing time (execution duration)
- Wrote logs to a file `logs.txt` with timestamped entries

### 📂 Example Log Entry

### 🛠️ How It Works

```python
from datetime import datetime
import time

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    log_entry = f"{datetime.now()}\tRequest : {request.method} {request.url.path} | "
    log_entry += f"start time : {start_time} | "
    log_entry += f"final time : {time.time()} | "
    log_entry += f"Processing time : {process_time}\n"

    with open("logs.txt", "a") as log_file:
        log_file.write(log_entry)

    return response
```

- `time.time()` → measure start/end
- `datetime.now()` → add human-readable timestamp
- Middleware wraps every request → no extra code in endpoints

👉 This lays the foundation for Module 5 (Logging & Error Handling).

## 🔹 Threading (Parallel Execution with ThreadPoolExecutor)

### ✅ What I Implemented

- Iteration 1 (Sequential) → `/bulk_summarizer/` loops through texts one by one
- Iteration 2 (Threaded) → `/bulk_summarizer2/` uses ThreadPoolExecutor to parallelize LLM calls

### 📂 Observed Results (from logs)

- Sequential `/bulk_summarizer/` = ~8.5s
- Threaded `/bulk_summarizer2/` = ~4.3s
- 🚀 ~2× speed improvement with threads

### 🛠️ How It Works

```python
from concurrent.futures import ThreadPoolExecutor

def LLM_integration(text):
    # Your LLM processing logic
    return summarized_text

@app.post("/bulk_summarizer2/")
async def threaded_summarizer(texts: List[str]):
    with ThreadPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(LLM_integration, texts))
    return {"summaries": results}
```

- Used Python's `concurrent.futures.ThreadPoolExecutor`
- `executor.map()` applied LLM_integration concurrently to all texts
- Each LLM call is I/O-bound (API call) → threads reduce waiting time

### 📌 Key Notes

- `max_workers=6` → controls parallel threads
- Best for I/O-bound tasks (API calls, DB queries)
- For CPU-bound tasks → use `ProcessPoolExecutor`
- Results are returned as an iterator → converted into list
