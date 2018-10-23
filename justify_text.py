from pprint import pprint

class Solution:
    def fullJustify(self, words, max_width):
        lines = []

        line = []
        wordlen = 0
        for w in words:
            if len(w) > max_width:
                raise Exception('word too long')
            if wordlen + len(line) + len(w) > max_width:
                lines.append((wordlen, line))
                line = []
                wordlen = 0
            line.append(w)
            wordlen += len(w)
        lines.append((wordlen, line))

        rv = []
        for line_num, pair in enumerate(lines):
            wordlen, line = pair
            if line_num == len(lines) - 1 or len(line) == 1:
                # left justify last line
                joined = ' '.join(line)
                justified = joined + ' ' * (max_width - len(joined))
                rv.append(justified)
            else:
                justified = []
                space_count = max_width - wordlen
                num_spaces = space_count // (len(line) - 1)
                extra_spaces = space_count % (len(line) - 1)
                for word_num, word in enumerate(line):
                    justified.append(word)
                    if word_num < len(line) - 1:
                        spaces = num_spaces
                        if word_num < extra_spaces:
                            spaces += 1
                        justified.append(' ' * spaces)
                rv.append(''.join(justified))

        return rv


if __name__ == '__main__':
    tests = [
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["What","must","be","acknowledgment","shall","be"], 16),
        (
            [
                "Science", "is", "what", "we", "understand", "well", "enough",
                "to", "explain",  "to", "a", "computer.", "Art", "is",
                "everything", "else", "we", "do"
            ],
            20
        ),
    ]
    for words, max_width in tests:
        print(max_width, words)
        pprint(Solution().fullJustify(words, max_width))
        print()

    s = (
        "I’m listening to a conference call happening in the other room "
        "regarding damaged steam turbine control valves and I’ve heard the "
        "phrase “get a nut off” 4 times. Why aren’t they all laughing?"
    )
    w = s.split(' ')
    j = Solution().fullJustify(w, 24)
    print('\n'.join(j))
