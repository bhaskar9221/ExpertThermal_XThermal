def calculate_heat_sink(TDP, V_air, k_tim):
    """
    Function to Calculate the Heat Sink
    """

    #Die Dimensions
    L_die = 0.0525
    W_die = 0.045
    Thickness_die = 0.0022

    #Heat Sink Geometry
    L = 90e-3
    W = 116e-3
    H = 27e-3
    Fin_Thickness = 0.8e-3
    N_fins = 60
    Base_Thickness = 2.5e-3
    t_tim = 0.1e-3
    R_jc = 0.2
    T_ambient = 25.0
    k_air = 0.0262
    nu_air = 1.57e-5
    Pr_air = 0.71


    #Fin Spacing Calculation
    s_f = (W - (N_fins * Fin_Thickness)) / (N_fins - 1)

    #Reynolds Number Calculation
    Re = (V_air * s_f) / nu_air

    #Nusselt Number Calculation (Laminar & Turbulent cases)
    if Re < 2300:  
        Nu = 1.86 * ((Re * Pr_air * (2 * s_f) / L) ** (1/3))
    else:  # Turbulent flow
        Nu = 0.023 * (Re**0.8) * (Pr_air**0.3)

    #Convective Heat Transfer Coefficient
    h = (Nu * k_air) / (2 * s_f)
    
    
    h_fin = H-Base_Thickness

    # Effective Surface Area Calculation
    A_fin = N_fins * (2 * h_fin * L)+ (s_f * L)
    A_Total_base = (L * W)
    
    A_base_convection = A_Total_base-(Fin_Thickness*N_fins*L) #only this area is exposed for convectionn
   
    A_total = A_fin + A_base_convection

    #Convective Thermal Resistance
    R_conv = 1 / (h * A_total)

    #TIM Thermal Resistance
    A_die = L_die*W_die # die area where thermal insulation is done
    R_tim = t_tim / (k_tim * A_die)

    #Total Heat Sink Thermal Resistance
    R_hs = R_conv + R_tim

    #Total Thermal Resistance
    R_total = R_jc + R_hs

    #Junction Temperature Calculation
    T_j = T_ambient + (TDP * R_total)

    return R_total, T_j



#Function Testing 
R, T = calculate_heat_sink(TDP=150, V_air=1, k_tim=4)
print(f"R_total = {R:.6f} °C/W, T_junction = {T:.4f} °C")