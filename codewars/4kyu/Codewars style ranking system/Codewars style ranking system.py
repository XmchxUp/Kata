# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method


class User:
    __min_rank, __max_rank = -8, 8

    def __init__(self) -> None:
        self.rank = User.__min_rank
        self.progress = 0
        pass

    def inc_progress(self, rank_level: int) -> None:
        if not self.__is_rank_level(rank_level):
            raise ValueError("not correct rank")
        if self.rank == User.__max_rank:
            return

        difference = self.__get_two_rank_difference(rank_level, self.rank)
        if rank_level == self.rank:
            self.progress += 3
        elif rank_level < self.rank and difference == 1:
            self.progress += 1
        elif rank_level < self.rank and difference >= 2:
            # ignore lower more than 2 level
            pass
        else:
            self.progress += difference * difference * 10

        if self.progress >= 100:
            self.__upgrade_rank_level()

    def __upgrade_rank_level(self):
        while self.progress >= 100:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank = 1
            elif self.rank == User.__max_rank:
                self.progress = 0
                return

    def __is_rank_level(self, rank_level: int) -> bool:
        return User.__min_rank <= rank_level <= User.__max_rank and rank_level != 0

    def __get_two_rank_difference(self, rank1: int, rank2: int) -> int:
        if rank1 > rank2:
            return self.__get_two_rank_difference(rank2, rank1)
        if rank2 < 0 or rank1 > 0:
            return abs(rank1 - rank2)
        else:
            return abs(rank1 - rank2) - 1


def example_test1():
    user = User()
    assert user.rank == -8  # => -8
    assert user.progress == 0  # => 0
    user.inc_progress(-7)
    assert user.progress == 10  # => 10
    user.inc_progress(-5)  # will add 90 progress
    assert user.progress == 0  # => 0 # progress is now zero
    assert user.rank == -7  # => -7 # rank was upgraded to -7


user = User()


def do_test(rank, expected_rank, expected_progress):
    if rank:
        user.inc_progress(rank)
    assert user.rank == expected_rank
    assert user.progress == expected_progress


def example_test2():
    global user
    do_test(-8, -8, 3)

    user = User()
    do_test(-7, -8, 10)

    user = User()
    do_test(-6, -8, 40)

    user = User()
    do_test(-5, -8, 90)

    user = User()
    do_test(-4, -7, 60)

    user = User()
    do_test(1, -2, 40)
    do_test(1, -2, 80)
    do_test(1, -1, 20)
    do_test(1, -1, 30)
    do_test(1, -1, 40)
    do_test(2, -1, 80)
    do_test(2, 1, 20)
    do_test(-1, 1, 21)
    do_test(3, 1, 61)


if __name__ == "__main__":
    example_test1()
    example_test2()
