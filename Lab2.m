%% Init
clear
clc
close all

%% Partie 2
N = 100000;
r = 1;

x = rand(N,1);

y = sqrt(r^2 - x.^2);

f_x = 1/N * sum(y)*2*pi*r^2;
V = 4/3*pi*r^2;