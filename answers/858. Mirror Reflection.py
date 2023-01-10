class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        858. Mirror Reflection

        2      11      22      1

     v3
        ?      00      ??      0
        ?      00      ??      0 (9, 6)
     v2
                       q
        2      11      22      1
        2      11      22      1
     v1        q

        ?      00      ??      0
            p h1    h2     h3

        p = 6, q = 4

        lcm(6, 4) 12

        _lcm = lcm(p, q)

        if _lcm // q % 2 == 0:
            return 2

        if _lcm // p % 2 == 0:
            return 0
        else:
            return 1


        p   q  lcm  sensor
        2   1   2     2
        3   1   3     1
        3   2   6     0
        """

        if p == 0:
            return 2
        if q == 0:
            return 0
        if p == q:
            return 1

        _lcm = lcm(p, q)

        if _lcm // q % 2 == 0:  # 6 2 3 % 2 1
            return 2

        return _lcm // p % 2  # 6 // 3 = 2 % 2 0
