# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    a,b,c = map(int,input().split())
    print(a+b >= c and b+c >= a and a+c >= b)
    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()