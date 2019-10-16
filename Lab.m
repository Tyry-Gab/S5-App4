%% Init
clear
clc
close all

%% Ex 1
N = 100;
x_barre = [0 0 0];
s = [0 0 0];
r = 0;

mu = mean(r);
sigma = 10/sqrt(12);

for n=[100 1000 10000]
    r = -5 + (5+5)*rand(n,1);
    x_barre = mean(r);
    s = std(r);


    figure
    histogram(r)
end

%% Ex 2

