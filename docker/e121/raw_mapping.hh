SIGNAL(	ADC1_1, esr.adc[0].data[0],
	ADC1_32, esr.adc[0].data[31], DATA12);
SIGNAL( ADC2_1, esr.adc[1].data[0],
	ADC2_32, esr.adc[1].data[31], DATA12);
SIGNAL( ADC3_1, esr.adc[2].data[0],
	ADC3_32, esr.adc[2].data[31], DATA12);
SIGNAL( SC_1, esr.scaler[0].data[0],
        SC_32, esr.scaler[0].data[31],DATA32);
SIGNAL( TDC_1, esr.tdc[0].data,
	TDC_10, esr.tdc[9].data,DATA32);
SIGNAL( TB_SI_IN, esr.tb_in[0].data[0],DATA32);
SIGNAL( TB_SI_RED, esr.tb_red[0].data[0],DATA32);
SIGNAL( TB_MWPC_IN, esr.tb_in[0].data[1],DATA32);
SIGNAL( TB_MWPC_RED, esr.tb_red[0].data[1],DATA32);
