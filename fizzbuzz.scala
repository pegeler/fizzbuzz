@main
def main(): Unit = {
  for (x <- 1 to 100)
    x match
      case x if x % 15 == 0 => println("fizzbuzz")
      case x if x % 5 == 0 => println("buzz")
      case x if x % 3 == 0 => println("fizz")
      case x => println(x)
}
