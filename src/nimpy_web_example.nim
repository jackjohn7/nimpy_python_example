# This is just an example to get you started. A typical library package
# exports the main API in this file. Note that you cannot rename this file
# but you can remove it if you wish.
import nimpy
import math

# normally, an asterisk denotes export but {.exportpy.}
#  metadata denotes it sufficiently for this case
#
# I include the asterisks anyway to illustrate how this
#  should look ordinarily

# iteratively calculate the nth fibonacci number
#  starting from 0 and 1
proc n_fib_iter*(n: int): int {.exportpy.} =
  var
    i = 0
    a = 0
    b = 1
  while i < n-1:
    # you can avoid a temporary variable like this
    b += a
    a = b - a
    i += 1
  return b

# recursively calculate the nth fibonacci number
#  starting from 0 and 1
proc n_fib_rec*(n: int): int {.exportpy.} =
  if n == 0 or n == 1:
    n
  else:
    n_fib_rec(n - 1) + n_fib_rec(n - 2)

proc is_prime(n: int): bool =
  # start by assuming the number is prime
  let
    upper_bound = math.floor(math.sqrt(n.float)).int
  var
    i = 2
  while i <= upper_bound:
    # if it's divisible here, it's not prime
    if n mod i == 0:
      return false
    i += 1
  true

# calculate the nth prime using iteration
proc n_prime*(n: int): int {.exportpy.} =
  var
    i = 1
    n = n
    prime = 1
  while n > 0:
    if is_prime(i):
      prime = i
      n -= 1
    i += 1
  echo "finished priming nim"
  n
