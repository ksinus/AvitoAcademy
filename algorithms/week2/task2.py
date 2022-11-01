def calculate_stock_spans(prices: list) -> list:
    days_stack = [0]
    spans = [1] * len(prices)
    for i in range(1, len(prices)):
        while days_stack and prices[days_stack[-1]] <= prices[i]:
            days_stack.pop()
        spans[i] = i + 1 if not days_stack else (i - days_stack[-1])
        days_stack.append(i)
    return spans


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


solution()
