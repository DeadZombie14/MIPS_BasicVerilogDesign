#include <verilated.h>          // Defines common routines
#include <iostream>             // Need std::cout
#include "VMIPS_TB.h"               // From Verilating "top.v"
#include "verilated_vcd_c.h"    // To trace waves for simulation

VMIPS_TB *top;                      // Instantiation of module

using namespace std;

vluint64_t main_time = 0;       // Current simulation time
// This is a 64-bit integer to reduce wrap over issues and
// allow modulus.  This is in units of the timeprecision
// used in Verilog (or from --timescale-override)

double sc_time_stamp () {       // Called by $time in Verilog
    return main_time;           // converts to double, to match
                                // what SystemC does
}

int main(int argc, char** argv) {
    Verilated::commandArgs(argc, argv);   // Remember args

    top = new VMIPS_TB;             // Create instance
    Verilated::traceEverOn(true);

    top->clkTB = 0;           // Set some inputs


    while (main_time < 10000 && !Verilated::gotFinish()) {
        if ((main_time % 10) == 0) {
            top->clkTB = !top->clkTB;       // Toggle clock
        }
        if (main_time > 10) {
            //top->reset_l = 1;   // Deassert reset
        }
        top->eval();            // Evaluate model
        // cout << "hola" << endl;
        // cout << top->resultadoTB << endl;       // Read a output
        main_time++;            // Time passes...
    }
    top->final();               // Done simulating
    delete top;
}