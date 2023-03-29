# Data extraction for the E121 experiment

## Intro

This image is based on the `ucesb` project (Håkan T Johansson, [project page](https://git.chalmers.se/expsubphys/ucesb)). You can use it to examine the content of a List Mode File (LMD) or extract the required information as a ROOT file. This file can then be processed in [ROOT](https://root.cern/) or [PyROOT](https://root.cern/manual/python/).

## Usage

After installing docker engine, you can type this command in the shell. These commands are for Linux, Mac and Windows Power Shells, for the standard Windows Command prompt `cmd`, please replace `-v "$(pwd):/pwd"` with `-v "%cd%:/pwd"`.

Check the file:

```
docker run --rm -v "$(pwd):/pwd" xaratustrah/unpack_e121 /pwd/test.lmd
```

or extract data, such as the DCCT values into a `root` file:

```
docker run --rm -v "$(pwd):/pwd" xaratustrah/unpack_e121 --ntuple=SC_DCCT,/pwd/test.root /pwd/test.lmd
```

## Result file
The resulting root file will have a tree in it with the name of `h101`, so you can run root, then inside the command line type:

```
h101->Show()
```

## Other mappings etc..
In order to check the structure and find out which data can be read, you can run the image without a file name:

```
docker run --rm -v "$(pwd):/pwd" xaratustrah/unpack_e121 --show-members
```

You will see something like this:

```
UNPACK_esr_adc3data96          .UNPACK.esr.adc[3].data[96]    
UNPACK_esr_scaler1data32       .UNPACK.esr.scaler[1].data[32] 
UNPACK_esr_tdc10data           .UNPACK.esr.tdc[10].data       
UNPACK_esr_tb_in1data16        .UNPACK.esr.tb_in[1].data[16]  
UNPACK_esr_tb_inhibit1data16   .UNPACK.esr.tb_inhibit[1].data[16] 
UNPACK_esr_tb_red1data16       .UNPACK.esr.tb_red[1].data[16] 
RAW_E_PAD6_7                   .RAW.E.PAD[6][7]               
RAW_E_PADN6                    .RAW.E.PADN[6]                 
RAW_E_DSSD_LEFT                .RAW.E.DSSD.LEFT               
RAW_E_DSSD_RIGHT               .RAW.E.DSSD.RIGHT              
RAW_E_DSSD_TOP                 .RAW.E.DSSD.TOP                
RAW_E_DSSD_BOTTOM              .RAW.E.DSSD.BOTTOM             
RAW_E_CSI2                     .RAW.E.CSI[2]                  
RAW_T_MWPC_ANODE               .RAW.T.MWPC.ANODE              
RAW_T_MWPC_X2                  .RAW.T.MWPC.X[2]               
RAW_T_MWPC_Y2                  .RAW.T.MWPC.Y[2]               
RAW_T_MWPC_RAW                 .RAW.T.MWPC.RAW                
RAW_T_MASTER_TRIGGER           .RAW.T.MASTER.TRIGGER          
RAW_T_TRIGGER2                 .RAW.T.TRIGGER[2]              
RAW_TBOX_SI_IN                 .RAW.TBOX.SI.IN                
RAW_TBOX_SI_RED                .RAW.TBOX.SI.RED               
RAW_TBOX_MWPC_IN               .RAW.TBOX.MWPC.IN              
RAW_TBOX_MWPC_RED              .RAW.TBOX.MWPC.RED             
RAW_SC_MASTER_TRIGGER          .RAW.SC.MASTER.TRIGGER         
RAW_SC_SI_OR                   .RAW.SC.SI.OR                  
RAW_SC_TRIGGER2                .RAW.SC.TRIGGER[2]             
RAW_SC_MWPC_RAW                .RAW.SC.MWPC.RAW               
RAW_SC_MWPC_ANODE              .RAW.SC.MWPC.ANODE             
RAW_SC_MWPC_X2                 .RAW.SC.MWPC.X[2]              
RAW_SC_MWPC_Y2                 .RAW.SC.MWPC.Y[2]              
RAW_SC_U_COOL                  .RAW.SC.U.COOL                 
RAW_SC_I_COOL                  .RAW.SC.I.COOL                 
RAW_SC_DCCT                    .RAW.SC.DCCT                   
RAW_SC_INHIBIT                 .RAW.SC.INHIBIT                
RAW_SC_CLOCK                   .RAW.SC.CLOCK                  
RAW_SC_TARGET_S1               .RAW.SC.TARGET.S[1] 
```

Here you can see the mappings, and the name of the parameters that can be extracted on the left side. Here the prefix `RAW_` should be removed before usage, like in the above examples, if we are interested in `RAW_SC_DCCT` then we set the command line argument to:

```
--ntuple=SC_DCCT
```
