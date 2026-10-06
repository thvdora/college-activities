% criando espacos para tempo em segundos
t = linspace(0, 5, 51);

% h(t)= -5t^2 + 20t + 2
h = -5*t.^2 + 20*t + 2;

plot(t, h);

grid on;

title("Grafico de h(t)= -5t^2 + 20t + 2");
xlabel("t");
ylabel("h");
