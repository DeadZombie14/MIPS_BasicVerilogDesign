// Def I/O
module SLTi(
	input [31:0]aSLTi32bit, bSLTi32bit,
    output reg [31:0]slti32bit
);
// Conexiones


// Cuerpo del modulo

always@*
begin
    if(aSLT32bit < bSLT32bit)
        begin
            slt32bit = 32'b00000000000000000000000000000001;
        end
    else
        begin
            slt32bit = 32'b00000000000000000000000000000000; 
        end
end

endmodule