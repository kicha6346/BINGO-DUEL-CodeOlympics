# 🎯 BINGO DUEL v10 — Talking CPU Edition (No imports, <100 lines)
def make_board(seed, shift=0):
    nums, b = [], []
    for i in range(1, 26):
        j = ((ord(seed[(i + shift) % len(seed)]) * (i + shift)) % 25) + 1
        while j in nums: j = (j % 25) + 1
        nums.append(j)
    for i in range(0, 25, 5): b.append(nums[i:i + 5])
    return b
def show(b, letters):
    print(f"\n   🅱️🅸🅽🅶🅾️ ({letters})")
    print("  +----+----+----+----+----+")
    for r in b:
        print("  |" + "|".join(str(x).rjust(3) for x in r) + "|")
        print("  +----+----+----+----+----+")
def mark(b, n):
    for r in range(5):
        for c in range(5):
            if b[r][c] == n: b[r][c] = "🔵"
def count_lines(b):
    cnt = 0
    for i in range(5):
        if all(b[i][c] == "🔵" for c in range(5)): cnt += 1
        if all(b[c][i] == "🔵" for c in range(5)): cnt += 1
    if all(b[i][i] == "🔵" for i in range(5)): cnt += 1
    if all(b[i][4 - i] == "🔵" for i in range(5)): cnt += 1
    return cnt
def cpu_pick(cpu, used):
    best, score = None, -1
    for r in range(5):
        for c in range(5):
            v = cpu[r][c]
            if v == "🔵" or v in used: continue
            row = sum(1 for x in cpu[r] if x == "🔵")
            col = sum(1 for i in range(5) if cpu[i][c] == "🔵")
            s = row + col
            if r == c: s += sum(1 for i in range(5) if cpu[i][i] == "🔵")
            if r + c == 4: s += sum(1 for i in range(5) if cpu[i][4 - i] == "🔵")
            if s > score: score, best = s, v
    return best
def main():
    print("🎮 BINGO DUEL v10 — Talking CPU Edition")
    seed = input("Enter seed word: ") or "HELLO"
    player, cpu = make_board(seed), make_board(seed, 9)
    used, linesP, linesC = [], 0, 0
    show(player, "-----")
    while True:
        cnum = cpu_pick(cpu, used)
        if not cnum: break
        used.append(cnum)
        print(f"\n💻 CPU calls: {cnum}")
        mark(player, cnum); mark(cpu, cnum)
        newP, newC = count_lines(player), count_lines(cpu)
        if newP > linesP:
            print("🔥 You completed a line! CPU: 😠 'You’re too good!'")
            linesP = newP
        if newC > linesC:
            print("🤖 CPU completed a line! CPU: 😎 'I’m unstoppable!'")
            linesC = newC
        letters = "BINGO"[:linesP] + "-" * (5 - linesP)
        show(player, letters)
        if linesP >= 5:
            print("🏆 YOU GOT FULL BINGO! 🎉 CPU: 😭 'How did you do that?!'")
            break
        if linesC >= 5:
            print("💻 CPU GOT FULL BINGO! 😎 'Victory is mine!'")
            break
        if linesC == 4:
            print("⚠️ CPU: 😏 'One more line and I win...'")
        elif linesP == 4:
            print("🔥 CPU: 😨 'No way... you’re about to win!'")
        try:
            pnum = int(input("🎯 Your call (1–25): "))
        except:
            print("⚠️ Invalid input!"); continue
        if pnum < 1 or pnum > 25 or pnum in used:
            print("⚠️ Invalid or used number!"); continue
        used.append(pnum)
        mark(player, pnum); mark(cpu, pnum)
        newP, newC = count_lines(player), count_lines(cpu)
        if newP > linesP:
            print("🔥 You completed a line! CPU: 😡 'Stop doing that!'")
            linesP = newP
        if newC > linesC:
            print("🤖 CPU completed a line! CPU: 😎 'Too easy!'")
            linesC = newC
        letters = "BINGO"[:linesP] + "-" * (5 - linesP)
        show(player, letters)
        if linesP >= 5:
            print("🏆 YOU GOT FULL BINGO! 🎉 CPU: 😭 'Nooo!'")
            break
        if linesC >= 5:
            print("💻 CPU GOT FULL BINGO! 😎 'Game over!'")
            break
if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt:
        print("\nGame exited.")