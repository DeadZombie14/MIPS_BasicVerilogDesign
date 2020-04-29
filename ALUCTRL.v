// Def I/O
module ALUCTRL(
	input [5:0]alu_in,
	output reg [3:0]alu_out
);
// Conexiones


// Cuerpo del modulo
always@*
begin
	case(alu_in)
		6'b100000:
			begin
				alu_out = 4'b0000; // ADD
			end
		6'b100010:
			begin
				alu_out = 4'b0001; // SUB
			end
		6'b000010:
			begin
				alu_out = 4'b0010;  // MUL
			end
		6'b011010:
			begin
				alu_out = 4'b0011;  // DIV
			end
		6'b100100:
			begin
				alu_out = 4'b0100;  // AND
			end
		6'b100101:
			begin
				alu_out = 4'b0101;  // OR
			end
		6'b100111:
			begin
				alu_out = 4'b0110;  // NOR
			end
		6'b000000:
			begin
				alu_out = 4'b0111;  // SLL
			end
		6'b000011:
			begin
				alu_out = 4'b1000;  // SRL
			end
		6'b101010:
			begin
				alu_out = 4'b1001;  // SLT
			end
		6'b100110:
			begin
				alu_out = 4'b1010;  // XOR
			end
		default:
			begin
				alu_out = 4'b0000;
			end
	endcase
end

endmodule
