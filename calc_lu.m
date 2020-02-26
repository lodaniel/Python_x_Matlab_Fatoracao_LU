% Author: Luciano de Oliveira Daniel
% https://sites.google.com/site/professorlucianodaniel

load('calc_lu_01.mat')
load('calc_lu_02.mat')
load('calc_lu_03.mat')
load('calc_lu_04.mat')
%A = [7 3 -1 2; 3 8 1 -4; -1 1 4 -1; 2 -4 -1 6];
tic
[L_M,U_M,P_M] = lu(A_P);
toc
%
difL=L_M-L_P;
[max_L,I]=max(abs(difL(:)));
[I_row_L, I_col_L] = ind2sub(size(difL),I);
erroL=(max_L/abs(L_M(I_row_L, I_col_L)))*100
%
difU=U_M-U_P;
[max_U,I]=max(abs(difU(:)));
[I_row_U, I_col_U] = ind2sub(size(difU),I);
erroU=(max_U/abs(U_M(I_row_U, I_col_U)))*100
%
figure(1)
spy(L_M)
hold on
plot([I_col_L I_col_L],[0 100])
plot([0 100],[I_row_L I_row_L])
%
figure(2)
spy(U_M)
hold on
plot([I_col_U I_col_U],[0 100])
plot([0 100],[I_row_U I_row_U])
%