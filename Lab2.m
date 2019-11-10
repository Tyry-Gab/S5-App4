%% Init
clear
clc
close all

%% Partie 2
N = 100000;
r = 1;

x = rand(N,1);

y = sqrt(r^2 - x.^2);

S = 1/N*sum(y);
S_p = pi*r^2;

f_x = 16*r*S/(3);
V = 4/3*pi*r^2;

%% Procedural 4, n 18

T = [1 2 ; 2 1];
C = [2 0 ; 0 2];

m = T*C*T;

%% Procedural 4, n 18

lamba = roots([1 -20 36]);
