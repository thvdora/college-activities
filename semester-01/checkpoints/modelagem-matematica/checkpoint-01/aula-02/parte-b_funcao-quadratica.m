% Cria 100 valores entre -2 e 6
x = linspace(-2, 6, 100);

% Calcula y para cada valor de x
y = x.^2 - 4*x + 2;

% Gera o gráfico
plot(x, y);

% Exibe as linhas de grade
grid on;

% Nomeia os eixos e o título do gráfico
xlabel("x");
ylabel("y");
title("Grafico de y = x^2 - 4x + 2");
