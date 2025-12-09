from utils import AOCSolution

class Day07(AOCSolution):
    def part1(self) -> None:
        def sorrter(card):
            counts = [card.count(x) for x in set(card)]
            if 5 in counts:
                index = 6
            elif 4 in counts:
                index = 5
            elif 3 in counts and 2 in counts:
                index = 4
            elif 3 in counts:
                index = 3
            elif counts.count(2) == 2:
                index = 2
            elif 2 in counts:
                index = 1
            else:
                index = 0
            cards_values='AKQJT98765432'
            value = [-cards_values.index(x) for x in card]
            # print(index,card,counts,value)
            return (index,value)
    
        count=0
        cards=[]
        for line in self.lines:
            cards.append((
                line.split()[0],
                int(line.split()[1])
            ))
        cards.sort(key=lambda x: sorrter(x[0]))
        for index,card in enumerate(cards,1):
            # print(index,card)
            count += card[1]*index
        print(count)

    def part2(self) -> None:
        def valuer(card):
            counts = [card.count(x) for x in set(card)]
            if 5 in counts:
                index = 6
            elif 4 in counts:
                index = 5
            elif 3 in counts and 2 in counts:
                index = 4
            elif 3 in counts:
                index = 3
            elif counts.count(2) == 2:
                index = 2
            elif 2 in counts:
                index = 1
            else:
                index = 0
            return index
        def sorrter(card):
            cards_values='AKQT98765432J'
            index_max = 0
            if 'J' in card:
                for card_value in cards_values:
                    new_card = card.replace('J',card_value)
                    index_max = max(valuer(new_card),index_max)
            else:
                index_max=valuer(card)        
            value = [-cards_values.index(x) for x in card]
            # print(index_max,card,value)
            return (index_max,value)
    
        count=0
        cards=[]
        for line in self.lines:
            cards.append((
                line.split()[0],
                int(line.split()[1])
            ))
        cards.sort(key=lambda x: sorrter(x[0]))
        for index,card in enumerate(cards,1):
            # print(index,card)
            count += card[1]*index
        print(count)

if __name__ == "__main__":
    Day07().run()