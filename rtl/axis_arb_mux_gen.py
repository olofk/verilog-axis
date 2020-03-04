#!/usr/bin/python
from fusesoc.capi2.generator import Generator
import subprocess
from axis_arb_mux_wrap import generate

class AxisArbMuxGenerator(Generator):
    def run(self):
        ports    = self.config.get('ports', 4)
        name     = self.config.get('name', "axis_arb_mux_wrap_{0}".format(ports))
        output   = self.config.get('output', name+'.v')

        generate(ports, name, output)

        self.add_files([{output : {'file_type' : 'verilogSource',}}])

g = AxisArbMuxGenerator()
g.run()
g.write()
