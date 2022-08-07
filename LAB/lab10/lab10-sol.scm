(define (student-get-name student)
    (car student)
)

(define (student-get-classes student)
    (cdr student)
)

(define (teacher-get-name teacher)
    (car teacher)
)

(define (teacher-get-class teacher)
    (car (cdr teacher))
)

(define (teacher-get-students teacher)
    (cdr (cdr teacher))
)

(define (student-attend-class student class)
    (student-create (student-get-name student) (cons class (student-get-classes student)))
)

(define (teacher-hold-class teacher)
    (define class (teacher-get-class teacher))
    (define new-students
        (map (lambda (x) (student-attend-class x class)) (teacher-get-students teacher))
    )
    (teacher-create (teacher-get-name teacher) class new-students)
)
