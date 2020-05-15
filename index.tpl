% x=3
<h1> Hello {{name}}</h1>
% if x == 3 :
    <h3>Worked</h3>
    <h4>Parameter 1 is {{var1}} and 2 is {{var2}}</h4>
% else:
     <h2>Not Worked</h2>    

% end
% for i in range(0,101):
      <h3>{{i}}<h3>
% end
<h2>Value of x is : {{x}} </h2>
