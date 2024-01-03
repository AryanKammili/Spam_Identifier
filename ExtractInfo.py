class ExtractInfo:
    def __init__(self, paragraph):
        self.paragraph = paragraph

    def getFreqAll(self):
        return self.paragraph.lower().count("all")

    def getFreqOur(self):
        return self.paragraph.lower().count("our")

    def getFreqRemove(self):
        return self.paragraph.lower().count("remove")

    def getFreqReceive(self):
        return self.paragraph.lower().count("receive")

    def getFreqCredit(self):
        return self.paragraph.lower().count("credit")

    def getFreq000(self):
        return self.paragraph.count("000")

    def getFreqFree(self):
        return self.paragraph.lower().count("free")

    def getFreqEmail(self):
        return self.paragraph.lower().count("email")

    def getFreqGeorge(self):
        return self.paragraph.lower().count("george")

    def getFreqData(self):
        return self.paragraph.lower().count("data")

    def getFreq415(self):
        return self.paragraph.count("415")

    def getFreqOriginal(self):
        return self.paragraph.lower().count("original")

    def getFreqEdu(self):
        return self.paragraph.lower().count("edu")

    def getFreqSemicolon(self):
        return self.paragraph.count(";")

    def getFreqExclamation(self):
        return self.paragraph.count("!")

    def getCapital_run_length_average(self):
        streaks = []
        streak = 0
        total = 0

        for i in range(len(self.paragraph)):
            letter = self.paragraph[i]

            if letter.isupper():
                streak += 1
            else:
                streaks.append(streak)
                streak = 0

        for j in range(len(streaks)):
            streak = streaks[j]
            total += streak

        return total / len(streaks)

    def getCapital_run_length_longest(self):
        longest = 0
        streak = 0

        for i in range(len(self.paragraph)):
            letter = self.paragraph[i]

            if letter.isupper():
                streak += 1
            else:
                if streak > longest:
                    longest = streak

                else:
                    continue
        return longest

    def getCapital_run_length_total(self):
        count = 0
        for i in range(len(self.paragraph)):
            letter = self.paragraph[i]

            if letter.isupper():
                count = count + 1
        return count
