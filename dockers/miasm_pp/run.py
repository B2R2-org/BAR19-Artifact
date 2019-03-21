from miasm2.analysis.binary import Container
from miasm2.analysis.machine import Machine
import sys

arch = 'x86_32' if sys.argv[1] == 'x86' else 'x86_64'
insns = open(sys.argv[2], 'rb').read()
offset = 0
machine = Machine(arch)
mdis = machine.dis_engine(insns)
ir_arch = machine.ir(mdis.loc_db)

while offset < len(insns):
    try:
        blk = mdis.dis_block(offset)
        for b in blk.lines:
            i, j = ir_arch.instr2ir(b)
            print i
            for _j in j:
                print _j
        linst = blk.lines[-1]
        offset = linst.offset + linst.l
    except:
        offset += 1
