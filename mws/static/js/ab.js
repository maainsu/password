Lov=prompt("원하는 멤버");
  if(Lov="슈가"){
    today = new Date();
    count = new Date("March 9,2021");
    calc = Math.ceil((count-today) /1000 / 24/60/60);
    if(calc<0)calc=0;
    result='<font color = red> <b>' + calc +'</b> </font>';
    document.write(result,"일");
  }else if (Lov="정국") {
    today = new Date();
    count = new Date("September 1,2020");
    calc = Math.ceil((count-today) /1000 / 24/60/60);
    if(calc<0)calc=0;
    result='<font color = red> <b>' + calc +'</b> </font>';
    document.write(result,"일");
  }else if (Lov="뷔") {
    today = new Date();
    count = new Date("December 30,2020");
    calc = Math.ceil((count-today) /1000 / 24/60/60);
    if(calc<0)calc=0;
    result='<font color = red> <b>' + calc +'</b> </font>';
    document.write(result,"일");
  }else if (Lov="지민") {
    today = new Date();
    count = new Date("October 13,2020");
    calc = Math.ceil((count-today) /1000 / 24/60/60);
    if(calc<0)calc=0;
    result='<font color = red> <b>' + calc +'</b> </font>';
    document.write(result,"일");
  }else if (Lov="진") {
    today = new Date();
    count = new Date("December 4,2020");
    calc = Math.ceil((count-today) /1000 / 24/60/60);
    if(calc<0)calc=0;
    result='<font color = red> <b>' + calc +'</b> </font>';
    document.write(result,"일");
  }else if (Lov="RM") {
    today = new Date();
    count = new Date("Agust 12,2020");
    calc = Math.ceil((count-today) /1000 / 24/60/60);
    if(calc<0)calc=0;
    result='<font color = red> <b>' + calc +'</b> </font>';
    document.write(result,"일");
  }else if (Lov="제이홉") {
    today = new Date();
    count = new Date("February 18,2021");
    calc = Math.ceil((count-today) /1000 / 24/60/60);
    if(calc<0)calc=0;
    result='<font color = red> <b>' + calc +'</b> </font>';
    document.write(result,"일");
  }else {
    alert("잘못입력하셨습니다.")
  }
