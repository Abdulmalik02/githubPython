function input(prompt::String="")::String
	print(prompt)
	return chomp(readline())
end

m = parse(Int, input("Enter 'm': "))
n = parse(Int, input("Enter 'n': "))

A = zeros(Int, m, n)

for i in 1:m
	row_raw = split(input("Enter row " + string(i)), "")
	row_int = map(n -> parse(Int, n), split(row_raw, " "))
end
