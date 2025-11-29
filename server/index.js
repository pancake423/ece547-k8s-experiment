const express = require("express");
const app = express();
const port = 8080;

const N_PRIMES = 5000;

app.get("/", (req, res) => {
  // compute the first N_PRIMES prime numbers. this should keep the CPU busy...
  const t0 = performance.now();
  let primes = [2];
  let n = 3;
  while (primes.length < N_PRIMES) {
    let is_prime = true;
    for (const p of primes) {
      if (n % p == 0) {
        is_prime = false;
        break;
      }
    }
    if (is_prime) {
      primes.push(n);
    }
    n++;
  }
  res.send(
    `the ${N_PRIMES}th prime is: ${primes[primes.length - 1]} (${performance.now() - t0} ms)`,
  );
});

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});
