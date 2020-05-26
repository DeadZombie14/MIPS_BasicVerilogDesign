/* verilator lint_off PINCONNECTEMPTY */
// Def I/O
module Add1(
	input [7:0]xAdd1,yAdd1,
	output [7:0]resAdd1
);
// Conexiones

// Cuerpo del modulo

ADD8bit adder1(.a8bit(xAdd1),.b8bit(yAdd1),.inputCarry8bit(1'b0),.sum8bit(resAdd1),.outputCarry8bit());

endmodule
