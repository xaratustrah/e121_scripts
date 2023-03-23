# Data extraction for the E121 experiment

You can use it to examine the content of a List Mode File (LMD):

```
docker run -it --rm -v "$(pwd):/pwd" xaratustrah/unpack_e121 /pwd/test.lmd
```

or extract data, such as the DCCT values into a `root` file:

```
docker run -it --rm -v "$(pwd):/pwd" xaratustrah/unpack_e121 --ntuple=SC_DCCT,/pwd/test.root /pwd/test.lmd````
```

The resulting root file will have a tree in it with the name of `h101`, so you can run root, then inside the command line type:

```
h101->Show()
```
