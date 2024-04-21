import nimpy_web_example
from flask import Flask
from timeit import timeit
from python_examples import n_prime, n_fib_iter, n_fib_rec

print(nimpy_web_example.n_fib_iter(10))
print(nimpy_web_example.n_fib_rec(10))
print(nimpy_web_example.n_prime(10))
print(n_fib_iter(10))
print(n_fib_rec(10))
print(n_prime(10))

class Bench:
    name: str
    def __init__(self, name: str, nim_func):
        self.name = name
        self.nim_func = nim_func

    def run(self):
        return {
            "name": self.name,
            "nim_stat": timeit(lambda: self.nim_func(10), number=100)/100
            }


stat_bench = [
    Bench("rec-fib", nimpy_web_example.n_fib_rec)
]

app = Flask(__name__)

@app.route("/")
def root():
    """Root `GET` route that returns a welcome message."""
    return "Hello, there!"


@app.route("/iter-fib/<n>")
def nth_fib_iter(n: int):
    """Nth Fib Iterative `GET` route that returns the nth fibonacci number."""
    return str(nimpy_web_example.n_fib_iter(int(n)))


@app.route("/rec-fib/<n>")
def nth_fib_rec(n: int):
    """Nth Fib Recursive `GET` route that returns the nth fibonacci number."""
    return str(nimpy_web_example.n_fib_rec(int(n)))


@app.route("/prime/<n>")
def nthprime(n: int):
    """Prime `GET` route that returns the nth prime."""
    return str(nimpy_web_example.n_prime(int(n)))


@app.route("/stats")
def stats():
    """Stats `GET` route that returns the benchmark results."""
    return [bench.run() for bench in stat_bench]
