# 843. Guess the Word

Refer to Lee's Answer:
https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison


Basic idea:
randomly choose one word, we can get e.g. m characters matches.
Since the answer is in the given list, we can remove all the other words that is not m characters matches 

And, since its randomly generated, the chance of 0 characters match is (25/26)^6 -> around 76%, which is pretty high.
So, the idea is to find a word that has less 0 characters match with other words, so we can remove more words


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        zero_matches = self.num_neighbors(wordlist)
        for _ in range(10):
            guess = min(wordlist, key=lambda w: zero_matches[w])
            # guess = random.choice(wordlist)
            m = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(guess, w) == m]
        
    def match(self, s1, s2):
        return sum(c1==c2 for c1, c2 in zip(s1, s2))
    
    def num_neighbors(self, words):
        neib = collections.Counter()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.match(words[i], words[j]) == 0:
                    neib[words[i]] += 1
                    neib[words[j]] += 1
        return neib