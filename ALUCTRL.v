// Def I/O
module ALUCTRL(
	input [31:0]alu_in,
	input [1:0]alu_op_in,
	output reg [3:0]alu_out
);
// Conexiones
wire [5:0]ALUselector;
wire [1:0]alu_op;

assign ALUselector[5:0] = alu_in[5:0];
assign alu_op[1:0] = alu_op_in[1:0];

// Cuerpo del modulo
always@*
begin
	case(alu_op)
		2'b10:
		begin	
			case(ALUselector)
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
						alu_out = 4'b0111;  // NOP
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
				6'b001010:
					begin
						alu_out = 4'b1011; // SLTi
					end
				6'b001101:
					begin
						alu_out = 4'b0101; //ORi
					end
				6'b001000:
					begin
						alu_out = 4'b0000; // ADDi
					end
				6'b001100:
					begin
						alu_out = 4'b0100;  // ANDi
					end
				default:
					begin
						alu_out = 4'b0000;
					end
			endcase
		end
		2'b00:
		begin
			alu_out = 4'b0000; // add
		end
		2'b01:
		begin
			alu_out = 4'b0001; // sub 
		end
	endcase 
end

endmodule
