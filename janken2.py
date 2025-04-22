import random

#プレイヤーが選べる手
hands = ["グー", "チョキ", "パー"]

#カウント用変数
wins = 0
losses = 0
draws = 0

print("番号で選んでね:")
print("1: グー　2:　チョキ　3: パー")


while True:
    try:
        player_index = int(input("あなたの手 (1~3) : "))
        if player_index < 1 or player_index > 3:
            print("1~3の数字を入力してね!")
            continue
    except ValueError:
        print("数字を入力してね！")
        continue
        
    
    # インデックスに変換（0始まりに合わせる)
    player = hands[player_index - 1]
    computer = random.choice(hands)
    
    print(f"\nあなたの手: {player}")
    print(f"コンピューターの手: {computer}")
    
    
    if player == computer:
        print("あいこ！")
        draws += 1
    elif (player == "グー" and computer == "チョキ") or \
         (player == "チョキ" and computer == "パー") or \
         (player == "パー" and computer == "グー"):
        print("あなたの勝ちです!")
        wins += 1
    else:
        print("あなたの負けです")
        losses += 1
        
    #カウント表示
    print(f"【　勝ち: {wins}|負け: {losses}|あいこ: {draws} 】")    
        
    again = input("もう一度遊びますか？ (y/n): ")
    if again.lower() != "y":
        print("最終結果:")
        print(f" 勝ち: {wins} / 負け:{losses} / あいこ: {draws}")
        print("ありがとう！またね！")
        break