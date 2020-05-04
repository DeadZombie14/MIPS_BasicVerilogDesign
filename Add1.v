// Def I/O
module Add1(
	input [31:0]xAdd1,yAdd1,
	output [31:0]resAdd1
);
// Conexiones

// Cuerpo del modulo

// Sumar 4 a la dirección de la instrucción actual
ADD32bit adder1(.a32bit(xAdd1),.b32bit(yAdd1),.inputCarry16bit(1'b0),.sum16bit(resAdd1),.outputCarry16bit());

endmodule
