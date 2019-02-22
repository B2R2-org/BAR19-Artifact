import pyvex
import archinfo
import sys

if sys.argv[1] == 'x86':
  arch = archinfo.ArchX86()
else:
  arch = archinfo.ArchAMD64()
insns = open(sys.argv[2], 'rb').read()
offset = 0

while offset < len(insns):
  irsb = pyvex.lift(insns[offset:], 0, arch, opt_level=-1)
  irsb.pp()
  offset += irsb.size
