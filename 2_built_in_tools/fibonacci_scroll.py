
# ✨🧙 The Ancient Scroll of Fibonacci ✨
# Inscribed by Kiro the Grey Hat
# A spell to summon the sacred sequence of numbers!

def cast_fibonacci_spell(n):
    """
    🔮 This arcane function summons the first `n` numbers
    of the legendary Fibonacci sequence into existence!
    """
    sequence = []
    a, b = 0, 1

    print("=" * 45)
    print("   🌀 CASTING THE FIBONACCI SPELL... 🌀")
    print("=" * 45)

    for i in range(n):
        sequence.append(a)
        print(f"  ✨ Summoning number {i + 1:>2}:  {a}")
        a, b = b, a + b

    print("=" * 45)
    print(f"\n🔮 The Sacred Sequence:\n  {sequence}")
    print(f"\n🧙 Kiro whispers: 'Each number is the sum")
    print(f"   of the two that came before it...'")
    print(f"\n⚡ Spell complete! {n} numbers summoned!")
    print("=" * 45)
    return sequence

# 🪄 Cast the spell for the first 10 Fibonacci numbers!
cast_fibonacci_spell(10)
