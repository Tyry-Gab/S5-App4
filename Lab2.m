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

