import pyvex
import archinfo
import sys

if sys.argv[1] == 'x86':
  arch = archinfo.ArchX86()
else:
  arch = archinfo.ArchAMD64()
insns = open(sys.argv[2], 'rb').read()

def transIR(data, arch) :
  dataLen = len(data)
  sPos = 0
  while sPos < dataLen :
    ePos = sPos + 20
    if ePos > dataLen : ePos = dataLen
    sData = data[sPos:ePos]
    irsb = pyvex.lift(sData, sPos, arch, opt_level=-1)
    irsb.pp()
    if irsb.size == 0:
      sPos += 1
    else:
      sPos = irsb.size + sPos

transIR(insns, arch)
