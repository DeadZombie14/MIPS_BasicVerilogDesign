// Def I/O
module SignE(
    input [15:0]inputSignE,
	output reg [31:0]outputSignE
);
// Conexiones 

// Cuerpo del modulo
always@*
begin
    outputSignE[31:0] = inputSignE[15:0] >>> 16;
end

endmodule
