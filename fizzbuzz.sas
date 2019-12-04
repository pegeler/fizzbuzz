data _null_;

  do x=1 to 100;

    fizz = ifn(^modz(i, 3), "fizz", "");
    buzz = cat(fizz, ifn(^modz(i, 5), "buzz", ""));

    if buzz then put buzz; else put i;

  end;

run;
