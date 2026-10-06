% Criação da matriz 3x3
A = [1 2 3; 0 1 0; 3 2 1];

% Cálculo da matriz transposta
T = A';

% Cálculo do determinante
det_A = det(A);

% Exibição dos resultados
disp("Matriz original:");
disp(A);

disp("Matriz transposta:");
disp(T);

disp("Determinante:");
disp(det_A);

% Verificação e cálculo da matriz inversa
if det_A ~= 0
    inversa = inv(A);

    disp("Matriz inversa:");
    disp(inversa);
else
    disp("A matriz não possui inversa.");
end
