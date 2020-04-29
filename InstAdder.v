// Def I/O
module InstAdder(
	input [7:0]currentInst,
	output [7:0]nextInst
);
// Conexiones

// Cuerpo del modulo

// Sumar 4 a la dirección de la instrucción actual
ADD8bit instAdder1(.a8bit(currentInst[7:0]),.b8bit(8'b00000100),.inputCarry8bit(1'b0),.sum8bit(nextInst[7:0]),.outputCarry8bit());

endmodule
