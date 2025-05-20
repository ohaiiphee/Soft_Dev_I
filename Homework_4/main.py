import score

# get lyrics to ONE from txt file, read and get score
one = open("./one.txt")
one_content = one.read()
score_one = score.score(one_content)
print(f"The score for [One] is: {score_one:.2f}")
one.close()

# get lyrics to STAIRWAY TO HEAVEN from txt file, read and get score
stairway = open("./stairway.txt")
stairway_content = stairway.read()
score_stairway = score.score(stairway_content)
print(f"The score for [Stairway to Heaven] is: {score_stairway:.2f}")
stairway.close()

# get lyrics to RESPECT from txt file, read and get score
respect = open("./respect.txt")
respect_content= respect.read()
score_respect = score.score(respect_content)
print(f"The score for [Respect] is: {score_respect:.2f}")
respect.close()

# get lyrics to LEMON TREE from txt file, read and get score
lemon = open("./lemon.txt")
lemon_content = lemon.read()
score_lemon = score.score(lemon_content)
print(f"The score for [Lemon Tree] is: {score_lemon:.2f}")
lemon.close()

# get lyrics to BARBARA STREISAND TREE from txt file, read and get score
barbara = open("./barbara.txt")
barbara_content = barbara.read()
score_barbara = score.score(barbara_content)
print(f"The score for [Barbara Streisand] is: {score_barbara:.2f}")
barbara.close()

# get lyrics to BOHEMIAN RHAPSODY from txt file, read and get score
bohemian = open("./bohemian.txt")
bohemian_content = bohemian.read()
score_bohemian = score.score(bohemian_content)
print(f"The score for [Bohemian Rhapsody] is: {score_bohemian:.2f}")
bohemian.close()