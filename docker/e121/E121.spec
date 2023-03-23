// -*- C++ -*-

ADC_CH(start, id)
{
  MEMBER(DATA12 data[96]);

  UINT32 item NOENCODE
  {
  0_15: channel = MATCH(id);
  16_27: value;
  28_31: unknown;  
  ENCODE(data[channel - start], (value=value));
  }
}

SCALER(start)
{
	MEMBER(DATA32 data[32]);

	list(0 <= ch < 32)
	{
		UINT32 high NOENCODE
		{
			0_15: channel;
			16_31: value;
		}

		UINT32 low NOENCODE
		{
			0_15: channel;
			16_31: value;

		}

		ENCODE(data[(high.channel - start) / 2], (value=(high.value << 16) | low.value));
	}
}

TDC(start)
{
  MEMBER(DATA32 data);

  UINT32 high NOENCODE
  {
  0_15: channel = MATCH(start);
  16_31: value;
  }

  UINT32 low NOENCODE
  {
  0_15: channel;
  16_31: value;
  }
      
  ENCODE(data,(value=(high.value << 16) | low.value));
}


TBOX(start)
{
  MEMBER(DATA32 data[16]);

  list(0 <= ch < 16)
    {
            UINT32 high NOENCODE
	    {
	    0_15: channel;
	    16_31: value;
	    }

	    UINT32 low NOENCODE
	    {
	    0_15: channel;
	    16_31: value;
	    }
	    
	    ENCODE(data[(high.channel - start) / 2], (value=(high.value << 16) | low.value));
    }
}

SUBEVENT(ESR)
{
  tb_in[0] = TBOX(start = 0x300);
  tb_inhibit[0] = TBOX(start = 0x380);
  tb_red[0] = TBOX(start = 0x400);
  //  adc[0]   = ADC(start = 0);
  //  adc[1]   = ADC(start = 32);
  //  adc[2]   = ADC(start = 64);
  select several {
    adc[0] = ADC_CH(start = 0 , id =  0);
    adc[0] = ADC_CH(start = 0 , id =  1);
    adc[0] = ADC_CH(start = 0 , id =  2);
    adc[0] = ADC_CH(start = 0 , id =  3);
    adc[0] = ADC_CH(start = 0 , id =  4);
    adc[0] = ADC_CH(start = 0 , id =  5);
    adc[0] = ADC_CH(start = 0 , id =  6);
    adc[0] = ADC_CH(start = 0 , id =  7);
    adc[0] = ADC_CH(start = 0 , id =  8);
    adc[0] = ADC_CH(start = 0 , id =  9);
    adc[0] = ADC_CH(start = 0 , id = 10);
    adc[0] = ADC_CH(start = 0 , id = 11);
    adc[0] = ADC_CH(start = 0 , id = 12);
    adc[0] = ADC_CH(start = 0 , id = 13);
    adc[0] = ADC_CH(start = 0 , id = 14);
    adc[0] = ADC_CH(start = 0 , id = 15);
    adc[0] = ADC_CH(start = 0 , id = 16);
    adc[0] = ADC_CH(start = 0 , id = 17);
    adc[0] = ADC_CH(start = 0 , id = 18);
    adc[0] = ADC_CH(start = 0 , id = 19);
    adc[0] = ADC_CH(start = 0 , id = 20);
    adc[0] = ADC_CH(start = 0 , id = 21);
    adc[0] = ADC_CH(start = 0 , id = 22);
    adc[0] = ADC_CH(start = 0 , id = 23);
    adc[0] = ADC_CH(start = 0 , id = 24);
    adc[0] = ADC_CH(start = 0 , id = 25);
    adc[0] = ADC_CH(start = 0 , id = 26);
    adc[0] = ADC_CH(start = 0 , id = 27);
    adc[0] = ADC_CH(start = 0 , id = 28);
    adc[0] = ADC_CH(start = 0 , id = 29);
    adc[0] = ADC_CH(start = 0 , id = 30);
    adc[0] = ADC_CH(start = 0 , id = 31);
    adc[1] = ADC_CH(start = 32, id = 32);
    adc[1] = ADC_CH(start = 32, id = 33);
    adc[1] = ADC_CH(start = 32, id = 34);
    adc[1] = ADC_CH(start = 32, id = 35);
    adc[1] = ADC_CH(start = 32, id = 36);
    adc[1] = ADC_CH(start = 32, id = 37);
    adc[1] = ADC_CH(start = 32, id = 38);
    adc[1] = ADC_CH(start = 32, id = 39);
    adc[1] = ADC_CH(start = 32, id = 40);
    adc[1] = ADC_CH(start = 32, id = 41);
    adc[1] = ADC_CH(start = 32, id = 42);
    adc[1] = ADC_CH(start = 32, id = 43);
    adc[1] = ADC_CH(start = 32, id = 44);
    adc[1] = ADC_CH(start = 32, id = 45);
    adc[1] = ADC_CH(start = 32, id = 46);
    adc[1] = ADC_CH(start = 32, id = 47);
    adc[1] = ADC_CH(start = 32, id = 48);
    adc[1] = ADC_CH(start = 32, id = 49);
    adc[1] = ADC_CH(start = 32, id = 50);
    adc[1] = ADC_CH(start = 32, id = 51);
    adc[1] = ADC_CH(start = 32, id = 52);
    adc[1] = ADC_CH(start = 32, id = 53);
    adc[1] = ADC_CH(start = 32, id = 54);
    adc[1] = ADC_CH(start = 32, id = 55);
    adc[1] = ADC_CH(start = 32, id = 56);
    adc[1] = ADC_CH(start = 32, id = 57);
    adc[1] = ADC_CH(start = 32, id = 58);
    adc[1] = ADC_CH(start = 32, id = 59);
    adc[1] = ADC_CH(start = 32, id = 60);
    adc[1] = ADC_CH(start = 32, id = 61);
    adc[1] = ADC_CH(start = 32, id = 62);
    adc[1] = ADC_CH(start = 32, id = 63);
    adc[2] = ADC_CH(start = 64, id = 64);
    adc[2] = ADC_CH(start = 64, id = 65);
    adc[2] = ADC_CH(start = 64, id = 66);
    adc[2] = ADC_CH(start = 64, id = 67);
    adc[2] = ADC_CH(start = 64, id = 68);
    adc[2] = ADC_CH(start = 64, id = 69);
    adc[2] = ADC_CH(start = 64, id = 70);
    adc[2] = ADC_CH(start = 64, id = 71);
    adc[2] = ADC_CH(start = 64, id = 72);
    adc[2] = ADC_CH(start = 64, id = 73);
    adc[2] = ADC_CH(start = 64, id = 74);
    adc[2] = ADC_CH(start = 64, id = 75);
    adc[2] = ADC_CH(start = 64, id = 76);
    adc[2] = ADC_CH(start = 64, id = 77);
    adc[2] = ADC_CH(start = 64, id = 78);
    adc[2] = ADC_CH(start = 64, id = 79);
    adc[2] = ADC_CH(start = 64, id = 80);
    adc[2] = ADC_CH(start = 64, id = 81);
    adc[2] = ADC_CH(start = 64, id = 82);
    adc[2] = ADC_CH(start = 64, id = 83);
    adc[2] = ADC_CH(start = 64, id = 84);
    adc[2] = ADC_CH(start = 64, id = 85);
    adc[2] = ADC_CH(start = 64, id = 86);
    adc[2] = ADC_CH(start = 64, id = 87);
    adc[2] = ADC_CH(start = 64, id = 88);
    adc[2] = ADC_CH(start = 64, id = 89);
    adc[2] = ADC_CH(start = 64, id = 90);
    adc[2] = ADC_CH(start = 64, id = 91);
    adc[2] = ADC_CH(start = 64, id = 92);
    adc[2] = ADC_CH(start = 64, id = 93);
    adc[2] = ADC_CH(start = 64, id = 94);
    adc[2] = ADC_CH(start = 64, id = 95);
  }
  select optional {
    scaler[0] = SCALER(start = 0x100);
  }
  select several {
    tdc[0] = TDC(start = 0x200);
    tdc[1] = TDC(start = 0x202);
    tdc[2] = TDC(start = 0x204);
    tdc[3] = TDC(start = 0x206);
    tdc[4] = TDC(start = 0x208);
    tdc[5] = TDC(start = 0x20a);
    tdc[6] = TDC(start = 0x20c);
    tdc[7] = TDC(start = 0x20e);
    tdc[8] = TDC(start = 0x210);
    tdc[9] = TDC(start = 0x212);
  }
  
}

EVENT
{
 esr		= ESR(type = 10, subtype = 1);
}

#include "det_mapping.hh"
