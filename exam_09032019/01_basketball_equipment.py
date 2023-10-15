yearly_fee = int(input())
sneakers = yearly_fee * 0.6
clothes = sneakers * 0.8
ball = clothes * 0.25
acc = ball * 0.2

total = yearly_fee + sneakers + clothes + ball + acc
print(f"{total:.2f}")
