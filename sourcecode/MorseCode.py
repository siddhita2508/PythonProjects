class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---               ", "-.-", ".-..",
               "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-               ", "..-", "...-", ".--", "-..-",
               "-.--", "--.."]
        result = set()
        for