class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        1169. Invalid Transactions

        brute force
        Time complexity: O(n^2), n is the max number of transactions among users.

        TODO: need to find a better solution.
        """

        if not transactions:
            return []

        invalid_transactions = list()

        group_by_name = defaultdict(list)

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            group_by_name[name].append((i, int(time), int(amount), city))

        invalid_index_set = set()

        for name, transactions_per_customer in group_by_name.items():
            transactions_per_customer.sort(key=lambda x: x[1])

            for i in range(len(transactions_per_customer)):
                index, time, amount, city = transactions_per_customer[i]

                if amount > 1000:
                    invalid_index_set.add(index)

                for j in range(i + 1, len(transactions_per_customer)):
                    next_index, next_time, next_amount, next_city = transactions_per_customer[j]
                    time_diff = next_time - time
                    if 60 < time_diff:
                        break
                    elif time_diff <= 60 and next_city != city:
                        invalid_index_set.add(index)
                        invalid_index_set.add(next_index)

        for i in invalid_index_set:
            invalid_transactions.append(transactions[i])

        return invalid_transactions
