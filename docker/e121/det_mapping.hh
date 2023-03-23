//Si pads: p-side strips
SIGNAL( E_PAD1_1, esr.adc[0].data[0],
	E_PAD1_7, esr.adc[0].data[6], DATA12);
SIGNAL( E_PAD2_1, esr.adc[0].data[8],
	E_PAD2_7, esr.adc[0].data[14], DATA12);
SIGNAL( E_PAD3_1, esr.adc[0].data[16],
	E_PAD3_7, esr.adc[0].data[22], DATA12);
SIGNAL( E_PAD4_1, esr.adc[0].data[24],
	E_PAD4_7, esr.adc[0].data[30], DATA12);
SIGNAL( E_PAD5_1, esr.adc[1].data[0],
	E_PAD5_7, esr.adc[1].data[6], DATA12);
SIGNAL( E_PAD6_1, esr.adc[1].data[16],
	E_PAD6_7, esr.adc[1].data[22], DATA12);

//Si pads: n-sides
SIGNAL( E_PADN_1, esr.adc[2].data[10],
	E_PADN_6, esr.adc[2].data[15], DATA12);
//SIGNAL( E_PAD_N_1, esr.adc[2].data[10], DATA12);
//SIGNAL( E_PAD_N_2, esr.adc[2].data[11], DATA12);
//SIGNAL( E_PAD_N_3, esr.adc[2].data[12], DATA12);
//SIGNAL( E_PAD_N_4, esr.adc[2].data[13], DATA12);
//SIGNAL( E_PAD_N_5, esr.adc[2].data[14], DATA12);
//SIGNAL( E_PAD_N_6, esr.adc[2].data[15], DATA12);

//DSSD
SIGNAL( E_DSSD_LEFT, esr.adc[2].data[0], DATA12);
SIGNAL( E_DSSD_RIGHT, esr.adc[2].data[1], DATA12);
SIGNAL( E_DSSD_TOP, esr.adc[2].data[2], DATA12);
SIGNAL( E_DSSD_BOTTOM, esr.adc[2].data[3], DATA12);

//CSI
SIGNAL( E_CSI_1, esr.adc[2].data[6], DATA12);
SIGNAL( E_CSI_2, esr.adc[2].data[7], DATA12);

//MWPC
SIGNAL( T_MWPC_ANODE, esr.tdc[0].data,DATA32);
SIGNAL( T_MWPC_X1, esr.tdc[1].data,DATA32);
SIGNAL( T_MWPC_X2, esr.tdc[2].data,DATA32);
SIGNAL( T_MWPC_Y1, esr.tdc[3].data,DATA32);
SIGNAL( T_MWPC_Y2, esr.tdc[4].data,DATA32);
SIGNAL( T_MWPC_RAW, esr.tdc[5].data,DATA32);

//TRIGGER TDC
SIGNAL( T_MASTER_TRIGGER, esr.tdc[7].data,DATA32);
SIGNAL( T_TRIGGER_1, esr.tdc[8].data,DATA32);
SIGNAL( T_TRIGGER_2, esr.tdc[9].data,DATA32);

//TRIGGER BOX
SIGNAL( TBOX_SI_IN, esr.tb_in[0].data[0],DATA32);
SIGNAL( TBOX_SI_RED, esr.tb_red[0].data[0],DATA32);
SIGNAL( TBOX_MWPC_IN, esr.tb_in[0].data[1],DATA32);
SIGNAL( TBOX_MWPC_RED, esr.tb_red[0].data[1],DATA32);

//TRIGGER SCALERS
SIGNAL( SC_MASTER_TRIGGER, esr.scaler[0].data[0],DATA32);
SIGNAL( SC_SI_OR, esr.scaler[0].data[1],DATA32);
SIGNAL( SC_MWPC_RAW, esr.scaler[0].data[2],DATA32);
SIGNAL( SC_TRIGGER_1, esr.scaler[0].data[14],DATA32);
SIGNAL( SC_TRIGGER_2, esr.scaler[0].data[15],DATA32);

//DETECTOR SCALERS
SIGNAL( SC_MWPC_ANODE, esr.scaler[0].data[7],DATA32);
SIGNAL( SC_MWPC_X1, esr.scaler[0].data[8],DATA32);
SIGNAL( SC_MWPC_X2, esr.scaler[0].data[9],DATA32);
SIGNAL( SC_MWPC_Y1, esr.scaler[0].data[10],DATA32);
SIGNAL( SC_MWPC_Y2, esr.scaler[0].data[11],DATA32);

//AUX SCALERS
SIGNAL( SC_U_COOL, esr.scaler[0].data[3],DATA32);
SIGNAL( SC_I_COOL, esr.scaler[0].data[4],DATA32);
SIGNAL( SC_DCCT, esr.scaler[0].data[5],DATA32);
SIGNAL( SC_INHIBIT, esr.scaler[0].data[6],DATA32);
SIGNAL( SC_CLOCK, esr.scaler[0].data[12],DATA32);
SIGNAL( SC_TARGET_S1, esr.scaler[0].data[13],DATA32);
