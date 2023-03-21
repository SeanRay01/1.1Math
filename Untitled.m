% 1st segment: Euler angle
clear all; clc;
syms phi theta psi

[R_zyz]=Euler_rot(phi,theta,psi);
phi_d=30; theta_d=15; psi_d=20;
phi=phi_d*pi/180; theta=theta_d*pi/180; psi=psi_d*pi/180;
[R_zyz_dgree]=Euler_rot(phi,theta,psi);