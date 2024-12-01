"""
파이썬 클래스에는 인스턴스 메소드뿐만 아니라 클래스 메소드와 스태틱 메소드도 존재한다.
이 두 메소드는 @classmethod, @staticmethod라는 데코레이터를 통해 정의될 수 있다.
두 메소드는 클래스 및 인스턴스를 통해 접근할 수 있다.
"""

"""
클래스 메소드는 첫 번째 인자로 클래스 자체(cls)를 받는 메소드이다.
클래스 메소드는 클래스 속성 및 메소드에는 접근할 수 있지만, 인스턴스 필드 및 메소드에는 접근할 수 없다.
클래스 레벨의 로직이나 대안 생성자를 구현할 때 사용된다.
"""


class MyClass:
    count = 0

    def __init__(self):
        self.score = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        # self.score


my_class = MyClass()
my_class.increment()
print(my_class.count, my_class.score)  # 1, 0


"""
스태틱 메소드는 특별한 첫 번째 인자(self나 cls)를 받지 않는 메소드이다.
클래스를 통해 클래스 속성 및 클래스 메소드에 접근할 수 있지만, 이는 해당 클래스에 속하지 않은 함수에서도 가능한 동작이다.
즉, 모듈 수준의 함수와 기능적으로 동일하지만, 해당 클래스와 논리적으로 연관되어 있음을 나타내기 위해 클래스 내에 정의한다.
"""
class CompletionList:
    major = 'computer_science'
    subject_list = {}

    def __init__(self):
        self.failed_count = 0
        self.passed_count = 0

    def show(self):
        print(f'{self.passed_count}, {self.failed_count}')

    @classmethod
    def append(cls, name, low_line):
        cls.subject_list[name] = low_line

    @staticmethod
    def academic_result(subject_name, score):
        # self.subject_list = []
        # cls.major = 'math'
        subject_list = CompletionList.subject_list

        if subject_list[subject_name] > score:
            return False
        else:
            return True

    def my_academic_result_counting(self, result):
        if result:
            self.passed_count += 1
        else:
            self.failed_count += 1


CompletionList.append('java', 3.5)
CompletionList.append('linux', 4.0)

my_completion_list = CompletionList()

my_completion_list.my_academic_result_counting(CompletionList.academic_result('java', 2.0))
my_completion_list.my_academic_result_counting(CompletionList.academic_result('linux', 4.0))

my_completion_list.show()

