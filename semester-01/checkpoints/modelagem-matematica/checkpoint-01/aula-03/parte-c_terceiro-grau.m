% criando espacos para x entre 0 e 10
x = 0:0.1:10;

% f(x)= -x^3 + 15x^2 + 5
y = -x.^3 + 15*x.^2 + 5

plot(x, y);

grid on;

title("Grafico de f(x)= -x^3 + 15x^2 + 5");
xlabel("x");
ylabel("y");
