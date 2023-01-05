for left in range(7):
    for right in range(left, 7):
        print('[' + str(left) + '|' + str(right) + ']', end=' ')
    print()
    
# Output: [0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6] 
#         [1|1] [1|2] [1|3] [1|4] [1|5] [1|6]
#         [2|2] [2|3] [2|4] [2|5] [2|6]
#         [3|3] [3|4] [3|5] [3|6]
#         [4|4] [4|5] [4|6]
#         [5|5] [5|6]
#         [6|6]

teams = ['Dragon', 'Wolves', 'Pandas', 'Unicorn']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + ' vs ' + away_team)
            
# Output: Dragon vs Wolves
#         Dragon vs Pandas
#         Dragon vs Unicorn
#         Wolves vs Dragon
#         Wolves vs Pandas
#         Wolves vs Unicorn
#         Pandas vs Dragon
#         Pandas vs Wolves
#         Pandas vs Unicorn
#         Unicorn vs Dragon
#         Unicorn vs Wolves
#         Unicorn vs Pandas