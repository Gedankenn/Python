%%

close all;
clear all;
clc;

%% import

data = csvread('C:\Users\gedan\Documents\python\file_write\fibonacci.csv',1,0);

tamanho = data(:,1);
tempo(:,1) = data(:,2);
tempo(:,2) = data(:,3);
tempo(:,3) = data(:,4);

clear data:

%% graficos

plot(tamanho,tempo,'LineWidth',2);
legend('Iterativo','Dinamico','Fast');
grid on;
title('Tempo de execucao');
ylabel('Tempo [s]');
xlabel('Tamanho');