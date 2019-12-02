fizzbuzz <- function(n) {
  out <- n <- if ( length(n) == 1 ) seq_len(n) else n
  
  fizz <- !n %% 3
  buzz <- !n %% 5

  out[fizz & !buzz] <- "fizz"
  out[buzz & !fizz] <- "buzz"
  out[fizz &  buzz] <- "fizzbuzz"

  out
}

fizzbuzz(100)
