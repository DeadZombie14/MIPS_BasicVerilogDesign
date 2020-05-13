// Def I/O
module PC(
    input [7:0]inputPC,
    input clk_PC,
	output reg [7:0]outputPC
);
// Conexiones 

// Cuerpo del modulo
always@(posedge clk_PC)
begin
    if(inputPC)
    begin
    outputPC[7:0] <= inputPC[7:0];
    end
    else
    begin
    outputPC = 8'd0;
    end
end

endmodule
