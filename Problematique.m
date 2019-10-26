%% Init
clc
clear
close all
N = 10000;

%% Générateur erreur additive de phi, U[0,2pi]

phi_error = rand(N,1)*2*pi;

figure
histogram(phi_error)

%% Générateur erreur additive distance radiale

% Pas mal de la sauce en live
var_50=4;
D_error = raylrnd(1:N);
D_error_50 = (D_error./var_50).*exp(-D_error./(2*var_50));

figure
histogram(D_error_50)

