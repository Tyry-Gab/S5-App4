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
mu = 10;
sigma = 2;

for n=[100 1000 10000]
    r = mu + sigma.*randn(n,1);
    x_barre = mean(r);
    s = std(r);

    figure
    histogram(r)
end

%% Ex 3


for n=[100 1000 10000]
    U1 = rand(n,1);
    U2 = rand(n,1);
    
    
    X = 10 + 2.*cos(2.*pi.*U1).*sqrt(-2.*log(U2));
    Y = 10 + 2.*cos(2.*pi.*U1 - pi/2).*sqrt(-2.*log(U2));
    
    figure
    hold on
    histogram(X)
    histogram(Y)
end

%% Ex 4

