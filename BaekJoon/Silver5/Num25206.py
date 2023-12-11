totalValue = totalScore = 0
checkSum = {
	"A+": 4.5,
	"A0": 4.0,
	"B+": 3.5,
	"B0": 3.0,
	"C+": 2.5,
	"C0": 2.0,
	"D+": 1.5,
	"D0": 1.0,
	"F": 0,
}

for x in range(20):
	name, value, score = input().split()
	if score == "P": continue
	value = float(value)
	totalValue += value
	totalScore += value * checkSum[score]

print(f'{totalScore / totalValue:.6f}')
