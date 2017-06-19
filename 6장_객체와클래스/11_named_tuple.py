"""
네임드 튜플은 튜플의 서브클래스이다.
이름(.name)과 위치([offset])로 값에 접근할 수 있다.
네임드튜플은 기본 지원이 아니므로 모듈을 불러와야 한다.

네임드 튜플의 특징
    1. 불면하는 객체처럼 행동한다.
    2. 객체보다 공간 효율성과 시간 효율성이 더 좋다.
    3. 딕셔녀리 형식의 괄호 대신 점 표기법으로 속성에 접근가능하다.
    4. 네임드 튜플을 딕셔너리의 키처럼 쓸 수 있다.
"""
from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
__duck__ = Duck('wide orange', 'long')
print(__duck__)
print(__duck__.bill)
print(__duck__.tail)

__parts__ = {'bill': 'wide orange', 'tail': 'long'}
__duck2__ = Duck(**__parts__)
print(__duck2__)

__duck3__ = __duck2__._replace(tail="magnificent", bill="crushing") # 필드이름만 카피하여 새객체로 반환한다.
print(__duck2__)
print(__duck3__)
