#!/usr/bin/env Rscript
fizzbuzz <- function(n) {
  if ( length(n) == 1 )
    n <- seq_len(n)

  fizz <- !n %% 3
  buzz <- !n %% 5

  n[fizz & !buzz] <- "fizz"
  n[buzz & !fizz] <- "buzz"
  n[fizz &  buzz] <- "fizzbuzz"

  n
}

cat(fizzbuzz(100), sep = "\n")
