// Def I/O
module SignE(
    input [15:0]inputSignE,
	output reg [31:0]outputSignE
);
// Conexiones 

// Cuerpo del modulo
always@*
begin
    if(inputSignE[15])
        begin
            outputSignE = {16'b1111111111111111,inputSignE[15:0]};
        end
    else
        begin
            outputSignE = {16'b0,inputSignE[15:0]};
        end
    //outputSignE[31:0] = inputSignE[15:0] <<< 16;
end

endmodule
