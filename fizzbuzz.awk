BEGIN {

  for (i=1; i <= 100; i++) {

    fizz = i % 3 == 0 ? "fizz" : ""
    buzz = i % 5 == 0 ? "buzz" : ""

    out = fizz buzz

    if ( out )
      print out
    else
      print i
  }

}
