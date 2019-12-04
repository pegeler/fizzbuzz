data _null_;

  do i=1 to 100;

    fizz = ifc(^modz(i, 3), "fizz", "");
    buzz = cats(fizz, ifc(^modz(i, 5), "buzz", ""));

    if buzz gt "" then put buzz; else put i;

  end;

run;
