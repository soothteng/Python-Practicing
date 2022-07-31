(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else 1))
)

(define (composed f g) 
  (lambda (x) (f (g x)))
)

(define (square n) (* n n))

(define (pow base exp)
  (cond ((= exp 0) 1)
        ((even? exp) (square (pow base (/ exp 2))))
        (else (* base (pow base (- exp 1)))))
)

(define (ascending? lst)
  (if (or (null? lst) (null? (cdr lst)))
      true
      (and (<= (car lst) (car (cdr lst))) (ascending? (cdr lst))))
)
