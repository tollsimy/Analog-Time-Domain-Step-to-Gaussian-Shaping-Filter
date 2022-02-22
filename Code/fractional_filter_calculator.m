%% Specifications
a=0.2;
cap=1E-04;
fo=1;
wo=2*pi*fo;
imped=1/(cap*wo);
%% Coefficients of the second-order continued fraction expansion
a5=(-(a^5)-15*(a^4)-85*(a^3)-225*(a^2)-274*a-120);
a4=wo*(5*(a^5)+45*(a^4)+5*(a^3)-1005*(a^2)-3250*a-3000);
a3=(wo^2)*(-10*(a^5)-30*(a^4)+410*(a^3)+1230*(a^2)-4000*a-12000);
a2=(wo^3)*(10*(a^5)-30*(a^4)-410*(a^3)+1230*(a^2)+4000*a-12000);
a1=(wo^4)*(-5*(a^5)+45*(a^4)-5*(a^3)-1005*(a^2)+3250*a-3000);
ao=(wo^5)*((a^5)-15*(a^4)+85*(a^3)-225*(a^2)+274*a-120);
b5=(imped)*((a^5)-15*(a^4)+85*(a^3)-225*(a^2)+274*a-120);
b4=(imped)*wo*(-5*(a^5)+45*(a^4)-5*(a^3)-1005*(a^2)+3250*a-3000);
b3=(imped)*(wo^2)*(10*(a^5)-30*(a^4)-410*(a^3)+1230*(a^2)+4000*a-12000);
b2=(imped)*(wo^3)*(-10*(a^5)-30*(a^4)+410*(a^3)+1230*(a^2)-4000*a-12000);
b1=(imped)*(wo^4)*(5*(a^5)+45*(a^4)+5*(a^3)-1005*(a^2)-3250*a-3000);
bo=(imped)*(wo^5)*(-(a^5)-15*(a^4)-85*(a^3)-225*(a^2)-274*a-120);
%% Foster II form
disp(' #########################################')
disp(' Foster II form ')
disp(' #########################################')
% Impedance of CPE
num=[b5 b4 b3 b2 b1 bo 0];
den=[a5 a4 a3 a2 a1 ao];
% Partial Fractional Expansion for the admittance (Foster II)
[r, p ]=residue(den,num);
% Calculation of passive element values for Foster II (rzero, ri,ci)
rzero_fii=1/r(6:6)
for n=[1,2,3,4,5];
r_fii=1/r(n:n)
c_fii=r(n:n)/abs(p(n:n))
end