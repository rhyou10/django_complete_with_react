class YearConverter():
    regex = r"20\d{2}" # 20으로 시작하며 정수 2번 반복

    def to_python(self, value):
        return int(value) #정수로 변환하여 넘긴다.

    def to_url(self, value):
        return str(value)


class MonthConverter(YearConverter):
    regex = r"\d{1,2}" 

class DayConverter(YearConverter):
    regex = r"[0123]\d" #좀더 타이트하게 쓰는경우