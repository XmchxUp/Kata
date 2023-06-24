def code(s):
    """
    a text t of length l.
    Consider the smallest integer n such that n * n be greater or equal to l.
    Complete t with the char of ascii code 11 (we suppose that this char is not in our original text) until the length of t is n * n.
    From now on we can transform the new t in a squared string s of size n by inserting '\n' where needed.
    Apply a clockwise rotation of 90 degrees to s: that's it for the coding part.
    """
    pass
    l = len(s)


def decode(s):
    # your code
    pass


if __name__ == "__main__":
    t = "I.was.going.fishing.that.morning.at.ten.o'clock"
    assert code(t) == "c.nhsoI\nltiahi.\noentinw\ncng.nga\nk..mg.s\n\voao.f.\n\v'trtig"
    assert decode(code(t)) == t
