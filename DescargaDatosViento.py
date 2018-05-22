#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "area": "16/273/9/285",
    "class": "ei",
    "dataset": "interim",
    "date": "1979-01-01/to/2017-12-31",
    "expver": "1",
    "format": "netcdf",
    "grid": "0.125/0.125",
    "levtype": "sfc",
    "param": "165.128/166.128",
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "target": "DataEraInterim_Wind.nc",
})



