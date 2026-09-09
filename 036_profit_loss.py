cp, sp = map(float, input().split())
if sp > cp:
    print(f"Profit: {sp - cp}")
elif cp > sp:
    print(f"Loss: {cp - sp}")
else:
    print("No Profit No Loss")
