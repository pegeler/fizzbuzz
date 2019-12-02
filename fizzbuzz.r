fizzbuzz <- function(n) {
  out <- n <- if ( length(n) == 1 ) seq_len(n) else n

  out[!n %% 3] <- "fizz"
  out[!n %% 5] <- "buzz"
  out[!n %% 3 & !n %% 5] <- "fizzbuzz"

  out
}

fizzbuzz(100)
